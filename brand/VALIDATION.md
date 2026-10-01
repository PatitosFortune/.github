# Identity validation record

Current state: M5 is complete and Brand System v1 is approved for publication. Historical milestone sections below retain earlier checkpoint results; this final record supersedes their pending-review and authorization statements.

## M5 final QA and handoff - 2026-10-01

M4 approval was finalized before M5. The approved project/repository system, its manifests and tooling now record approval; custom input files still generate pending-review candidates. No visual concept or real-project identity was added. The same fixed laboratory grammar is explicitly documented as a lightweight project-identity generator, of which social previews are one application.

### Fresh verification

All five existing validators passed with fresh Edge/Chromium `154.0.4258.48` render reports: core, family, expressive, profile and social. Python `3.14.7` and Node `24.21.0` used existing Playwright/marked dependencies. No installation, font file or remote font was required.

- Core: XML/accessibility/IDs/palette; exact silhouette and facet tiling; complete approved Ochre A/P path and bill; measured contrast; 16 PNG size checks and no browser errors.
- Family: 11 clean family SVGs, six 512 px exports, 48 square/circle small-size samples, 10 preferred/fallback lettering checks.
- Expressive: four derivative SVGs, matching wear masks, exact underlying clean geometry, one registration marker per construction, six detailed PNG dimensions, three lettering checks and sheet bounds.
- Profile: exact duck reuse, descriptive alt text, three relative image paths, 10 width/theme checks, four alternate-font checks, image-free copy and current render hashes.
- Social: five SVGs, four exact 1280 x 640 PNGs below 1 MB, 10 preferred/generic-font checks, safe margins, slots, canonical palette and exact primary/reverse avatar reuse. Previously passed long/short/unbroken-name and input-rejection evidence from M4 remains applicable; M5 did not change the fitter.

Fresh core, family, expressive, profile and social sheets were visually inspected. All 37 pre-M5 artwork/input files remain byte-identical after rebuilding and rendering. A Pillow audit confirms the six avatar and four social PNGs are fully opaque and have their intended dimensions and file-size limits. Repeated generation of all four builders leaves generated SVGs and manifests byte-identical. The frozen `review/V1_INTEGRITY.json` now covers those 37 files plus the finalized palette document.

### Genuine defects resolved and disclosed limits

The profile validator previously required a historical `m2-approved-hashes.json` outside the repository. That extra audit is now optional; mandatory preservation checks still use `M3_MANIFEST.json`. A fresh review directory validates without any original chat artifacts.

The palette document's old pending-M2 wording was corrected to describe the approved dark avatar and existing stamp/PA use. All HEX tokens, roles and artwork remain unchanged. Dependent documentation hashes were deliberately refreshed in M2/M3/M4 manifests for that text-only correction.

One Ink-avatar PNG export temporarily differed from the approved hash despite unchanged SVG input. A repeat of the existing renderer restored the exact original hash. This confirms the documented raster limitation: SVG generation is deterministic, but browser PNG bytes should be checked rather than presumed stable even on the same machine. No approved PNG mismatch remains. Future cross-platform typography/rasterization, live GitHub sanitization/cropping, arbitrary scripts and physical printing remain unverified.

### Final handoff

`README.md` is the navigation entry point. `HANDOFF.md` inventories canonical sources, generated clean/expressive derivatives, avatars, profile assets, fictional social fixtures and external review-only evidence. `REPRODUCING.md` provides ordered commands and independent hash checks. `GITHUB_SETUP_CHECKLIST.md` separates future authorized publication and manual settings/uploads. The website handoff is explicitly scoped to the next independent PatitosFortune.com / Brand Application Stage.

Documentation links, UTF-8 text, whitespace, source inventory, SVG dependencies and public-content patterns were audited. No credentials, local personal paths, private project names, font binaries, historical review screenshots or unrelated binaries were found in public files. Git diff whitespace checks pass; all files remain untracked on the unborn working branch, so direct content/inventory checks supplement Git. Full local reports remain in the external `m5-review/` workspace; the concise durable result is `review/M5_QA.json`.

**M5 COMPLETE / BRAND SYSTEM V1 APPROVED.** The user approved final QA and handoff and authorized commit/push/PR publication. No merge, other-repository rollout, settings changes, avatar/social uploads or website work is authorized. The preceding M5 audit describes the pre-publication state.

