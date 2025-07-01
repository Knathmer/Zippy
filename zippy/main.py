# zippy/main.py
from .ui import create_tray

def main():
    icon = create_tray()
    icon.run()

if __name__ == "__main__":
    main()
