import pytest
import zippy.main
from zippy.ui import close_zippy
import threading
import time

def test_main():

    icon = None

    def run_icon():
        nonlocal icon
        icon = zippy.main.main(run_in_thread=True)

    t = threading.Thread(target=run_icon)
    t.start()
    time.sleep(4)

    assert icon is not None

    if icon:
        icon.stop()

    t.join(timeout=3)