## Historical milestone evidence

The remaining sections preserve the observations and gates at the time of each review. All M1–M5 milestones are now approved; references below to pending review or restricted next milestones are historical, not current instructions.

## M3 approval finalization — 2026-10-01

The user approved the M3 composition and responsive application. Header description metadata, manifest/generator/validator status and documentation were canonicalized before M4 began. Recursive paint signatures remained identical; the profile README remained byte-identical. Structural profile validation passed. M3 review screenshots remain historical evidence of the identical artwork, with their original pre-approval metadata hashes. No profile redesign was performed.

## Historical M4 visual-review record — subsequently approved, 2026-10-01

The reusable template and four fictional specimens are in `social/`. The complete contract, inventory and reproduction commands are in [REPOSITORY_VISUALS.md](REPOSITORY_VISUALS.md). No public repository names were needed. No uploads or other-repository modifications occurred.

### Structural and preservation checks

- All **28 protected M1–M3 files** match the independent pre-M4 SHA-256 baseline now preserved in `review/M4_MANIFEST.json`: masters, stamps, avatars and PNGs, expressive derivatives, palette, both profile headers and profile README.
- Five SVGs pass XML, unique IDs, accessible title/description, palette, local-reference and no-external-resource checks. Their canvas/viewBox is exactly 1280 × 640. The default text pair is Ink/Paper (13.1456:1); accents and faint guides carry no required instructions.
- Paper card duck elements match the exact canonical geometric source recursively. Ink card duck elements match the approved M2 Ink avatar recursively. No project-specific recoloring or altered geometry is applied to either source.
- All four sample PNGs are 1280 × 640 with alpha 255 throughout: Number Puzzle 63,730 bytes; Game Companion 72,270; Data Tool 56,581; Simulation Lab 81,892. Each is below GitHub's documented 1 MB limit. The PNG opacity audit used the available Pillow runtime; the normal validator requires only the Python standard library.
- Repeating generation produces byte-identical SVGs and manifest. Twelve rejection checks cover unsafe filenames, blank/over-limit text, unsupported theme/accent/motif, label control characters, invalid sample type, an unrenderable wide title, reserved template ID and duplicate IDs. Rejected batches fail before creating output.

### Browser and visual checks

Edge/Chromium `154.0.4258.48`, device scale 1, HTTP(S) requests blocked. Five compositions × preferred/generic serif/sans/mono stacks give **10 passing layout checks**. Measured text bounds stay in the 64 px essential-content margin and within their slots; titles do not collide with descriptors, footer or the separate illustration field. Decorative frames intentionally sit outside the margin. No page errors.

Four separate stress fixtures plus the anatomy template add **10 passing font/layout checks**. Fixtures include `Pi`, “Probabilistic Simulation and Visualization Workbench”, a 55-character hyphenated name and a 40-character unbroken wide-letter string. A 140-character descriptor wraps to three lines. A wide-letter failure exposed an underestimated character width; the estimate was increased, then the fixtures were regenerated and passed. Longer unrenderable titles are rejected rather than clipped or shrunk below the documented minimum. An omitted motif was checked as an empty field. Maximum-character limits alone do not ensure arbitrary text fits.

The focused **1384 × 1918** review sheet contains the anatomy, fixed/variable rules, all four 640 × 320 previews and four native 320 × 160 reductions. It and the large long-name stress render were visually inspected. A review-label encoding issue was corrected before final export. Final reports bind both SVG and PNG hashes to the measured/rendered output.

At 640 px, project names and descriptors remain readable. At 320 px, project names and broad motif shapes carry recognition; fine labels and descriptors should not carry information available nowhere else. The colorful lab signature remains secondary. Large multi-line names work within the grid but benefit from a shorter editorial display name at the smallest sharing sizes.

### Limits and checkpoint

Generic fallbacks pass without a required proprietary font file, but exact typography and PNG bytes can differ with browser/installed fonts. No claim is made about all scripts, emoji, arbitrary future illustrations or every platform. The SVG generator is deterministic; use a fixed rendering environment when byte-identical PNGs matter.

GitHub compatibility was checked against its official social-preview dimensions, format and size guidance linked in the application guide. Live GitHub upload/unfurl behavior, third-party cropping and compression are untested. No dependencies were installed. Review sheets, stress fixtures and reports are local task artifacts outside the public repository.

