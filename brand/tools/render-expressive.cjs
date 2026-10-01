/* node brand/tools/render-expressive.cjs REVIEW_DIR [CHROMIUM_EXECUTABLE] [BEFORE_SVG_DIR]
   Render six focused review panels and four derivative previews, outside the repo. */
const fs=require('node:fs'),path=require('node:path'),{createHash}=require('node:crypto');
const {pathToFileURL}=require('node:url'),{chromium}=require('playwright');
const root=path.resolve(__dirname,'../..'),out=process.argv[2];
if(!out)throw Error('Provide a review directory outside the repository.');
fs.mkdirSync(out,{recursive:true});
const p=JSON.parse(fs.readFileSync(path.join(root,'brand/palette/palette.json'),'utf8'));
const manifest=JSON.parse(fs.readFileSync(path.join(root,'brand/review/M2_EXPRESSIVE_MANIFEST.json'),'utf8'));
const files=['brand/source/rectangular-stamp.svg','brand/derived/rectangular-stamp-aged-ink.svg','brand/derived/rectangular-stamp-aged-ochre.svg','brand/stamps/round-stamp-ochre.svg','brand/derived/technical-construction.svg','brand/derived/round-stamp-construction.svg'];
const svgs=files.map(f=>fs.readFileSync(path.join(root,f),'utf8'));
const beforeDir=process.argv[4];
const data=s=>'data:image/svg+xml;base64,'+Buffer.from(s).toString('base64');
function img(s,w,h,alt){return `<img src="${data(s)}" width="${w}" height="${h}" alt="${alt}">`;}
function detail(s){return s.replace(/width="640" height="320" viewBox="0 0 640 320"/,'width="644" height="84" viewBox="4 6 230 30"');}
const css=`<style>*{box-sizing:border-box}body{margin:0;background:${p.paper};color:${p.ink};font:16px 'Segoe UI',Arial,sans-serif}main{width:1600px;padding:48px 56px}h1{font:normal 44px Georgia,serif;margin:12px 0 16px}h2{font:normal 28px Georgia,serif;margin:8px 0 10px}p{color:${p.slate};font-size:15px;line-height:1.55;margin:10px 0}.eyebrow{font-size:11px;letter-spacing:2px;text-transform:uppercase}.intro{display:flex;justify-content:space-between;align-items:end}.intro aside{width:260px;text-align:right}.grid{display:grid;grid-template-columns:1fr 1fr;gap:28px 36px;margin-top:32px}.panel{border-top:1px solid ${p.rule};padding-top:24px;min-height:568px}.panel>p{max-width:690px}.art{height:352px;display:flex;align-items:center;justify-content:center}.art img{display:block}.detail{margin-top:10px}.detail img{display:block;margin:8px auto}.detail .eyebrow{text-align:center;font-size:10px}.drawing .art{height:446px}.foot{border-top:1px solid ${p.rule};padding-top:20px;margin-top:32px}.foot p{font-size:13px}</style>`;
function stamp(i,title,copy){return `<section class="panel"><div class="eyebrow">${String(i+1).padStart(2,'0')} / Rectangular Lab Stamp</div><h2>${title}</h2><p>${copy}</p><div class="art">${img(svgs[i],640,320,title)}</div><div class="detail"><div class="eyebrow">Same upper-left rules · 2.8× detail</div>${img(detail(svgs[i]),644,84,'Magnified edge contact detail')}</div></section>`;}
function drawing(i,title,copy,size){return `<section class="panel drawing"><div class="eyebrow">${String(i+1).padStart(2,'0')} / Technical expression</div><h2>${title}</h2><p>${copy}</p><div class="art">${img(svgs[i],size,size,title)}</div></section>`;}
const html=`<!doctype html><html lang="en"><meta charset="utf-8"><title>Patitos Fortune · M2 approved expressive treatments</title>${css}<main><header class="intro"><div><div class="eyebrow">Patitos Fortune / M2 refinement / Expressive derivatives</div><h1>Impression & construction</h1><p>Clean identity underneath. Controlled physical wear and quiet drafting around it.</p></div><aside><div class="eyebrow">M2 expressive system approved</div><p>All clean assets preserved.<br>Colorful faceted duck remains primary.</p></aside></header><div class="grid">
${stamp(0,'Clean rectangular Lab Stamp','The existing Ink master, unchanged. The same layout and geometry underpin both impressions.')}
${drawing(3,'Clean round Lab Stamp','The existing Ochre-detail seal, unchanged. Its rings, lettering, date and PA duck stay intact.',420)}
${stamp(1,'A1 · Aged Ink impression','Transfer variation across borders, lettering, date and duck. All source geometry stays unchanged.')}
${drawing(4,'Technical construction study','A crown-to-body diameter, aligned extrema and one PA-apex compass sweep. Canonical duck above the guides.',440)}
${stamp(2,'A2 · Aged Ochre impression','The same worn contact pattern in canonical Ochre. A single-pigment archive stamp on warm Paper.')}
${drawing(5,'Round seal + construction','Interior guides remain within the quiet center. Registration arcs and alignment marks extend beyond the seal.',440)}
</div><footer class="foot"><p>Two aged impressions · one drafting system, shown standalone and with the seal. Wear is a fixed-seed vector mask applied only to pigment; no grunge layer or altered logo geometry. Drafting lines derive from existing vertices, bounds and the seal artboard.</p><p>M2 is complete and approved. M1 masters, clean stamps, PF and colorful avatars are unchanged. No M3 work, commits, pushes or uploads.</p></footer></main></html>`;
let comparison=html;
const beforeHashes={};
if(beforeDir){
 const titles={1:'Aged Ink impression',2:'Aged Ochre impression',4:'Technical construction study',5:'Round seal / Construction Study'};
 const crop=(svg,box,w,h)=>svg.replace(/width="640" height="320" viewBox="0 0 640 320"/,`width="${w}" height="${h}" viewBox="${box}"`);
 const pairs=[1,2,4,5].map(i=>{
  const oldFile=path.join(beforeDir,path.basename(files[i]));const old=fs.readFileSync(oldFile,'utf8');beforeHashes[oldFile]=createHash('sha256').update(old).digest('hex');
  return [false,true].map(after=>`<section class="pair ${i<3?'stamp-pair':'drawing-pair'}"><div class="eyebrow">${after?'After / revised intensity':'Before / previous treatment'}</div><h2>${titles[i]}</h2><div class="pair-art">${img(after?svgs[i]:old,i<3?640:440,i<3?320:440,titles[i]+(after?' revised':' previous'))}</div></section>`).join('');
 }).join('');
 comparison=`<!doctype html><html lang="en"><meta charset="utf-8"><title>M2 · Expressive intensity before and after</title>${css}<style>.comparison{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px 36px;margin-top:32px}.pair{border-top:1px solid ${p.rule};padding-top:20px}.pair h2{font-size:26px}.pair-art{display:flex;justify-content:center;align-items:center;height:344px}.drawing-pair .pair-art{height:452px}.ink-detail{margin-top:30px;border-top:1px solid ${p.rule};padding-top:20px}.detail-row{display:flex;gap:32px;align-items:center;justify-content:center}.detail-row img{display:block}</style><main><header class="intro"><div><div class="eyebrow">Patitos Fortune / M2 / Focused intensity refinement</div><h1>Physical ink. Visible construction.</h1><p>The same marks, with one controlled increase in expressive character.</p></div><aside><div class="eyebrow">M2 expressive system approved</div><p>All clean masters unchanged.<br>One Ochre marker per drafting study.</p></aside></header><div class="comparison">${pairs}</div><section class="ink-detail"><div class="eyebrow">Enlarged revised impression / Ochre / 2× source size</div><h2>Transfer across lettering and the technical duck</h2><div class="detail-row">${img(crop(svgs[2],'45 55 550 80',1100,160),1100,160,'Revised name and tagline pigment transfer at 2x')}${img(crop(svgs[2],'475 190 110 100',220,200),220,200,'Revised technical duck pigment transfer at 2x')}</div><p>Missing pigment and pressure variation are confined to the deposited impression. Paper stays pristine.</p></section><footer class="foot"><p>Before sources are preserved from the previous review. Revised sources use the same fixed seed and unchanged clean geometry. The major drafting relationships are more visible; secondary alignment guides remain quieter.</p><p>M2 is complete and approved. No M3 work, commits, pushes or uploads.</p></footer></main></html>`;
}
(async()=>{
 const browser=await chromium.launch({headless:true,...(process.argv[3]?{executablePath:process.argv[3]}:{})});
 try{
  const page=await browser.newPage({viewport:{width:1600,height:1200},deviceScaleFactor:1});
  const errors=[];page.on('pageerror',e=>errors.push(e.message));await page.route(/^https?:/,r=>r.abort());
  const sheetName=beforeDir?'m2-intensity-review':'m2-refinement-review';
  const file=path.resolve(out,sheetName+'.html');fs.writeFileSync(file,comparison);await page.goto(pathToFileURL(file).href);
  await page.evaluate(()=>document.fonts.ready);await page.locator('img').evaluateAll(ns=>Promise.all(ns.map(n=>n.decode())));
  const layoutOverflow=await page.evaluate(()=>[...document.querySelectorAll('main p, main h1, main h2, main img')].filter(n=>{const b=n.getBoundingClientRect();return b.left<0||b.right>1600;}).map(n=>({tag:n.tagName,text:n.textContent})));if(layoutOverflow.length)throw Error('Review sheet overflows: '+JSON.stringify(layoutOverflow));
  await page.locator('main').screenshot({path:path.join(out,sheetName+'.png')});
  const samples=[];
  for(let i=0;i<files.length;i++){
   const width=i<3?1280:i===3?1024:i===4?1008:1344,height=i<3?640:width;
   await page.setViewportSize({width:Math.max(1600,width),height:Math.max(1200,height)});
   await page.setContent(`<style>body{margin:0;background:${p.paper}}img{display:block}</style>${img(svgs[i],width,height,'Review specimen')}`);
   await page.locator('img').evaluate(n=>n.decode());
   const name=path.basename(files[i],'.svg')+'.png';await page.locator('img').screenshot({path:path.join(out,name),omitBackground:false});samples.push({path:name,width,height});
  }
  const textChecks=[];
  for(const i of [1,2,5]){
   await page.setContent(`<style>body{margin:0}</style>${svgs[i]}`);await page.evaluate(()=>document.fonts.ready);
   const result=await page.evaluate(()=>{const root=document.querySelector('svg'),r=root.getBoundingClientRect();return [...root.querySelectorAll('text')].map(t=>{const b=t.getBoundingClientRect();return {text:t.textContent,inside:b.x>=r.x&&b.y>=r.y&&b.right<=r.right&&b.bottom<=r.bottom};});});
   if(result.some(t=>!t.inside))throw Error('Clipped lettering: '+files[i]);textChecks.push({path:files[i],text:result});
  }
  fs.writeFileSync(path.join(out,'expressive-render-report.json'),JSON.stringify({browser:await browser.version(),deviceScaleFactor:1,errors,layoutOverflow,textChecks,samples,beforeHashes,sourceHashes:Object.fromEntries(files.map((f,i)=>[f,createHash('sha256').update(svgs[i]).digest('hex')]))},null,2)+'\n');
  if(errors.length)throw Error(errors.join('\n'));
  console.log('Rendered '+(beforeDir?'four before/after pairs and enlarged revised ink detail':'one six-panel refinement sheet')+', six detailed specimens and three lettering checks.');
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
