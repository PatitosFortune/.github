"""Validate M4 social SVGs, PNG headers, preserved assets and browser evidence.

python brand/tools/validate-social.py [--renders REVIEW_DIR] [--source-dir DIR]
Standard library only. Run with normal Python (assertions enabled).
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
P=json.loads((ROOT/'brand/palette/palette.json').read_text(encoding='utf-8'))


def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def sig(n):return (n.tag,dict(n.attrib),(n.text or '').strip(),[sig(c) for c in n])


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--renders',type=Path)
    parser.add_argument('--source-dir',type=Path,default=ROOT/'brand/social')
    a=parser.parse_args();m=json.loads((a.source_dir/'manifest.json').read_text(encoding='utf-8'))
    approved=json.loads((ROOT/'brand/review/M4_MANIFEST.json').read_text(encoding='utf-8'))
    assert approved['status']=='approved'
    assert m['status'] in ('approved','visual-review-pending')
    assert (m['width'],m['height'],m['safeMargin'])==(1280,640,64)
    for rel,h in approved['protectedM3Assets'].items():assert digest(ROOT/rel)==h,rel
    hashes={};sizes={}
    for card in m['cards']:
        p=a.source_dir/card['file'];hashes[p.name]=digest(p);svg=ET.parse(p).getroot()
        assert (svg.get('width'),svg.get('height'),svg.get('viewBox'))==('1280','640','0 0 1280 640')
        ids=[n.get('id') for n in svg.iter() if n.get('id')];assert len(ids)==len(set(ids))
        assert svg.get('role')=='img' and all(x in ids for x in svg.get('aria-labelledby').split())
        assert all(svg.find('s:'+tag,NS).text for tag in ('title','desc'))
        for n in svg.iter():
            assert n.tag.split('}')[-1] not in ('script','image','foreignObject','style','filter')
            for k,v in n.attrib.items():
                assert not k.lower().startswith('on')
                if k.endswith('href'):assert v.startswith('#') and v[1:] in ids
                if 'url(' in v:
                    ref=re.fullmatch(r'url\(#([\w-]+)\)',v);assert ref and ref[1] in ids
                if k in ('fill','stroke'):assert v=='none' or v in P.values(),v
        bg=svg.find('s:rect',NS)
        assert (bg.get('width'),bg.get('height'),bg.get('fill'))==('1280','640',P[card['theme']])
        source='brand/avatars/duck-ink.svg' if card['theme']=='ink' else 'brand/source/geometric-duck.svg'
        assert card['markSource']==source
        original=[sig(n) for n in ET.parse(ROOT/source).getroot() if n.tag.split('}')[-1] not in ('title','desc')]
        assert [sig(n) for n in svg.find(".//*[@id='lab-duck']")]==original,'Lab mark drift'
        for group,lines in [('project-name','titleLines'),('project-descriptor','descriptorLines')]:
            assert [n.text for n in svg.find(f".//*[@id='{group}']")]==card[lines]
            assert 1<=len(card[lines])<=3
        assert 44<=card['fontSize']<=80
        if card['id']!='social-preview-template':
            png=p.with_suffix('.png');b=png.read_bytes();sizes[png.name]=len(b)
            assert b[:8]==b'\x89PNG\r\n\x1a\n' and struct.unpack('>II',b[16:24])==(1280,640)
            assert len(b)<1_000_000
    if a.renders:
        report=json.loads((a.renders/'social-render-report.json').read_text(encoding='utf-8'))
        assert not report['errors'] and report['sourceHashes']==hashes,'Stale SVG render evidence'
        assert len(report['checks'])==2*len(m['cards'])
        for card in m['cards']:
            checks=[c for c in report['checks'] if c['id']==card['id']]
            assert {c['mode'] for c in checks}=={'preferred','generic-fallback'}
            assert all(c['slots'] and all(t['safe'] for t in c['text']) for c in checks)
        for file,h in report['pngHashes'].items():
            base=a.renders if file=='social-preview-template.png' else a.source_dir
            assert digest(base/file)==h,'Stale PNG render evidence'
    print(f'PASS: {len(hashes)} SVGs; palette, source geometry, titles, {len(sizes)} 1280x640 PNGs below 1 MB; {len(approved["protectedM3Assets"])} preserved files.')
    print(json.dumps(sizes,sort_keys=True))


if __name__=='__main__':main()
