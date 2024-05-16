from tkinter import ttk
import tkinter as tk
from tkinter.filedialog import asksaveasfilename
from services.ui_service import service
from tkinter.scrolledtext import ScrolledText


class MenuView:
    def __init__(self, root, start_command):
        self._root = root
        self._frame = None

        self._start_command = start_command

        self._init()

    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.place(relx=.5, rely=.5, anchor='c')

    def _init(self):
        self._frame = ttk.Frame(master=self._root)
        header = ttk.Label(
            master=self._frame,
            text="MTG high res pdf tool",
            font=("Noto Mono", 30, 'bold')
        )
        header.pack(anchor='n', pady=10)

        notice_lable = ttk.Label(master=self._frame,
                                 text="Instuctions follow in blue.", foreground='blue', font=("Noto Mono", 15, 'bold')
                                 )
        notice_lable.pack(anchor='w')

        instructions = """1. Go to mtgprint.net and select the cards that you want.
2. Copy past the cardnames with all the extra bits. Make sure that there is no extra characters.
3. Select the desiered dpi filename and mark size. Set mark size 1 for no cutmarks.
4. Wait patiently while the aplication is working.
5. Select the direcotry and filename for saving the file."""
        notice_lable = ttk.Label(master=self._frame,
                                 text=instructions, foreground='blue', font=("Noto Mono", 11)
                                 )
        notice_lable.pack(anchor='w', pady=5)

        contetn_frame = ttk.Frame(master=self._frame)

        filename_frame = ttk.Frame(master=contetn_frame)

        self.dpi = self._draw_text_box(
            'dpi', '1200', filename_frame)

        self.mark = self._draw_text_box(
            'mark size', '401', filename_frame)

        start_button = ttk.Button(
            master=filename_frame,
            text="Run",
            command=self._start_function
        )

        start_button.pack(anchor='w', pady=5)

        filename_frame.grid(row=0, column=0)
        self.textfield = ScrolledText(master=contetn_frame, wrap=tk.WORD)
        self.textfield.grid(row=0, column=1, padx=10)
        contetn_frame.pack(pady=5)

    def _loop_function(self, value):

        self.progres.set(min(int(value*100), 99))
        self._root.update()

    def _start_function(self):
        text = self.textfield.get("1.0", tk.END)
        filename = asksaveasfilename()
        dpi = self.dpi.get()
        mark = self.mark.get()

        service.init(text, dpi, mark, filename)

        self._start_command()

    def _draw_text_box(self, lable_text, placeholder_text, frame):
        '''
        Draws text box in frame with given placeholder text and lable text.
        The ttk.Entry object will be returned.
        '''
        box_frame = ttk.Frame(master=frame)
        lable_obj = ttk.Label(master=box_frame, text=lable_text)
        box_variable = ttk.Entry(master=box_frame, foreground='gray')

        def on_entry_click(event):
            if box_variable.get() == placeholder_text:
                box_variable.delete(0, 'end')
                box_variable.configure(foreground="black")

        def on_focus_out(event):
            if box_variable.get() == "":
                box_variable.insert(0, placeholder_text)
                box_variable.configure(foreground="gray")

        box_variable.insert(0, placeholder_text)

        box_variable.bind("<FocusIn>", on_entry_click)
        box_variable.bind("<FocusOut>", on_focus_out)

        lable_obj.pack(anchor='nw')
        box_variable.pack(anchor='ne')

        box_frame.pack(anchor='w', pady=5)
        return box_variable
