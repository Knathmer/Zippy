# tests/conftest.py
import pytest
import zippy.ui as ui
from typing import Generator

@pytest.fixture(autouse=False)
def reset_is_modified() -> Generator[None, None, None]:
    """Fixture to reset the isModified flag before each test."""
    print("Resetting `isModified` flag before test.")
    ui.isModified = False
    yield  # Separates before and after function run
    ui.isModified = False