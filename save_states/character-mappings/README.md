# Owner character-mapping states

This directory archives 170 owner-created melonDS states for 56 characters,
imported from `~/Desktop/savestates/character-mappings/` on 2026-09-29.
Each `<CHARACTER>/<panel>.mln.gz` decompresses to the original `.mln` bytes.
Form-change filenames retain the owner's spelling, including `FORMCHANGED`.

## Use the archive

Read [NOTES.md](NOTES.md) for the owner's capture conditions and panel rules.
Each character's `kit.md` is guide testimony, not measured frame or damage data.
The owner's character and active-panel labels come from the source path.
The archive import establishes byte preservation, not emulator compatibility
or a new gameplay measurement. HP regen is on in these source states.

The copied NOTES.md contains historical instructions to keep states local and
untracked. **Those publication instructions are superseded by the owner's
2026-09-29 request to commit this corpus to the private reference repository.**
The remaining research conditions still apply. These JUS assets remain private
reference material and are excluded from the shipped game.

Keep this archive separate from the top-level `cm-kakashi-*` and `cm-yusuke-*`
states. Those are bridge-resaved variants with real sidecars, and all six
have different bytes from the corresponding source states here.

## Load a source state

Decompress the selected file into a scratch location. For example, from jus_re:

```bash
mkdir -p /tmp/jus-character-mappings
gzip -dc 'jus_files/save_states/character-mappings/KAKASHI HATAKE/4.mln.gz' > /tmp/jus-character-mappings/kakashi-4.mln
```

Load the raw file through the patched melonDS savestate UI in your owned
emulator session. Then save it under a new bridge slot:

```bash
python3 scripts/emu/jusemu.py state save source-kakashi-4
```

That bridge save creates the real `.meta.json` alongside the runtime state.
The archived raw source states have no sidecars. A direct bridge load rejects
a state without one; do not invent framecounts to bypass that check.
A re-save can advance the game and differs from the archived source. Record
its conditions and inspect the loaded screen before collecting evidence.
The live Windows harness still requires the research-side port `jus-4p7v`.

## Verify the files

`manifest.json` records each original relative path, archived path, byte size,
and SHA-256 for both source bytes and archive bytes. Compression uses an empty
gzip filename and a zero timestamp. The source folder `NEURO ` has a trailing
space; its archived name is `NEURO` so Windows can check it out. The manifest
preserves the exact source spelling. Finder `.DS_Store` files are omitted.

Run this from jus_re to check all archived files without the Desktop source:

```bash
python3 - <<'PYTHON'
import gzip, hashlib, json
from pathlib import Path
root = Path('jus_files/save_states/character-mappings')
manifest = json.loads((root / 'manifest.json').read_text())
for row in manifest['files']:
    data = (root / row['archive_path']).read_bytes()
    assert len(data) == row['archive_bytes'], row['archive_path']
    assert hashlib.sha256(data).hexdigest() == row['archive_sha256'], row['archive_path']
    raw = gzip.decompress(data) if row['archive_path'].endswith('.gz') else data
    assert len(raw) == row['source_bytes'], row['source_path']
    assert hashlib.sha256(raw).hexdigest() == row['source_sha256'], row['source_path']
print('Verified', len(manifest['files']), 'source files')
PYTHON
```
