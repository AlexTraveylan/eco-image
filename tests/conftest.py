from pathlib import Path

import pytest


@pytest.fixture
def data_dir() -> Path:
    return Path(__file__).parent / "data"


@pytest.fixture
def jpg_test(data_dir: Path) -> Path:
    return data_dir / "688-536x354.jpg"
