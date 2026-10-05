# nami: shared form container

<!-- current-art-summary:start -->
Character package: 19 categorized assets, including 0 transparent native tracks. 58 canonical native cell PNGs. [Attack map](ATTACKS.md) contains 2 action groups.

Authored alternate-facing assets: 0. Source-controlled loose-pose references: 0. Move groups retain body, summon, projectile, effect and conditional-phase associations in `art.json`. Shared art records every action use. Alternate-facing assets preserve actual authored pixels and record runtime display mirroring separately.

Unresolved native node records: 0; unsupported texture records: 0. Source references and poses with unknown sequence positions remain explicit; art-track key times do not establish gameplay trigger times.
<!-- current-art-summary:end -->

Each fighter form has its own source, native bundles and categorized assets.

- [Orange outfit / original staff](../forms/orange_outfit/labeled_split/README.md)
- [Blue outfit / upgraded staff](../forms/blue_outfit/labeled_split/README.md)

This parent package retains shared supports, source panels, source extras and their region dispositions. Canonical cells remain reference files.

Remaining source/composition review:

- Two staff forms are separate. Weather, lightning and heart projectiles need charge/follow-up relationships.
- Native cell/texture identity and pixels are verified. Source-to-native pose coverage, node transforms, playback timing and gameplay selection are not certified. Regions marked reviewed_reference_unreconciled do not prove complete extraction.
