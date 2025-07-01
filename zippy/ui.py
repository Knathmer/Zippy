# zippy/ui.py
# This module handles creation of the system tray icon and its menu

from pystray import Icon, MenuItem as item, Menu  # pystray provides cross-platform tray support
from PIL import Image  # PIL is used to load the tray icon image
from .config import load, save  # config helpers to read/write settings.json
from .extractor import extract  # extraction logic for archives
import os
import tkinter as tk  # tkinter for folder selection dialog
from tkinter import filedialog


def get_folder(data, key):
    """
    Open a folder selection dialog, update the 'data' dict under 'key',
    and save the updated settings to disk.
    """
    root = tk.Tk()
    root.withdraw()  # hide the root window
    path = filedialog.askdirectory()  # show folder picker
    if path:
        # store selected path and persist
        data[key] = path
        save(data)


def close_zippy(icon, _):
    """
    Stop the tray icon event loop, effectively closing the app.
    """
    icon.stop()


def create_tray():
    """
    Build and return a configured pystray.Icon instance.
    """
    # Load user settings (e.g., stored folder paths)
    data = load()

    # Determine the absolute path to the tray icon image
    icon_path = os.path.join(
        os.path.dirname(__file__),  # this file's directory
        "..",                     # parent project folder
        "icons",
        "zippy.png"
    )
    image = Image.open(icon_path)  # load the icon image

    # Build submenu items for "File Locations"
    loc_items = []
    for i in range(1, 6):
        key = f"folder_path_{i}"
        # Use a factory to capture the loop variable correctly
        def make_action(k):
            # Each action must accept (icon, menu_item)
            return lambda icon, item: get_folder(data, k)
        # Create a menu item labeled "Location {i}" with its callback
        loc_items.append(item(f"Location {i}", make_action(key)))

    # Define the main tray menu structure
    tray_menu = Menu(
        item("Exit", close_zippy),  # top-level Exit option
        item("File Locations", Menu(*loc_items)),  # nested submenu
    )

    # Create and return the Icon object with title, image, and menu
    return Icon("Zippy", image, menu=tray_menu)
