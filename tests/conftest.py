import shutil
from pathlib import Path

import pytest


@pytest.fixture
def data_dir() -> Path:
    return Path(__file__).parent / "data"


@pytest.fixture
def jpg_test(data_dir: Path, tmpdir) -> Path:
    inital_path = data_dir / "688-536x354.jpg"

    copy_path = Path(tmpdir) / inital_path.name
    shutil.copy(inital_path, copy_path)

    return copy_path


@pytest.fixture
def png_test(data_dir: Path, tmpdir) -> Path:
    inital_path = data_dir / "dice.png"

    copy_path = Path(tmpdir) / inital_path.name
    shutil.copy(inital_path, copy_path)

    return copy_path


@pytest.fixture
def webp_test(data_dir: Path, tmpdir) -> Path:
    inital_path = data_dir / "1.webp"

    copy_path = Path(tmpdir) / inital_path.name
    shutil.copy(inital_path, copy_path)

    return copy_path
