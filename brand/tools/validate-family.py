"""Validate M2 candidates without publishing them.

python brand/tools/validate-family.py [--renders REVIEW_DIR]
Uses Python's standard library. Visual inspection of the review sheet is required.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import struct
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[2]
NS={'s':'http://www.w3.org/2000/svg'}
P=json.loads((ROOT/'brand/palette/palette.json').read_text())
M=json.loads((ROOT/'brand/review/M2_MANIFEST.json').read_text())
FILLED=ET.parse(ROOT/'brand/source/geometric-duck.svg').getroot()
TECH=ET.parse(ROOT/'brand/source/technical-line-duck.svg').getroot()


def node(tree,id):return tree.find(f".//*[@id='{id}']")


def png_size(path):
    b=path.read_bytes();assert b[:8]==b'\x89PNG\r\n\x1a\n'
    return struct.unpack('>II',b[16:24])


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--renders',type=Path)
    args=parser.parse_args()
    assert len(M['assets'])==11 and M['status']=='approved'
    for name,h in M['sources'].items():
        assert hashlib.sha256((ROOT/'brand/source'/name).read_bytes()).hexdigest()==h,'Regenerate stale M2 assets'
    assert {a.get('slug') for a in M['assets'] if a['kind']=='avatar'}=={'cream','ink','ochre','sage','line','seal'}
    for a in M['assets']:
        f=ROOT/a['path'];tree=ET.parse(f).getroot()
        assert tree.get('viewBox')==f"0 0 {a['width']} {a['height']}"
        assert tree.find('s:title',NS) is not None and tree.find('s:desc',NS) is not None
        ids=[e.get('id') for e in tree.iter() if e.get('id')];assert len(ids)==len(set(ids))
        assert all(i in ids for i in tree.get('aria-labelledby','').split())
        for e in tree.iter():
            assert e.tag.split('}')[-1] not in {'script','image','foreignObject','style'}
            for k,v in e.attrib.items():
                assert not k.startswith('on') and 'data:' not in v
                if k.endswith('href'):assert v.startswith('#') and v[1:] in ids
                if 'url(' in v:
                    ref=re.fullmatch(r'url\(#([\w-]+)\)',v);assert ref and ref[1] in ids
                if k in ('fill','stroke'):assert v=='none' or v in P.values(),(f,v)
        assert node(tree,'duck-silhouette').get('d')==node(FILLED,'silhouette').get('d')
        if a.get('expression') in ('faceted','faceted-seal'):
            subs=a.get('facetSubstitutions',{})
            for source in FILLED.findall('.//s:polygon',NS):
                copy=node(tree,'duck-'+source.get('id'))
                assert copy.get('points')==source.get('points')
                expected=P[subs[source.get('id')]] if source.get('id') in subs else source.get('fill')
                assert copy.get('fill')==copy.get('stroke')==expected
            assert node(tree,'duck-eye').get('cx')=='178' and node(tree,'duck-eye').get('cy')=='65'
        if a['kind'] in ('round-stamp','rectangular-stamp') or a.get('expression')=='technical':
            for id in ('pa-left-leg','pa-right-leg','pa-counter','body-brace','neck-seams'):
                assert node(tree,'duck-'+id).get('d')==node(TECH,id).get('d')
            accent=P['ink'] if a.get('treatment')=='ink' else P['ochre']
            for id in ('pa-left-leg','pa-right-leg','pa-counter'):
                assert node(tree,'duck-'+id).get('stroke')==accent
            assert node(tree,'duck-bill').get('fill')==accent
        if a.get('expression')=='technical':
            assert node(tree,'duck-body-seams').get('d')==node(TECH,'body-seams').get('d').replace(' M 124,168 L 160,210','').replace(' M 154,136 L 196,166','')
        if a['kind'] in ('round-stamp','rectangular-stamp'):
            letters=' '.join(t.text or '' for t in tree.iter())
            assert '2025' in letters and '2026' not in letters
        if a['kind']=='avatar':assert png_size(f.with_suffix('.png'))==(512,512)
        print(a['path']+': SVG, local references, palette, shared geometry and role checks PASS')
    if args.renders:
        report=json.loads((args.renders/'family-render-report.json').read_text())
        assert report['errors']==[] and report['deviceScaleFactor']==1
        for a in M['assets']:
            assert hashlib.sha256((ROOT/a['path']).read_bytes()).hexdigest()==report['sourceHashes'][a['path']]
            if a['kind']=='avatar':
                for n in (32,48,64,128):
                    for suffix in ('','-circle'):
                        assert png_size(args.renders/f"duck-{a['slug']}-{n}{suffix}.png")==(n,n)
        assert len(report['textChecks'])==10
        assert all(t['inside'] for check in report['textChecks'] for t in check['text'])
        print(f"Browser {report['browser']}: 6 upload-size PNGs, 48 square/circle samples and 10 preferred/fallback lettering checks PASS")


if __name__=='__main__':main()
