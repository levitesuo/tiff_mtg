from tkinter import ttk
from services.ui_service import service


class ConfirmView:
    def __init__(self, root, start_command, cancel_command):
        self._root = root
        self._frame = None

        self._start_command = start_command
        self._cancel_command = cancel_command

        self._init()

    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.place(relx=.5, rely=.5, anchor='c')

    def _init(self):
        self._frame = ttk.Frame(master=self._root)
        notice_lable = ttk.Label(master=self._frame,
                                 text=f"Do you want to generate pdf(s) of {self._calc_cards()} cards?", foreground='red', font=("Noto Mono", 15, 'bold')
                                 )
        notice_lable.pack(anchor='w', pady=20)

        confirm_button = ttk.Button(
            master=self._frame,
            text="Confirm",
            command=self._start_command
        )
        confirm_button.pack(anchor='center', pady=10)
        cancel_button = ttk.Button(
            master=self._frame,
            text="Cancel",
            command=self._cancel_command
        )
        cancel_button.pack(anchor='center', pady=10)

    def _calc_cards(self):
        return sum([int(card['amount']) for card in service.text])
