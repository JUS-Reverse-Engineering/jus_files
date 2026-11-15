# Cast frame libraries

79 libraries contain 67 fighter/form entries and 12 shared-art containers: 8,658
named sequences and 33,531 individual PNG frames. Each directory uses the
normalized-v1 contract: `animations.json`, named sequence directories containing
numbered frame PNGs, and export provenance. Names and move components come from
categorized authoring manifests.

Multi-form characters have independent libraries. Summons, effects, text and
companion art stay attached to their owning move through source-asset identities
and action groups; shared art retains multiple uses. Panels and whole-sheet
references remain in character authoring directories.

Native art tracks use their measured 60 Hz timeline. Unknown move selectors,
gameplay epochs and single-pose hold durations remain explicit candidate evidence.
Art availability does not certify a complete playable kit. The Kakashi and Yusuke
libraries were removed from the tip on 2026-11-15 and remain in the history at
af2863cc4.

`rollout-report.json` lists each library and sequence; `pixel-audit.json`,
`source-snapshot-audit.json` and `determinism-audit.json` record verification.
All generated files matched across two independent export runs. The source
repository keeps the final random-ten original-sheet review in
`docs/rebuild/cast-art/verification/`.
