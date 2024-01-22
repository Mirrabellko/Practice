import system_settings as sysset
from tkinter import *

"""
Класс пользовательского интерфейса. 
"""


class MainWindow(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root

    def make_window(self):
        self.root.title('Notebook')
        self.root.geometry('600x400')
        self.root.iconbitmap('icon.ico')
        self.root.resizable(width=False, height=False)

    def add_frame(self, root):
        frame = Frame(root)
        frame.pack()
        return frame

    def add_textbook(self, root):
        txtbox = Text(root, height=20, width=100)
        scroll = Scrollbar(root)
        scroll.pack(side=RIGHT, fill=Y)
        txtbox.pack(side=LEFT, fill=Y)
        scroll.config(command=txtbox.yview)
        txtbox.config(yscrollcommand=scroll.set)
        txtbox.pack()
        return txtbox

    def __add_button(self, frame, name: str, btn_command, x: int, y: int):
        btn = Button(frame, text=name, command=btn_command, width=20)
        btn.grid(row=x, column=y)
        return btn


    def add_menu(self, btn_frame, notebook: sysset.Notebook):
        btn_frame.pack(side=BOTTOM)
        btn_new = self.__add_button(btn_frame, name='New', btn_command=notebook.new_file, x=0, y=0)
        btn_save = self.__add_button(btn_frame, name='Save', btn_command=notebook.save_file, x=0, y=1)
        btn_open = self.__add_button(btn_frame, name='Open', btn_command=notebook.open_file, x=0, y=2)
        btn_exit = self.__add_button(btn_frame, name='Exit', btn_command=exit, x=0, y=3)


def start():
    root = Tk()
    ntbk = MainWindow(root)
    ntbk.make_window()
    main_frame = ntbk.add_frame(root)
    btn_frame = ntbk.add_frame(main_frame)
    textbook = ntbk.add_textbook(main_frame)
    notebook = sysset.Notebook(textbook)
    ntbk.add_menu(btn_frame, notebook)
    root.mainloop()
