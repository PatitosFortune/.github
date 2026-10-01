# M2 — stamp and avatar review

Approved 2026-10-01. **M2 COMPLETE / M3 AUTHORIZED.** The complete family and final controlled-intensity-2 expressive derivatives are approved. The colorful geometric duck remains primary. All five complementary family members remain in the system.

The user strongly endorsed the clean M2 direction and the expressive direction, then requested one controlled intensity increase before final approval. The clean assets are preserved. The current refinement strengthens aged impressions and construction visibility without replacing any family member.

## Review inventory

| Approved asset | Editable SVG | Intended role |
| --- | --- | --- |
| Round / Ink | [Round stamp](source/round-stamp.svg) | Institutional seal with monochrome technical geometry |
| Round / Ochre detail | [Round stamp with detail](stamps/round-stamp-ochre.svg) | Approved PA/beak accents and one fine Ochre ring |
| Rectangular / Ink | [Lab Label](source/rectangular-stamp.svg) | Research and documentation label |
| Rectangular / Ochre detail | [Lab Label with detail](stamps/rectangular-stamp-ochre.svg) | Ochre inner rule, short rule and canonical PA/beak accents |
| PF | [Monogram](source/pf-monogram.svg) | Secondary editorial mark, octagonal frame and small duck silhouette |
| Paper / Cream | [SVG](avatars/duck-cream.svg) · [512 px PNG](avatars/duck-cream.png) | Recommended default; unchanged primary facet colors |
| Ink / Navy | [SVG](avatars/duck-ink.svg) · [512 px PNG](avatars/duck-ink.png) | Light-facet mosaic adaptation for a dark field |
| Ochre | [SVG](avatars/duck-ochre.svg) · [512 px PNG](avatars/duck-ochre.png) | Warm field with selective light facets |
| Sage | [SVG](avatars/duck-sage.svg) · [512 px PNG](avatars/duck-sage.png) | Cool field with Mist wing separation |
| Technical PA | [SVG](avatars/duck-line.svg) · [512 px PNG](avatars/duck-line.png) | Simplified secondary avatar; complete PA and Ochre beak |
| Faceted seal | [SVG](avatars/duck-seal.svg) · [512 px PNG](avatars/duck-seal.png) | Colorful duck within two quiet rings; no tiny lettering |

The round and rectangular forms are both retained. The date is secondary `EST. 2025`. Ink stamp versions are explicit monochrome derivatives; they do not replace the approved two-color technical source. The Ochre treatments retain its complete PA accent. All institutional lettering remains Ink.

## Controlled derivative changes

The filled and technical M1 sources remain unchanged during M2. All silhouettes and polygon coordinates derive directly from them. Palette substitutions are limited to the following faces; every unlisted face retains its canonical value.

| Avatar | Substitutions |
| --- | --- |
| Paper | None |
| Ink | Tail → Mist; keel → Paper; breast → Mist; neck-front → Paper; neck-plane → Sage; neck-fold → Mist; crown → Paper; bill → Mist |
| Ochre | Head → Paper; neck-fold → Mist |
| Sage | Wing → Mist; neck-fold → Mist |
| Seal | None; whole duck scaled uniformly inside rings |

The technical avatar thickens the Ink strokes to 4 units and PA strokes to 4.6 units. It omits only the hinge-to-bottom-right and apex-to-breast diagonals that do not form the PA. The full left leg, right leg, counter/crossbar and triangular bill remain unchanged in geometry. The canonical technical SVG is not simplified.

The PF miniature uses the shared silhouette as one Ink shape. No new duck geometry is introduced.

## Practical review findings

- Colorful avatars are strongest at **32 px and above**. Paper is the proposed default, with Ink, Ochre and Sage retained as purposeful companions.
- The technical avatar is clearer from **64 px**. The seal is clearer from **48 px**. Their 32 px samples are stress tests; hidden letter discovery is not expected at these sizes.
- Keep the complete square avatar artboard when uploading; circular previews preserve the mark. PNG exports are opaque 512 × 512 images with intentional backgrounds.
- Round stamps are shown at 288 px and labels at 584 px in the family sheet. Their fine metadata is secondary; use them at substantial sizes, not as tiny avatars. Use the dedicated text-free seal avatar for compact circular applications.
- Lettered SVGs retain editable text with local font stacks. Preferred fonts and a Times New Roman / Arial / Courier New fallback were rendered and checked. Exact cross-platform typography remains variable; no font files are embedded or downloaded.

The review sheet presents the colorful primary family first, then both stamp forms and the compact secondary marks. Separate sheets show square/circular avatar sizes and font fallbacks. Review HTML/PNGs are temporary local artifacts outside the repository.

## Reproduction

```text
python brand/tools/build-family.py
node brand/tools/render-family.cjs "<review-output-directory>" "<browser-executable>"
python brand/tools/validate-family.py --renders "<review-output-directory>"
```

The generator reads the canonical sources and [palette tokens](palette/palette.json), then writes only the M2 approved SVGs and [manifest](review/M2_MANIFEST.json). The renderer needs Node.js, Playwright and an available Chromium-family browser. It writes six upload-size PNG exports into `avatars/` and keeps review sheets and small QA samples outside the repository. The validator uses Python's standard library. See [VALIDATION.md](VALIDATION.md) for evidence and limits.

## M2 approval checkpoint

The complete identity family is approved. Choosing a default avatar does not discard complementary marks or either stamp shape. M3 organization-profile work is authorized; M4 remains gated. No upload, commit or push has occurred.

