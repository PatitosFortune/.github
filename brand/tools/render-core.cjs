/* Local visual QA, not an asset generator. Requires Node.js, Playwright and a
   Chromium-family browser. No network requests or font downloads are needed.
   Usage: node brand/tools/render-core.cjs OUTPUT_DIR [BROWSER_EXECUTABLE]
   Supply Playwright through normal module resolution or NODE_PATH. */
const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const { createHash } = require('node:crypto');
const { chromium } = require('playwright');
const root = path.resolve(__dirname, '../..');
const out = process.argv[2];
if (!out) throw new Error('An explicit output directory is required (prefer outside the repository).');
fs.mkdirSync(out, { recursive: true });
const names = ['geometric-duck', 'technical-line-duck'];
const svgs = names.map(name => fs.readFileSync(path.join(root, 'brand/source', name + '.svg'), 'utf8'));
const data = svg => 'data:image/svg+xml;base64,' + Buffer.from(svg).toString('base64');
const img = (index, size, extra = '') => `<img alt="${names[index]}" src="${data(svgs[index])}" width="${size}" height="${size}" ${extra}>`;
const colors = JSON.parse(fs.readFileSync(path.join(root, 'brand/palette/palette.json'), 'utf8'));
const style = `<style>
*{box-sizing:border-box}body{margin:0;background:#F5F0E6;color:#102A36;font:16px 'Segoe UI',Arial,sans-serif}main{width:1120px;padding:44px 48px}p{line-height:1.55;margin:8px 0}.eyebrow{font-size:11px;letter-spacing:2.4px;text-transform:uppercase}h1{font:normal 34px Georgia,serif;letter-spacing:1px;margin:12px 0}h2{font:normal 23px Georgia,serif;margin:0 0 8px}.rule{border-top:1px solid #C7CBC5;margin:24px 0}.muted{color:#52616A}.marks{display:grid;grid-template-columns:1fr 1fr;gap:32px}.mark{padding:16px 24px 24px;border:1px solid #C7CBC5}.art{height:300px;display:flex;align-items:center;justify-content:center}.swatches{display:grid;grid-template-columns:repeat(8,1fr);gap:12px}.chip{height:42px;border:1px solid #C7CBC5;margin-bottom:8px}.swatches p{font-size:11px}.type{display:grid;grid-template-columns:1.3fr 1fr;gap:36px}.caption{font-size:13px;color:#52616A}.ladder{display:grid;grid-template-columns:repeat(6,1fr);align-items:end;margin:16px 0 28px}.sample{height:160px;display:flex;flex-direction:column;justify-content:end;align-items:center;gap:12px}.sample span{font:12px Consolas,monospace}.circle{border-radius:50%;background:#F5F0E6;overflow:hidden;line-height:0}.contexts{display:flex;gap:24px;align-items:center}.dark{background:#102A36;padding:16px}.white{background:white;padding:16px}.warn{font-size:13px;color:#52616A}img{display:block}
</style>`;
const review = `<!doctype html><html lang="en"><meta charset="utf-8"><title>Patitos Fortune · M1 core review</title>${style}<main id="review">
<div class="eyebrow">Patitos Fortune / Identity development / M1</div>
<h1>One geometry. Two complementary expressions.</h1>
<p class="muted">M1 approved · colorful primary mark and complementary technical PA mark</p>
<div class="rule"></div><div class="marks">
<section class="mark"><div class="art">${img(0,320)}</div><h2>The Impossible Duck</h2><p class="caption">Primary geometric mark. Angular silhouette, broad folded planes,<br>restrained warm accents. No founding date or lettering.</p></section>
<section class="mark"><div class="art">${img(1,320)}</div><h2>The technical duck</h2><p class="caption">The same silhouette, with one cross-body construction brace.<br>A subtle P / A reading belongs only to this technical treatment.</p></section></div>
<div class="rule"></div><div class="swatches">${Object.entries(colors).map(([n,c])=>`<div><div class="chip" style="background:${c}"></div><p>${n.toUpperCase()}<br>${c}</p></div>`).join('')}</div>
<div class="rule"></div><div class="type"><div><div class="eyebrow">Typography specimen · not a finished lockup</div><h2 style="font-size:30px;margin-top:14px">Patitos Fortune</h2><p style="letter-spacing:3px;font-size:12px">CREATIVE SOFTWARE LAB</p></div><div><p>A small, independent software lab.<br>Exploring curious ideas and turning them into useful software.</p><p style="font:12px Consolas,monospace;margin-top:14px">EST. 2025 · reserved for secondary institutional use</p></div></div>
</main></html>`;
// Reveal overlays are explanatory review diagrams, never production mark variants.
// Each highlighted segment already exists in the technical SVG.
const reveal = d => data(svgs[1].replaceAll('#102A36', colors.rule).replaceAll('#C49449', colors.rule).replace('</svg>',
  `<path d="${d}" fill="none" stroke="${colors.rust}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>`));
