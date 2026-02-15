# tests/conftest.py
import pytest
import zippy.ui as ui
import zippy.config as config
from typing import Generator


# Deprecated fixture
@pytest.fixture(autouse=False)
def reset_is_modified() -> Generator[None, None, None]:
    """Fixture to reset the isModified flag before each test."""
    ui.isModified = False
    yield  # Separates before and after function run
    ui.isModified = False
@pytest.fixture(autouse=True)
def mock_save(monkeypatch) -> None:
    monkeypatch.setattr(ui, "save", lambda data: None)