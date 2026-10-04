import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "download_sprites.py"
SPEC = importlib.util.spec_from_file_location("download_sprites", SCRIPT)
download = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(download)


class DownloadLayoutTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(callable(getattr(download, "source_destination", None)), "source refresh must resolve the nested character destination")

    def test_refresh_preserves_existing_character_folder(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            rows = [{"file_id": 911, "path": "characters/Black Cat/eve/Eve.png"}]
            result = download.source_destination(root, rows, 911, "Black Cat", "Eve.png", ".png")
            self.assertEqual(result, root / rows[0]["path"])

    def test_new_source_uses_character_slug_folder(self):
        result = download.source_destination(Path("sprites"), [], 912, "Black Cat", "Train_Heartnet.png", ".png")
        self.assertEqual(result, Path("sprites/characters/Black Cat/train_heartnet/Train_Heartnet.png"))

    def test_manifest_cannot_escape_sprite_root(self):
        with self.assertRaises(ValueError):
            download.source_destination(Path("sprites"), [{"file_id": 911, "path": "../outside.png"}], 911, "Black Cat", "Eve.png", ".png")


if __name__ == "__main__":
    unittest.main()
