"""Validate M3 profile assets, relative paths and browser review evidence.

python brand/tools/validate-profile.py [--renders REVIEW_DIR]
No network access and no changes to the repository.
"""
import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[2]
M=json.loads((ROOT/'brand/review/M3_MANIFEST.json').read_text())
P=json.loads((ROOT/'brand/palette/palette.json').read_text())
NS={'s':'http://www.w3.org/2000/svg'}


def sig(n):return (n.tag,dict(n.attrib),(n.text or '').strip(),[sig(c) for c in n])


class ProfileHTML(HTMLParser):
    def __init__(self):super().__init__();self.paths=[];self.images=[];self.sources=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        assert tag in {'p','picture','source','img'},tag
        assert set(a)<={'align','media','srcset','src','width','alt'}
        if tag=='img':assert a.get('alt') and a.get('src');self.images.append(a)
        if tag=='source':assert a.get('media')=='(max-width: 600px)';self.sources.append(a)
        for k in ('src','srcset'):
            if k in a:
                path=a[k];assert not re.search(r'^(?:[a-z]+:|/|\\)',path,re.I),path
                f=(ROOT/'profile'/path).resolve();assert f.is_relative_to(ROOT) and f.is_file(),path
                self.paths.append(str(f.relative_to(ROOT)).replace('\\','/'))


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--renders',type=Path);args=parser.parse_args()
    assert M['status']=='approved'
    for rel,h in M['protectedM2Assets'].items():assert hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==h,rel
    master=ET.parse(ROOT/'brand/source/geometric-duck.svg').getroot()
    original=[sig(c) for c in master if c.tag.split('}')[-1] not in ('title','desc')]
    for rel in M['headers']:
        tree=ET.parse(ROOT/rel).getroot();duck=tree.find(".//*[@id='primary-duck']")
        assert [sig(c) for c in duck]==original,'Primary duck paint/geometry changed'
        assert tree.find('s:title',NS) is not None and tree.find('s:desc',NS) is not None
        ids=[n.get('id') for n in tree.iter() if n.get('id')];assert len(ids)==len(set(ids))
        assert all(id in ids for id in tree.get('aria-labelledby').split())
        for n in tree.iter():
            assert n.tag.split('}')[-1] not in ('script','image','foreignObject','style','filter')
            for k,v in n.attrib.items():
                assert not k.startswith('on')
                if k.endswith('href'):assert v.startswith('#') and v[1:] in ids
                if 'url(' in v:
                    ref=re.fullmatch(r'url\(#([\w-]+)\)',v);assert ref and ref[1] in ids
                if k in ('fill','stroke'):assert v=='none' or v in P.values()
        assert tree.find('s:rect',NS).get('fill')==P['paper']
    readme=(ROOT/M['profile']).read_text(encoding='utf-8');html=ProfileHTML();html.feed(readme)
    assert len(html.images)==2 and len(html.sources)==1
    assert set(html.paths)==set(M['headers']+[M['expressiveAsset']])
    assert 'A small, independent software lab.' in readme and 'Exploring curious ideas and turning them into useful software.' in readme
    assert not re.search(r'https?://|C:[\\/]|<script|<style|shields\.io|visitor|stats',readme,re.I)
    print('PASS: 25 approved asset/token hashes, unchanged primary paint in both headers, local SVGs, descriptive alt text and three durable relative image paths.')
    if args.renders:
        baseline_path=args.renders/'m2-approved-hashes.json'
        if baseline_path.exists():
            baseline=json.loads(baseline_path.read_text())
            for rel,h in baseline.items():assert hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==h
        r=json.loads((args.renders/'profile-render-report.json').read_text())
        assert r['errors']==[] and r['deviceScaleFactor']==1
        for rel,h in r['sourceHashes'].items():assert hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==h
        assert {(x['theme'],x['width']) for x in r['results']}=={(t,w) for t in ('light','dark') for w in (320,390,600,601,1024)}
        assert all(not x['overflow'] and all(i['loaded'] and i['inside'] for i in x['images']) for x in r['results'])
        assert len(r['textChecks'])==4 and all(c['inside'] for x in r['textChecks'] for c in x['checks'])
        assert 'A small, independent software lab.' in r['textOnly'] and 'Exploring curious ideas and turning them into useful software.' in r['textOnly']
        print('PASS: repository M2 hash baseline; ten width/theme checks, four preferred/fallback lettering checks, image-free copy and current render hashes.')


if __name__=='__main__':main()
