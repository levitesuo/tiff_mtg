from tkinter import Tk
from ui.main_view import MenuView
from ui.confirm_view import ConfirmView
from ui.progres_view import ProgresView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_main()

    def _show_main(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = MenuView(
            self._root,
            self._show_confirm
        )
        self._current_view.pack()

    def _show_confirm(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = ConfirmView(
            self._root,
            self._show_progres,
            self._show_main
        )
        self._current_view.pack()

    def _show_progres(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = ProgresView(
            self._root
        )
        self._current_view.pack()
