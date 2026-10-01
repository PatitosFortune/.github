# Patitos Fortune — core identity guide

M1 core identity approved and canonicalized on 2026-10-01. M2 is complete and approved, including all final expressive derivatives. M3 is complete and approved. M4 project/repository visual system is approved; M5 is complete and Brand System v1 is approved for publication. The current marks are deterministic SVG interpretations of the approved reference board, not raster traces.

## Concept and family

**Patitos Fortune / Creative Software Lab** is a small, independent software lab exploring curious ideas and turning them into useful software. The Lab Stamp supplies structure; the Impossible Duck supplies character. Preserve a thoughtful, technical and playful identity through coherent construction and restrained editorial composition.

This is a family of complementary marks. The hierarchy assigns roles; it does not select a winner and discard the others. Preserve both halves of the merged B+C direction: colorful mosaic/faceted recognition on Paper and appropriate palette backgrounds, plus technical/institutional marks for the Lab Stamp system. Ink, Sage, Mist, Ochre and Rust remain active across the family.

| Member | Role | Delivery |
| --- | --- | --- |
| Geometric Impossible Duck | Primary recognition; foundation for avatars, repository and documentation identity | M1 core SVG |
| Round Lab Stamp | Institutional / archival / experimental seal for larger use | M2 approved; Ink and Ochre-detail forms |
| Rectangular Lab Stamp / Label | Research labels, documentation and organization header structure | M2 approved; Ink and Ochre-detail forms |
| PF monogram | Compact typographic secondary identity | M2 approved |
| Technical line duck | Diagrammatic, construction-oriented companion | M1 core SVG |

**EST. 2025** is the confirmed institutional date. It may appear as secondary metadata in stamps and labels. Never put the date into the primary geometric duck or treat it as the main message. No extra project-origin story is needed in public brand assets.

## Primary mark

Use [geometric-duck.svg](source/geometric-duck.svg) as the canonical geometry. Its reference anchor is the far-right standalone duck in section A of the approved board. Preserve the angular tail, low folded body, upright neck, right-facing bill, and restrained locator eye. No expressions, wings in motion or mascot features.

The master has a transparent 256 × 256 artboard, with nominal silhouette bounds from `(32,44)` to `(220,210)`. Its width is 188 units and height 166 units. The silhouette is centered optically close to `(128,128)`; do not recenter the colored mass independently in different family members.

Twelve named polygon faces tile the silhouette. A local silhouette clip and matching 0.5-unit facet strokes overlap adjacent fills to suppress raster seams without enlarging the outer shape. No external dependencies, images, fonts, gradients or scripts are present in either SVG. Never auto-trace a PNG export to make a derivative.

Six palette colors appear in the filled mark: ink, paper, sage, ochre, rust and slate. Slate forms one cool neck shadow. The paper back plane is deliberately quiet on paper. Keep the large sage wing and small rust fold in their existing relationship; do not shuffle colors per polygon to create arbitrary variants.

## Technical companion

Use [technical-line-duck.svg](source/technical-line-duck.svg) as the approved complementary secondary mark. The corrected R3-B treatment is canonical as of 2026-10-01. The colorful faceted duck remains the primary Patitos Fortune identity: the technical PA treatment must never collapse the overall system into Ink/Ochre alone.

The technical mark retains the shared silhouette, vertices, eye and body construction. Its base strokes are 2 units of Ink. The approved complete A and shared P counter use Ochre: the rising left leg and counter are 2.4 units, and the descending right leg is 2.2 units. These accent overlays follow existing edges. The sole filled shape is the approved triangular bill in Ochre; its Ink boundary, unfilled head, eye and surrounding construction remain intact.

### Canonical hidden P / A

Both readings now live in the **lower body**, superseding the earlier head/neck P proposal.

