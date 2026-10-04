# Train Heartnet art

The existing manually categorized PNGs and category READMEs are preserved.
New native strips use `ROLE_ARCHIVE_anim_AUTHORED_ID_node_N_strip.png`;
canonical frame PNGs live under `misc/native_cells/` and are referenced by
`art.json`. The manifest records source hashes, native texture ownership,
explicit pose order, origins, facing, branches and shared uses.

Start with `generics`, `hitstun`, `attacks_light`, `attacks_heavy`,
`attacks_special`, `supports`, `panels` and `taunt`. `misc` retains unclassified
native art and references. The old `split/` cuts remain proposals.
`*_ORIGINAL` files retain source context for rearranged strips.

Native body strips and effects are separate assets. Japanese text, speech
balloons and beam parts are components; they are not extra fighter poses.
Native cell origins govern alignment. Frame order lists distinct keyed poses
in their first native occurrence; full native tracks remain in the manifest.
Playback duration, runtime selector and node transform evidence are separate.

Repairs and preserved relationships:

- Native4k body excludes detached Japanese balloons; speech and beam assets are components.
- Byte-identical owner4k and3k-support uses share provenance but retain their categories.

Animation09 remains unclassified. Jump-air variants05/06 remain distinct
without universal peak/fall labels. Special names retain exact panel/native
identity when input or branch selection is unresolved. Authored facing
differences must be preserved rather than recreated by mirroring.

`art.json` retains the exact unresolved items. This is a reviewed authoring
candidate; the normalized-v1 runtime export still requires its own timing,
role and selector evidence.
