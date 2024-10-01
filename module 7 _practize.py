import os
import tkinter
from tkinter import filedialog


def file_select():
    filename = filedialog.askopenfilename(initialdir="/", title="Выберите файл",
                                          filetypes=(("Текстовый файл", ".txt"),
                                                     ("Все файлы", "*")))
    text["text"] = text["text"] + filename
    os.startfile(filename)


window = tkinter.Tk()
window.title("Проводник")
window.geometry("500x350")
window.configure(bg="black")
window.resizable(False, False)
text = tkinter.Label(window, text="Файл", height=3, width=80, background="purple", foreground="blue")
text.grid(column=1, row=1)
text.place(x=0, y=120)
button_select = tkinter.Button(window, height=5, text="Выбрать файл", background="green", foreground="blue",
                               command=file_select)
button_select.grid(column=1, row=2)
button_select.place(x=130, y=200)
window.mainloop()
