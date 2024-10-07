import shutil
from pathlib import Path

from ecoimage.core.converter import JpgConverter


def test_jpg_converter(jpg_test: Path, tmpdir):
    copy_jpg_path = Path(tmpdir) / jpg_test.name
    shutil.copy(jpg_test, copy_jpg_path)

    converter = JpgConverter(initial_path=copy_jpg_path)

    avif_path = converter.to_avif()
    webp_path = converter.to_webp()

    assert avif_path.exists()
    assert webp_path.exists()
