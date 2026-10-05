# Neuro Nōgami categorized art

<!-- current-art-summary:start -->
Character package: 135 categorized assets, including 12 transparent native tracks. 549 canonical native cell PNGs. [Attack map](ATTACKS.md) contains 48 action groups.

Authored alternate-facing assets: 0. Source-controlled loose-pose references: 0. Move groups retain body, summon, projectile, effect and conditional-phase associations in `art.json`. Shared art records every action use. Alternate-facing assets preserve actual authored pixels and record runtime display mirroring separately.

Unresolved native node records: 96; unsupported texture records: 0. Source references and poses with unknown sequence positions remain explicit; art-track key times do not establish gameplay trigger times.
<!-- current-art-summary:end -->

Native body poses, components and supports are exported separately from the immutable source sheet. `art.json` records authored animation IDs, exact archive/texture/cell ownership, frame bounds/origins, source pieces and uncertain branches. Files retain authored facing.

Native origins: `nn_b_01`, `nn_b_01_4`, `nn_b_01_5`, `nn_s_01`, `nn_s_01_2`, `nn_s_01_3`.

Categories: `attacks_heavy` (21), `attacks_light` (9), `attacks_special` (23), `generics` (16), `hitstun` (15), `misc` (14), `panels` (5), `supports` (5), `taunt` (3). Total: 111 selected assets.

Body and component strips are separate assets. Base support `_s_` speech/SFX/graphics are `support_component`; actual main-body support nodes are `support_actor`. `misc/native_cells` preserves canonical unused cells and palettes as well as referenced cells. Deck art in `panels` uses reviewed source pieces; touching printed layouts are separate `misc/source_references` crops. Portrait/HUD references also live in `misc`.

Visual review covered all full source sheet tile overviews, crop candidates and outputs, and native first/last-cell category contacts. The DSIGv2 allocation repair changed 90 canonical cells; before/after contacts were inspected for every affected asset. Native cells and composed source outputs pass exact regeneration verification. Review does not certify gameplay playback, transforms, branch selection or state duration.

Source coverage remains separate from native archive coverage: 44 bounded source row groups are retained as reference dispositions for compound examples, source-only poses, repeat guides and attribution. They do not assert one-to-one native correspondence or a selected runtime asset for every source pixel.

Residuals:

- Yako/summon body, purple demon effects, and rotating ring source compounds require transform/branch selection.
- Native body main-node endpoints contain white flash silhouettes; source confirms these are intentional.
