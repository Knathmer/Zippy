# zippy/main.py
from .ui import create_tray
import threading
import time as t

def main(run_in_thread=False):

    icon = None
    def create_and_run_icon():
        nonlocal icon
        icon = create_tray()
        icon.run()

    if not run_in_thread:  # For testing purposes

        create_and_run_icon()
        return True
    else:
        icon_thread = threading.Thread(target=create_and_run_icon, daemon=True)
        icon_thread.start()
        t.sleep(4)
        return icon

if __name__ == "__main__":
    main()
