import pytest
import zippy.ui as ui

@pytest.fixture(autouse=False)
def reset_is_modified():
    """Fixture to reset the isModified flag before each test."""
    print("Resetting `isModified` flag before test.")
    ui.isModified = False
    yield  # Separates before and after function run
    ui.isModified = False