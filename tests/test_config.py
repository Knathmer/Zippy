# tests/test_config.py
import pytest
import zippy.config as config

def test_load_settings() -> None:
    settings = config.load()
    assert isinstance(settings, dict)
    assert "current_file" in settings
    assert "folder_path_1" in settings
    assert len(settings) == 7 # Adjust based on actual settings.json content