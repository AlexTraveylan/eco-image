from pathlib import Path

from ecoimage.core.converter import JpgConverter, PngConverter, WebpConverter


def test_jpg_converter(jpg_test: Path):
    converter = JpgConverter(initial_path=jpg_test)

    avif_path = converter.to_avif()
    webp_path = converter.to_webp()

    assert avif_path.exists()
    assert webp_path.exists()


def test_png_converter(png_test: Path):
    converter = PngConverter(initial_path=png_test)

    avif_path = converter.to_avif()
    webp_path = converter.to_webp()

    assert avif_path.exists()
    assert webp_path.exists()


def test_webp_converter(webp_test: Path):
    converter = WebpConverter(initial_path=webp_test)

    avif_path = converter.to_avif()
    webp_path = converter.to_webp()

    assert avif_path.exists()
    assert webp_path.exists()
