"""The main runner for the program"""
__version__ = 1.0

from ctypes import windll

from interface.user import UserInterface
from confuse import Configuration

if __name__ == "__main__":
    CONFIG = Configuration("Record Keeper", __name__)
    # Set HiDPI mode
    windll.shcore.SetProcessDpiAwareness(2)

    Instance = UserInterface()
    Instance.mainloop()
