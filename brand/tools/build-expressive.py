"""Build four reversible M2 expressive derivatives; never write clean sources.

python brand/tools/build-expressive.py
Standard library only. Fixed-seed vector masks model contact wear across all ink;
the construction guides have explicit geometric anchors. The controlled-intensity-2 outputs are approved.
"""
from copy import deepcopy
import hashlib
import json
import math
from pathlib import Path
import random
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[2]
BRAND=ROOT/'brand'
OUT=BRAND/'derived'
NS='http://www.w3.org/2000/svg'
ET.register_namespace('',NS)
P=json.loads((BRAND/'palette/palette.json').read_text())
SEED=20251001
assets=[]


def el(tag,**attrs):
    return ET.Element('{'+NS+'}'+tag,{k.replace('_','-'):str(v) for k,v in attrs.items()})


def source(rel):
    tree=ET.parse(BRAND/rel).getroot()
    for child in list(tree):
        if child.tag.split('}')[-1] in ('title','desc'):tree.remove(child)
    return tree


def root(w,h,title,desc):
    svg=el('svg',width=w,height=h,viewBox=f'0 0 {w} {h}',role='img',aria_labelledby='title desc')
    for tag,value in [('title',title),('desc','Approved M2 expressive derivative. '+desc)]:
        t=el(tag,id=tag);t.text=value;svg.append(t)
    return svg


def save(name,svg,kind,source_path):
    ET.indent(svg,space='  ')
    OUT.mkdir(exist_ok=True)
    data=ET.tostring(svg,encoding='unicode')
    (OUT/name).write_text('\n'.join(s.rstrip() for s in data.splitlines())+'\n',encoding='utf-8',newline='\n')
    assets.append({'path':'brand/derived/'+name,'kind':kind,'source':'brand/'+source_path,'status':'approved'})


def ellipse(parent,x,y,rx,ry,opacity):
    parent.append(el('ellipse',cx=f'{x:.3f}',cy=f'{y:.3f}',rx=f'{rx:.3f}',ry=f'{ry:.3f}',fill='#000000',opacity=f'{opacity:.3f}'))


def mask(defs,id):
    m=el('mask',id=id,maskUnits='userSpaceOnUse',x=0,y=0,width=640,height=320,style='mask-type:luminance')
    m.append(el('rect',width=640,height=320,fill='#FFFFFF',opacity='0.97'))
    # Broad, low-amplitude pressure variation. Only the ink, never the paper, is masked.
    for x,y,rx,ry,o in [(126,22,132,18,.13),(505,300,116,13,.18),(23,226,19,77,.12),(530,88,100,30,.06)]:
        ellipse(m,x,y,rx,ry,o)
    defs.append(m)
    return m


def wear_masks(defs):
    rng=random.Random(SEED)
    rules=mask(defs,'contact-wear')
    segments=[]
    for x,y,w,h,thick in [(14,14,612,292,2),(22,22,596,276,.9)]:
        segments.extend([(x,y,x+w,y,thick),(x+w,y,x+w,y+h,thick),(x+w,y+h,x,y+h,thick),(x,y+h,x,y,thick)])
    segments.extend([(22,180,618,180,1),(450,180,450,298,1),(60,267,116,267,1.5)])
    for x1,y1,x2,y2,w in segments:
        length=math.hypot(x2-x1,y2-y1);tx=(x2-x1)/length;ty=(y2-y1)/length
        for side in (-1,1):
            for i in range(int(length/3)):
                if rng.random()>.69:continue
                d=(i+rng.random())*3;offset=side*(w*.42+rng.uniform(-.18,.22))
                x=x1+tx*d-ty*offset;y=y1+ty*d+tx*offset
                along=rng.uniform(.35,1.25);normal=rng.uniform(.18,.52)
                ellipse(rules,x,y,along if tx else normal,normal if tx else along,rng.uniform(.45,.98))
        # Rare short gaps through a rule; gaps are never applied to lettering.
        for _ in range(max(1,int(length/90))):
            d=rng.uniform(8,length-8);along=rng.uniform(.45,1.1)
            ellipse(rules,x1+tx*d,y1+ty*d,along if tx else w*1.2,w*1.2 if tx else along,rng.uniform(.75,1))
    transfer=mask(defs,'impression-transfer')
    # One mask in the label coordinate system covers every deposited component.
    # Jittered pores affect only intersecting pigment, including glyph/duck edges.
    for x,y,w,h,step,lo,hi in [(52,58,535,32,2.25,.32,.82),
                              (84,111,478,21,2.0,.22,.58),
                              (55,228,215,26,2.1,.28,.72),
                              (482,194,105,92,2.2,.27,.67)]:
        for row in range(int(h/step)+1):
            for col in range(int(w/step)+1):
                if rng.random()>.74:continue
                px=x+(col+rng.random())*step;py=y+(row+rng.random())*step
                ellipse(transfer,px,py,rng.uniform(lo,hi),rng.uniform(lo*.65,hi*.8),rng.uniform(.65,1))
    # A few localized contact-poor areas, not damage to the paper or source paths.
    for x,y,rx,ry,o in [(174,72,32,12,.13),(439,78,21,9,.17),(327,122,42,5,.12),
                        (178,241,25,8,.16),(550,247,15,23,.13),(326,14,44,3,.14)]:
        ellipse(transfer,x,y,rx,ry,o)


