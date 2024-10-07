from abc import ABC
from collections.abc import Iterable
from pathlib import Path
from typing import override

import pillow_avif  # noqa: F401
from PIL import Image

from ecoimage.common.exc import InvalidFormatError
from ecoimage.common.settings import AVIF_DEFAULT_QUALITY, WEBP_DEFAULT_QUALITY


class Converter(ABC):
    _SUFFIXES: Iterable[str]

    def __init__(self, initial_path: Path) -> None:
        self.initial_path = initial_path
        self._check_format()

    def to_avif(self, *, quality: int = AVIF_DEFAULT_QUALITY) -> Path:
        initial_img = Image.open(self.initial_path)
        avif_path = self.initial_path.with_suffix(".avif")
        initial_img.save(avif_path, format="avif", quality=quality, encoder="auto")

        return avif_path

    def to_webp(self, *, quality: int = WEBP_DEFAULT_QUALITY) -> Path:
        initial_img = Image.open(self.initial_path)
        initial_img = initial_img.convert("RGB")

        webp_path = self.initial_path.with_suffix(".webp")
        initial_img.save(webp_path, format="webp", optimize=True, quality=quality)

        return webp_path

    def _check_format(self) -> None:
        if self.initial_path.suffix not in self._SUFFIXES:
            raise InvalidFormatError(f"Invalid format {self.initial_path.suffix}")


class JpgConverter(Converter):
    _SUFFIXES = [".jpg", ".jpeg"]


class PngConverter(Converter):
    _SUFFIXES = [".png"]


class WebpConverter(Converter):
    _SUFFIXES = [".webp"]

    @override
    def to_webp(self, *, quality: int = WEBP_DEFAULT_QUALITY) -> Path:
        return self.initial_path


def converter_factory(image_path: Path | str) -> Converter:
    image_path = Path(image_path)

    if image_path.suffix in [".jpg", ".jpeg"]:
        return JpgConverter(image_path)

    elif image_path.suffix == ".png":
        return PngConverter(image_path)

    elif image_path.suffix == ".webp":
        return WebpConverter(image_path)

    elif image_path.suffix == ".avif":
        raise InvalidFormatError(".avif is still the best format !")

    else:
        raise InvalidFormatError(f"Invalid format {image_path.suffix}")
