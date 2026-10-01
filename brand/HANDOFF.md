# Brand System v1 — final handoff

**M5 COMPLETE / BRAND SYSTEM V1 APPROVED.** This repository is the source of truth for the identity and its first GitHub applications. It contains no website implementation or rollout to other repositories. Commit, branch push and a PR against `main` are authorized. Merge and deployment actions remain outside this publication step.

## Canonical hierarchy

1. **Geometric Impossible Duck:** primary colorful mosaic identity. Preserve silhouette, proportions, facets and the Ink/Sage/Mist/Ochre/Rust relationships of the approved family. Use the original on Paper/white; use the approved light-facet avatar adaptation on Ink.
2. **Technical PA duck:** complementary technical/research expression. Both A legs and the shared counter are Ochre, as is the triangular beak. The P shares construction edges; head, eye and other geometry remain Ink. Do not transfer PA lines into the filled master.
3. **Round Lab Stamp and rectangular Lab Label/Stamp:** complementary institutional forms; both are retained in Ink and restrained Ochre-detail treatments. Neither replaces the primary duck.
4. **PF monogram:** subordinate compact typographic device.
5. **Construction and aged derivatives:** purposeful larger presentations. Construction preserves the clean underlying mark with hierarchical guides and one Ochre registration marker. Aged masks vary deposited pigment only, leaving Paper pristine.

`EST. 2025` is secondary institutional metadata. The signature-wing exploration is not selected for the canonical technical mark. No historical alternative should be promoted over the approved assets below.

## Asset inventory

Dimensions refer to SVG artboards unless PNG is specified. All linked visual files are approved applications or derivatives except the explicitly fictional/template fixtures.

| Class | Assets | Role / dimensions |
| --- | --- | --- |
| Hand-authored canonical sources | [Geometric duck](source/geometric-duck.svg), [technical PA duck](source/technical-line-duck.svg) | 256 × 256; immutable inputs to family generation |
| Generated clean masters | [Round Ink stamp](source/round-stamp.svg), [rectangular Ink stamp](source/rectangular-stamp.svg), [PF](source/pf-monogram.svg) | 512 × 512; 640 × 320; 256 × 256 respectively |
| Clean production derivatives | [Round Ochre detail](stamps/round-stamp-ochre.svg), [rectangular Ochre detail](stamps/rectangular-stamp-ochre.svg) | Same dimensions as their Ink masters; restrained accents |
| Colorful avatar SVGs | [Paper](avatars/duck-cream.svg), [Ink](avatars/duck-ink.svg), [Ochre](avatars/duck-ochre.svg), [Sage](avatars/duck-sage.svg) | 256 × 256; primary recognizable expression |
| Colorful avatar exports | [Paper PNG](avatars/duck-cream.png), [Ink PNG](avatars/duck-ink.png), [Ochre PNG](avatars/duck-ochre.png), [Sage PNG](avatars/duck-sage.png) | 512 × 512 opaque; Paper is the recommended organization default |
| Secondary avatars | [Technical SVG](avatars/duck-line.svg), [seal SVG](avatars/duck-seal.svg), [technical PNG](avatars/duck-line.png), [seal PNG](avatars/duck-seal.png) | SVG 256 × 256; PNG 512 × 512; simplified, purpose-specific derivatives |
| Aged production derivatives | [Aged Ink](derived/rectangular-stamp-aged-ink.svg), [aged Ochre](derived/rectangular-stamp-aged-ochre.svg) | 640 × 320; deterministic physical-impression masks |
| Construction derivatives | [Technical construction](derived/technical-construction.svg), [round construction](derived/round-stamp-construction.svg) | Explicit Paper presentations; keep whole artboards and generous surrounding guides |
| Organization application | [README](../profile/README.md), [wide label](../profile/assets/lab-header.svg), [compact label](../profile/assets/lab-header-compact.svg) | Wide 1040 × 256; compact 400 × 248; reuses technical construction at 192 px |
| Project system template | [Editable anatomy SVG](social/social-preview-template.svg), [input examples](social/examples.json), [output manifest](social/manifest.json) | 1280 × 640 layout; template placeholder is not an upload asset |
| Fictional project fixtures | [Number Puzzle](social/example-number-puzzle.png), [Game Companion](social/example-game-companion.png), [Data Tool](social/example-data-tool.png), [Simulation Lab](social/example-simulation-lab.png) | Four 1280 × 640 PNGs and same-stem editable SVGs; demonstrate the approved system, not real project identities |
| Palette | [Tokens](palette/palette.json), [contrast/roles](palette/PALETTE.md) | Exact eight-color source and usage restrictions |
| Evidence/maintenance | [Tools](tools), [approval manifests](review), [v1 hashes](review/V1_INTEGRITY.json), [validation](VALIDATION.md) | Reproduction, approval boundaries and integrity; not visual assets |

### Review-only artifacts

HTML mockups, screenshots, native-size ladders, font substitutions, stress-test cards, before/after sheets, reading keys and unsuccessful M1 alternatives live in the task's external review directories. They are evidence, not canonical identity or deployment files. They are not needed to regenerate approved sources. In particular, explanatory PA highlights must not be copied into the canonical mark.

