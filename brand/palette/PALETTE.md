# Patitos Fortune palette

Canonical Brand System v1 palette, approved in M1 and preserved through M5. The M0 proposed values are retained after browser rendering and contrast measurement. The machine-readable source is [palette.json](palette.json); SVGs use its literal HEX values to remain standalone.

| Role | Token | HEX | Use |
| --- | --- | --- | --- |
| Primary | Ink | `#102A36` | Main text, dark facets, outline mark, dark fields |
| Primary | Paper | `#F5F0E6` | Default field, pale folded plane, reverse text |
| Secondary | Sage | `#628580` | Broad wing and neck planes; controlled project fields |
| Secondary | Mist | `#AFBDB5` | Quiet secondary fields and approved light treatments |
| Accent | Ochre | `#C49449` | Head plane, PA/beak accents and stamp details |
| Accent | Rust | `#BA6041` | Single folded body plane; restrained project accents |
| Neutral | Slate | `#52616A` | Supporting text on paper; a single shadow plane on the neck |
| Neutral | Rule | `#C7CBC5` | Decorative separators and nonessential drafting guides |

## Interpretation and normalization

The reference board is a shaded raster composition, not a flat-color specification. These colors preserve its visual relationships without treating printed color labels as authoritative or claiming sampled pixel values. Paper replaces texture with a flat cream; ink replaces several nearly black shades. Sage and slate express the cool folded planes, and ochre/rust supply muted warmth. Mist remains part of the broader family; every token need not appear in the primary duck.

No accessibility-driven HEX changes were necessary for the intended text pairings. Restrict applications instead of saturating or darkening every accent. The slate neck plane is an intentional use of an existing neutral, not a new navy tint. Do not add gradients, metallic gold, grain, or random near-duplicate colors to the core marks.

## Measured pairings

Calculated from sRGB values using relative luminance and `(lighter + 0.05) / (darker + 0.05)`. Linearize each normalized channel with `c / 12.92` when `c <= 0.04045`, otherwise `((c + 0.055) / 1.055)^2.4`; luminance weights are `0.2126`, `0.7152`, `0.0722`.

Decisions use unrounded results. Displayed ratios are rounded to two decimals. The table is symmetric: reversing foreground and background preserves the ratio.

| Pair | Ratio | Normal text ≥ 4.5 | Large text / essential graphics ≥ 3 |
| --- | ---: | :---: | :---: |
| Ink / Paper | 13.15:1 | Pass | Pass |
| Slate / Paper | 5.64:1 | Pass | Pass |
| Ink / Ochre | 5.46:1 | Pass | Pass |
| Ink / Mist | 7.66:1 | Pass | Pass |
| Ink / Rule | 9.08:1 | Pass | Pass |
| Ink / Sage | 3.69:1 | Fail | Pass |
| Ink / Rust | 3.44:1 | Fail | Pass |
| Ink / Slate | 2.33:1 | Fail | Fail |
| Sage / Paper | 3.57:1 | Fail | Pass |
| Rust / Paper | 3.82:1 | Fail | Pass |
| Ochre / Paper | 2.41:1 | Fail | Fail |
| Mist / Paper | 1.72:1 | Fail | Fail |
| Rule / Paper | 1.45:1 | Fail | Fail |

Use ink on paper for primary copy and slate on paper for supporting copy. Use paper on ink for reverse copy. Ochre and mist fields can carry ink text. Place small labels beside sage/rust fields on paper instead of on the color. Use ink for essential drafting geometry on paper; pale rules and ochre details must remain decorative.

These thresholds follow [W3C text contrast guidance](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) and [non-text contrast guidance](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html). Large text means at least 24 CSS px regular or approximately 18.67 CSS px bold. Logo facets are not an information chart: this table is guidance for surrounding text and functional diagrams, not a claim that every neighboring logo plane meets 3:1 or that the whole system is WCAG certified.

## Restraint and backgrounds

- Paper and ink establish the composition. Use one leading accent outside the mark per layout.
- The duck's ochre head and rust fold are geometry, not a license to repeat bright accents throughout a page.
- On paper, the pale back plane intentionally merges with the field; the angular wing and neck carry recognition. The line duck shows the full constructed boundary.
- The filled master is approved for paper or white fields. It loses dark planes directly on ink; use a Paper panel or the approved M2 Ink avatar with its deliberate light-facet substitutions.
- The technical master uses Ink construction plus the approved Ochre PA and beak on a transparent background. Use it on Paper. Its Ochre logo accent is intentionally subtle, not a functional diagram indicator or text color. Future reverse treatments must adapt all strokes, the eye and beak deliberately and be visually checked.
- Do not use color alone to distinguish projects or convey status. Pair project variations with their written names and descriptive text.

Recompute ratios with `python brand/tools/validate-core.py` from the repository root whenever a token changes.
