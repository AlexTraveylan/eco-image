from pathlib import Path

from ecoimage.core.resizer import open_img, resize_image


def test_resize_image(jpg_test: Path):
    img_data = open_img(jpg_test)
    factor = 0.5
    resized_img = resize_image(img_data, scale_factor=factor)

    assert resized_img.path.exists()
    assert img_data.width * factor - resized_img.width < 1
    assert img_data.height * factor - resized_img.height < 1
