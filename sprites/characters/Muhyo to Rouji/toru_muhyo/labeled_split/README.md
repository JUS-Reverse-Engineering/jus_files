# Toru Muhyo art

<!-- current-art-summary:start -->
Character package: 207 categorized assets, including 1 transparent native tracks. 739 canonical native cell PNGs. [Attack map](ATTACKS.md) contains 52 action groups.

Authored alternate-facing assets: 0. Source-controlled loose-pose references: 0. Move groups retain body, summon, projectile, effect and conditional-phase associations in `art.json`. Shared art records every action use. Alternate-facing assets preserve actual authored pixels and record runtime display mirroring separately.

Unresolved native node records: 174; unsupported texture records: 0. Source references and poses with unknown sequence positions remain explicit; art-track key times do not establish gameplay trigger times.
<!-- current-art-summary:end -->

This package uses the shared cast authoring layout. `art.json` records source hashes, authored animation IDs, exact texture ownership, frame bounds, source rectangles and review status.

Native strips contain unique keyed poses, not a frame-timed playback movie. Their suffix identifies archive, authored animation ID and node. Primary fighter bodies, support actors and detached native components remain distinct records. `hit_type_0`, `hit_type_1`, `hit_type_2` and `surprised` follow the four-character reaction evidence. Unknown native 09 stays explicitly unresolved. Jump variants 05/06 and selector timing are not inferred from appearance.

Original sheets and old splits remain in the parent directory. `_ORIGINAL` files are named source placement references containing contextual labels and combined artwork; they are not playable frame strips. Panel filename numbers identify source ordering, not koma count. Source panel silhouettes and Japanese text were visually reviewed; printed lettering is not a fighter frame.

Archives: `mr_b_01`, `mr_b_01_4`, `mr_b_01_5`, `mr_b_01_6`, `mr_b_01_7`, `mr_s_01`, `mr_s_01_2`, `mr_s_01_3`.

This package contains 154 native sequence/node assets and 6 reviewed source panels. All native first/middle/last poses were inspected after the DSIG tile-alignment correction. Source foreground coverage remains independent of native coverage.

Remaining composition questions:

- Native playback/state selection and node transform composition are not certified.
- hit_branch_and_book: If Hit creature branch, book pages and Japanese text are separate components.
- summons_and_magic_circle: Train, knight, skull, bird and gorilla summons have independent bodies/effects/circle placement.
- Native archive cells outside resolved animation tracks and untouched source pixels retain separate coverage; no complete sheet-to-frame or runtime-selector claim.

Source-authored cuts use explicit rectangles. Editorial canvas anchors do not establish engine origins. Native bounds and source layouts preserve the evidence needed for that later work. No runtime normalized assets are modified.