**M4 awaits visual approval. M5 has not begun. No staging, commits or pushes.**

## M1 — complete and approved, 2026-10-01

The approved corrected R3-B technical treatment is canonical. Its SVG paint attributes and element order match the approved temporary candidate exactly; only descriptive metadata, comments and stable IDs changed. The primary colorful faceted duck is unchanged.

Canonical SHA-256:

```text
geometric-duck.svg
5321a3c82a1a367e77c9c5714556df73328bb694c22243af43088e47b8ff7d5f
technical-line-duck.svg
05c2c0209e685436be4ef75fd578bd98540975e2f7411ee4b1d9dff05cc643b4
```

### Structural and geometric checks

- SVG XML, 256-unit viewBoxes, dimensions, accessible names, IDs, local references and canonical colors pass. Neither master needs fonts, raster images, scripts or external resources.
- The shared outer path and eye geometry match. Twelve filled facets tile 15,754 square units; 31,208 sample points reveal no gaps/overlaps. Filled source and palette tokens remain byte-for-byte unchanged.
- Technical base vertices derive from the filled construction. The accent counter ends at an existing line intersection, not a relocated vertex. Each accent segment lies on an existing base segment.
- **All four A-key segments are Ochre in the actual canonical SVG:** two rising left-leg segments, the entire descending right leg, and the crossbar. The lower-body P path is covered by the same Ochre geometry. The accent group is last, with no later Ink overpainting.
- The bill polygon uses the exact existing bill points and canonical Ochre; it is the only filled technical polygon. Head, eye and remaining construction stay Ink. The 2-unit base and 2.2/2.4-unit accent weights preserve the approved treatment.
- Silhouette bounds remain `(32,44)`–`(220,210)`, with 26.87 units of nominal circular-crop clearance before stroke.

### Rendering and practical limits

Rendered again in installed Edge/Chromium `154.0.4258.48` through Playwright at device scale factor 1. Page HTTP(S) requests were blocked; no page errors occurred. Sixteen PNG dimensions passed: both masters at 16/24/32/48/64/128/256 px, plus technical 512/768 px. Render-source hashes prevent stale results. The canonical core review was visually inspected; the technical rendering retains the approved complete A and bill.

Filled use is recommended from 32 px; 24 px is contextual and 16 px remains a stress test. Full technical use is recommended from 128 px. Small-size derivatives require separate review. Direct-on-Ink use of the unchanged filled master loses dark facets; M2 must adapt derivative facets without changing the primary source. One browser engine is verified, not every renderer or live GitHub.

All thirteen documented contrast pairings were rerun. Ink/Paper is 13.1456:1; Slate/Paper 5.6425:1; Ink/Ochre 5.4599:1; Ink/Mist 7.6567:1. Ochre/Paper is 2.4077:1: the approved logo accent is intentionally subtle and must not become essential diagram text. See [PALETTE.md](palette/PALETTE.md) for all pairings and W3C references. No palette values changed.

### Reproduction

```text
python brand/tools/validate-core.py
node brand/tools/render-core.cjs "<review-output-directory>" "<browser-executable>"
python brand/tools/validate-core.py --renders "<review-output-directory>"
```

The validator uses Python's standard library. The renderer requires Node.js, Playwright via module resolution or `NODE_PATH`, and an available Chromium-family browser. It does not install dependencies. Keep review output outside the repository. Inspect native-size images after automated checks.

## M2 boundary

M1 canonicalization and validation finished before M2 implementation began. The user authorizes M2 to develop both the colorful primary expression and complementary technical/institutional family. M2 stamp/avatar variants require a review sheet before being treated as final; M3 remains unauthorized. No commits, pushes or GitHub settings changes are authorized.

## M2 — candidates ready for visual review, 2026-10-01

Eleven candidate SVGs were built from the canonical sources: four stamp treatments, one PF monogram and six avatars. Both M1 SHA-256 values above still match; the primary geometry and palette tokens were not changed. Candidate status, source hashes and deliberate facet substitutions are recorded in [M2_MANIFEST.json](review/M2_MANIFEST.json). See [M2_REVIEW.md](M2_REVIEW.md) for the full asset inventory and usage findings.

### Checks completed

