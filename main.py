from pystray import Icon, MenuItem, Menu
from PIL import Image
import time

def exit_action(icon, item):
    icon.stop()

image = Image.new('RGB', (64, 64), (255, 0, 0)) # Creates the image for the tray
menu = Menu(MenuItem('Exit', exit_action)) # Creates
icon = Icon("test_icon", image, "My Tray App", menu)

icon.run()
