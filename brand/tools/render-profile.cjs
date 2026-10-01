/* node brand/tools/render-profile.cjs REVIEW_DIR [CHROMIUM_EXECUTABLE]
   Local approximation of GitHub Markdown presentation. Never uploads content. */
const fs=require('node:fs'),path=require('node:path'),{pathToFileURL}=require('node:url');
const {createHash}=require('node:crypto'),{chromium}=require('playwright');
const root=path.resolve(__dirname,'../..'),out=process.argv[2];
if(!out)throw Error('Provide an external review output directory.');
fs.mkdirSync(out,{recursive:true});
const manifest=JSON.parse(fs.readFileSync(path.join(root,'brand/review/M3_MANIFEST.json'),'utf8'));
const readme=fs.readFileSync(path.join(root,manifest.profile),'utf8');
const hash=s=>createHash('sha256').update(s).digest('hex');
const themes={light:{bg:'#ffffff',fg:'#1f2328',muted:'#59636e',border:'#d1d9e0',bar:'#f6f8fa'},dark:{bg:'#0d1117',fg:'#f0f6fc',muted:'#9198a1',border:'#3d444d',bar:'#151b23'}};
function pageHtml(body,theme,width){const c=themes[theme];return `<!doctype html><html lang="en"><meta charset="utf-8"><title>Patitos Fortune · M3 ${theme} review</title><base href="${pathToFileURL(path.join(root,'profile')+path.sep).href}"><style>
*{box-sizing:border-box}body{margin:0;background:${c.bg};color:${c.fg};font:16px/1.5 -apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif}.review-note{padding:10px 24px;background:${c.bar};color:${c.muted};border-bottom:1px solid ${c.border};font-size:12px}.shell{max-width:960px;margin:24px auto 40px;padding:0 24px}.org{display:flex;align-items:center;gap:16px;margin:0 0 24px}.org img{width:64px;height:64px;border-radius:8px;border:1px solid ${c.border}}.org h1{font-size:24px;margin:0;font-weight:600}.org span{font-size:14px;color:${c.muted}}.tabs{display:flex;gap:24px;border-bottom:1px solid ${c.border};margin:0 0 24px;padding:0 4px;font-size:14px}.tabs span{padding:10px 0}.tabs .active{font-weight:600;border-bottom:2px solid #fd8c73}.readme-card{border:1px solid ${c.border};border-radius:6px;overflow:hidden}.card-label{background:${c.bar};font-size:12px;padding:12px 24px;border-bottom:1px solid ${c.border}}.markdown-body{padding:32px;font-size:16px;line-height:1.5;overflow-wrap:break-word}.markdown-body p{margin-top:0;margin-bottom:16px}.markdown-body h2{margin-top:24px;margin-bottom:16px;font-weight:600;font-size:1.5em;line-height:1.25;padding-bottom:.3em;border-bottom:1px solid ${c.border}}.markdown-body img{max-width:100%;box-sizing:content-box;background-color:transparent;height:auto;vertical-align:middle}.markdown-body>:last-child{margin-bottom:0}.markdown-body strong{font-weight:600}.preview-foot{color:${c.muted};font-size:12px;margin-top:14px}@media(max-width:600px){.shell{padding:0 16px;margin-top:20px}.org{gap:12px}.org img{width:48px;height:48px}.org h1{font-size:22px}.markdown-body{padding:16px}.card-label{padding:10px 16px}.review-note{padding:8px 16px}.tabs{gap:20px}}
</style><div class="review-note">LOCAL REVIEW · ${theme.toUpperCase()} · ${width} px viewport · GitHub-style approximation, not a live profile</div><main class="shell"><header class="org"><img src="../brand/avatars/duck-cream.png" alt="Proposed Paper avatar"><div><h1>PatitosFortune</h1><span>Organization profile</span></div></header><nav class="tabs" aria-label="Illustrative navigation"><span class="active">Overview</span><span>Repositories</span></nav><section class="readme-card"><div class="card-label">profile/README.md</div><article class="markdown-body">${body}</article></section><p class="preview-foot">README content and images above are rendered from the local files. Surrounding interface is illustrative.</p></main></html>`;}
const fallback=svg=>svg.replace(/font-family="([^"]*)"/g,(_,f)=>`font-family="${f.includes('Georgia')?'Times New Roman, serif':f.includes('Consolas')?'Courier New, monospace':'Arial, sans-serif'}"`);
(async()=>{
 const {marked}=await import(pathToFileURL(require.resolve('marked')).href);const body=marked.parse(readme,{gfm:true});
 const browser=await chromium.launch({headless:true,...(process.argv[3]?{executablePath:process.argv[3]}:{})});
 try{
  const page=await browser.newPage({deviceScaleFactor:1});const errors=[];page.on('pageerror',e=>errors.push(e.message));await page.route(/^https?:/,r=>r.abort());
  const results=[];
  for(const theme of ['light','dark'])for(const width of [320,390,600,601,1024]){
   const name=`profile-${theme}-${width}`;const file=path.resolve(out,name+'.html');fs.writeFileSync(file,pageHtml(body,theme,width));
   await page.setViewportSize({width,height:1000});await page.emulateMedia({colorScheme:theme});await page.goto(pathToFileURL(file).href);
   await page.evaluate(()=>document.fonts.ready);await page.locator('img').evaluateAll(ns=>Promise.all(ns.map(n=>n.decode())));
   const result=await page.evaluate(()=>{const a=document.querySelector('article'),b=a.getBoundingClientRect();return {overflow:document.documentElement.scrollWidth>innerWidth||a.scrollWidth>a.clientWidth,images:[...a.querySelectorAll('img')].map(n=>{const r=n.getBoundingClientRect();return {src:n.currentSrc.split('/').pop(),width:r.width,height:r.height,alt:n.alt,inside:r.left>=b.left&&r.right<=b.right,loaded:n.complete&&n.naturalWidth>0};}),bodyText:a.innerText};});
   if(result.overflow||result.images.some(n=>!n.inside||!n.loaded||!n.alt))throw Error('Layout/image failure '+name);
   if(result.images[0].src!==(width<=600?'lab-header-compact.svg':'lab-header.svg'))throw Error('Wrong responsive header '+name);
   results.push({theme,width,...result});
   if(width===390||width===1024)await page.screenshot({path:path.join(out,name+'.png'),fullPage:true});
  }
  const textChecks=[];
  for(const rel of manifest.headers)for(const mode of ['preferred','fallback']){
   const svg=fs.readFileSync(path.join(root,rel),'utf8');await page.setViewportSize({width:1200,height:400});await page.setContent(`<style>body{margin:0}</style>${mode==='fallback'?fallback(svg):svg}`);await page.evaluate(()=>document.fonts.ready);
   const checks=await page.evaluate(()=>{const v=document.querySelector('svg').viewBox.baseVal;return [...document.querySelectorAll('text')].map(n=>{const b=n.getBBox();return {text:n.textContent,x:b.x,y:b.y,width:b.width,height:b.height,inside:b.x>=0&&b.y>=0&&b.x+b.width<=v.width&&b.y+b.height<=v.height};});});
   if(checks.some(c=>!c.inside))throw Error('Header lettering exceeds bounds '+rel+' '+mode);textChecks.push({asset:rel,mode,checks});
   await page.locator('body > svg').screenshot({path:path.join(out,path.basename(rel,'.svg')+'-'+mode+'.png')});
  }
  const file=path.resolve(out,'profile-no-images.html');fs.writeFileSync(file,pageHtml(body,'light',390));await page.setViewportSize({width:390,height:900});await page.goto(pathToFileURL(file).href);
  await page.locator('article img, article source').evaluateAll(ns=>ns.forEach(n=>n.remove()));
  const textOnly=await page.locator('article').innerText();if(!textOnly.includes('A small, independent software lab.')||!textOnly.includes('Exploring curious ideas and turning them into useful software.'))throw Error('Description depends on images');
  await page.screenshot({path:path.join(out,'profile-no-images.png'),fullPage:true});
  const reviewHtml=`<!doctype html><html lang="en"><meta charset="utf-8"><title>M3 · GitHub organization profile review</title><style>body{margin:0;background:#F5F0E6;color:#102A36;font:16px 'Segoe UI',Arial,sans-serif}main{width:1494px;padding:28px}h1{font:normal 34px Georgia,serif;margin:8px 0}p{font-size:14px;color:#52616A}.pair{display:flex;align-items:flex-start;gap:18px;margin:18px 0 30px}img{display:block;border:1px solid #C7CBC5;box-sizing:content-box}h2{font:normal 24px Georgia,serif;border-top:1px solid #C7CBC5;padding-top:18px}</style><main><p>M3 / VISUAL REVIEW / LOCAL GITHUB-STYLE APPROXIMATION</p><h1>Patitos Fortune · Organization profile</h1><p>The approved colorful identity leads. A single technical notebook study follows concise native Markdown.</p>${['light','dark'].map(t=>`<h2>${t==='light'?'Light theme':'Dark theme'} · desktop and narrow</h2><div class="pair"><img src="profile-${t}-1024.png" width="1024" alt="Desktop ${t}"><img src="profile-${t}-390.png" width="390" alt="Narrow ${t}"></div>`).join('')}<p>These are local renders, not screenshots of a published GitHub page. M3 is approved. No commit, push or upload.</p></main></html>`;
  const reviewFile=path.resolve(out,'m3-profile-review.html');fs.writeFileSync(reviewFile,reviewHtml);await page.setViewportSize({width:1494,height:1200});await page.goto(pathToFileURL(reviewFile).href);await page.locator('img').evaluateAll(ns=>Promise.all(ns.map(n=>n.decode())));await page.locator('main').screenshot({path:path.join(out,'m3-profile-review.png')});
  const tracked=[manifest.profile,...manifest.headers,manifest.expressiveAsset];
  fs.writeFileSync(path.join(out,'profile-render-report.json'),JSON.stringify({browser:await browser.version(),deviceScaleFactor:1,errors,results,textChecks,textOnly,sourceHashes:Object.fromEntries(tracked.map(f=>[f,hash(fs.readFileSync(path.join(root,f)))]))},null,2)+'\n');
  if(errors.length)throw Error(errors.join('\n'));
  console.log('Rendered light/dark desktop and narrow previews; ten width/theme checks, four font checks, image-free copy and combined review.');
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
