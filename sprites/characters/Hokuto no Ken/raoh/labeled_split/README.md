# Raoh art

<!-- current-art-summary:start -->
Character package: 123 assets, 123 visible strips/panels and 0 transparent native tracks. 392 referenced canonical native cell PNGs. [Attack map](ATTACKS.md) contains 49 action groups.

Native diagnostics in the current manifest: 267 nodes without cell tracks, 0 unresolved-node records and 0 unsupported-texture records. These diagnostics describe decoding; gameplay selection and composition remain separate review items.
<!-- current-art-summary:end -->

This package uses the shared cast authoring layout. `art.json` records source hashes, authored animation IDs, exact texture ownership, frame bounds, source rectangles and review status.

Native strips contain unique keyed poses, not a frame-timed playback movie. Their suffix identifies archive, authored animation ID and node. Primary fighter bodies, support actors and detached native components remain distinct records. `hit_type_0`, `hit_type_1`, `hit_type_2` and `surprised` follow the four-character reaction evidence. Unknown native 09 stays explicitly unresolved. Jump variants 05/06 and selector timing are not inferred from appearance.

Original sheets and old splits remain in the parent directory. `_ORIGINAL` files are named source placement references containing contextual labels and combined artwork; they are not playable frame strips. Panel filename numbers identify source ordering, not koma count. Source panel silhouettes and Japanese text were visually reviewed; printed lettering is not a fighter frame.

Archives: `hk_b_02`, `hk_b_02_6`, `hk_b_02_7`, `hk_b_02_8`, `hk_s_02`, `hk_s_02_2`.

This package contains 107 native sequence/node assets and 4 reviewed source panels. All native first/middle/last poses were inspected after the DSIG tile-alignment correction. Source foreground coverage remains independent of native coverage.

Remaining composition questions:

- Native playback/state selection and node transform composition are not certified.
- six_koma_horse: Horse actor and rider placements remain separate summon/body composition.
- seven_koma_horse: Second horse/rider special group has distinct charge/impact poses.
- eight_koma_aura_and_cape: Yellow outline, grey stone effect and victory cape displacement are detached components.
- Native archive cells outside resolved animation tracks and untouched source pixels retain separate coverage; no complete sheet-to-frame or runtime-selector claim.

Source-authored cuts use explicit rectangles. Editorial canvas anchors do not establish engine origins. Native bounds and source layouts preserve the evidence needed for that later work. No runtime normalized assets are modified.
