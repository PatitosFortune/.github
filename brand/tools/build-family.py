"""Build the approved M2 family from the approved M1 sources.

Run: python brand/tools/build-family.py
Writes the approved M2 SVG family and manifest; does not publish or change either core master.
"""
from pathlib import Path
import hashlib
import json
import re
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[2]
BRAND=ROOT/'brand'
NS='http://www.w3.org/2000/svg'
ET.register_namespace('',NS)
P=json.loads((BRAND/'palette/palette.json').read_text())
INK,PAPER,OCHRE=P['ink'],P['paper'],P['ochre']
SANS="'Segoe UI', Arial, Helvetica, sans-serif"
SERIF="Georgia, 'Times New Roman', serif"
MONO="Consolas, 'Liberation Mono', monospace"
assets=[]


def mark(kind, prefix, mapping=None, mono=False, small=False):
    tree=ET.parse(BRAND/'source'/f'{kind}.svg').getroot()
    if kind=='geometric-duck' and mono:
        silhouette=tree.find(f".//{{{NS}}}path[@id='silhouette']")
        return f'<path id="{prefix}-silhouette" d="{silhouette.get("d")}" fill="{INK}"/>'
    for child in list(tree):
        if child.tag.split('}')[-1] in ('title','desc'):tree.remove(child)
    for el in tree.iter():
        name=el.get('id','')
        if mapping and name in mapping:
            for attr in ('fill','stroke'):
                if attr in el.attrib:el.set(attr,P[mapping[name]])
        if mono:
            for attr in ('fill','stroke'):
                if el.get(attr) in P.values():el.set(attr,INK)
        if small:
            if el.get('stroke-width')=='2':el.set('stroke-width','4')
            elif el.get('stroke-width') in ('2.2','2.4'):el.set('stroke-width','4.6')
            if name=='body-seams':
                el.set('d',el.get('d').replace(' M 124,168 L 160,210','').replace(' M 154,136 L 196,166',''))
    ids={el.get('id'):prefix+'-'+el.get('id') for el in tree.iter() if el.get('id')}
    for el in tree.iter():
        if el.get('id'):el.set('id',ids[el.get('id')])
        for key,value in list(el.attrib.items()):
            if key.endswith('href') and value.startswith('#'):el.set(key,'#'+ids[value[1:]])
            if 'url(#' in value:el.set(key,re.sub(r'url\(#([^)]*)\)',lambda m:'url(#'+ids[m[1]]+')',value))
    return '\n'.join(ET.tostring(el,encoding='unicode').replace(f' xmlns="{NS}"','') for el in tree)


def nested(body,x,y,w,h=None):
    return f'<svg x="{x}" y="{y}" width="{w}" height="{h or w}" viewBox="0 0 256 256">\n{body}\n</svg>'


def save(rel,title,description,w,h,body,kind,**extra):
    svg=f'''<svg xmlns="{NS}" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
  <title id="title">Patitos Fortune — {title}</title>
  <desc id="desc">Approved M2 identity. {description}</desc>
{body}
</svg>
'''
    file=BRAND/rel;file.parent.mkdir(parents=True,exist_ok=True)
    file.write_text('\n'.join(line.rstrip() for line in svg.splitlines())+'\n',encoding='utf-8',newline='\n')
    assets.append(dict(path='brand/'+rel,title=title,kind=kind,width=w,height=h,status='approved',**extra))


def round_stamp(ochre=False):
    accent=OCHRE if ochre else INK
    body=f'''  <circle cx="256" cy="256" r="238" fill="{PAPER}" stroke="{INK}" stroke-width="2.4"/>
  <circle cx="256" cy="256" r="229" fill="none" stroke="{INK}" stroke-width="1"/>
  <circle cx="256" cy="256" r="164" fill="none" stroke="{accent}" stroke-width="1.2"/>
  <defs>
    <path id="name-arc" d="M 56,256 A 200,200 0 0,1 456,256"/>
    <path id="lab-arc" d="M 56,256 A 200,200 0 0,0 456,256"/>
  </defs>
  <g fill="{INK}" font-family="{SANS}" text-anchor="middle">
    <text font-size="26" letter-spacing="4"><textPath href="#name-arc" startOffset="50%">PATITOS FORTUNE</textPath></text>
    <text font-size="19" letter-spacing="2.8"><textPath href="#lab-arc" startOffset="50%">CREATIVE SOFTWARE LAB</textPath></text>
  </g>
  <g fill="{INK}" font-family="{MONO}" font-size="16" letter-spacing="1" text-anchor="middle">
    <text x="65" y="260">EST.</text><text x="447" y="260">2025</text>
  </g>
  {nested(mark('technical-line-duck','duck',mono=not ochre),96,96,320)}'''
    save('stamps/round-stamp-ochre.svg' if ochre else 'source/round-stamp.svg',
         'Round Lab Stamp / '+('Ochre detail' if ochre else 'Ink'),
         'Circular institutional seal, technical duck, lab name and EST. 2025. The date remains secondary.',512,512,body,'round-stamp',treatment='ochre' if ochre else 'ink')


