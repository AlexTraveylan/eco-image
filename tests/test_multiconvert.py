from pathlib import Path

import pytest

from ecoimage.common.exc import EcoImageError
from ecoimage.usecase.website_multiconverter import multiconvert


def test_multiconvert_jpg(jpg_test: Path):
    multiconvert(jpg_test, sizes=[1, 0.9, 0.5, 0.3])


def test_multiconvert_webp(webp_test: Path):
    multiconvert(webp_test, sizes=[1, 0.9, 0.5, 0.3])


def test_multiconvert_with_bad_size():
    with pytest.raises(EcoImageError):
        multiconvert("", sizes=[0.5, 2])
