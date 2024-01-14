from tkinter import *
from tkinter import filedialog

class Notebook:
    def __init__(self, root):
        self.root = root
        self.root.title('Notebook')
        self.root.geometry('600x350')
        self.root.iconbitmap('icon.ico')
        self.root.resizable(width=False, height=False)
        self.frame = self.add_frame(root)
        self.btn_frame = self.add_frame(root)
        self.textbox = self.add_textbox(root)

    def add_frame(self, root):
        frame = Frame(root)
        frame.pack()
        return frame

    def add_button(self, name: str, btn_command, x: int, y: int):
        btn = Button(self.btn_frame, text=name, command=btn_command, width=20)
        btn.grid(row=x, column=y)


    def add_textbox(self, root):
        #frame = self.add_frame(root)
        txtbox = Text(self.frame, height=20, width=60)
        scroll = Scrollbar(self.frame)
        scroll.pack(side=RIGHT, fill=Y)
        txtbox.pack(side=LEFT, fill=Y)
        scroll.config(command=txtbox.yview)
        txtbox.config(yscrollcommand=scroll.set)
        txtbox.pack()
        return txtbox


    def add_menu(self, root):
        self.btn_frame.pack(side=LEFT)
        bnt_new = self.add_button(name='New', btn_command=self.new_file, x=0, y=0)
        btn_save = self.add_button(name='Save', btn_command=self.save_file, x=0, y=1)
        btn_open = self.add_button(name='Open', btn_command=self.open_file, x=0, y=2)
        btn_exit = self.add_button(name='Exit', btn_command=exit, x=0, y=3)

    def new_file(self):
        self.textbox.delete('1.0', END)


    def save_file(self):
        fileName = filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt")])
        data = self.textbox.get(1.0, "end-1c")
        print(fileName)
        fobj = open(fileName, "w")
        fobj.write(data)
        fobj.close()

    def open_file(self):
        self.textbox.delete('1.0', END)
        fileName = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        print(fileName)
        fobj = open(fileName, "r")
        data = fobj.readlines()
        fobj.close()
        self.textbox.insert(END, data)


def start():
    root = Tk()
    ntbk = Notebook(root)
    ntbk.add_menu(root)
    root.mainloop()


if __name__ == '__main__':
    start()
