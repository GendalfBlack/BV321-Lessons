# Canvas, checkbox, list, dictionary, functions

from tkinter import *
from listItem import *

w = Tk()
w.geometry("400x600")
e1 = Entry(w, width=40)
e1.grid(row=0, column=0, columnspan=6)

list = []
row = 1
def buttonClick():
    global row
    element = {}
    list.append(element)
    createItem(w, row, e1.get(), element)
    e1.delete(0, END)
    row += 2

b1 = Button(w, text="Додати", command=buttonClick)
b1.grid(row=0, column=6, columnspan=2)

w.mainloop()