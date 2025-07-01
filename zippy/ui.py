from pystray import Icon, MenuItem as item, Menu
from PIL import Image
from .config import load, save
from .extractor import list_contents

def create_tray():
    data = load()
    image = Image.open("icons/zippy.png")
    # build your Menu(...) here, wiring getFolderPath & list_contents
    return Icon("Zippy", image, menu=...)