`brand/social/example-*` and the anatomy template are intentionally shipped as reproducible fictional fixtures. The design system is approved, but their fictional text and diagrams must not be uploaded to real repositories as though they described those projects. Public production READMEs must not link to a local review directory.

## Palette and type

| Ink | Paper | Sage | Mist | Ochre | Rust | Slate | Rule |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `#102A36` | `#F5F0E6` | `#628580` | `#AFBDB5` | `#C49449` | `#BA6041` | `#52616A` | `#C7CBC5` |

Use Ink/Paper for primary text (13.1456:1) and Slate/Paper for supporting text (5.6425:1). Ochre/Paper is 2.4077:1: it is an identity/detail pairing, not normal text or an essential interface indicator. Sage/Rust/Paper combinations have documented restrictions; never assume a brand accent is automatically a readable text color. Give required meaning in words and not only in color. This is not a blanket WCAG certification.

Headings: `Georgia, 'Times New Roman', serif`. Body/labels: `'Segoe UI', Arial, Helvetica, sans-serif`. Sparse study metadata: `Consolas, 'Liberation Mono', monospace`. No font binaries or remote fonts are included. Generic and alternate stacks were checked, but metrics vary; render new compositions before use. Keep README content as real Markdown and supply alt text for informative images.

## Project identity model

The generator is a lightweight identity system: the lab fixes visual grammar and projects provide controlled content. Name and descriptor are required; category, one canonical accent, Paper/Ink field, meaningful identifier and one study motif are optional inputs. Typography roles, margins, parent attribution, duck geometry and palette rules remain fixed.

The four fictional fixtures demonstrate a puzzle grid, exploration route, data bars and simulation curve. An empty study field is supported; arbitrary icon import is not. The [complete contract](REPOSITORY_VISUALS.md) includes examples, limits, motif extension guidance and anti-patterns. A project is an experiment within Patitos Fortune, not an independent sub-brand. No identities for existing repositories were made during M5.

## Final QA and limits

All five existing validation suites pass with fresh M5 rendering: core, family, expressive, profile and social. Repeated generation preserves SVGs and manifests. All 37 pre-M5 artwork/input files remain byte-identical, including six avatar PNGs and four social PNGs. The palette document was updated only to remove outdated milestone wording; values and roles are unchanged. Related manifest hashes were explicitly refreshed for that documentation change.

The profile validator now works without a chat-only historical baseline file, while retaining the required repository hash checks. A transient browser export mismatch was resolved by rerendering to the original approved PNG hash. That limitation is documented rather than promising deterministic PNG bytes across every run/platform. See [reproduction commands](REPRODUCING.md) and [validation evidence](VALIDATION.md).

Preserve the following practical limits:

- Full technical mark: prefer 128 px and above; hidden PA discovery is secondary. Prefer colorful avatars at small sizes, technical avatar from 64 px and seal avatar from 48 px. Fine stamp text belongs at larger sizes.
- Small social previews prioritize the title and motif; descriptors/metadata are secondary at 320 px. Essential information must also exist in real page text.
- M3 previews approximate GitHub locally. Live sanitization, relative-path rewriting, organization visibility, actual theme rendering and third-party social cropping/compression still require post-publication checks.
- Physical stamp manufacture/printing, all browser engines, all scripts and emoji, and arbitrary future motifs have not been validated.
- No proprietary font file is required; a compatible rendering runtime is required. Preserve the reviewed PNGs when exact raster appearance matters.

## Manual deployment

Follow [GITHUB_SETUP_CHECKLIST.md](../GITHUB_SETUP_CHECKLIST.md) for the authorized PR workflow and the later deployment actions that still require separate authorization. Organization avatar selection, settings, profile inspection and project social-preview uploads remain human-controlled steps. Do not upload fictional fixtures. This branch has not changed any remote settings or other repository.

## Website handoff

**Next independent stage: PatitosFortune.com / Brand Application Stage.** Use Brand System v1 as the source of truth; do not redesign the duck, replace the palette or create a competing institutional style.

Use the colorful canonical duck for primary recognition, with explicit Paper fields or the approved dark adaptation where needed. Consume `palette.json` as design tokens and preserve text-contrast restrictions. Translate the serif/sans/mono hierarchy into responsive website typography without assuming the current system fonts are available everywhere.

Both clean stamp forms are available for institutional sections; aged and construction treatments belong in restrained notebook/research contexts. Keep clean navigation and readable text ahead of expressive detail. The technical PA mark remains secondary. Use the project-identity grammar for future project listings: project name, descriptor, one accent, relevant motif and small parent-lab attribution.

The website stage should decide information architecture, content, accessible interactions, responsive layouts and performance separately. It can adapt layout to the web while preserving approved geometry and hierarchy. No website code, hosting, domain configuration, new project identities or deployment has been started here.

**Final M5 approval received.** Stop after the authorized commit, branch push and pull request. Do not merge, change organization settings, upload assets or begin website work.
