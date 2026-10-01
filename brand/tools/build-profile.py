"""Compose M3 profile headers from the approved primary duck; no master edits.

python brand/tools/build-profile.py
The compact header preserves lettering at narrow widths through a picture source.
The profile reuses the approved construction SVG directly; no duplicate is made.
"""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[2]
NS='http://www.w3.org/2000/svg'
ET.register_namespace('',NS)
P=json.loads((ROOT/'brand/palette/palette.json').read_text())


def e(tag,**attrs):return ET.Element('{'+NS+'}'+tag,{k.replace('_','-'):str(v) for k,v in attrs.items()})


def text(parent,value,x,y,size,family,**attrs):
    n=e('text',x=x,y=y,font_size=size,font_family=family,fill=P['ink'],**attrs);n.text=value;parent.append(n)


def header(compact):
    w,h=(400,248) if compact else (1040,256)
    svg=e('svg',width=w,height=h,viewBox=f'0 0 {w} {h}',role='img',aria_labelledby='title desc')
    for tag,s in [('title','Patitos Fortune â€” Creative Software Lab'),('desc','Organization-profile lab label with the approved colorful primary duck and secondary EST. 2025. Approved M3 organization-profile presentation.')]:
        n=e(tag,id=tag);n.text=s;svg.append(n)
    svg.append(e('rect',width=w,height=h,fill=P['paper']))
    margin=12 if compact else 16
    for inset,sw in [(margin,1.4),(margin+8,.65)]:
        svg.append(e('rect',x=inset,y=inset,width=w-2*inset,height=h-2*inset,fill='none',stroke=P['ink'],stroke_width=sw))
    svg.append(e('path',d='M 180,20 V 166 M 20,166 H 380' if compact else 'M 244,24 V 232 M 244,184 H 1016',fill='none',stroke=P['ink'],stroke_width='.7'))
    duck=e('svg',id='primary-duck',x=28 if compact else 32,y=20 if compact else 24,width=144 if compact else 208,height=144 if compact else 208,viewBox='0 0 256 256')
    source=ET.parse(ROOT/'brand/source/geometric-duck.svg').getroot()
    for child in source:
        if child.tag.split('}')[-1] not in ('title','desc'):duck.append(deepcopy(child))
    svg.append(duck)
    serif="Georgia, 'Times New Roman', serif";sans="'Segoe UI', Arial, Helvetica, sans-serif";mono="Consolas, 'Liberation Mono', monospace"
    if compact:
        text(svg,'PATITOS',199,86,31,serif,letter_spacing='2')
        text(svg,'FORTUNE',199,129,31,serif,letter_spacing='2')
        text(svg,'CREATIVE SOFTWARE LAB',200,200,18,sans,letter_spacing='1.8',text_anchor='middle')
        text(svg,'EST. 2025',200,224,12,mono,letter_spacing='2',text_anchor='middle')
    else:
        text(svg,'PATITOS FORTUNE',286,106,49,serif,letter_spacing='4')
        text(svg,'CREATIVE SOFTWARE LAB',290,150,21,sans,letter_spacing='4.7')
        text(svg,'EST. 2025',290,215,14,mono,letter_spacing='2.4')
    ET.indent(svg,space='  ')
    name='lab-header-compact.svg' if compact else 'lab-header.svg'
    out=ROOT/'profile/assets'/name;out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text('\n'.join(line.rstrip() for line in ET.tostring(svg,encoding='unicode').splitlines())+'\n',encoding='utf-8',newline='\n')
    return str(out.relative_to(ROOT)).replace('\\','/')


def main():
    for name in ('M2_MANIFEST.json','M2_EXPRESSIVE_MANIFEST.json'):
        assert json.loads((ROOT/'brand/review'/name).read_text())['status']=='approved','M2 must be approved first'
    protected={str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest()
               for d in ('source','stamps','avatars','derived','palette') for p in (ROOT/'brand'/d).glob('*') if p.is_file()}
    assets=[header(False),header(True)]
    manifest={'milestone':'M3','status':'approved','profile':'profile/README.md','headers':assets,
              'expressiveAsset':'brand/derived/technical-construction.svg','protectedM2Assets':protected,
              'compactBreakpoint':600,'paperFieldForBothThemes':True}
    (ROOT/'brand/review/M3_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8',newline='\n')
    print('Built two M3 header layouts; reused the approved construction study; no M1/M2 asset writes.')


if __name__=='__main__':main()
