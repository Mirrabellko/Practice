import GUIsettings as GUI
from tkinter import *
from tkinter import filedialog
import system_adapter as sysad


class Notebook:
    def __init__(self, textbook: Text):
        self.textbook = textbook

    def new_file(self):
        self.textbook.delete('1.0', END)

    def save_file(self):
        filename = filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt")])
        data = self.textbook.get(1.0, "end-1c")
        sysad.Handler.save_file_txt(filename, data)

    def open_file(self):
        self.textbook.delete('1.0', END)
        filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        data = sysad.Handler.open_file(filename)
        self.textbook.insert(END, data)
