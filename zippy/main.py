# zippy/main.py
from .ui import create_tray
import threading
import time as t

def main(run_in_thread=False):

    icon = None
    def create_and_run_icon():
        nonlocal icon
        icon = create_tray()
        icon.run()  # Blocking call, runs the icon event loop

    if not run_in_thread:
        create_and_run_icon()
        return True
    else:
        print("Running icon in a separate thread")
        icon_thread = threading.Thread(target=create_and_run_icon, daemon=True)
        icon_thread.start()
        t.sleep(4)
        return icon

if __name__ == "__main__":
    main()
