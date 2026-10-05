# vegeta: shared form container

<!-- current-art-summary:start -->
Character package: 30 categorized assets, including 0 transparent native tracks. 56 canonical native cell PNGs. [Attack map](ATTACKS.md) contains 2 action groups.

Authored alternate-facing assets: 0. Source-controlled loose-pose references: 0. Move groups retain body, summon, projectile, effect and conditional-phase associations in `art.json`. Shared art records every action use. Alternate-facing assets preserve actual authored pixels and record runtime display mirroring separately.

Unresolved native node records: 0; unsupported texture records: 0. Source references and poses with unknown sequence positions remain explicit; art-track key times do not establish gameplay trigger times.
<!-- current-art-summary:end -->

Each fighter form has its own source, native bundles and categorized assets.

- [Vegeta](../forms/normal/labeled_split/README.md)
- [Super Saiyan Vegeta](../forms/super_saiyan/labeled_split/README.md)

This parent package retains shared supports, source panels, source extras and their region dispositions. Canonical cells remain reference files.

Remaining source/composition review:

- Native playback/state selection and node transform composition are not certified.
- support_special_components: Source labels 2k through 6k; beams, blast silhouettes and Japanese lettering are components.
- Native archive cells outside resolved animation tracks and untouched source pixels retain separate coverage; no complete sheet-to-frame or runtime-selector claim.
