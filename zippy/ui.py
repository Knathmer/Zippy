# zippy/ui.py

from pystray import Icon, MenuItem as item, Menu
from PIL import Image
import tkinter as tk  # tkinter for folder selection dialog
from tkinter import filedialog
from functools import partial
from .config import load, save
from .extractor import extract
import os

isModified = False
# Helper Functions

def setpath(data, key, path):
            global isModified
            if key not in data:
                raise KeyError(f"Key `{key}` not found in data.")
            if data[key] != path:
                data[key] = path
                isModified = True

# Callback Functions

def get_folder(data, key):
    global isModified
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askdirectory(
        initialdir=os.path.expanduser('~'),
        title=f"Select Folder for {key.replace('_', ' ').title()}",
        mustexist=True
    )
    if data[key] != path and path != "":
        setpath(data, key, path)


def get_file(data, key="current_file"):
    global isModified
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askopenfilename(
        initialdir=os.path.expanduser('~'),
        title=f"Select File to Extract",
        filetypes=[("RAR files", "*.rar"), ("All files", "*.*")]
    )
    if data[key] != path and path != "":
        setpath(data, key, path)

def close_zippy(icon, _, data):
    if isModified:
        save(data)
    icon.stop()


# Functions

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

    def on_click_select(icon, menu_item, f_key, getfolder=False):
        if getfolder:
            get_folder(data, f_key)
        else:
            get_file(data, f_key)

    for i in range(1, 6):
        key = f"folder_path_{i}"
        label = f"Location {i}"
        handler = partial(on_click_select, f_key=key, getfolder=True)
        loc_items.append(item(label, handler))

    close_handler = partial(close_zippy, data=data)  # Handler for Exit option
    select_file_handler = partial(on_click_select, f_key='current_file')  # Handler for Extract File option

    # Define the main tray menu structure
    tray_menu = Menu(
        item("Exit", close_handler),  # top-level Exit option
        item("File Locations", Menu(*loc_items)),  # nested submenu
        item("Extract File", select_file_handler)  # Extract File option
    )

    # Create and return the Icon object with title, image, and menu
    return Icon("Zippy", image, menu=tray_menu)
