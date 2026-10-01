/* Render the approved M2 family review and avatar PNG exports.
   node brand/tools/render-family.cjs REVIEW_DIR [CHROMIUM_EXECUTABLE]
   Requires Playwright; no remote resources or font downloads. */
const fs=require('node:fs'),path=require('node:path');
const {pathToFileURL}=require('node:url');
const {createHash}=require('node:crypto');
const {chromium}=require('playwright');
const root=path.resolve(__dirname,'../..'),out=process.argv[2];
if(!out)throw new Error('Provide a review directory outside the repository.');
fs.mkdirSync(out,{recursive:true});
const manifest=JSON.parse(fs.readFileSync(path.join(root,'brand/review/M2_MANIFEST.json'),'utf8'));
const palette=JSON.parse(fs.readFileSync(path.join(root,'brand/palette/palette.json'),'utf8'));
const {ink,paper,ochre,slate,rule}=palette;
const assets=manifest.assets.map(a=>({...a,svg:fs.readFileSync(path.join(root,a.path),'utf8')}));
const get=p=>assets.find(a=>a.path===p);
const data=s=>'data:image/svg+xml;base64,'+Buffer.from(s).toString('base64');
const img=(a,w,h=a.height/a.width*w,cls='')=>`<img alt="${a.title}" src="${data(a.svg)}" width="${w}" height="${h}" class="${cls}">`;
const core={title:'Primary faceted Impossible Duck',width:256,height:256,svg:fs.readFileSync(path.join(root,'brand/source/geometric-duck.svg'),'utf8')};
const avatar=slug=>assets.find(a=>a.kind==='avatar'&&a.slug===slug);
const colors=['cream','ink','ochre','sage'];
const labels={cream:'Paper',ink:'Ink / light facets',ochre:'Ochre',sage:'Sage',line:'Technical PA',seal:'Faceted seal'};
const css=`<style>*{box-sizing:border-box}body{margin:0;background:${paper};color:${ink};font:16px 'Segoe UI',Arial,sans-serif}main{width:1440px;padding:36px 48px}img{display:block}h1{font:normal 42px Georgia,serif;letter-spacing:1px;margin:8px 0}h2{font:normal 26px Georgia,serif;margin:0}h3{font:normal 22px Georgia,serif;margin:14px 0 6px}p{font-size:14px;line-height:1.5;color:${slate};margin:8px 0}.eyebrow{font-size:11px;letter-spacing:2px;text-transform:uppercase}.label{font-size:12px;letter-spacing:1.5px;text-transform:uppercase}.rule{border-top:1px solid ${rule};margin:26px 0}.masthead{display:flex;gap:28px;align-items:center}.masthead .meta{margin-left:auto;text-align:right;max-width:315px}.swatches{display:flex;gap:8px;margin-top:18px}.swatches span{width:30px;height:10px;background:var(--c)}.section-head{display:flex;align-items:baseline;justify-content:space-between;margin-bottom:20px}.section-head p{margin:0;font-size:13px}.primary{display:grid;grid-template-columns:repeat(4,1fr);gap:24px}.tile{border:1px solid ${rule};padding:18px;text-align:center}.tile>img{margin:0 auto}.tile .circle{border-radius:50%;margin:14px auto 0}.tile p{font-size:12px}.stamp-pair{display:grid;grid-template-columns:1fr 1fr;gap:24px}.stamp{border:1px solid ${rule};padding:20px}.stamp-top{display:flex;gap:24px;align-items:center}.stamp-top p{max-width:240px}.stamp>.rect{margin:12px auto 0}.secondary{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}.secondary .tile{display:flex;align-items:center;text-align:left;gap:18px}.secondary .tile>div{flex:1}.secondary .tile>img{margin:0}.secondary p{font-size:12px}.circle{border-radius:50%;overflow:hidden}.foot{font-size:12px}.qa-grid{display:grid;grid-template-columns:repeat(6,1fr);gap:20px}.qa-col{text-align:center}.qa-col img{margin:14px auto}.qa-col .sample{height:100px;display:flex;flex-direction:column;align-items:center;justify-content:end;gap:8px}.qa-col .sample img{margin:0}.qa-col .sample span{font:12px Consolas,monospace}.fallback-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:24px}.fallback-grid>div{border:1px solid ${rule};padding:20px}.fallback-grid img{margin:0 auto}</style>`;
const sheet=`<!doctype html><html lang="en"><meta charset="utf-8"><title>Patitos Fortune · M2 family review</title>${css}<main>
<header class="masthead">${img(core,128)}<div><div class="eyebrow">Patitos Fortune / Creative Software Lab</div><h1>One lab. A family of marks.</h1><p>Colorful geometric recognition · technical and institutional companions</p><div class="swatches">${Object.values(palette).map(c=>`<span style="--c:${c}"></span>`).join('')}</div></div><div class="meta"><div class="eyebrow">M2 / Approved identity</div><p>M1 core marks are approved.<br>Stamp, monogram and avatar family approved.</p></div></header>
<div class="rule"></div><section><div class="section-head"><h2>01. The colorful primary expression</h2><p>Same facets and silhouette · background-specific light substitutions</p></div><div class="primary">${colors.map(s=>`<article class="tile">${img(avatar(s),176)}<h3>${labels[s]}</h3><p>${s==='cream'?'Unchanged primary colors.':'Controlled palette adaptation.'}</p>${img(avatar(s),48,48,'circle')}</article>`).join('')}</div></section>
<div class="rule"></div><section><div class="section-head"><h2>02. The Lab Stamp family</h2><p>Both forms retained · EST. 2025 remains secondary</p></div><div class="stamp-pair">${['ink','ochre'].map(t=>`<article class="stamp"><div class="stamp-top">${img(get(t==='ink'?'brand/source/round-stamp.svg':'brand/stamps/round-stamp-ochre.svg'),288)}<div><div class="label">${t==='ink'?'Ink / Paper':'Ink / Ochre detail'}</div><h3>Round Lab Stamp</h3><p>${t==='ink'?'Monochrome technical geometry for an archival seal.':'Canonical PA and beak accents, plus one fine Ochre ring.'}</p></div></div>${img(get(t==='ink'?'brand/source/rectangular-stamp.svg':'brand/stamps/rectangular-stamp-ochre.svg'),584,292,'rect')}<p>Rectangular Lab Label · shared editorial hierarchy and research-label rules.</p></article>`).join('')}</div></section>
<div class="rule"></div><section><div class="section-head"><h2>03. Compact secondary uses</h2><p>Supporting choices; the faceted duck remains primary</p></div><div class="secondary"><article class="tile">${img(avatar('line'),144)}<div><div class="label">Technical avatar</div><p>Complete PA, stronger strokes, two secondary seams removed.</p>${img(avatar('line'),48,48,'circle')}</div></article><article class="tile">${img(avatar('seal'),144)}<div><div class="label">Seal avatar</div><p>Colorful faceted duck and quiet rings. No tiny lettering.</p>${img(avatar('seal'),48,48,'circle')}</div></article><article class="tile">${img(get('brand/source/pf-monogram.svg'),144)}<div><div class="label">PF monogram</div><p>Editorial secondary mark in an archival frame.</p></div></article></div></section>
<div class="rule"></div><p class="foot">Four stamp treatments · one PF monogram · six avatar treatments. Small circles above are 48 px; the separate QA sheet shows all avatars at 32/48/64 px in square and circular display. No profile or social-card work is included.</p><p class="foot">Colorful / mosaic identity remains primary. The technical PA mark is complementary. The complete M2 family is approved. No commits, pushes or uploads.</p>
</main></html>`;
const qa=`<!doctype html><html lang="en"><meta charset="utf-8"><title>M2 avatars · actual-size QA</title>${css}<main><div class="eyebrow">M2 / Native browser pixels / Device scale 1</div><h1>Small-square and circular checks</h1><p>View at 100%. The production-size candidate exports are 512 × 512; samples below are independently rendered at their display size.</p><div class="rule"></div><div class="qa-grid">${[...colors,'line','seal'].map(s=>`<section class="qa-col"><h3>${labels[s]}</h3>${img(avatar(s),128)}<div class="rule"></div><div class="label">Square</div>${[64,48,32].map(n=>`<div class="sample">${img(avatar(s),n)}<span>${n} px</span></div>`).join('')}<div class="rule"></div><div class="label">Circle</div>${[64,48,32].map(n=>`<div class="sample">${img(avatar(s),n,n,'circle')}<span>${n} px</span></div>`).join('')}</section>`).join('')}</div><div class="rule"></div><p>PA letter discovery and institutional lettering are not required at avatar sizes. Judge silhouette recognition, useful color separation and crop clearance.</p></main></html>`;
const lettered=assets.filter(a=>a.kind!=='avatar');
function fallback(svg){return svg.replace(/font-family="([^"]*)"/g,(_,family)=>`font-family="${family.includes('Georgia')?"'Times New Roman', serif":family.includes('Consolas')?"'Courier New', monospace":"Arial, sans-serif"}"`);}
const fallbackSheet=`<!doctype html><html lang="en"><meta charset="utf-8"><title>M2 type fallback QA</title>${css}<main><div class="eyebrow">M2 / Font fallback review</div><h1>Lettering with alternate system fonts</h1><p>Times New Roman / Arial / Courier New. These local fallback checks do not guarantee every operating system's font metrics.</p><div class="rule"></div><div class="fallback-grid">${lettered.map(a=>`<div><h3>${a.title}</h3>${img({...a,svg:fallback(a.svg)},a.kind==='rectangular-stamp'?580:320)}</div>`).join('')}</div></main></html>`;
(async()=>{
 const browser=await chromium.launch({headless:true,...(process.argv[3]?{executablePath:process.argv[3]}:{})});
 try{
  const page=await browser.newPage({viewport:{width:1440,height:1100},deviceScaleFactor:1});
  const errors=[];page.on('pageerror',e=>errors.push(e.message));await page.route(/^https?:/,r=>r.abort());
  for(const [name,html] of [['family-review',sheet],['avatar-size-review',qa],['font-fallback-review',fallbackSheet]]){
   const file=path.resolve(out,name+'.html');fs.writeFileSync(file,html);await page.goto(pathToFileURL(file).href);
   await page.evaluate(()=>document.fonts.ready);await page.locator('img').evaluateAll(nodes=>Promise.all(nodes.map(n=>n.decode())));
   await page.locator('main').screenshot({path:path.join(out,name+'.png')});
  }
  const textChecks=[];
  for(const a of lettered)for(const mode of ['preferred','fallback']){
   await page.setContent(`<style>body{margin:0}svg{display:block}</style>${mode==='fallback'?fallback(a.svg):a.svg}`);
   await page.evaluate(()=>document.fonts.ready);
   const result=await page.evaluate(()=>{const root=document.querySelector('svg'),v=root.viewBox.baseVal;return [...root.querySelectorAll('text')].map(t=>{const b=t.getBBox();return {text:t.textContent,x:b.x,y:b.y,width:b.width,height:b.height,inside:b.x>=0&&b.y>=0&&b.x+b.width<=v.width&&b.y+b.height<=v.height};});});
   if(result.some(t=>!t.inside))throw new Error('Text exceeds artboard: '+a.path+' '+mode);
   textChecks.push({asset:a.path,mode,text:result});
  }
  for(const a of assets.filter(a=>a.kind==='avatar'))for(const size of [32,48,64,128,512]){
   await page.setContent(`<style>body{margin:0;background:${a.background}}img{display:block}</style>${img(a,size,size)}`);await page.locator('img').evaluate(n=>n.decode());
   const destination=size===512?path.join(root,a.path.replace(/\.svg$/,'.png')):path.join(out,`duck-${a.slug}-${size}.png`);
   if(size===512){
    // An opaque canvas guarantees upload exports have no fractional-alpha raster seams.
    const png=await page.locator('img').evaluate((n,bg)=>{const c=document.createElement('canvas');c.width=c.height=512;const ctx=c.getContext('2d',{alpha:false});ctx.fillStyle=bg;ctx.fillRect(0,0,512,512);ctx.drawImage(n,0,0,512,512);return c.toDataURL('image/png').split(',')[1];},a.background);
    fs.writeFileSync(destination,Buffer.from(png,'base64'));
   }else await page.locator('img').screenshot({path:destination,omitBackground:false});
   if(size!==512){await page.locator('img').evaluate(n=>{n.style.borderRadius='50%';document.body.style.background='transparent';});await page.locator('img').screenshot({path:path.join(out,`duck-${a.slug}-${size}-circle.png`),omitBackground:true});}
  }
  const report={browser:await browser.version(),deviceScaleFactor:1,errors,sourceHashes:Object.fromEntries(assets.map(a=>[a.path,createHash('sha256').update(a.svg).digest('hex')])),textChecks,exports:6,avatarSizes:[32,48,64,128,512]};
  fs.writeFileSync(path.join(out,'family-render-report.json'),JSON.stringify(report,null,2)+'\n');
  if(errors.length)throw new Error(errors.join('\n'));
  console.log('Rendered family, small-size and fallback review sheets; six approved 512 px PNG exports; square/circle QA samples.');
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
