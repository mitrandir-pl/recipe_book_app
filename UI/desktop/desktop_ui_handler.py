import tkinter as tk

from dataclasses import dataclass

from fastapi_app.DB import DatabaseHandler
from UI import UIHandler
from UI.desktop.MainWindow import Windows


@dataclass
class DesktopUIHandler(UIHandler):
    db_handler: DatabaseHandler

    def run(self) -> None:
        start = Windows()
        start.MainWindows()
        tk.mainloop()