def aged(pigment):
    svg=root(640,320,'Patitos Fortune — aged '+pigment+' Lab Stamp',
             'Clean rectangular layout with fixed-seed transfer wear across rules, all lettering and the duck. Single-pigment impression on pristine Paper. EST. 2025.')
    defs=el('defs');wear_masks(defs);svg.append(defs)
    svg.append(el('rect',width=640,height=320,fill=P['paper']))
    impression=el('g',id='impression',mask='url(#impression-transfer)')
    for child in source('source/rectangular-stamp.svg'):
        clone=deepcopy(child)
        for n in clone.iter():
            for a in ('fill','stroke'):
                if n.get(a)==P['paper']:n.set(a,'none')
                elif n.get(a) in P.values():n.set(a,P[pigment])
        tag=clone.tag.split('}')[-1]
        if tag not in ('text','svg'):clone.set('mask','url(#contact-wear)')
        impression.append(clone)
    svg.append(impression)
    save(f'rectangular-stamp-aged-{pigment}.svg',svg,'aged-'+pigment,'source/rectangular-stamp.svg')


def drafting(id):
    g=el('g',id=id,fill='none',stroke=P['mist'],stroke_width='.6',stroke_linecap='round')
    # Crown (166,44) and lower-left body (86,210) define this diameter exactly.
    radius=math.hypot(40,83)
    g.append(el('circle',cx=126,cy=127,r=f'{radius:.6f}',stroke=P['ink'],opacity='.48',stroke_width='1',stroke_dasharray='4 2'))
    g.append(el('path',d='M 76,230.75 L 176,23.25',stroke_width='.65',opacity='.9'))
    # Bounding extrema and the bounding-box center provide alignment guides.
    g.append(el('path',d='M 126,25 V 231 M 17,127 H 258',stroke=P['ink'],opacity='.40',stroke_dasharray='4 3 1 3',stroke_width='.8'))
    g.append(el('path',d='M 148,44 H 241 M 17,210 H 241 M 32,97 V 231 M 220,64 V 231',opacity='.82',stroke_width='.6'))
    # Compass sweep from PA apex through the bottom-right vertex; no invented units.
    r=math.hypot(6,74)
    start=(154+r*math.cos(math.radians(47)),136+r*math.sin(math.radians(47)))
    end=(154+r*math.cos(math.radians(118)),136+r*math.sin(math.radians(118)))
    g.append(el('path',d=f'M {start[0]:.6f},{start[1]:.6f} A {r:.6f},{r:.6f} 0 0 1 {end[0]:.6f},{end[1]:.6f}',stroke=P['ink'],opacity='.38',stroke_width='.8'))
    ticks=el('g',stroke=P['ink'],opacity='.4',stroke_width='.65')
    for x,y in [(166,44),(86,210),(32,114),(220,86),(126,127),(154,136),(160,210)]:
        ticks.append(el('path',d=f'M {x-2},{y} H {x+2} M {x},{y-2} V {y+2}'))
    g.append(ticks)
    return g