def rectangular_stamp(ochre=False):
    accent=OCHRE if ochre else INK
    body=f'''  <rect x="14" y="14" width="612" height="292" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>
  <rect x="22" y="22" width="596" height="276" fill="none" stroke="{accent}" stroke-width="0.9"/>
  <path d="M 22,180 H 618 M 450,180 V 298" fill="none" stroke="{INK}" stroke-width="1"/>
  <text x="320" y="85" fill="{INK}" font-family="{SERIF}" font-size="32" letter-spacing="3.2" text-anchor="middle">PATITOS FORTUNE</text>
  <text x="320" y="128" fill="{INK}" font-family="{SANS}" font-size="17" letter-spacing="3.8" text-anchor="middle">CREATIVE SOFTWARE LAB</text>
  <text x="60" y="250" fill="{INK}" font-family="{MONO}" font-size="23" letter-spacing="3">EST. 2025</text>
  <path d="M 60,267 H 116" fill="none" stroke="{accent}" stroke-width="1.5"/>
  {nested(mark('technical-line-duck','duck',mono=not ochre),470,176,128)}'''
    save('stamps/rectangular-stamp-ochre.svg' if ochre else 'source/rectangular-stamp.svg',
         'Rectangular Lab Label / '+('Ochre detail' if ochre else 'Ink'),
         'Double-rule research label, editorial lab name, technical duck and EST. 2025.',640,320,body,'rectangular-stamp',treatment='ochre' if ochre else 'ink')


def main():
    round_stamp();round_stamp(True);rectangular_stamp();rectangular_stamp(True)
    body=f'''  <path d="M 64,20 H 192 L 236,64 V 192 L 192,236 H 64 L 20,192 V 64 Z" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>
  <g fill="{INK}" font-family="{SERIF}" font-size="108">
    <text x="54" y="133">P</text><text x="123" y="164">F</text>
  </g>
  {nested(mark('geometric-duck','duck',mono=True),103,166,50)}'''
    save('source/pf-monogram.svg','PF monogram','Staggered editorial PF in an archival octagonal frame, with a small duck silhouette. Secondary typographic mark.',256,256,body,'monogram')
    settings=[
        ('cream','Paper',PAPER,{}),
        ('ink','Ink / light facets',INK,{'tail':'mist','keel':'paper','breast':'mist','neck-front':'paper','neck-plane':'sage','neck-fold':'mist','crown':'paper','bill':'mist'}),
        ('ochre','Ochre',OCHRE,{'head':'paper','neck-fold':'mist'}),
        ('sage','Sage',P['sage'],{'wing':'mist','neck-fold':'mist'})
    ]
    for slug,name,bg,mapping in settings:
        body=f'<rect width="256" height="256" fill="{bg}"/>\n'+mark('geometric-duck','duck',mapping=mapping)
        save(f'avatars/duck-{slug}.svg',f'Faceted avatar / {name}',
             'Colorful primary mosaic expression. Source geometry is unchanged; background-specific facet substitutions are documented.',256,256,body,'avatar',slug=slug,expression='faceted',background=bg,facetSubstitutions=mapping)
    body=f'<rect width="256" height="256" fill="{PAPER}"/>\n'+mark('technical-line-duck','duck',small=True)
    save('avatars/duck-line.svg','Technical PA avatar','Secondary technical avatar. Two non-PA seams omitted; strokes adapted to 4/4.6 units. Complete Ochre PA and bill retained.',256,256,body,'avatar',slug='line',expression='technical',background=PAPER)
    body=f'''<rect width="256" height="256" fill="{PAPER}"/>
  <circle cx="128" cy="128" r="113" fill="none" stroke="{INK}" stroke-width="2"/>
  <circle cx="128" cy="128" r="105" fill="none" stroke="{OCHRE}" stroke-width="1"/>
  {nested(mark('geometric-duck','duck'),23,23,210)}'''
    save('avatars/duck-seal.svg','Faceted seal avatar','Text-free circular seal with colorful primary duck. No tiny institutional lettering.',256,256,body,'avatar',slug='seal',expression='faceted-seal',background=PAPER)
    manifest={'milestone':'M2','status':'approved','primaryExpression':'colorful faceted duck','sources':{n:hashlib.sha256((BRAND/'source'/n).read_bytes()).hexdigest() for n in ('geometric-duck.svg','technical-line-duck.svg')},'assets':assets}
    (BRAND/'review').mkdir(exist_ok=True)
    (BRAND/'review/M2_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    print('Built 4 stamp treatments, 1 PF monogram and 6 approved avatars.')


if __name__=='__main__':main()
