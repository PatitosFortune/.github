"""Generate M4 specimen cards from JSON; no edits to approved M1–M3 assets.

python brand/tools/build-social.py [--input JSON] [--output-dir DIR]
SVG layout is deterministic and uses the standard library only. Raster exports
and actual font bounds are checked separately by render-social.cjs.
"""
import argparse
from copy import deepcopy
import json
import math
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[2]
NS='http://www.w3.org/2000/svg';ET.register_namespace('',NS)
P=json.loads((ROOT/'brand/palette/palette.json').read_text())
SERIF="Georgia, 'Times New Roman', serif";SANS="'Segoe UI', Arial, Helvetica, sans-serif";MONO="Consolas, 'Liberation Mono', monospace"


def e(tag,**a):return ET.Element('{'+NS+'}'+tag,{k.replace('_','-'):str(v) for k,v in a.items()})


def txt(parent,s,x,y,size,color,family=SANS,**a):
    n=e('text',x=x,y=y,font_size=size,font_family=family,fill=color,**a);n.text=s;parent.append(n);return n


def estimate(s,size):
    # Conservative width envelope across the established serif/sans fallbacks.
    return sum(.30 if c in ' il.,:;!|\'' else 1.03 if c in 'MW@%' else .71 if c.isupper() else .59 for c in s)*size


def wrap(s,size,width):
    lines=[]
    for paragraph in s.split('\n'):
        line=''
        for token in re.findall(r'[^\s\-/]+[-/]?|[-/]',paragraph):
            if estimate(token,size)>width:
                if line:lines.append(line);line=''
                part=''
                for c in token:
                    if estimate(part+c,size)>width:lines.append(part);part=''
                    part+=c
                line=part
            elif line and estimate(line+('' if line.endswith(('-','/')) else ' ')+token,size)>width:lines.append(line);line=token
            else:line=(line+('' if line.endswith(('-','/')) else ' ')+token).strip()
        if line:lines.append(line)
    return lines


def fit(s,width,sizes,maxlines,three_line_limit=None):
    for size in sizes:
        lines=wrap(s,size,width)
        if len(lines)<=maxlines and not (len(lines)==3 and three_line_limit and size>three_line_limit):return size,lines
    raise ValueError('Text exceeds layout contract; provide a shorter editorial title/descriptor.')


def validate(c):
    assert set(c)<={'id','name','descriptor','category','accent','theme','motif','catalogueId','sample'}
    assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',c['id'])
    assert isinstance(c.get('sample',False),bool)
    for k,limit in [('name',84),('descriptor',140),('category',24),('catalogueId',16)]:
        value=c.get(k,'');assert isinstance(value,str) and len(value)<=limit,(k,'too long')
        assert not any(ord(ch)<32 and not (ch=='\n' and k in ('name','descriptor')) for ch in value),(k,'control character')
    assert c['name'].strip() and c['descriptor'].strip()
    assert c.get('accent','ochre') in ('ochre','rust','sage','mist')
    assert c.get('theme','paper') in ('paper','ink')
    assert c.get('motif','none') in ('number-grid','route','data-bars','oscillation','none')


