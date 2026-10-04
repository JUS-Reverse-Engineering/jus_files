# Jump Ultimate Stars character sprites

`characters/` contains sprite sheets from [Sprite Database's Jump Ultimate
Stars page](https://spritedatabase.net/game/2). The selection follows the 56
characters with at least one battle koma in Genroh's roster at
`docs/research/guides/systems/koma-list.json`; support-only and help-only
characters are omitted. Pegasus Seiya has two source sheets because the
database separates koma 1–7 from koma 8.

Files are grouped by series and character slug. The source sheets are kept at their original
resolution and in their source image format (PNG or GIF). `source_manifest.json`
maps each sheet to its Genroh character, Sprite Database entry, and direct
source URL and actual nested sheet path. Refreshing a source retains its existing character directory.

Each character keeps its original sheet, previous automatic cuts under `split/`,
and reviewed categories under `labeled_split/`. The four manually categorized
examples are Yusuke, Kakashi, Train and Eve. `labeled_split/art.json` makes frame
order, source components, facing, branches and unresolved items explicit.
`characters/01_template/` supplies the shared directory convention. The parent
source repository documents authoring and verification in
`docs/rebuild/cast-art/README.md`. These editable assets precede the existing
`normalized/` runtime export; they do not establish combat playback timing.

The Sprite Database states that its game materials are provided for private
or non-commercial use. The sprites are copyrighted by their respective
creators and rights holders.

Run `python3 jus_files/sprites/download_sprites.py` from the repository root to
refresh the selected sheets and manifest.

Browse the reviewed cast through [the character index](characters/README.md)
or [the sprite browser](ART_REVIEW.html). Packages retain categorized art,
per-character review notes and `art.json` provenance.
