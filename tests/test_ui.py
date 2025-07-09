import pytest
import zippy.ui as ui
from PIL import Image

""" setpath  """

@pytest.mark.parametrize("data, key, path, expected_modified", [
    ({'key1': 'value1'}, 'key1', 'new_value1', True),
    ({'key1': 'value1'}, 'key1', 'value1', False)  # No change expected
])
def test_setpath(data, key, path, expected_modified, reset_is_modified):
    ui.setpath(data, key, path)
    assert data[key] == path
    assert ui.isModified == expected_modified

def test_setpath_non_existent():
    with pytest.raises(KeyError):
        ui.setpath({}, 'non_existent_key', 'some_path')

""" get_folder tests """

def test_get_folder(monkeypatch, tmp_path): #tmp_path is a pytest fixture for temporary directories
    data = {"key1": "value1"}
    class DummyTk:
        def withdraw(self):
            pass
    monkeypatch.setattr(ui.tk, "Tk", DummyTk)
    fake_folder = tmp_path / 'fake_path'
    fake_folder.mkdir()  # Create the directory to simulate user selection
    monkeypatch.setattr(ui.filedialog, "askdirectory", lambda **kwargs: str(fake_folder))

    ui.get_folder(data, "key1")
    assert data["key1"] == str(fake_folder)

def test_get_folder_empty_selection(monkeypatch):
    data = {"key1": "value1"}
    class DummyTk:
        def withdraw(self):
            pass
    monkeypatch.setattr(ui.tk, "Tk", DummyTk)
    monkeypatch.setattr(ui.filedialog, "askdirectory", lambda **kwargs: "")

    ui.get_folder(data, "key1")
    assert data["key1"] == "value1"

""" get_file tests """

def test_get_file(monkeypatch, tmp_path):
    data = {"current_file": "old_file.rar"}
    class DummyTk:
        def withdraw(self):
            pass
    monkeypatch.setattr(ui.tk, "Tk", DummyTk)
    fake_file = tmp_path / 'fake_file.rar'
    fake_file.touch()  # Create the file to simulate user selection
    monkeypatch.setattr(ui.filedialog, "askopenfilename", lambda **kwargs: str(fake_file))

    ui.get_file(data)
    assert data["current_file"] == str(fake_file)

def test_get_file_empty_selection(monkeypatch):
    data = {"current_file": "old_file.rar"}
    class DummyTk:
        def withdraw(self):
            pass
    monkeypatch.setattr(ui.tk, "Tk", DummyTk)
    monkeypatch.setattr(ui.filedialog, "askopenfilename", lambda **kwargs: "")

    ui.get_file(data)
    assert data["current_file"] == "old_file.rar"

""" create_tray tests """

class DummyIcon:
    def __init__(self, title, image, menu):
        self.title = title
        self.image = image
        self.menu = menu

def test_create_tray(monkeypatch, tmp_path):

    # Mock settings.json loading
    monkeypatch.setattr(ui, "load", lambda: {
        "folder_path_1": "value1",
        "folder_path_2": "value2",
        "folder_path_3": "value3",
        "folder_path_4": "value4",
        "folder_path_5": "value5",
        "folder_path_6": "value6",
        "current_file": "some_file.rar"
    })

    # Mock the Image.open method to return a dummy image
    dummy_image = Image.new("RGB",(1,1))
    monkeypatch.setattr(ui.Image, "open", lambda x: dummy_image)

    # Mock the Icon class to return a dummy icon
    monkeypatch.setattr(ui, "Icon", lambda title, image, menu: DummyIcon(title, image, menu))

    # Assertions
    icon = ui.create_tray()
    assert isinstance(icon, DummyIcon)
    assert icon.title == "Zippy"
    assert icon.image == dummy_image

    # Top Level Menu
    top_menu_items = list(icon.menu)

    labels = [item.text for item in top_menu_items]
    assert labels == ["Exit", "File Locations", "Extract File"]

    # File Locations Submenu
    file_locs_item = top_menu_items[1]
    submenu = file_locs_item.submenu
    sub_items = list(submenu)
    assert len(sub_items) == 5
    assert [i.text for i in sub_items] == [
        "Location 1", "Location 2", "Location 3", "Location 4", "Location 5"
    ]
