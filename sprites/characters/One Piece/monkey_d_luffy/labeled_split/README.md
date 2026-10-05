# monkey_d_luffy: shared form container

<!-- current-art-summary:start -->
Character package: 24 categorized assets, including 0 transparent native tracks. 61 canonical native cell PNGs. [Attack map](ATTACKS.md) contains 2 action groups.

Authored alternate-facing assets: 0. Source-controlled loose-pose references: 0. Move groups retain body, summon, projectile, effect and conditional-phase associations in `art.json`. Shared art records every action use. Alternate-facing assets preserve actual authored pixels and record runtime display mirroring separately.

Unresolved native node records: 0; unsupported texture records: 0. Source references and poses with unknown sequence positions remain explicit; art-track key times do not establish gameplay trigger times.
<!-- current-art-summary:end -->

Each fighter form has its own source, native bundles and categorized assets.

- [Red vest / early form](../forms/red_vest/labeled_split/README.md)
- [Black outfit / later form](../forms/black_outfit/labeled_split/README.md)

This parent package retains shared supports, source panels, source extras and their region dispositions. Canonical cells remain reference files.

Remaining source/composition review:

- Base and Gear 2 forms are separate. Gear 3 inflate/recoil, detachable fists and steam need branch and composition links.
- Native cell/texture identity and pixels are verified. Source-to-native pose coverage, node transforms, playback timing and gameplay selection are not certified. Regions marked reviewed_reference_unreconciled do not prove complete extraction.