- **Left leg / shared P stem:** `(86,210) → (124,168) → (154,136)` is entirely Ochre.
- **Right A leg:** `(154,136) → (160,210)` is entirely Ochre.
- **Counter / crossbar:** the triangle `(124,168) → (154,136) → (156.521348,167.096629) → (124,168)` is Ochre. The final point is the existing brace/fold intersection, not a moved construction vertex.
- **P reading:** follow the same rising diagonal to the apex, down to the brace intersection, then back to the wing hinge. Its bowl is oblique; the A is asymmetric. Do not typeset, straighten or geometrically perfect these readings.

The candidate was promoted without visual changes: only descriptive metadata, stable IDs and comments changed. All four A reading-key segments and the shared P path are checked against the actual Ochre strokes by `validate-core.py`. Rust reveal diagrams are explanatory only; the approved production accent is Ochre. The parked signature-wing concept is not part of the canonical mark.

Do not add permanent drafting circles/grids to the canonical source. The M2 construction study keeps anchored guides in a separate expressive derivative. For smaller applications, a reviewed derivative may simplify seams or adapt stroke weight; keep the shared silhouette and complete PA relationship. The full master remains intended for 128 px and larger. Ink-only stamp treatments are explicit monochrome derivatives of this approved geometry, never replacements for the canonical two-color source.

## Size, spacing and background rules

All sizes below refer to the full 256-unit artboard scaled to the given pixel width, not the silhouette alone.

| Treatment | Guidance from actual browser renders |
| --- | --- |
| Filled, 32 px and larger | Recommended minimum for an independent mark; the principal facets remain distinguishable |
| Filled, 24 px | Contextual use next to the name; eye and narrow facets are no longer reliable details |
| Filled, 16 px | Recognition stress test only; not approved as a finished standalone favicon in M1 |
| Line, 128 px and larger | Recommended minimum for the full technical master; at 128 px the stroke is 1 px |
| Line, 64 px and below | Too thin for reliable primary identification; use the filled mark |

Keep at least **24 source units** of clear space outside the silhouette (one eighth of its width rounded up). The supplied artboard already provides at least that much on all sides. Do not add the same allowance a second time when using the whole artboard. Neighboring labels must sit outside that protected space.

Use an 8-unit layout rhythm for related rules, labels and margins; optical corrections to typography are allowed. Preserve aspect ratio. For circular use, retain the whole square artboard: the farthest silhouette vertex sits 26.87 units inside the centered 128-unit radius. M2 avatar crops were checked at 32/48/64/128 px with no mark clipping.

Use the filled mark on paper or white. On a dark page, give it a paper field. The unchanged filled mark placed directly on ink loses its dark structure. Keep that canonical master unchanged; the separate M2 Ink avatar uses appropriate light/Paper facet substitutions with the same recognizable geometry. The technical SVG uses Ink/Ochre and requires a light field; reverse treatments must be explicit. Do not rely on GitHub or a browser to recolor an external SVG automatically.

At tiny sizes, a later reviewed derivative may omit the eye or merge narrow facets. It must preserve silhouette proportions, tail/body/neck/bill relationships and the broad wing/fold division. Do not add an outline to the primary filled master to solve every background problem.

## Palette

Use the exact values and pairing restrictions in [PALETTE.md](palette/PALETTE.md), backed by [palette.json](palette/palette.json). Ink/paper and slate/paper are the default text pairings. Ochre is a small warm detail; sage and mist are supporting fields. Rust should remain restrained. No bright yellow or metallic gold substitutes.

## Typography

| Function | Stack | Starting rules for future compositions |
| --- | --- | --- |
| Editorial / institutional heading | `Georgia, 'Times New Roman', serif` | Regular weight, 24–40 px; 1.15–1.25 line height; 0–0.04em tracking |
| Technical label / body | `'Segoe UI', Arial, Helvetica, sans-serif` | Body 14–16 px, line height 1.5; short uppercase labels 12–14 px with 0.16–0.22em tracking |
| Sparse specimen metadata | `Consolas, 'Liberation Mono', monospace` | 12–13 px; normal tracking; avoid blocks of decorative code |

