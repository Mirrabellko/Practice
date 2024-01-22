import tkinter
from tkinter import messagebox

"""
Класс системного помощника, реализованы методы открытия файлов, сохранения файлов,
и вывод информационного окна
"""


class Handler:

    @staticmethod
    def save_file_txt(filename: str, data: str):
        if filename[-4:] != '.txt':
            filename = filename + '.txt'
        file = open(filename, "w")
        file.write(data)
        file.close()
        save_info = 'Your Note was saved.'
        Handler.show_info(save_info)

    @staticmethod
    def open_file(filename: str):
        file = open(filename, "r")
        data = file.read()
        file.close()
        return data

    @staticmethod
    def show_info(info: str):
        tkinter.messagebox.showinfo(title='Some infotmation:', message=info)