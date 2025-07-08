import pytest
import zippy.ui as ui


@pytest.mark.parametrize("data, key, path, expected_modified", [
    ({'key1': 'value1'}, 'key1', 'new_value1', True),
    ({'key1': 'value1'}, 'key1', 'value1', False)  # No change expected
])
def test_setpath(data, key, path, expected_modified):
    ui.setPath(data, key, path)
    assert data[key] == path
    assert ui.isModified == expected_modified

def test_setpath_non_existent():
    with pytest.raises(KeyError):
        ui.setPath({}, 'non_existent_key', 'some_path')

