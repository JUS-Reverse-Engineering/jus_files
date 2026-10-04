#!/usr/bin/env python3
"""Download battle-character sprite sheets listed by the Sprite Database.

The inclusion roster comes from docs/research/guides/systems/koma-list.json.
Each value maps one Genroh guide character to the Sprite Database file entry
ID(s). Pegasus Seiya has two entries because the database splits his koma
versions across two sprite sheets.
"""

from __future__ import annotations

import concurrent.futures
import html
import json
import re
import sys
import unicodedata
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ROSTER = ROOT / "docs/research/guides/systems/koma-list.json"
OUT = Path(__file__).resolve().parent / "characters"
BASE = "https://spritedatabase.net"

# Canonical guide name -> (series directory, Sprite Database file id(s),
# output filename(s)). The list is audited against the guide's 56 battle
# characters below so additions to the source roster cannot silently vanish.
ENTRIES = {
    'TSUNAYOSHI "TSUNA" SAWADA & REBORN': ("Katekyo Hitman Reborn", [(1029, "Tsuna")]),
    "GINTOKI SAKATA": ("Gintama", [(968, "Gintoki")]),
    "KAGURA": ("Gintama", [(969, "Kagura")]),
    "KINNIKUMAN": ("Kinnikuman", [(991, "Kinnikuman")]),
    "RYOTSU KANKICHI": ("Kochikame", [(999, "Ryotsu")]),
    "EDAJIMA HEIHACHI": ("Sakigake Otokojuku", [(1047, "Heihachi Edajima")]),
    "MOMOTARO TSURUGI": ("Sakigake Otokojuku", [(11897, "Momotaro")]),
    "YOH ASAKURA": ("Shaman King", [(1050, "Yoh Asakura")]),
    "ANNA KYOYAMA": ("Shaman King", [(1051, "Anna")]),
    "JOTARO KUJO": ("JoJos Bizarre Adventure", [(11693, "Jotaro Kujo")]),
    "DIO BRANDO": ("JoJos Bizarre Adventure", [(984, "Dio Brando")]),
    "SEIYA": ("Saint Seiya", [(1041, "Pegasus Seiya 1-7 koma"), (1042, "Pegasus Seiya 8 koma")]),
    "ALLEN WALKER": ("D.Gray-man", [(11839, "Allen Walker")]),
    "LINALI LEE": ("D.Gray-man", [(938, "Lenalee Lee")]),
    "ARALE NORIMAKI": ("Dr. Slump", [(956, "Arale")]),
    "DR. MASHIRITO": ("Dr. Slump", [(957, "Dr. Mashirito")]),
    "SON GOKU": ("Dragon Ball", [(947, "Goku")]),
    "VEGETA": ("Dragon Ball", [(950, "Vegeta")]),
    "SUPER SAIYJIN SON GOHAN": ("Dragon Ball", [(949, "Gohan")]),
    "GOTENKS": ("Dragon Ball", [(951, "Gotenks")]),
    "PICCOLO": ("Dragon Ball", [(952, "Piccolo")]),
    "FRIEZA": ("Dragon Ball", [(953, "Frieza")]),
    "MAJIN BUU": ("Dragon Ball", [(954, "Majin Buu")]),
    "NARUTO UZUMAKI": ("Naruto", [(1008, "Naruto")]),
    "SASUKE UCHIHA": ("Naruto", [(1009, "Sasuke")]),
    "SAKURA HARUNO": ("Naruto", [(1010, "Sakura")]),
    "KAKASHI HATAKE": ("Naruto", [(1011, "Kakashi")]),
    "FUUSUKE": ("Ninku", [(1013, "Fuusuke")]),
    "GON FREECS": ("Hunter x Hunter", [(909, "Gon Freecss")]),
    "KILLUA ZOALDYCK": ("Hunter x Hunter", [(910, "Killua Zoldyck")]),
    "JAGUAR JUNICHI": ("Pyu to Fuku Jaguar", [(12079, "Jaguar")]),
    "KAZUKI MUTOU": ("Buso Renkin", [(932, "Kazuki")]),
    "EVE": ("Black Cat", [(911, "Eve")]),
    "TRAIN HEARTNET": ("Black Cat", [(912, "Train Heartnet")]),
    "ICHIGO KUROSAKI": ("Bleach", [(915, "Ichigo Kurosaki")]),
    "RUKIA KUCHIKI": ("Bleach", [(918, "Rukia Kuchiki")]),
    "RENJI ABARAI": ("Bleach", [(917, "Renji Abarai")]),
    "TOUSHIRO HITSUGAYA": ("Bleach", [(916, "Toshirō Hitsugaya")]),
    "TAIKOUBOU": ("Houshin Engi", [(1056, "Taikobo")]),
    "KENSHIRO": ("Hokuto no Ken", [(906, "Kenshiro")]),
    "RAOH": ("Hokuto no Ken", [(907, "Raoh")]),
    "BOBOBO-BO BO-BOBO": ("Bobobo-bo Bo-bobo", [(926, "Bobobo-bo Bo-bobo")]),
    "DON PATCH": ("Bobobo-bo Bo-bobo", [(927, "Don Patch")]),
    "NEURO NOGAMI & YAKO KATSUGRA": ("Majin Tantei Nogami Neuro", [(1002, "Neuro Nōgami")]),
    "MUHYO TORU": ("Muhyo to Rouji", [(1005, "Toru Muhyo")]),
    "YUGI MUTOU": ("Yu-Gi-Oh!", [(1062, "Yugi")]),
    "YUSUKE URAMESHI": ("YuYu Hakusho", [(1064, "Yusuke Urameshi")]),
    "KURAMA aka SHUICHI MINAMINO": ("YuYu Hakusho", [(1067, "Kurama")]),
    "HIEI": ("YuYu Hakusho", [(1065, "Hiei")]),
    "KENSHIN HIMURA": ("Rurouni Kenshin", [(1036, "Kenshin Himura")]),
    "MONKEY D. LUFFY": ("One Piece", [(5, "Monkey D. Luffy")]),
    "RORONOA ZORO": ("One Piece", [(1016, "Roronoa Zoro")]),
    "NAMI": ("One Piece", [(1017, "Nami")]),
    "SANJI": ("One Piece", [(1018, "Sanji")]),
    "NICO ROBIN": ("One Piece", [(1019, "Nico Robin")]),
    "FRANKY": ("One Piece", [(1020, "Franky")]),
}


