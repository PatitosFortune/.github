# GitHub publication and remaining manual setup

**M5 and Brand System v1 are approved.** Commit the implementation on `brand/github-identity-v01`, push it and open a PR against `main`. Do not merge the PR. Avatar/social uploads, visibility/settings changes, other-repository rollout and website work remain outside this authorization. Record later deployment actions when performed.

## Release preparation

- [x] M5 handoff and final QA approved by the user.
- [ ] Review the full repository inventory and public content. Keep external review screenshots, historical alternatives and private project information out of the publication.
- [x] Commit/push/PR workflow authorized; merge is explicitly excluded. Remote inspection found no commits or refs, with `main` configured as the default name. Establish an empty baseline on `main` solely as the PR target, keeping the complete implementation on `brand/github-identity-v01`. Do not force-push or overwrite existing work.
- [ ] Run the [reproduction/validation checks](brand/REPRODUCING.md) and retain the final [integrity manifest](brand/review/V1_INTEGRITY.json).
- [ ] Open the implementation PR against `main`; include `profile/README.md`, its headers and referenced `brand/derived/technical-construction.svg` together. Leave the PR open for human review; do not merge.

## Organization avatar and settings

- [ ] Confirm the operator has organization settings access and select the intended organization.
- [ ] Recommended default: [Paper duck, 512 px PNG](brand/avatars/duck-cream.png). The approved Ink/Ochre/Sage PNGs are deliberate alternatives; the technical mark does not replace the primary colorful identity.
- [ ] In GitHub, open **Organizations → PatitosFortune → Settings → Upload new picture**, select the chosen PNG, and inspect any crop before saving. Keep tail, beak and complete silhouette visible.
- [ ] Inspect the avatar in small square/circular contexts and light/dark surroundings.
- [ ] Review organization display name, description, website URL and other profile fields manually if an authorized update is needed. Do not invent contact details, change visibility, alter pins or modify member/private settings as part of an avatar upload.

GitHub documents organization picture uploads and the public organization README in a public `.github` repository at `profile/README.md`. Verify the account's actual organization type and visibility before publication. [Official organization-profile documentation](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/customizing-your-organizations-profile)

## Organization profile after a separately authorized merge

- [ ] Visit the organization **Overview** in its **Public** view; also inspect as a signed-out visitor where appropriate. The repository root README is the system manual, not the organization profile.
- [ ] Check that both relative header paths load and the compact header appears at narrow widths; check the technical study below the native copy.
- [ ] Check desktop and narrow layouts in GitHub light and dark themes. Look for clipping, missing SVGs, illegible text and unwanted scrollbars.
- [ ] Verify the description and broad work categories remain readable without images. Inspect alt text and the placement of the single technical study.
- [ ] Treat local `marked`/Chromium previews as approximations. Resolve any real GitHub sanitization or path-rewriting issue with a focused fix and rerun checks; do not redesign approved identity to compensate for a preview difference.

## Per-repository project identity and social preview — later rollout

- [ ] Explicitly authorize a rollout for a named repository. Verify its public/private status and approved content; do not use confidential or unreleased details to fill a card.
- [ ] Gather the project's approved display name and descriptor, plus appropriate optional category, single palette accent, study identifier and motif. Follow the [project-identity contract](brand/REPOSITORY_VISUALS.md).
- [ ] Generate into a separate directory, then render, validate and approve the project card. The four `example-*` cards are fictional fixtures and must not be uploaded as real project previews.
- [ ] Select the approved **1280 × 640 PNG**, under **1 MB**, with its explicit Paper/Ink field.
- [ ] Open the target repository **Settings → Social preview → Edit → Upload an image**. Inspect the selected file and save/confirm as prompted.
- [ ] Inspect the repository preview and a real shared-link rendering. Allow for caches; inspect text clipping and crop behavior. Keep required project information in the README as real text.

GitHub accepts PNG/JPG/GIF under 1 MB and recommends 1280 × 640 for best display. Image sharing depends on repository visibility; confirm current eligibility in the target repository. [Official social-preview instructions](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview)

## Record the handoff

- [ ] Record which avatar and real project previews were published, their source/input revision and export hashes, operator/date and post-publication findings.
- [ ] Update `STATUS.md` after the explicitly authorized release, keeping remaining manual checks visible.
- [ ] Start **PatitosFortune.com / Brand Application Stage** only as a separate scoped task using the [website handoff](brand/HANDOFF.md#website-handoff). Do not configure the website/domain during this checklist's preparation.