These are layout starting points, not a fixed wordmark created in M1. Use sentence case for descriptive copy and spaced uppercase only for short labels. Increase space around labels instead of tracking entire sentences. Keep supporting metadata smaller than the lab name. Do not put fine text in primary avatars.

Georgia, Segoe UI, Arial and Consolas were available in the validation environment. The browser-rendered specimen uses the serif/sans/mono roles without font downloads. M2 lettered marks were also rendered with Times New Roman, Arial and Courier New fallbacks; no text exceeded its artboard. Other platforms may vary. No font binaries are included, and users are not required to obtain a proprietary font file. GitHub README text stays in GitHub's native typography.

Editable templates should keep editable text and document the stack. If a finished lockup later needs outlined lettering for portability, preserve its editable source and keep readable titles/alt text. Do not introduce an opaque outlined-only workflow.

## Approved M2 family

See [M2_REVIEW.md](M2_REVIEW.md) for all eleven approved SVGs, six 512 px PNG exports and the exact facet substitutions. These variants are approved. Both round and rectangular stamps exist in Ink and restrained Ochre-detail forms, with secondary `EST. 2025` metadata. The PF monogram remains subordinate to the duck.

Paper, Ink, Ochre and Sage avatars preserve the colorful mosaic expression. Paper retains all canonical facet colors; the dark adaptation substitutes light Paper/Mist planes to maintain recognition. These derivative treatments do not alter the filled master. The text-free seal also uses the colorful duck.

The technical avatar retains the complete Ochre PA and beak, with stronger strokes and two non-PA diagonals omitted. Prefer the colorful avatars at 32 px and above; the technical avatar is clearer from 64 px and the seal from 48 px. Keep the entire square artboard for circular display. Lettered stamps belong at larger sizes, not inside tiny avatar crops.

The user-endorsed clean family is also the source for four approved expressive derivatives: aged Ink/Ochre rectangular impressions, a standalone technical construction study and a round-seal construction presentation. Keep these separate from clean masters. Stamp wear uses repeatable vector masks across deposited lettering, rules, date and duck; Paper remains pristine. Construction uses stronger major relationships, quieter secondary guides and one small Ochre registration marker per study. All guides and markers must correspond to real vertices, bounds or registration geometry. See the method and candidate links in [M2_REVIEW.md](M2_REVIEW.md). The full expressive treatment, including its final revised intensity, is approved.

## Supporting visual language and future applications

### M3 organization-profile application

The approved [organization README](../profile/README.md) uses the colorful duck in a clean Paper lab-label header, followed by the exact public description in native Markdown. Wide and compact header compositions share the approved geometry, palette and typography; the compact layout is selected through a native picture source. The Paper field preserves the same identity in light and dark themes.

One approved technical construction study appears below the concise area copy as a notebook signature. Do not add the other stamps, PF or multiple avatars simply to display the inventory. This application is approved. See [PROFILE_REVIEW.md](PROFILE_REVIEW.md) for files, GitHub compatibility sources, local rendering evidence and limits.

Use thin rules, measured spacing and occasional drafting lines. Paper is primarily a flat field; texture is optional in later presentation artwork and never essential to recognition. Alchemical references must remain subtle. Do not surround every mark with a star, grid, coordinate and seal.

Both approved round and rectangular stamp forms remain in the system, with Ink structure and restrained Ochre-detail counterparts. The PF monogram is a secondary typographic mark, not an alternate organization replacing the duck. The approved organization profile uses a shallow lab-label header and real text. M4 social previews use a shared 1280 x 640 framework; repositories are different experiments from the same lab.

## Incorrect use and correction

