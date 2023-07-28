from tkinter import *
import random as r
w = Tk()
w.geometry("400x300")
def game(move, button):
    button.config(bg="")
    bot = r.randint(1,3)
    if bot == 1: l3.config(text="Камінь")
    elif bot == 2: l3.config(text="Ножиці")
    else: l3.config(text="Папір")
    if move == bot:
        l2.config(text="Нічия!", fg="yellow")
    elif (bot == 1 and move == 2) or (bot == 2 and move == 3) or (bot == 3 and move == 1):
        l2.config(text="Поразка!", fg="red")
    else:
        l2.config(text="Перемога!", fg="green")
l2 = Label(w, text="Ви граєте з комп'ютером\nзробіть хід:", font="Arial 18")
l3 = Label(w, text="", font="Arial 18", fg="red")
b3 = Button(w, text="Камінь", command=lambda: game(1,b3), font="Arial 20", width= 15)
b4 = Button(w, text="Ножиці", command=lambda: game(2), font="Arial 20", width= 15)
b5 = Button(w, text="Папір", command=lambda: game(3), font="Arial 20", width= 15)
l1 = Label(w, text="Вітаємо у грі\n Камінь-ножиці-папір", font="Arial 28")
l1.pack(pady=40)
def start(): l1.destroy(); b1.destroy(); b2.destroy(); l2.pack(); l3.pack(); b3.pack(); b4.pack(); b5.pack()
b1 = Button(w, text="Розпочати", command=start, width= 15, font="Arial 18")
b1.pack()
def exit(): w.destroy()
b2 = Button(w, text="Вийти", command=exit, width= 15, font="Arial 18")
b2.pack(pady=10)
w.mainloop()