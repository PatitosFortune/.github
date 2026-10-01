"""Validate M2 expressive derivatives, preservation and optional browser renders.

python brand/tools/validate-expressive.py [--renders REVIEW_DIR]
Uses Python's standard library. Inspection of wear and drafting hierarchy remains
a visual check, not an inference from XML validity.
"""
import argparse
from copy import deepcopy
import hashlib
import json
import math
from pathlib import Path
import re
import struct
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[2]
NS={'s':'http://www.w3.org/2000/svg'}
P=json.loads((ROOT/'brand/palette/palette.json').read_text())
M=json.loads((ROOT/'brand/review/M2_EXPRESSIVE_MANIFEST.json').read_text())


def node(t,id):return t.find(f".//*[@id='{id}']")


def content(t):return [c for c in t if c.tag.split('}')[-1] not in ('title','desc')]


def signature(n):
    return (n.tag,dict(n.attrib),(n.text or '').strip(),[signature(c) for c in n])


def same_children(a,b):assert [signature(c) for c in a]==[signature(c) for c in b]


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--renders',type=Path);args=parser.parse_args()
    assert M['status']=='approved' and len(M['assets'])==4
    for rel,h in M['protectedCleanAssets'].items():assert hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==h,rel
    print(f"PASS: {len(M['protectedCleanAssets'])} clean assets and palette files unchanged.")
    trees={}
    for a in M['assets']:
        t=ET.parse(ROOT/a['path']).getroot();trees[a['kind']]=t
        assert t.find('s:title',NS) is not None and t.find('s:desc',NS) is not None
        ids=[n.get('id') for n in t.iter() if n.get('id')];assert len(ids)==len(set(ids))
        assert all(i in ids for i in t.get('aria-labelledby').split())
        mask_nodes={id(n) for m in t.findall('.//s:mask',NS) for n in m.iter()}
        for n in t.iter():
            assert n.tag.split('}')[-1] not in ('script','image','foreignObject','filter')
            for k,v in n.attrib.items():
                assert not k.startswith('on') and 'data:' not in v
                if k.endswith('href'):assert v.startswith('#') and v[1:] in ids
                if 'url(' in v:
                    ref=re.fullmatch(r'url\(#([\w-]+)\)',v);assert ref and ref[1] in ids
                if k in ('fill','stroke'):
                    assert v=='none' or v in P.values() or (id(n) in mask_nodes and v in ('#FFFFFF','#000000'))
        print(a['path']+': local SVG references, accessibility and palette PASS')
    rect=ET.parse(ROOT/'brand/source/rectangular-stamp.svg').getroot()
    for pigment in ('ink','ochre'):
        t=trees['aged-'+pigment];assert t.get('viewBox')=='0 0 640 320'
        expected=deepcopy(content(rect))
        for child in expected:
            for n in child.iter():
                for key in ('fill','stroke'):
                    if n.get(key)==P['paper']:n.set(key,'none')
                    elif n.get(key) in P.values():n.set(key,P[pigment])
        actual=deepcopy(list(node(t,'impression')))
        for child in actual:child.attrib.pop('mask',None)
        assert node(t,'impression').get('mask')=='url(#impression-transfer)'
        same_children(actual,expected)
        assert 'EST. 2025' in ''.join(t.itertext())
    same_children(trees['aged-ink'].find('s:defs',NS),trees['aged-ochre'].find('s:defs',NS))
    print('PASS: both aged layouts/lettering/duck geometry unchanged; same deterministic wear masks; pigment only recolored.')
    tech=ET.parse(ROOT/'brand/source/technical-line-duck.svg').getroot()
    same_children(node(trees['construction'],'canonical-duck'),content(tech))
    guide=node(trees['construction'],'drafting-guides');circle=guide.find('s:circle',NS)
    cx=float(circle.get('cx'));cy=float(circle.get('cy'));r=float(circle.get('r'))
    for x,y in M['construction']['diameterVertices']:assert abs(math.hypot(x-cx,y-cy)-r)<1e-6
    assert (cx,cy)==(126,127)
    seal=ET.parse(ROOT/'brand/stamps/round-stamp-ochre.svg').getroot()
    same_children([c for c in node(trees['round-construction'],'clean-seal') if c.get('id')!='interior-drafting'],content(seal))
    assert signature(guide)==signature(node(trees['round-construction'],'drafting-guides'))
    for kind in ('construction','round-construction'):
        markers=trees[kind].findall(".//*[@id='ochre-registration-marker']")
        assert len(markers)==1 and markers[0].get('fill')==P['ochre']
    print('PASS: canonical technical paint/geometry exact; crown/body circle anchored; clean round seal exact beneath additions.')
    if args.renders:
        baseline=args.renders/'clean-baseline.json'
        if baseline.exists():
            for rel,h in json.loads(baseline.read_text()).items():assert hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==h
            print('PASS: clean files also match the independent pre-refinement baseline.')
        report=json.loads((args.renders/'expressive-render-report.json').read_text())
        assert report['errors']==[] and report['deviceScaleFactor']==1
        for rel,h in report['sourceHashes'].items():assert hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==h
        for rel,h in report.get('beforeHashes',{}).items():assert hashlib.sha256(Path(rel).read_bytes()).hexdigest()==h
        for sample in report['samples']:
            b=(args.renders/sample['path']).read_bytes();assert b[:8]==b'\x89PNG\r\n\x1a\n'
            assert struct.unpack('>II',b[16:24])==(sample['width'],sample['height'])
        assert len(report['textChecks'])==3 and all(t['inside'] for c in report['textChecks'] for t in c['text'])
        assert report['layoutOverflow']==[]
        print(f"PASS: {report['browser']}, six detailed PNG sizes, lettering bounds, sheet layout and current source hashes.")


if __name__=='__main__':main()
