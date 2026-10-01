"""Validate the M1 SVG geometry and palette with Python's standard library.

Run from any directory: python brand/tools/validate-core.py
Optional: --renders DIR checks browser-export PNG headers and browser report.
This is focused brand QA, not a general SVG validator or visual-review substitute.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import re
import struct
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
NS = {"s": "http://www.w3.org/2000/svg"}
PALETTE = json.loads((ROOT / "brand/palette/palette.json").read_text())
SIZES = (16, 24, 32, 48, 64, 128)


def points(text):
    nums = [float(n) for n in re.findall(r"-?\d+(?:\.\d+)?", text)]
    assert len(nums) % 2 == 0
    return list(zip(nums[::2], nums[1::2]))


def area(poly):
    return abs(sum(a[0]*b[1]-b[0]*a[1] for a,b in zip(poly,poly[1:]+poly[:1])))/2


def segments(d):
    result=[]
    for sub in d.split('M')[1:]:
        p=points(sub)
        result.extend(zip(p,p[1:]))
        if 'Z' in sub: result.append((p[-1],p[0]))
    return result


def on_segment(p,a,b):
    return (abs((p[0]-a[0])*(b[1]-a[1])-(p[1]-a[1])*(b[0]-a[0])) < 0.0001
            and min(a[0],b[0])-1e-5 <= p[0] <= max(a[0],b[0])+1e-5
            and min(a[1],b[1])-1e-5 <= p[1] <= max(a[1],b[1])+1e-5)


def contains(p, poly):
    x,y = p
    inside = False
    for a,b in zip(poly, poly[1:]+poly[:1]):
        if (a[1]>y) != (b[1]>y) and x < (b[0]-a[0])*(y-a[1])/(b[1]-a[1])+a[0]:
            inside = not inside
    return inside


def luminance(hex_value):
    values = [int(hex_value[i:i+2],16)/255 for i in (1,3,5)]
    linear = [v/12.92 if v<=0.04045 else ((v+0.055)/1.055)**2.4 for v in values]
    return sum(v*w for v,w in zip(linear,(0.2126,0.7152,0.0722)))


def contrast(a,b):
    hi,lo = sorted((luminance(PALETTE[a]),luminance(PALETTE[b])),reverse=True)
    return (hi+0.05)/(lo+0.05)


def validate_svg(name):
    file = ROOT / "brand/source" / (name+".svg")
    text = file.read_text(encoding="utf-8")
    tree = ET.fromstring(text)
    assert tree.get("viewBox")=="0 0 256 256"
    assert tree.get("width")==tree.get("height")=="256"
    assert tree.find("s:title",NS) is not None and tree.find("s:desc",NS) is not None
    ids = [e.get("id") for e in tree.iter() if e.get("id")]
    assert len(ids)==len(set(ids))
    assert all(ref in ids for ref in tree.get("aria-labelledby","").split())
    allowed = {"svg","title","desc","g","path","polygon","circle","defs","clipPath","use"}
    for el in tree.iter():
        assert el.tag.split("}")[-1] in allowed, el.tag
        for key,value in el.attrib.items():
            assert not key.startswith("on") and "data:" not in value
            if "href" in key: assert value.startswith("#") and value[1:] in ids
            if "url(" in value:
                match=re.fullmatch(r"url\(#([\w-]+)\)",value)
                assert match and match[1] in ids
            if key in {"fill","stroke"}: assert value=="none" or value in PALETTE.values(), value
    silhouette = tree.find(".//s:path[@id='silhouette']",NS).get("d")
    assert set(re.findall(r"[A-Za-z]",silhouette)) <= {"M","L","Z"}
    print(f"{name}: XML, dimensions, accessibility labels, IDs, palette and dependency checks PASS")
    print("  SHA256",hashlib.sha256(file.read_bytes()).hexdigest())
    return tree,silhouette


def check_renders(directory):
    report = json.loads((directory/"browser-report.json").read_text())
    assert report["errors"] == [] and report["deviceScaleFactor"] == 1
    for name in ("geometric-duck","technical-line-duck"):
        source=ROOT / "brand/source" / (name+".svg")
        assert report["sourceHashes"][name] == hashlib.sha256(source.read_bytes()).hexdigest(), "Stale render: " + name
        detail_sizes = tuple(report.get("technicalDetailSizes",[])) if name=="technical-line-duck" else ()
        for size in (*SIZES,256,*detail_sizes):
            raw = (directory/f"{name}-{size}.png").read_bytes()
            assert raw[:8] == b"\x89PNG\r\n\x1a\n"
            assert struct.unpack(">II",raw[16:24]) == (size,size)
    count=14+len(report.get("technicalDetailSizes",[]))
    print(f"Browser {report['browser']}: no page errors; all {count} PNG sample dimensions PASS")


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--renders",type=Path)
    args=parser.parse_args()
    filled,outline = validate_svg("geometric-duck")
    line,line_outline = validate_svg("technical-line-duck")
    assert outline == line_outline, "Core silhouettes have drifted"
    assert filled.find("s:circle",NS).attrib == line.find("s:circle",NS).attrib
    border=points(outline)
    facets=[points(e.get("points")) for e in filled.findall(".//s:polygon",NS)]
    assert len(facets)==12
    assert math.isclose(sum(area(p) for p in facets),area(border),abs_tol=0.001)
    # Non-integer offsets avoid sampling the exact shared diagonals.
    for y in range(44,210):
        for x in range(32,220):
            p=(x+0.317,y+0.619)
            assert sum(contains(p,f) for f in facets) == int(contains(p,border)), (x,y)
    vertices=set(v for poly in facets for v in poly)
    base_paths=[el for el in line.findall(".//s:path",NS) if not el.get('id','').startswith('pa-')]
    for el in base_paths:
        assert all(v in vertices for v in points(el.get("d"))), el.get("id")
    edges=[seg for el in base_paths for seg in segments(el.get('d'))]
    accents=line.find(".//s:g[@id='pa-accent']",NS)
    assert accents is not None and list(line)[-1] is accents
    gold=[]
    for el in accents:
        assert el.get('stroke') == PALETTE['ochre'] and el.get('fill')=='none'
        for p,q in segments(el.get('d')):
            assert any(on_segment(p,a,b) and on_segment(q,a,b) for a,b in edges)
            gold.append((p,q))
    a_reading='M 86,210 L 124,168 154,136 160,210 M 124,168 L 156.521348,167.096629'
    p_reading='M 86,210 L 124,168 154,136 156.521348,167.096629 124,168'
    for d in (a_reading,p_reading):
        for p,q in segments(d):
            assert any(on_segment(p,a,b) and on_segment(q,a,b) for a,b in gold), 'Missing Ochre PA segment'
    bill=line.find("s:polygon[@id='bill']",NS)
    assert bill.get('points')==filled.find(".//s:polygon[@id='bill']",NS).get('points')
    assert bill.get('fill')==PALETTE['ochre'] and len(line.findall('.//s:polygon',NS))==1
    assert line.find('s:g',NS).get('stroke')==PALETTE['ink']
    print('Canonical PA: all four A-key segments and P reading covered by Ochre; only existing edges; approved bill facet')
    brace=points(line.find(".//s:path[@id='body-brace']",NS).get("d"))
    assert len(brace)==2 and brace[0]!=brace[1]
    for step in range(1,100):
        t=step/100
        p=tuple(a+(b-a)*t for a,b in zip(*brace))
        assert contains(p,border), "Technical brace leaves the duck silhouette"
    print("Technical brace: existing facet-vertex endpoints; 99 interior samples remain inside silhouette")
    xs,ys=zip(*border)
    radius=max(math.hypot(x-128,y-128) for x,y in border)
    assert radius+1<128  # includes the line master's 1-unit half-stroke
    print(f"Geometry: identical silhouette; 12 facets tile {area(border):.0f} square units; no sampled holes/overlaps")
    print(f"Bounds: ({min(xs):g},{min(ys):g}) to ({max(xs):g},{max(ys):g}); circular clearance {128-radius:.2f} units before stroke")
    print("\nContrast ratios (threshold decisions use unrounded values):")
    pairs=[("ink",c) for c in ("paper","sage","mist","ochre","rust","slate","rule")]
    pairs += [(c,"paper") for c in ("slate","sage","mist","ochre","rust","rule")]
    for a,b in pairs:
        ratio=contrast(a,b)
        print(f"{a:6} / {b:6} {ratio:.4f}:1  normal text: {'PASS' if ratio>=4.5 else 'FAIL'}; large text / essential graphics: {'PASS' if ratio>=3 else 'FAIL'}")
    assert contrast("ink","paper")>=4.5 and contrast("slate","paper")>=4.5
    if args.renders: check_renders(args.renders)


if __name__ == "__main__":
    main()
