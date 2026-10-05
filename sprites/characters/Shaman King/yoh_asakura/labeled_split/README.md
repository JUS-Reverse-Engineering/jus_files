# yoh_asakura: shared form container

<!-- current-art-summary:start -->
Character package: 30 categorized assets, including 0 transparent native tracks. 77 canonical native cell PNGs. [Attack map](ATTACKS.md) contains 2 action groups.

Authored alternate-facing assets: 0. Source-controlled loose-pose references: 0. Move groups retain body, summon, projectile, effect and conditional-phase associations in `art.json`. Shared art records every action use. Alternate-facing assets preserve actual authored pixels and record runtime display mirroring separately.

Unresolved native node records: 0; unsupported texture records: 0. Source references and poses with unknown sequence positions remain explicit; art-track key times do not establish gameplay trigger times.
<!-- current-art-summary:end -->

Each fighter form has its own source, native bundles and categorized assets.

- [Spirit blade / first form](../forms/spirit_blade/labeled_split/README.md)
- [Sword / alternate Oversoul form](../forms/sword_form/labeled_split/README.md)

This parent package retains shared supports, source panels, source extras and their region dispositions. Canonical cells remain reference files.

Remaining source/composition review:

- Source lower-half white-armored form matches additional sk_b_02, included alongside sk_b_01. Flames, spirits and transitions need composition links.
- Native cell/texture identity and pixels are verified. Source-to-native pose coverage, node transforms, playback timing and gameplay selection are not certified. Regions marked reviewed_reference_unreconciled do not prove complete extraction.
