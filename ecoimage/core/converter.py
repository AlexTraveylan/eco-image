from abc import ABC, abstractmethod
from collections.abc import Iterable
from enum import Enum
from functools import cached_property
from pathlib import Path

import pillow_avif  # noqa: F401
from PIL import Image

from ecoimage.common.exc import InvalidFormatError


class Format(str, Enum):
    JPG = "jpg"
    PNG = "png"
    WEBP = "webp"
    AVIF = "avif"


class Converter(ABC):
    _SUFFIXES: Iterable[str]

    def __init__(self, initial_path: Path) -> None:
        self.initial_path = initial_path
        self._check_format()

    @abstractmethod
    def to_webp(self, *, quality: int) -> Path:
        pass

    @abstractmethod
    def to_avif(self, *, quality: int) -> Path:
        pass

    def _check_format(self) -> None:
        if self.initial_path.suffix not in self._SUFFIXES:
            raise InvalidFormatError(f"Invalid format {self.initial_path.suffix}")

    @cached_property
    def initial_width(self) -> int:
        return Image.open(self.initial_path).width

    @cached_property
    def initial_height(self) -> int:
        return Image.open(self.initial_path).height


class JpgConverter(Converter):
    _SUFFIXES = [".jpg", ".jpeg"]

    def to_avif(self, *, quality: int = 30) -> Path:
        jpg_img = Image.open(self.initial_path)
        avif_path = self.initial_path.with_suffix(".avif")
        jpg_img.save(avif_path, format="avif", quality=quality, encoder="auto")

        return avif_path

    def to_webp(self, *, quality: int = 25) -> Path:
        jpg_img = Image.open(self.initial_path)
        jpg_img = jpg_img.convert("RGB")

        webp_path = self.initial_path.with_suffix(".webp")
        jpg_img.save(webp_path, format="webp", optimize=True, quality=quality)

        return webp_path


class PngConverter(Converter):
    _SUFFIXES = [".png"]


class WebpConverter(Converter):
    _SUFFIXES = [".webp"]


class AvifConverter(Converter):
    _SUFFIXES = [".avif"]


def converter_factory(image_path: Path | str) -> Converter:
    image_path = Path(image_path)

    if image_path.suffix in [".jpg", ".jpeg"]:
        return JpgConverter(image_path)

    elif image_path.suffix == ".png":
        return PngConverter(image_path)

    elif image_path.suffix == ".webp":
        return WebpConverter(image_path)

    elif image_path.suffix == ".avif":
        return AvifConverter(image_path)

    else:
        raise InvalidFormatError(f"Invalid format {image_path.suffix}")
