from pathlib import Path

from ecoimage.core.resizer import resize_image


def test_resize_image(jpg_test: Path):
    resized_img = resize_image(jpg_test, scale_factor=0.5)

    assert resized_img.exists()