const detail = `<!doctype html><html lang="en"><meta charset="utf-8"><title>Technical duck · P/A refinement</title>${style}<main>
<div class="eyebrow">Patitos Fortune / M1 refinement / Technical mark only</div>
<h1>A quiet P / A in the construction</h1><p class="muted">Canonical technical PA treatment · complete Ochre A and approved Ochre beak.</p>
<div class="rule"></div><div style="display:grid;grid-template-columns:600px 392px;gap:32px">
<section><div style="height:560px;display:flex;align-items:center;justify-content:center">${img(1,576)}</div><h2>Unannotated technical master</h2><p class="caption">The duck remains the first reading. Ink construction, Ochre PA,<br>and a small Ochre beak; no typographic glyphs are inserted.</p></section>
<section><div class="eyebrow">Reading key · explanatory overlays only</div><img alt="Existing lower-body edges highlighted to reveal the P reading" src="${reveal('M 86,210 L 124,168 154,136 156.521348,167.096629 124,168')}" width="288" height="288"><h2>P · lower body</h2><p class="caption">The shared rising diagonal and angular counter.<br>All highlighted P segments are Ochre in the mark.</p><img alt="Existing body folds and the new brace highlighted to reveal the A-like reading" src="${reveal('M 86,210 L 124,168 154,136 160,210 M 124,168 L 156.521348,167.096629')}" width="288" height="288"><h2>A · lower body</h2><p class="caption">Both legs and the shared crossbar are Ochre.<br>Four key segments match the canonical accent.</p></section>
</div><div class="rule"></div><p class="caption">P and A share an oblique lower-body construction. Their irregularity is intentional.<br>The colorful faceted duck remains primary; the technical PA duck is secondary.</p>
</main></html>`;
const ladder = index => `<div class="ladder">${[16,24,32,48,64,128].map(s=>`<div class="sample">${img(index,s,`id="${names[index]}-${s}"`)}<span>${s} px</span></div>`).join('')}</div>`;
const sizing = `<!doctype html><html lang="en"><meta charset="utf-8"><title>Patitos Fortune · actual-size QA</title>${style}<main id="sizes">
<div class="eyebrow">M1 / Actual-size browser renders / 1 CSS px = 1 image px</div><h1>Small-size and background checks</h1><p class="muted">View this sheet at 100% to assess the native samples. No enlargement or sharpening.</p>
<div class="rule"></div><h2>Geometric duck</h2>${ladder(0)}<h2>Technical line duck</h2>${ladder(1)}
<div class="rule"></div><div class="contexts"><div class="dark">${[32,48,64].map(s=>`<div class="circle" style="display:inline-block;margin:0 8px">${img(0,s)}</div>`).join('')}</div><p class="caption">Circular crop checks on paper, shown against ink.<br>32 / 48 / 64 px. These are QA samples, not avatar exports.</p></div>
<div class="rule"></div><div class="contexts"><div class="white">${img(0,128)}</div><div class="dark">${img(0,128)}</div><p class="warn">White background / direct ink background<br>The unchanged filled master is not approved directly on ink.<br>Use a paper field until dark avatar treatments are developed in M2.</p></div>
</main></html>`;
(async () => {
  const browser = await chromium.launch({headless:true, ...(process.argv[3] ? { executablePath:process.argv[3] } : {})});
  try {
    const page = await browser.newPage({viewport:{width:1120,height:1100},deviceScaleFactor:1});
    const errors=[]; page.on('pageerror', e=>errors.push(e.message));
    await page.route(/^https?:/, route => route.abort());
    for (const [name,html] of [['core-review',review],['technical-detail-review',detail],['size-ladder',sizing]]) {
      const file=path.resolve(out,name+'.html');fs.writeFileSync(file,html);
      await page.goto(pathToFileURL(file).href);await page.evaluate(()=>document.fonts.ready);
      await page.locator('img').evaluateAll(nodes => Promise.all(nodes.map(n=>n.decode())));
      await page.locator('main').screenshot({path:path.join(out,name+'.png')});
    }
    // An isolated transparent render validates the full SVG, independently of the sheets.
    for(let i=0;i<names.length;i++) for(const size of [16,24,32,48,64,128,256,...(i===1?[512,768]:[])]) {
      await page.setContent(`<style>body{margin:0;background:transparent}img{display:block}</style>${img(i,size)}`);
      await page.locator('img').evaluate(n=>n.decode());
      await page.locator('img').screenshot({path:path.join(out,names[i]+'-'+size+'.png'),omitBackground:true});
    }
    fs.writeFileSync(path.join(out,'browser-report.json'),JSON.stringify({browser:await browser.version(),deviceScaleFactor:1,errors,sizes:[16,24,32,48,64,128],samples:12,technicalDetailSizes:[512,768],network:'Page HTTP(S) requests blocked',sourceHashes:Object.fromEntries(names.map((n,i)=>[n,createHash('sha256').update(svgs[i]).digest('hex')])),fonts:await page.evaluate(()=>Object.fromEntries(['Georgia','Segoe UI','Arial','Consolas'].map(f=>[f,document.fonts.check(`16px "${f}"`)])))},null,2)+'\n');
    if(errors.length) throw new Error(errors.join('\n'));
    console.log('Rendered three review sheets, twelve native-size samples, two 256 px masters and 512/768 px technical details.');
    console.log('Browser:',await browser.version());
  } finally {await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
