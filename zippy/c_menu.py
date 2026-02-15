from context_menu import menus
from zippy.ui import fetch_icon_path
from PIL import Image
import time

def test_menu(filenames, params):
    print(filenames)
    input()

if __name__ == "__main__":
    def create_context_menu(data=None):
        cm = menus.FastCommand('Zippy', type='.rar', python=test_menu, command_vars=['FILENAME'], icon_path=fetch_icon_path())
        cm.compile()

    def delete_context_menu():
        menus.removeMenu('Zippy', type='.rar')

create_context_menu()
time.sleep(10)
delete_context_menu()  # Required to clean up the context menu after testing
