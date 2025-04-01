# Standard Library
import platform
import time
import os
import json
import tkinter as tk
from tkinter import filedialog

#Environment Variable Set
os.environ["UNRAR_LIB_PATH"] = r"C:\Users\18324\Documents\VSCodeProjects\Zippy\unrar.dll" # Environment Variable for unrar

# Third-Party Library
from pystray import Icon, MenuItem as item, Menu
from PIL import Image
from unrar import rarfile

# Global Variables
state = False


# Settings Import
with open("settings.json", "r") as f:
    data = json.load(f)


# Functions
def close_zippy(icon, item):
    icon.stop()
def getFolderPath(settingName):
    folder_path = filedialog.askdirectory()
    if folder_path:
        data[settingName] = folder_path
        with open("settings.json", "w") as f:
            json.dump(data, f, indent = 4) 
        print("Selected folder:", folder_path)
        print(data)
    else:
        print("No folder selected.")
def on_clicked(icon, item):
    global state
    state = not item.checked

# tkinter init
root = tk.Tk()
root.withdraw()



image = Image.open("icons/zippy.png") # Creates the image for the tray

# Tray options
menu = Menu(
    item('Exit', close_zippy), 
    item(
        'File Locations',
        Menu(
            item(
                'Location 1',
                lambda: getFolderPath('folder_path_1')),
            item(
                'Location 2',
                lambda: getFolderPath('folder_path_2')),
            item(
                'Location 3',
                lambda: getFolderPath('folder_path_3')),
            item(
                'Location 4',
                lambda: getFolderPath('folder_path_4')),
            item(
                'Location 5',
                lambda: getFolderPath('folder_path_5'))
        )
    ),
    item(
        'Checkable',
        on_clicked,
        checked=lambda item: state)
)



# Constructing the entire menu
icon = Icon("test_icon", image, "Zippy", menu)







#rar = rarfile.RarFile('Industry Resumes.rar')
#print(rar.namelist())



icon.run()
