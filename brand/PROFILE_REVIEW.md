# M3 — GitHub organization profile review

**M3 COMPLETE / M4 AUTHORIZED.** The organization-profile presentation is approved. The profile applies the completed identity system; it does not redesign it. At the historical M3 approval checkpoint no publication had occurred. M5 approval now authorizes commit/push/PR publication, but no settings changes or asset uploads.

## Approved presentation

[profile/README.md](../profile/README.md) leads with a Paper laboratory label and the colorful faceted Impossible Duck. Double rules, a divided layout, the established serif/sans roles and secondary `EST. 2025` carry the institutional language. The public description is real Markdown immediately below the image:

> A small, independent software lab.
>
> Exploring curious ideas and turning them into useful software.

One short section names broad areas of exploration. It includes no project names, claims of releases or achievements, links to unverified repositories, counters or badges. The approved technical construction study sits lower in the profile as a small notebook signature. It is the only expressive treatment used here; stamps and PF remain available in the wider family.

## Public files and dependencies

| File | Role |
| --- | --- |
| [README](../profile/README.md) | Concise native Markdown and basic image HTML |
| [Wide header](../profile/assets/lab-header.svg) | 1040 × 256 Paper label; 2.8 KB SVG |
| [Compact header](../profile/assets/lab-header-compact.svg) | 400 × 248 layout preserving name/tagline readability at narrow widths; 3.0 KB SVG |
| [Existing construction study](derived/technical-construction.svg) | Reused directly at 192 px; no duplicate profile asset |

The headers contain exact copies of the canonical colorful duck's paint tree, scaled uniformly. No facet, vertex, palette or source geometry changes. The second header is needed to avoid shrinking all lettering in the wide composition on phones. A native `<picture>` source selects it at viewport widths of 600 px or less; the wide SVG is the `<img>` fallback.

Both layouts and the secondary study carry explicit Paper fields. The profile uses the same approved colors in light and dark mode; no dark master recoloring or extra theme asset is needed. Public files contain no CSS, JavaScript, external font loading, embedded raster image or remote image dependency. Static SVG and the tested system-font fallbacks suffice for this review, so no redundant PNG header was added.

## GitHub compatibility basis

GitHub documents the public organization README in `profile/README.md` inside a public `.github` repository. The profile does not change repository visibility or publish itself. [GitHub organization-profile documentation](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/customizing-your-organizations-profile)

Image paths are relative to the README: `./assets/…` and `../brand/derived/technical-construction.svg`. There are no branch-specific or local-machine URLs. GitHub documents relative image/link rewriting and supports the `<picture>` element. Alt text describes both the institutional header and the notebook study. [GitHub formatting documentation](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

## Render and validation findings

- Rendered the actual Markdown through `marked`, with a small illustrative GitHub-style shell and Markdown typography. CSS/JavaScript belongs only to the local review tooling; it is not part of the public README.
- Edge/Chromium `154.0.4258.48`, device scale 1, HTTP(S) requests blocked. No browser page errors.
- **Ten layout checks:** light and dark at 320, 390, 600, 601 and 1024 px. No horizontal overflow; images load, stay within the README, retain alt text and select the expected header at the breakpoint.
- **Four font checks:** both headers with preferred Georgia/Segoe UI/Consolas and alternate Times New Roman/Arial/Courier New. Lettering fits all artboards. Preferred and fallback layouts were visually inspected; font metrics may still vary elsewhere.
- **Geometry/preservation:** all 25 approved M1/M2 asset/token hashes match the post-approval baseline. Both headers reproduce the primary duck exactly. SVG structure, IDs, local references and canonical colors pass.
- **Text-only check:** the exact public description and area copy remain readable after removing images. No essential description is baked exclusively into artwork. Native GitHub text follows the reader's theme; header Ink/Paper uses the existing 13.1456:1 pairing.
- Public content and relative paths were inspected. The three image paths resolve locally without leaving the repository. No private project identifiers or unsupported marketing claims were introduced.

The compact date is deliberately small and secondary. The 192 px notebook study communicates its silhouette and construction character; discovering the PA is optional at that scale. The primary colorful expression remains above it and is the main recognition cue.

## Review artifacts and limits

The task's external `m3-review/` folder contains the combined `m3-profile-review.png`, separate light/dark desktop and narrow images, native header/fallback specimens, image-free copy preview, HTML sources and machine-readable report. The proposed Paper avatar appears in the illustrative shell only; no organization avatar was uploaded or changed.

These are **local approximations, not live GitHub screenshots**. The surrounding organization interface, exact GitHub CSS/sanitization, relative-path rewriting on the organization Overview page, repository visibility and other browser engines are not verified by this preview. No existing pins, statistics or repositories were invented to fill the mock interface. Inspect the published organization view only after a later authorized publication step.

## Reproduce

```text
python brand/tools/build-profile.py
node brand/tools/render-profile.cjs "<review-output-directory>" "<browser-executable>"
python brand/tools/validate-profile.py --renders "<review-output-directory>"
```

Python generation/validation uses the standard library. Rendering requires the existing Node.js, `marked`, Playwright and Chromium-family browser. It does not install dependencies. An optional `m2-approved-hashes.json` in the review directory provides an additional historical baseline when available; it is not required to reproduce QA. [M3_MANIFEST.json](review/M3_MANIFEST.json) also records all protected source hashes.

Review the profile's hierarchy, amount of whitespace, compact header and secondary notebook study. M3 is approved. Preserve this composition. M4 is also approved and M5 is complete and approved.
