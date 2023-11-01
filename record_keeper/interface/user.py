"""This is the UserInterface module. It contains the code for generating the
user interface
"""

from tkinter import Tk
from tkinter.ttk import Button, Frame, Label
from screeninfo import Monitor, get_monitors

import sv_ttk as SunValleyTheme

from .new_record import NewRecordInterface


class UserInterface(Tk):
    """Overrides the Tk function to create a custom user interface

    Args:
        Tk (Tk): The root Tk from tkinter
    """

    def __init__(self):
        super().__init__()
        self.monitor: Monitor

        self.create_ui()

    def create_ui(self) -> None:
        """Creates the UI elements
        """
        self.withdraw()  # Hide the window
        self.resizable(False, False)
        SunValleyTheme.set_theme("light")

        def _create_title() -> None:
            frame = Frame(self)
            frame.pack(fill="x")
            title = Label(frame, text="Record Keeper")
            title.pack(side="left")
            action_button = Button(frame, text="Update Data")
            action_button.pack(side="right")

        _create_title()
        self.update_ui()
        NewRecordInterface(self, self.monitor)
        self.deiconify()
        # self.state('zoomed')    # Full screen

    def update_ui(self) -> None:
        """Update function"""
        self.update()

        def get_current_screen_info() -> None:
            x = self.winfo_x()
            y = self.winfo_y()

            def which_monitor() -> Monitor:
                monitors = get_monitors()
                for m in reversed(monitors):
                    if ((m.x <= x <= m.width + m.x)
                            and (m.y <= y <= m.height + m.y)):
                        return m

                return monitors[0]

            self.monitor = which_monitor()

        get_current_screen_info()
        self.update()
