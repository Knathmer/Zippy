# zippy/ui.py
# This module handles creation of the system tray icon and its menu


from pystray import Icon, MenuItem as item, Menu
from PIL import Image
import tkinter as tk  # tkinter for folder selection dialog
from tkinter import filedialog
from functools import partial
from .config import load, save
from .extractor import extract
import os


def get_folder(data, key):
    root = tk.Tk()
    root.withdraw()  # hide the root window
    path = filedialog.askdirectory()  # show folder picker
    if path:
        # store selected path and persist
        data[key] = path
        print(f"Here is the data that is being saved: {data}")
        save(data)


def close_zippy(icon, _):
    icon.stop()


def create_tray():
    # File locations are loaded from settings.json from a previous session
    data = load()

    # icon_path set to location of the icon image
    icon_path = os.path.join(
        os.path.dirname(__file__),
        "..",                     
        "icons",
        "zippy.png"
    )
    image = Image.open(icon_path)  # load the icon image

    # Build submenu items for "File Locations"
    loc_items = []

    def on_click(icon, menu_item, folder_key): # Callback function for folder selection
        get_folder(data, folder_key)

    for i in range(1, 6):
        key = f"folder_path_{i}"
        label = f"Location {i}"
        handler = partial(on_click, folder_key=key) #  partial presets the folder_key in a special function
        loc_items.append(item(label, handler))

    # Define the main tray menu structure
    tray_menu = Menu(
        item("Exit", close_zippy),  # top-level Exit option
        item("File Locations", Menu(*loc_items)),  # nested submenu
    )

    # Create and return the Icon object with title, image, and menu
    return Icon("Zippy", image, menu=tray_menu)