- All eleven SVGs pass XML parsing, dimensions/viewBox, unique IDs, accessible title/description, local references and canonical palette checks. No scripts, embedded raster images, remote fonts or external references.
- Shared silhouettes and mosaic polygon coordinates match M1. Per-face color substitutions match the manifest. Technical derivatives preserve the PA, neck and brace geometry; the avatar's two deliberate non-PA seam omissions are verified. Stamp metadata uses 2025.
- All six PNG exports are 512 × 512 with fully opaque backgrounds. Upload-size exports use an opaque browser canvas to prevent fractional-alpha raster seams. A separate Pillow inspection verified alpha is 255 throughout all six images.
- Forty-eight square/circular samples pass dimensions at 32/48/64/128 px. A separate pixel inspection of the 24 circular samples found every mark pixel retained at full alpha, allowing an 8/255 channel difference from the background when classifying antialiased pixels.
- Ten preferred/fallback lettering checks (five assets × two font modes) found no text bounding boxes outside the artboards. Preferred Georgia/Segoe UI/Consolas and forced Times New Roman/Arial/Courier New sheets were rendered and visually inspected.
- Family and actual-size avatar sheets were rendered and visually inspected. There were no browser page errors. Source hashes match the render report, preventing stale source/render validation.

Renderer: Edge/Chromium `154.0.4258.48`, device scale 1, HTTP(S) page requests blocked. Review sheets and native-size samples are kept outside the public repository; six avatar PNG candidates are included in `brand/avatars/`.

### Findings and limits

The colorful Paper/Ink/Ochre/Sage avatars remain the main expression. At 32 px their overall facet and silhouette relationships are stronger than the technical alternative. Prefer the technical avatar from 64 px and the seal from 48 px. The full technical master retains its M1 128 px guidance. PA discovery is secondary at avatar sizes.

Round stamps were inspected at 288 px, rectangular labels at 584 px, and PF at 144 px in the family sheet, with larger fallback specimens. Fine stamp lettering belongs in larger institutional uses; it is deliberately omitted from the seal avatar. Exact font metrics and rasterization on other platforms, live GitHub presentation and physical printing remain unverified.

Palette contrast values remain unchanged from M1. All stamp lettering uses Ink on Paper (13.1456:1). Ochre rules and PA details remain decorative logo accents (2.4077:1 on Paper), not essential instructional indicators. Colored avatar facets were judged visually; no claim is made that every adjacent facet pair meets UI contrast thresholds.

### Reproduction

```text
python brand/tools/build-family.py
node brand/tools/render-family.cjs "<review-output-directory>" "<browser-executable>"
python brand/tools/validate-family.py --renders "<review-output-directory>"
```

Generation and structural validation use Python's standard library; browser rendering uses Node.js and Playwright. The one-time alpha/crop pixel audit used Pillow. No dependencies were installed. M2 remains at visual review; these successful checks do not constitute user approval of the variants.

## M2 expressive refinement — review pending, 2026-10-01

Added two aged rectangular impressions and one drafting system shown standalone and with the round seal. The focused sheet contains those four additions and two unchanged clean controls. All **21 existing clean SVG/PNG and palette files** match both the expressive manifest and an independent SHA-256 baseline captured before refinement. No canonical master or clean M2 asset was rewritten.

- Four derivative SVGs pass XML, accessible title/description, unique IDs, local references and palette checks. Black/white values occur only inside luminance masks. No raster textures, external resources, scripts or filter effects.
- Aged label element geometry, text, font attributes, positions and hierarchy match the clean rectangular source after accounting for monochrome pigment and mask references. Ink and Ochre derivatives use identical wear masks. Date remains `EST. 2025`.
- The standalone construction duck's full SVG paint/geometry tree matches the canonical technical source. The round composition retains the exact clean Ochre-detail seal elements beneath the additional drafting groups. The main circle is verified against its crown/body diameter endpoints.
- Repeating generation yields byte-identical four derivative SVGs and manifest. The fixed seed and construction anchors are recorded in `review/M2_EXPRESSIVE_MANIFEST.json`.
- Rendered in Edge/Chromium `154.0.4258.48` at device scale 1 with HTTP(S) requests blocked and no page errors. Six detailed specimens pass PNG dimensions: three 1280 × 640 rectangular impressions, clean round 1024 × 1024, standalone construction 1008 × 1008, and round construction 1344 × 1344. The six-panel sheet is 1600 × 2232.
- Lettering bounds pass for both aged impressions and the derived round seal; review-sheet content stays inside its width. The sheet, Ochre impression and both drafting presentations were visually inspected at useful detail sizes.
- A separate Pillow pixel comparison found no added pigment over previously blank paper in either aged impression (1/255 clean-background tolerance, 3/255 changed-pixel tolerance). Wear is therefore contained to the existing impression footprint in the tested raster renders.

