from tkinter import *
import os
from random import randint, choice

w = Tk() # создание окна
w.config(bg="coral1")
w.title("less21-22")
w.geometry("800x600")

e = Entry(w, font="Consolas 20", width=40)
e.pack()

def buttonClick():
    dirname = e.get()
    dirfiles = os.listdir(dirname)
    for element in dirfiles:
        fullpath = dirname+'\\'+element
        if os.path.isfile(fullpath):
            l.config(text=l["text"]+element+'\n')
        else:
            l.config(text=l["text"] + element + '\\\n')

b = Button(w, text="Open", font="Consolas 20", width=20, command=buttonClick)
b.pack()

l = Label(w, text="Files:", fg="red4", font="Consolas 8", width=90)
l.pack()

w.mainloop()