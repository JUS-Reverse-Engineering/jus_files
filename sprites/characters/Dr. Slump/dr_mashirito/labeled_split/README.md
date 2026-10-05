# dr_mashirito: shared form container

<!-- current-art-summary:start -->
Character package: 41 categorized assets, including 0 transparent native tracks. 93 canonical native cell PNGs. [Attack map](ATTACKS.md) contains 3 action groups.

Authored alternate-facing assets: 0. Source-controlled loose-pose references: 0. Move groups retain body, summon, projectile, effect and conditional-phase associations in `art.json`. Shared art records every action use. Alternate-facing assets preserve actual authored pixels and record runtime display mirroring separately.

Unresolved native node records: 11; unsupported texture records: 0. Source references and poses with unknown sequence positions remain explicit; art-track key times do not establish gameplay trigger times.
<!-- current-art-summary:end -->

Each fighter form has its own source, native bundles and categorized assets.

- [Caramel Man / base](../forms/base_caramel/labeled_split/README.md)
- [Gold Caramel Man / native only](../forms/gold_caramel/labeled_split/README.md)

This parent package retains shared supports, source panels, source extras and their region dispositions. Canonical cells remain reference files.

Remaining source/composition review:

- Caramel Man ds_b_03 is an alternate native family; its 8k special pieces are separate from ds_b_02 robot summon bodies.
- No ds_s_03_3 archive exists. Color/palette alternates and source compound transform sequence selection remain unresolved.
- Gold ds_b_03 / ds_s_03 art is a native-only alternate-form candidate: corrected idle opaque-RGB source probe found no match, so it has no source-confirmed coordinate or equivalence.
