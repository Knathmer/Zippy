# Standard Library
import platform
import time
import os

#Environment Variable Set
os.environ["UNRAR_LIB_PATH"] = r"C:\Users\18324\Documents\VSCodeProjects\Zippy\unrar.dll" # Environment Variable for unrar

# Third-Party Library
from pystray import Icon, MenuItem as item, Menu
from PIL import Image
from unrar import rarfile

# Functions
def close_zippy(icon, item): 
    icon.stop()
def testFunction():
    print("Button pressed!")


image = Image.open("icons/zippy.png") # Creates the image for the tray


menu = Menu(
        item('Exit', close_zippy), 
        item(
            'File Locations',
            Menu(
                item(
                    'Location 1',
                    testFunction),
                item(
                    'Location 2',
                    testFunction))))


# Constructing the entire menu
icon = Icon("test_icon", image, "Zippy", menu)







#rar = rarfile.RarFile('Industry Resumes.rar')
#print(rar.namelist())



icon.run()
