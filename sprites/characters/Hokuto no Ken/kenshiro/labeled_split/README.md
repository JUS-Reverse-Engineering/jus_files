# Kenshiro art

<!-- current-art-summary:start -->
Character package: 156 assets, 146 visible strips/panels and 10 transparent native tracks. 527 referenced canonical native cell PNGs. [Attack map](ATTACKS.md) contains 54 action groups.

Native diagnostics in the current manifest: 398 nodes without cell tracks, 1 unresolved-node records and 0 unsupported-texture records. These diagnostics describe decoding; gameplay selection and composition remain separate review items.
<!-- current-art-summary:end -->

This package uses the shared cast authoring layout. `art.json` records source hashes, authored animation IDs, exact texture ownership, frame bounds, source rectangles and review status.

Native strips contain unique keyed poses, not a frame-timed playback movie. Their suffix identifies archive, authored animation ID and node. Primary fighter bodies, support actors and detached native components remain distinct records. `hit_type_0`, `hit_type_1`, `hit_type_2` and `surprised` follow the four-character reaction evidence. Unknown native 09 stays explicitly unresolved. Jump variants 05/06 and selector timing are not inferred from appearance.

Original sheets and old splits remain in the parent directory. `_ORIGINAL` files are named source placement references containing contextual labels and combined artwork; they are not playable frame strips. Panel filename numbers identify source ordering, not koma count. Source panel silhouettes and Japanese text were visually reviewed; printed lettering is not a fighter frame.

Archives: `hk_b_01`, `hk_b_01_4`, `hk_b_01_5`, `hk_b_01_6`, `hk_b_01_7`, `hk_b_01_8`, `hk_s_01`, `hk_s_01_2`, `hk_s_01_3`.

This package contains 130 native sequence/node assets and 7 reviewed source panels. All native first/middle/last poses were inspected after the DSIG tile-alignment correction. Source foreground coverage remains independent of native coverage.

Remaining composition questions:

- Native playback/state selection and node transform composition are not certified.
- seven_koma_friends: 7k Up X calls distinct allies; these actors are summons, not Kenshiro hitstun frames.
- Native archive cells outside resolved animation tracks and untouched source pixels retain separate coverage; no complete sheet-to-frame or runtime-selector claim.

Source-authored cuts use explicit rectangles. Editorial canvas anchors do not establish engine origins. Native bounds and source layouts preserve the evidence needed for that later work. No runtime normalized assets are modified.
