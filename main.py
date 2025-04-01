# Standard Library
import platform
import time
import os
import tkinter as tk
from tkinter import filedialog

#Environment Variable Set
os.environ["UNRAR_LIB_PATH"] = r"C:\Users\18324\Documents\VSCodeProjects\Zippy\unrar.dll" # Environment Variable for unrar

# Third-Party Library
from pystray import Icon, MenuItem as item, Menu
from PIL import Image
from unrar import rarfile

# Functions
def close_zippy(icon, item): 
    icon.stop()
def getFolderPath():
    folder_path = filedialog.askdirectory()
    if folder_path:
        print("Selected folder:", folder_path)
    else:
        print("No folder selected.")


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
                    getFolderPath),
                item(
                    'Location 2',
                    getFolderPath))))


# Constructing the entire menu
icon = Icon("test_icon", image, "Zippy", menu)







#rar = rarfile.RarFile('Industry Resumes.rar')
#print(rar.namelist())



icon.run()
