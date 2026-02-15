from context_menu import menus
from zippy.ui import fetch_icon_path
from PIL import Image
import time
import os

def test_menu(filenames, params):  # We are going to call this using shell commands
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    log_path = os.path.join(desktop, "zippy_log.txt")
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"{filenames}\n")


if __name__ == "__main__":
    def create_context_menu(data=None):
        cm = menus.FastCommand('Zippy', type='.rar', command='cmd /c pause && echo hello && pause', command_vars=['FILENAME'], icon_path=fetch_icon_path())
        cm.compile()

    def delete_context_menu():
        menus.removeMenu('Zippy', type='.rar')

create_context_menu()
time.sleep(10)
delete_context_menu()  # Required to clean up the context menu after testing