| Avoid | Use instead |
| --- | --- |
| Stretching the neck, widening the body or independently resizing the bill | Scale the whole square artboard uniformly |
| Recoloring arbitrary facets for every project | Keep the master; vary a surrounding field or approved accent |
| The unchanged ink-filled duck directly on an ink background | A paper field or the approved M2 Ink avatar treatment |
| Shrinking a full technical duck or text-heavy stamp into a tiny avatar | The filled duck; a specifically reviewed simplified derivative where needed |
| Bright gold, gradients, mascot eyes, arbitrary grunge or drop shadows | Flat muted palette and clean geometry; controlled stamp wear only in documented expressive derivatives |
| Placing `EST. 2025` inside the primary duck | Secondary institutional metadata in a stamp/label |
| Discarding one stamp shape after choosing a primary avatar | Retain both stamp forms in their complementary roles |

## Current file inventory and maintenance

| File | Purpose |
| --- | --- |
| [source/geometric-duck.svg](source/geometric-duck.svg) | Canonical filled mark; source for later family compositions |
| [source/technical-line-duck.svg](source/technical-line-duck.svg) | Technical companion sharing the same geometry |
| [palette/PALETTE.md](palette/PALETTE.md) | Color roles, measured contrast and restrictions |
| [palette/palette.json](palette/palette.json) | Exact reusable palette tokens |
| [tools/validate-core.py](tools/validate-core.py) | Standard-library SVG geometry, palette and contrast checks |
| [tools/render-core.cjs](tools/render-core.cjs) | Local browser review sheets and native-size QA renders |
| [VALIDATION.md](VALIDATION.md) | M1/M2 evidence, reproduction commands and known limits |
| [M2_REVIEW.md](M2_REVIEW.md) | Approved inventory, derivative mappings and usage |
| [review/M2_MANIFEST.json](review/M2_MANIFEST.json) | Approved roles, dimensions, source hashes and facet substitutions |
| [tools/build-family.py](tools/build-family.py) | Deterministic stamp, monogram and avatar derivation |
| [tools/render-family.cjs](tools/render-family.cjs) | Family/fallback review sheets and six 512 px PNG exports |
| [tools/validate-family.py](tools/validate-family.py) | Candidate SVG, shared geometry, palette and export checks |
| [PROFILE_REVIEW.md](PROFILE_REVIEW.md) | M3 presentation, relative-path rules, theme/narrow checks and preview limits |
| [review/M3_MANIFEST.json](review/M3_MANIFEST.json) | M3 review status, header inventory and protected M2 source hashes |
| This guide | Core usage, typography and family commitments |

The helpers make core geometry and candidate derivation reproducible; they do not replace visual judgment. Review PNGs and temporary HTML are kept outside the public repository. Six approved M2 avatar PNGs are included in `avatars/`; four M4 fictional social-preview PNGs are included in `social/` for review.

When changing the geometry, update the technical companion in the same edit, run the validator, regenerate review renders, inspect them at native size and update [STATUS.md](../STATUS.md). Recheck downstream compositions once they exist. Stop at the milestone review gate; no automatic GitHub uploads, commits or pushes.

## Approved M4 project and repository application

The [repository visual guide](REPOSITORY_VISUALS.md) defines a reusable specimen-label system with a prominent project name, concise descriptor, one project study and small colorful lab attribution. Paper cards reuse the exact primary duck; Ink cards reuse the approved M2 dark avatar. The project accent never recolors the lab mark. The technical PA, PF and stamp family remain supporting options for relevant large documentation contexts.

Four clearly fictional examples and the anatomy template are in `social/`. Fixed typography/grid/attribution coexist with variable category, title, descriptor, catalogue ID, one palette accent and illustration. The guide includes the JSON contract, generation and validation commands, font limits, export requirements and restrained README use. This application is approved. It is also a lightweight project-identity generator: fixed lab grammar plus controlled project inputs, without independent sub-brands. M5 consolidates the system; other-repository edits and uploads require later authorization.