The worn-rule enlargements show controlled contact losses; type remains readable. Construction is intentionally faint at reduced sizes and is a larger presentation treatment, not an avatar. Ochre-on-Paper remains the already documented low-contrast logo pairing; choose the clean Ink label for functional small text. System-font and other-renderer differences remain possible. Physical rubber-stamp manufacture/printing and live GitHub rendering were not tested.

Reproduction commands and the full treatment rationale are in [M2_REVIEW.md](M2_REVIEW.md). The derivatives await visual approval; M2 is still open and M3 has not begun.

## M2 expressive intensity revision — review pending

Revision `controlled-intensity-2` increases contact variation across the entire stamp impression and strengthens the drafting hierarchy. Each construction study has exactly one canonical Ochre four-point registration marker. The previous derivative SVGs are preserved separately for the before/after sheet; the preceding record describes the earlier, lighter treatment.

The four revised SVGs pass structural, palette, reference and geometry validation. All 21 clean assets/tokens still match the independent pre-refinement baseline. Canonical technical duck paint/geometry and the clean round seal elements are exact; only derivative masks and surrounding drafting treatments changed. Repeated generation produces identical SVGs and manifest. The Ink/Ochre impressions share identical mask definitions.

The renderer verifies both old and new source hashes, lettering bounds and sheet bounds. The **1600 × 2727** sheet shows all four before/after pairs plus 2× details of revised lettering and duck. Six detailed specimen PNG dimensions pass. Rendered in the same Edge version at device scale 1, without page errors or remote resources. The sheet and enlarged stamp impression were visually inspected: lettering remains readable, major drafting relationships are visible at review size, and secondary guides recede behind the duck. The requested 25–35% apparent-strength range is a visual target, not a measured opacity or a certified perceptual ratio.

A fresh Pillow pixel audit found no new pigment over clean Paper in either aged impression (1/255 background tolerance; 3/255 change tolerance). Pixel changes were confirmed in the main name, tagline, date, duck, borders and short secondary rule. These checks establish coverage of the requested components and preserve the blank field; they do not replace judgment of the physical impression.

The existing limitations still apply: no physical printing, live GitHub or alternate-browser test, and system-font rasterization may differ. M2 remains open for visual review. No M3 work, commits or pushes.

## M2 approval finalization — 2026-10-01

M2 is complete. The complete clean family and final `controlled-intensity-2` derivatives are approved. Descriptive M2 SVG metadata and manifest/generator/validator status were canonicalized; recursive paint-tree comparisons confirm every shape, font attribute, color, mask, layer order and transform matches the approved files. The six avatar PNGs, palette and both M1 sources remain byte-identical. Structural validators pass against approved status. Prior render reports remain historical evidence tied to their pre-approval metadata hashes; no visual assets were redesigned. M3 is authorized; M4 is not.

## M3 organization profile — visual review ready

Built the actual `profile/README.md` and two necessary responsive header SVGs, reusing the approved construction study by relative path. All 25 M1/M2 asset/token files match the post-approval baseline. Header duck paint trees match the canonical filled source exactly. SVG structure, palette, local references, Markdown image paths and alt text pass.

Rendered in Edge/Chromium `154.0.4258.48` through local `marked` and Playwright. Ten width/theme checks (320/390/600/601/1024 px × light/dark), four preferred/fallback header-font checks and an image-free copy check passed without page errors or horizontal overflow. Desktop/narrow light/dark compositions and fallback lettering were visually inspected. Core text remains native Markdown. Explicit Paper fields make extra dark variants unnecessary.

The preview uses illustrative GitHub-style framing and is not a live GitHub verification. Publication, remote path rewriting/sanitization, organization visibility and other rendering engines remain untested. Full findings, official compatibility references, inventory and reproduction commands are in [PROFILE_REVIEW.md](PROFILE_REVIEW.md). No M4 work, uploads, commits or pushes occurred. M3 awaits user approval.
