import shutil
from pathlib import Path

from ecoimage.common.exc import EcoImageError
from ecoimage.common.settings import AVIF_DEFAULT_QUALITY, WEBP_DEFAULT_QUALITY
from ecoimage.core.converter import converter_factory
from ecoimage.core.resizer import open_img, resize_image


def multiconvert(
    img_path: Path | str,
    sizes: list[float],
    *,
    webp_quality: int = WEBP_DEFAULT_QUALITY,
    avif_quality: int = AVIF_DEFAULT_QUALITY,
) -> None:
    img_path = Path(img_path)
    sizes = set(sizes)

    if any((size <= 0 or size > 1) for size in sizes) is True:
        raise EcoImageError("Sizes must be between 0 and 1")

    # 1 is a particular case
    if 1 in sizes:
        sizes.remove(1)

    new_folder = img_path.parent / img_path.stem
    new_folder.mkdir()

    initial_img = open_img(img_path)

    # Case 1
    folder_init_size = new_folder / "init_size"
    folder_init_size.mkdir()
    img_dest_path = folder_init_size / img_path.name
    shutil.copy(img_path, img_dest_path)

    converter = converter_factory(img_dest_path)

    converter.to_webp(quality=webp_quality)
    converter.to_avif(quality=avif_quality)

    # Other Cases
    for size in sizes:
        resize_width = int(initial_img.width * size)
        resize_height = int(initial_img.height * size)

        size_folder = new_folder / f"w{resize_width}_h{resize_height}"
        size_folder.mkdir()

        resized = resize_image(initial_img, size, output_folder=size_folder)

        converter = converter_factory(resized.path)
        converter.to_webp(quality=webp_quality)
        converter.to_avif(quality=avif_quality)
