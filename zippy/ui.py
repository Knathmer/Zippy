# zippy/ui.py

from pystray import Icon, MenuItem as item, Menu
from PIL import Image
import tkinter as tk  # tkinter for folder selection dialog
from tkinter import filedialog
from functools import partial
from .config import load, save
from .extractor import extract
import os
from typing import Any


# Helper Functions
def fetch_icon_path() -> str:
    icon_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "icons",
        "zippy.png"
    )
    return icon_path

# Changing settings in settings.json
def setpath(data: dict, key: str, path: str) -> None:
            if key not in data:
                raise KeyError(f"Key `{key}` not found in data.")
            if data[key] != path:
                data[key] = path
                save(data)


# Callback Functions
def get_folder(data: dict, key: str) -> None:
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askdirectory(
        initialdir=os.path.expanduser('~'),
        title=f"Select Folder for {key.replace('_', ' ').title()}",
        mustexist=True
    )
    if data[key] != path and path != "":
        setpath(data, key, path)


def get_file(data: dict, key: str = "current_file") -> None:
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askopenfilename(
        initialdir=os.path.expanduser('~'),
        title=f"Select File to Extract",
        filetypes=[("RAR files", "*.rar"), ("All files", "*.*")]
    )
    if data[key] != path and path != "":
        setpath(data, key, path)


def close_zippy(icon: Icon, _: Any, data: dict) -> None:
    icon.stop()


# Functions
def create_tray() -> Icon:

    def on_click_select(icon, menu_item, f_key: str, folder: bool = False):
        if folder:
            get_folder(data, f_key)
        else:
            get_file(data, f_key)
    
    def on_click_set_current_folder(icon, menu_item, source_key: str):
        """Set current_file to the value of the specified folder path"""
        if source_key in data and data[source_key]:
            setpath(data, "current_folder", data[source_key])

    def on_click_extract_current_file(icon, menu_item, data: dict):
        """Extract the current file to the current folder"""
        if data["current_file"] and data["current_folder"]:
            extract(data["current_file"], data["current_folder"])

            
    # File locations are loaded from settings.json from a previous session
    data = load()
    number_of_locations = 6
    # icon_path set to location of the icon image
    image = Image.open(fetch_icon_path())  # load the icon image

    # Build submenu items for "File Locations"
    loc_items = []

    for i in range(1, number_of_locations):
        key = f"folder_path_{i}"
        label = f"Location {i}"
        handler = partial(on_click_select, f_key=key, folder=True)
        loc_items.append(item(label, handler))
    
    # Build submenu items for "Current Folder" - these set current_file to existing folder paths
    current_folder_items = []
    
    for i in range(1, number_of_locations):
        key = f"folder_path_{i}"
        label = f"Location {i}"
        # Show the actual path in the label if it exists
        if key in data and data[key]:
            label = f"Location {i}: {data[key]}"
        handler = partial(on_click_set_current_folder, source_key=key)
        current_folder_items.append(item(label, handler))

    close_handler = partial(close_zippy, data=data)  # Handler for Exit option
    select_file_handler = partial(on_click_select, f_key='current_file')  # Handler for Extract File option
    extract_current_file_handler = partial(on_click_extract_current_file, data=data)  # Handler for Extract Current File option

    # Define the main tray menu structure
    tray_menu = Menu(
        item("Exit", close_handler),  # top-level Exit option
        item("File Locations", Menu(*loc_items)),  # nested submenu for setting folder paths
        item("Extract File", select_file_handler),  # Extract File option
        item("Current Folder", Menu(*current_folder_items)),  # nested submenu for selecting current folder
        item("Extract Current File", extract_current_file_handler)
    )

    # Create and return the Icon object with title, image, and menu
    return Icon("Zippy", image, menu=tray_menu)
