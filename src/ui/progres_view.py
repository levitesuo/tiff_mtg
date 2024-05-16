import sys
import tkinter as tk
from tkinter import ttk
from services.ui_service import service


class ProgresView:
    def __init__(self, root):
        self._root = root
        self._frame = None

        self.progres_val = tk.IntVar()
        self.progresbar = None
        self.lable = None

        self._init()

    def _init(self):
        self._frame = ttk.Frame(master=self._root)
        self.progresbar = ttk.Progressbar(
            master=self._frame, length=400, variable=self.progres_val)
        self.progresbar.pack(anchor='center', pady=10)
        self.lable = ttk.Label(
            master=self._frame, text=f"0 %")
        self.lable.pack(anchor='center', pady=10)

        self._frame.place(relx=.5, rely=.5, anchor='c')
        self._root.update()

        service.run(self._running_fucntion)

        self._root.destroy()
        sys.exit()

    def _running_fucntion(self, value):
        self.progres_val.set(int(value*100))
        self.lable.destroy()
        self.lable = ttk.Label(
            master=self._frame, text=f"{round(value*100, 2)} %")
        self.lable.pack(anchor='center', pady=10)

        self._root.update()
