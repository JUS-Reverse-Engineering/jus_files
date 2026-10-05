# Kazuki categorized art

<!-- current-art-summary:start -->
Character package: 132 assets, 132 visible strips/panels and 0 transparent native tracks. 514 referenced canonical native cell PNGs. [Attack map](ATTACKS.md) contains 50 action groups.

Native diagnostics in the current manifest: 139 nodes without cell tracks, 0 unresolved-node records and 0 unsupported-texture records. These diagnostics describe decoding; gameplay selection and composition remain separate review items.
<!-- current-art-summary:end -->

Native body poses, components and supports are exported separately from the immutable source sheet. `art.json` records authored animation IDs, exact archive/texture/cell ownership, frame bounds/origins, source pieces and uncertain branches. Files retain authored facing.

Native origins: `bu_b_01`, `bu_b_01_4`, `bu_b_01_5`, `bu_b_01_6`, `bu_s_01`, `bu_s_01_2`, `bu_s_01_3`.

Categories: `attacks_heavy` (18), `attacks_light` (12), `attacks_special` (41), `generics` (19), `hitstun` (15), `misc` (7), `panels` (8), `supports` (9), `taunt` (3). Total: 132 selected assets.

Body and component strips are separate assets. Base support `_s_` speech/SFX/graphics are `support_component`; actual main-body support nodes are `support_actor`. `misc/native_cells` preserves canonical unused cells and palettes as well as referenced cells. Deck art in `panels` uses reviewed source pieces; touching printed layouts are separate `misc/source_references` crops. Portrait/HUD references also live in `misc`.

Visual review covered all full source sheet tile overviews, crop candidates and outputs, and native first/last-cell category contacts. The DSIGv2 allocation repair changed 120 canonical cells; before/after contacts were inspected for every affected asset. Native cells and composed source outputs pass exact regeneration verification. Review does not certify gameplay playback, transforms, branch selection or state duration.

Source coverage remains separate from native archive coverage: 42 bounded source row groups are retained as reference dispositions for compound examples, source-only poses, repeat guides and attribution. They do not assert one-to-one native correspondence or a selected runtime asset for every source pixel.

Residuals:

- Source gray panel alternatives are preserved separately; engine availability/selection is unresolved. Touching source bank references are separate from clean multipart panel assets.
- Radial thrust source arrangements require rotation/transform composition; native piece facing is retained.
