import pytest
import zippy.config as config

def test_load_settings():
    settings = config.load()
    assert isinstance(settings, dict)
    assert "current_file" in settings
    assert "folder_path_1" in settings
    assert len(settings) == 7 # Adjust based on actual settings.json content

def test_save_settings(tmp_path):
    test_data = {
        "current_file": "test_file.rar",
        "current_folder": str(tmp_path / "test_folder"),
        "folder_path_1": str(tmp_path / "folder1"),
    }
    # Mock the SETTINGS_FILE path to use a temporary file
    original_settings_file = config.SETTINGS_FILE
    temp_settings_file = tmp_path / "settings.json"
    config.SETTINGS_FILE = str(temp_settings_file)

    try:
        config.save(test_data)
        loaded = config.load()
        assert loaded == test_data
    finally:
        config.SETTINGS_FILE = original_settings_file