## Approved expressive derivatives

Four additional SVGs form one focused six-panel sheet alongside the existing clean rectangular Ink label and clean round Ochre-detail seal:

| Addition | SVG | Treatment |
| --- | --- | --- |
| A1 — Aged Ink | [Aged Ink impression](derived/rectangular-stamp-aged-ink.svg) | Monochrome Ink, worn rules, gentle pressure variation, clear lettering |
| A2 — Aged Ochre | [Aged Ochre impression](derived/rectangular-stamp-aged-ochre.svg) | Identical contact pattern in canonical Ochre on Paper |
| Standalone construction | [Technical construction study](derived/technical-construction.svg) | Exact canonical PA duck with subdued Rule/Mist drafting geometry |
| Round relationship | [Round seal + construction](derived/round-stamp-construction.svg) | Existing clean seal retained, quiet interior guides and exterior registration arcs |

These are expressive derivatives in `derived/`. Both canonical ducks, all clean stamps, PF, avatar SVG/PNGs and palette files remain byte-for-byte unchanged. The single-pigment aged impressions intentionally recolor the label's duck together with its type and rules; they do not revise the approved standalone Ink/Ochre technical mark.

### Repeatable stamp wear

`build-expressive.py` uses Python's fixed random seed **20251001** to construct vector luminance masks. Edge-contact losses follow the existing rectangular borders and divider rules; rare short gaps cross a rule. The mask removes pigment only where that pigment already exists. It cannot scatter ink or scratches over blank paper.

The current `controlled-intensity-2` revision places an additional transfer mask over the entire deposited impression in label coordinates. Jittered micro-pores affect the name, tagline, date and technical duck, including their edges. Pore sizes are smaller in the fine tagline and duck than in the main name. Local coverage patches suggest pressure variation; the existing rule-contact mask still supplies small gaps and uneven border transfer. Both colors share precisely the same masks. Paper remains pristine, flat canonical Paper. There are no raster textures, filter noise, displaced paths, altered glyph coordinates or font outlines.

The original sheet retains its 2.8× rule details as history. The current before/after sheet includes **2× revised name, tagline and duck details**, so transfer across the whole impression can be judged. Judge overall readability in the normal-size comparisons as well. Aged Ochre is an expressive logo treatment; retain the clean Ink version for functional small text and labels.

### Drafting geometry and hierarchy

- The main circle has diameter endpoints at crown `(166,44)` and lower-left body `(86,210)`, center `(126,127)` and radius `sqrt(8489)`. Its diagonal extends that exact diameter.
- Alignment guides use the bounding-box center and the crown, bottom, tail and bill coordinates. Ticks identify these existing intersections.
- One compass sweep is centered on the PA apex `(154,136)` and passes through bottom-right vertex `(160,210)`, radius `sqrt(5512)`.
- All guides sit behind the unmodified technical duck. The major broken circle uses a 1-unit Ink stroke at 0.48 opacity; axes use 0.8 units at 0.40; the compass arc uses 0.8 units at 0.38. Secondary Mist guides stay at 0.6–0.65 units. These separate paint levels target a clearly visible but subordinate drafting system, judged visually rather than by a single opacity percentage.
- The round presentation retains the clean Ochre-detail seal's elements and paint. Interior drafting is clipped to radius 154, clear of the existing radius-164 ring and lettering. Exterior guides use the seal center, outer-ring tangents and a radius-256 registration arc derived from its 512-unit artboard.
- Exterior round registration arcs now use 1.5-unit Ink at 0.55 opacity; quieter axes extend from 24 to 648, with tangent guides extending from 46 to 626. These are more confident extensions of the existing system, not changes to the seal.
- Exactly one small four-point Ochre marker appears per study: standalone `(248,127)` on the extended horizontal center axis; round `(592,336)` at the registration circle's rightmost axis intersection. The markers are separate from the duck and clean seal geometry.

The initial sheet shows the clean round seal and its construction presentation. The current intensity sheet shows four previous → revised pairs: Aged Ink, Aged Ochre, standalone construction and round construction. Previous SVGs are preserved in the local review folder. Neither construction presentation replaces the clean round master.

### Reproduce the refinement

```text
python brand/tools/build-expressive.py
node brand/tools/render-expressive.cjs "<review-output-directory>" "<browser-executable>"
python brand/tools/validate-expressive.py --renders "<review-output-directory>"
```

For the before/after sheet, pass a fourth command argument to the renderer: `"<preserved-before-SVG-directory>"`. This directory must contain the four prior derivative SVGs under their original filenames. The renderer records hashes for both generations; it does not overwrite the preserved files.

The [expressive manifest](review/M2_EXPRESSIVE_MANIFEST.json) records the revision, seed, source hashes, geometry anchors, marker positions and review status. Generation/structural validation use Python's standard library; rendering uses the existing Node.js/Playwright setup. The renderer writes the selected review sheet and detailed specimens outside the repository. Repeated generation was byte-identical. See [VALIDATION.md](VALIDATION.md) for preservation and rendering checks.

**Approved:** both final aged impressions, the stronger drafting hierarchy, the extended round-seal study and one Ochre registration marker per composition. Clean masters remain separate. M3 and M4 applications are also approved. M5 verifies and documents the completed family without redesign.

Approval finalization changed only M2 descriptive SVG metadata and manifest/tool status. All SVG paint trees, geometry, lettering, masks and seeds match the approved review. Existing avatar PNGs, palette tokens and both M1 core source files remain byte-identical. Historical review renders stay outside the repository.
