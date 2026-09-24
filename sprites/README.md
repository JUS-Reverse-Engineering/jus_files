# Jump Ultimate Stars character sprites

`characters/` contains sprite sheets from [Sprite Database's Jump Ultimate
Stars page](https://spritedatabase.net/game/2). The selection follows the 56
characters with at least one battle koma in Genroh's roster at
`docs/research/guides/systems/koma-list.json`; support-only and help-only
characters are omitted. Pegasus Seiya has two source sheets because the
database separates koma 1–7 from koma 8.

Files are grouped by series. The source sheets are kept at their original
resolution and in their source image format (PNG or GIF). `source_manifest.json`
maps each sheet to its Genroh character, Sprite Database entry, and direct
source URL. Existing flat files directly under `characters/` are retained.

The Sprite Database states that its game materials are provided for private
or non-commercial use. The sprites are copyrighted by their respective
creators and rights holders.

Run `python3 jus_files/sprites/download_sprites.py` from the repository root to
refresh the selected sheets and manifest.
