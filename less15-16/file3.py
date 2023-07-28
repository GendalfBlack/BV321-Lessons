'''

Зробити програмку-гру в якій є 1 напис та 9 кнопок, де користувач вгдує число.
Якщо число вірно, кнопка стає зеленою
Якщо ні - червоною

'''

from tkinter import *
import random as r

w = Tk()

l1 = Label(w, text="Вгадай число!", font="Arial 18")
l1.grid(row=0, column=0, columnspan=3)
bot = r.randint(1,9)
n = 3
def game(number, button):
    global n
    if n > 0 and n != 10:
        if bot == number:
            button.config(bg="green")
            l1.config(text="Перемога!")
            n = 10
        else:
            button.config(bg="red")
            n -= 1
    elif n == 0:
        l1.config(text="Програли!")
    else:
        pass

b1 = Button(w, text="1", command=lambda: game(1, b1), font="Arial 18", width=5)
b1.grid(row=1, column=0)
b2 = Button(w, text="2", command=lambda: game(2, b2), font="Arial 18", width=5)
b2.grid(row=1, column=1)
b3 = Button(w, text="3", command=lambda: game(3, b3), font="Arial 18", width=5)
b3.grid(row=1, column=2)
b4 = Button(w, text="4", command=lambda: game(4, b4), font="Arial 18", width=5)
b4.grid(row=2, column=0)
b5 = Button(w, text="5", command=lambda: game(5, b5), font="Arial 18", width=5)
b5.grid(row=2, column=1)
b6 = Button(w, text="6", command=lambda: game(6, b6), font="Arial 18", width=5)
b6.grid(row=2, column=2)
b7 = Button(w, text="7", command=lambda: game(7, b7), font="Arial 18", width=5)
b7.grid(row=3, column=0)
b8 = Button(w, text="8", command=lambda: game(8, b8), font="Arial 18", width=5)
b8.grid(row=3, column=1)
b9 = Button(w, text="9", command=lambda: game(9, b9), font="Arial 18", width=5)
b9.grid(row=3, column=2)

w.mainloop()