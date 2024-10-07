import shutil
from pathlib import Path

from ecoimage.core.converter import JpgConverter, PngConverter, WebpConverter


def test_jpg_converter(jpg_test: Path, tmpdir):
    copy_jpg_path = Path(tmpdir) / jpg_test.name
    shutil.copy(jpg_test, copy_jpg_path)

    converter = JpgConverter(initial_path=copy_jpg_path)

    avif_path = converter.to_avif()
    webp_path = converter.to_webp()

    assert avif_path.exists()
    assert webp_path.exists()


def test_png_converter(png_test: Path, tmpdir):
    copy_png_path = Path(tmpdir) / png_test.name
    shutil.copy(png_test, copy_png_path)

    converter = PngConverter(initial_path=copy_png_path)

    avif_path = converter.to_avif()
    webp_path = converter.to_webp()

    assert avif_path.exists()
    assert webp_path.exists()


def test_webp_converter(webp_test: Path, tmpdir):
    copy_webp_path = Path(tmpdir) / webp_test.name
    shutil.copy(webp_test, copy_webp_path)

    converter = WebpConverter(initial_path=copy_webp_path)

    avif_path = converter.to_avif()
    webp_path = converter.to_webp()

    assert avif_path.exists()
    assert webp_path.exists()