def marker(x,y,r):
    # Four concave points centered on an actual horizontal registration axis.
    return el('path',id='ochre-registration-marker',fill=P['ochre'],
              d=f'M {x},{y-r} Q {x},{y} {x+r},{y} Q {x},{y} {x},{y+r} Q {x},{y} {x-r},{y} Q {x},{y} {x},{y-r} Z')


def sketch():
    svg=root(336,336,'Patitos Fortune — technical construction study',
             'Canonical technical PA duck with quiet, vertex-related compass and alignment guides. The duck and Ochre PA/beak retain their exact approved geometry and paint.')
    svg.append(el('rect',width=336,height=336,fill=P['paper']))
    scene=el('g',transform='translate(40 40)');scene.append(drafting('drafting-guides'))
    duck=el('g',id='canonical-duck');duck.extend(list(source('source/technical-line-duck.svg')));scene.append(duck)
    scene.append(marker(248,127,7))
    svg.append(scene)
    save('technical-construction.svg',svg,'construction','source/technical-line-duck.svg')


def round_construction():
    svg=root(672,672,'Patitos Fortune — round seal construction study',
             'The clean Ochre-detail round seal stays intact. Quiet interior drafting and exterior registration arcs relate to its existing duck, center and 512-unit artboard. Approved expressive presentation.')
    svg.append(el('rect',width=672,height=672,fill=P['paper']))
    outside=el('g',id='exterior-registration',fill='none',stroke=P['ink'],stroke_width='1.3')
    # Registration arcs are on the existing square seal artboard's inscribed circle.
    outside.append(el('path',d='M 207.999999,114.297497 A 256,256 0 1 1 95.438689,423.557157',stroke_dasharray='2 4',stroke_width='1.5',opacity='.55'))
    outside.append(el('path',d='M 24,336 H 648 M 336,24 V 648',stroke_dasharray='7 5 1 5',stroke_width='1',opacity='.32'))
    outside.append(el('path',d='M 98,46 V 626 M 574,46 V 626',stroke=P['mist'],opacity='.9',stroke_width='1.1'))
    for x,y in [(336,80),(336,592),(80,336),(592,336)]:
        outside.append(el('path',d=f'M {x-5},{y} H {x+5} M {x},{y-5} V {y+5}',opacity='.45',stroke_width='1.1'))
    svg.append(outside)
    defs=el('defs');clip=el('clipPath',id='interior-clearance');clip.append(el('circle',cx=256,cy=256,r=154));defs.append(clip);svg.append(defs)
    seal=el('g',id='clean-seal',transform='translate(80 80)')
    for child in source('stamps/round-stamp-ochre.svg'):
        if child.tag.split('}')[-1]=='svg':
            clipped=el('g',id='interior-drafting',clip_path='url(#interior-clearance)')
            guide=el('g',transform='translate(96 96) scale(1.25)');guide.append(drafting('drafting-guides'));clipped.append(guide);seal.append(clipped)
        seal.append(deepcopy(child))
    svg.append(seal)
    svg.append(marker(592,336,10))
    save('round-stamp-construction.svg',svg,'round-construction','stamps/round-stamp-ochre.svg')


def main():
    protected={str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest()
               for d in ('source','stamps','avatars','palette') for p in (BRAND/d).glob('*') if p.is_file()}
    aged('ink');aged('ochre');sketch();round_construction()
    manifest={'milestone':'M2','status':'approved','revision':'controlled-intensity-2','seed':SEED,'protectedCleanAssets':protected,
              'assets':assets,'construction':{'diameterVertices':[[166,44],[86,210]],'circleCenter':[126,127],
              'circleRadius':math.hypot(40,83),'compassCenter':[154,136],'compassVertex':[160,210],
              'sealRegistrationRadius':256,'interiorClipRadius':154,'standaloneMarker':[248,127],'sealMarker':[592,336]}}
    (BRAND/'review/M2_EXPRESSIVE_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8',newline='\n')
    for rel,h in protected.items():assert hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==h
    print('Built two aged impressions and two construction presentations; all 21 clean assets/tokens preserved.')


if __name__=='__main__':main()
