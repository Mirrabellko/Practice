from tkinter import *

MainCatalog = []

def btn_click():
    print('Button click!')

def btn_exit():
    exit()

def auto_save(maincatalog: list):
    new_txt = ''
    for i in maincatalog:
        new_txt = str(i[0]) + ',' + str(i[1]) + '\n'
    with open('note_catalog.txt', 'a') as file:
        file.write(new_txt)
    print('Catalog was saved')


def btn_load():
    pass

def set_noteid(maincatalog: list):
    id = len(maincatalog) + 1
    return id

def add_new_to_catalog():
    new_note = entry1.get()
    add = [set_noteid(MainCatalog), new_note]
    MainCatalog.append(add)
    print(len(MainCatalog))
    auto_save(MainCatalog)


root = Tk()

root.title('Notebook')
root.geometry('300x200')
root.iconbitmap('icon.ico')
root.resizable(width=False, height=False)

frame1 = Frame(root)
frame1.grid()

label1 = Label(frame1, text='Введите заметку:', pady=10)
label1.grid(column=0, row=0)

entry1 = Entry(frame1, width=20)
entry1.grid(column=0, row=1, padx=10)

label2 = Label(frame1, text='Меню')
label2.grid(column=8,row=0, padx=80)

button_save = Button(frame1, text='Сохранить', command=add_new_to_catalog, width=10)
button_save.grid(column=8,row=1, padx=70)

button_open = Button(frame1, text='Открыть', command=btn_click, width=10)
button_open.grid(column=8,row=2, padx=70)

button_delete = Button(frame1, text='Удалить', command=btn_click, width=10)
button_delete.grid(column=8,row=3, padx=70)

button_exit = Button(frame1, text='Выход', command=btn_exit, width=10)
button_exit.grid(column=8,row=6, padx=70)

label3 = Label(frame1, text='Каталог:')
label3.grid(column=0, row=3, padx=10)

root.mainloop()