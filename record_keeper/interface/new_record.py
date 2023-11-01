"""Contains the NewRecordInterface module"""
from tkinter import Tk, Toplevel
from tkinter.ttk import Button, Frame

from noahs_utilities import center_window

from screeninfo import Monitor


class NewRecordInterface(Toplevel):
    """Creates the New Record interface

    Args:
        Toplevel (Toplevel): A toplevel window
    """

    def __init__(self, master: Tk, monitor: Monitor):
        self.master = master
        self.monitor = monitor
        super().__init__(master, background="red", highlightthickness=1)

        self.create_ui()

    def create_ui(self):
        """Creates the UI elements
        """
        # self.withdraw()

        self.geometry("500x500")
        self.resizable(False, False)
        self.grab_set()
        self.overrideredirect(True)
        self.focus_force()
        self.transient(self.master)  # type: ignore

        def _draw_button_box():
            frame = Frame(self)
            frame.pack(side="bottom")
            create = Button(frame, text="Create", command=self.destroy)
            create.pack(side="right")
            cancel = Button(frame, text="Cancel", command=self.destroy)
            cancel.pack(side="left")

        _draw_button_box()
        self.update()
        center_window(self, self.monitor)
        # self.deiconify()