def battle_characters() -> list[tuple[str, str]]:
    data = json.loads(ROSTER.read_text(encoding="utf-8"))
    return [
        (series["series"], character["name"])
        for series in data["series"]
        for character in series["characters"]
        if any(koma["role"] == "battle" for koma in character["koma"])
    ]


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "jus-re sprite asset fetcher"})
    with urllib.request.urlopen(request, timeout=45) as response:
        return response.read()


def get_download(file_id: int) -> tuple[str, str]:
    page = fetch(f"{BASE}/file/{file_id}").decode("iso-8859-1")
    match = re.search(r"<a href='([^']+)' download='([^']+)' class='selectedview'", page)
    if not match:
        raise RuntimeError(f"No download link found for Sprite Database entry {file_id}")
    url = BASE + "/" + html.unescape(match.group(1)).lstrip("/")
    return url, html.unescape(match.group(2))


def source_destination(sprite_root: Path, manifest: list[dict], file_id: int,
                       series: str, filename: str, extension: str) -> Path:
    existing = next((row for row in manifest if row["file_id"] == file_id), None)
    if existing:
        relative = Path(existing["path"])
        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError("Source path must stay within the sprite root")
    else:
        relative = Path("characters") / series / Path(filename).stem.lower() / filename
    return (sprite_root / relative).with_suffix(extension)


def main() -> int:
    battle = battle_characters()
    guide_names = {name for _, name in battle}
    missing = guide_names - ENTRIES.keys()
    extra = ENTRIES.keys() - guide_names
    if missing or extra or len(battle) != 56:
        raise RuntimeError(f"Roster mismatch: guide has {len(battle)} battle characters; missing={sorted(missing)}; extra={sorted(extra)}")

    jobs = []
    for _, guide_name in battle:
        series_dir, sprites = ENTRIES[guide_name]
        for file_id, database_name in sprites:
            filename_base = unicodedata.normalize("NFKD", database_name).encode("ascii", "ignore").decode("ascii")
            filename = re.sub(r"[^A-Za-z0-9]+", "_", filename_base).strip("_") + ".png"
            jobs.append((guide_name, series_dir, file_id, database_name, filename))

    OUT.mkdir(parents=True, exist_ok=True)
    manifest_path = OUT.parent / "source_manifest.json"
    previous = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else []
    manifest = []

    def download(job: tuple[str, str, int, str, str]) -> dict[str, str | int]:
        guide_name, series_dir, file_id, database_name, filename = job
        page_url = f"{BASE}/file/{file_id}"
        image_url, source_filename = get_download(file_id)
        payload = fetch(image_url)
        formats = {
            ".png": b"\x89PNG\r\n\x1a\n",
            ".gif": b"GIF8",
            ".jpg": b"\xff\xd8\xff",
            ".jpeg": b"\xff\xd8\xff",
            ".bmp": b"BM",
        }
        extension = Path(source_filename).suffix.lower()
        if extension not in formats or not payload.startswith(formats[extension]):
            raise RuntimeError(f"Entry {file_id} did not return the advertised {extension or 'image'} file")
        destination = source_destination(OUT.parent, previous, file_id, series_dir, filename, extension)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(payload)
        return {
            "guide_character": guide_name,
            "database_name": database_name,
            "series": series_dir,
            "file_id": file_id,
            "page_url": page_url,
            "image_url": image_url,
            "path": destination.relative_to(OUT.parent).as_posix(),
            "bytes": len(payload),
        }

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        for result in pool.map(download, jobs):
            manifest.append(result)
            print(f"{result['path']} ({result['bytes']} bytes)")

    manifest.sort(key=lambda row: (str(row["series"]), str(row["guide_character"]), int(row["file_id"])))
    (OUT.parent / "source_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Downloaded {len(manifest)} sprite sheets for {len(battle)} guide battle characters.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as error:
        print(f"error: {error}", file=sys.stderr)
        sys.exit(1)
