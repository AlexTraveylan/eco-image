from pathlib import Path
from typing import NamedTuple

from PIL import Image

from ecoimage.common.exc import EcoImageError


class ImgData(NamedTuple):
    path: Path
    image: Image.Image
    width: int
    height: int


def open_img(img_path: Path | str) -> ImgData:
    img_path = Path(img_path)
    img = Image.open(img_path)

    return ImgData(img_path, img, *img.size)


def resize_image(
    img_data: ImgData,
    scale_factor: float,
    *,
    output_folder: Path | str = None,
) -> ImgData:
    if output_folder is None:
        output_folder = img_data.path.parent

    if output_folder.is_dir is False:
        raise EcoImageError(f"{output_folder} is not a directory")

    new_width = int(img_data.width * scale_factor)
    new_height = int(img_data.height * scale_factor)

    resized_img = img_data.image.resize(
        (new_width, new_height), Image.Resampling.LANCZOS
    )

    new_path = (
        output_folder
        / f"{img_data.path.stem}_{new_width}x{new_height}{img_data.path.suffix}"
    )
    resized_img.save(new_path, format=img_data.image.format)

    return ImgData(new_path, resized_img, new_width, new_height)