def motif(c,fg,accent):
    g=e('g',id='project-study');kind=c.get('motif','none')
    # Fixed study region: x=864..1216, y=144..480. Motifs are illustrative, not logos.
    if kind=='number-grid':
        for row,values in enumerate(((8,1,6),(3,5,7),(4,9,2))):
            for col,value in enumerate(values):
                x=892+col*96;y=156+row*96
                g.append(e('rect',x=x,y=y,width=88,height=88,fill=accent if value==5 else 'none',stroke=fg,stroke_width='1',stroke_opacity='.32'))
                txt(g,str(value),x+44,y+57,34,P['ink'] if value==5 else fg,MONO,text_anchor='middle')
        txt(g,'3 × 3 / SUM = 15',1040,476,14,fg,MONO,text_anchor='middle',letter_spacing='1.2')
    elif kind=='route':
        for x in range(880,1217,48):g.append(e('path',d=f'M {x},156 V 444',stroke=fg,stroke_opacity='.12',stroke_width='.7'))
        for y in range(156,445,48):g.append(e('path',d=f'M 880,{y} H 1216',stroke=fg,stroke_opacity='.12',stroke_width='.7'))
        g.append(e('path',d='M 892,416 L 940,368 916,296 1008,268 1056,196 1144,220 1192,160',fill='none',stroke=accent,stroke_width='3',stroke_dasharray='8 6'))
        for x,y,r in [(892,416,7),(940,368,5),(916,296,5),(1008,268,8),(1056,196,5),(1144,220,5)]:
            g.append(e('circle',cx=x,cy=y,r=r,fill=P['ink'],stroke=fg,stroke_width='1.6'))
        g.append(e('path',d='M 1192,146 L 1206,160 1192,174 1178,160 Z',fill=accent))
        g.append(e('path',d='M 900,196 L 944,156 976,196 M 924,196 V 220',fill='none',stroke=fg,stroke_width='1.2',stroke_opacity='.5'))
        txt(g,'ROUTES / DISCOVERIES',1040,476,14,fg,MONO,text_anchor='middle',letter_spacing='1.2')
    elif kind=='data-bars':
        for i,(label,value) in enumerate([('A',16),('B',28),('C',45),('D',62)]):
            y=184+i*65;txt(g,label,876,y+18,19,fg,MONO)
            g.append(e('path',d=f'M 908,{y+34} H 1208',stroke=fg,stroke_opacity='.18',stroke_width='1'))
            g.append(e('rect',x=908,y=y,width=value*3.6,height=24,fill=accent))
            txt(g,str(value),1208,y+18,18,fg,MONO,text_anchor='end')
        txt(g,'OBSERVE / ORGANIZE',1040,476,14,fg,MONO,text_anchor='middle',letter_spacing='1.2')
    elif kind=='oscillation':
        g.append(e('path',d='M 880,168 V 432 H 1216 M 880,300 H 1216',fill='none',stroke=fg,stroke_opacity='.3',stroke_width='1'))
        for phase,alpha in [(1.15,.17),(.55,.30),(0,1)]:
            pts=[]
            for n in range(169):
                t=n/168;pts.append((880+336*t,300-106*math.exp(-1.25*t)*math.sin(2*math.pi*2.3*t+phase)))
            d='M '+' L '.join(f'{x:.3f},{y:.3f}' for x,y in pts)
            g.append(e('path',d=d,fill='none',stroke=accent if phase==0 else fg,opacity=alpha,stroke_width='2.2' if phase==0 else '1.2'))
        for x in (880,964,1048,1132,1216):g.append(e('path',d=f'M {x},428 V 436',stroke=fg,stroke_width='1'))
        txt(g,'DAMPED OSCILLATION',1040,476,14,fg,MONO,text_anchor='middle',letter_spacing='1.2')
    elif c['id']=='social-preview-template':
        g.append(e('rect',x=880,y=156,width=320,height=288,fill='none',stroke=fg,stroke_opacity='.25',stroke_dasharray='4 6'))
        txt(g,'PROJECT STUDY',1040,306,18,fg,MONO,text_anchor='middle',letter_spacing='1.5')
    return g


def build(c,out):
    validate(c);dark=c.get('theme')=='ink';bg=P['ink'] if dark else P['paper'];fg=P['paper'] if dark else P['ink'];accent=P[c.get('accent','ochre')]
    svg=e('svg',width=1280,height=640,viewBox='0 0 1280 640',role='img',aria_labelledby='title desc')
    for tag,value in [('title',c['name'].replace('\n',' ')+' — Patitos Fortune'),('desc',('Fictional sample. ' if c.get('sample') else '')+c['descriptor'])]:
        n=e(tag,id=tag);n.text=value;svg.append(n)
    svg.append(e('rect',width=1280,height=640,fill=bg))
    svg.append(e('rect',x=24,y=24,width=1232,height=592,fill='none',stroke=fg,stroke_width='1.3'))
    svg.append(e('rect',x=32,y=32,width=1216,height=576,fill='none',stroke=fg,stroke_width='.6',stroke_opacity='.35'))
    svg.append(e('path',d='M 824,64 V 480 M 64,492 H 1216',stroke=fg,stroke_opacity='.3',stroke_width='1',fill='none'))
    svg.append(e('path',d='M 64,66 H 112',stroke=accent,stroke_width='4'))
    if c.get('category','REPOSITORY').strip():txt(svg,c.get('category','REPOSITORY').upper(),64,108,16,fg,MONO,id='category',letter_spacing='2')
    if c.get('catalogueId'):txt(svg,c['catalogueId'],1216,108,15,fg,MONO,id='catalogue',text_anchor='end',letter_spacing='1.5')
    size,lines=fit(c['name'],720,(80,72,64,56,48,44),3,56)
    title=e('g',id='project-name')
    for i,line in enumerate(lines):txt(title,line,68,222+i*(size+9),size,fg,SERIF)
    svg.append(title)
    ds,dl=fit(c['descriptor'],710,(25,24),3)
    desc=e('g',id='project-descriptor')
    for i,line in enumerate(dl):txt(desc,line,66,410+i*34,ds,fg,SANS)
    svg.append(desc);svg.append(motif(c,fg,accent))
    source='brand/avatars/duck-ink.svg' if dark else 'brand/source/geometric-duck.svg'
    duck=e('svg',id='lab-duck',x=64,y=496,width=80,height=80,viewBox='0 0 256 256')
    for n in ET.parse(ROOT/source).getroot():
        if n.tag.split('}')[-1] not in ('title','desc'):duck.append(deepcopy(n))
    svg.append(duck)
    txt(svg,'PATITOS FORTUNE',160,533,24,fg,SERIF,id='lab-name',letter_spacing='2.5')
    txt(svg,'CREATIVE SOFTWARE LAB',161,561,13,fg,SANS,id='lab-role',letter_spacing='2.8')
    if c.get('sample'):txt(svg,'FICTIONAL SAMPLE',1216,568,13,fg,MONO,id='sample-label',text_anchor='end',letter_spacing='1.3')
    ET.indent(svg,space='  ');dest=out/(c['id']+'.svg');dest.write_text('\n'.join(s.rstrip() for s in ET.tostring(svg,encoding='unicode').splitlines())+'\n',encoding='utf-8',newline='\n')
    return {'id':c['id'],'file':dest.name,'theme':c.get('theme','paper'),'accent':c.get('accent','ochre'),'motif':c.get('motif','none'),'name':c['name'],'fontSize':size,'titleLines':lines,'descriptorLines':dl,'markSource':source}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--input',type=Path,default=ROOT/'brand/social/examples.json');parser.add_argument('--output-dir',type=Path,default=ROOT/'brand/social');args=parser.parse_args()
    assert json.loads((ROOT/'brand/review/M3_MANIFEST.json').read_text())['status']=='approved'
    config=json.loads(args.input.read_text(encoding='utf-8'));assert config['schemaVersion']==1
    assert len({c['id'] for c in config['cards']})==len(config['cards'])
    assert all(c['id']!='social-preview-template' for c in config['cards']),'Reserved template ID'
    # Reject unsupported inputs before writing any candidate files.
    for c in config['cards']:
        validate(c)
        fit(c['name'],720,(80,72,64,56,48,44),3,56)
        fit(c['descriptor'],710,(25,24),3)
    args.output_dir.mkdir(parents=True,exist_ok=True)
    records=[build(c,args.output_dir) for c in config['cards']]
    template={'id':'social-preview-template','name':'Project name','descriptor':'A concise description of the project and what it explores.','category':'Category','accent':'ochre','theme':'paper','motif':'none','sample':True}
    records.insert(0,build(template,args.output_dir))
    manifest={'milestone':'M4','status':'approved' if args.input.resolve()==(ROOT/'brand/social/examples.json').resolve() else 'visual-review-pending','width':1280,'height':640,'safeMargin':64,'cards':records}
    (args.output_dir/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(f'Built template + {len(records)-1} specimen cards; custom projects require review.')


if __name__=='__main__':main()
