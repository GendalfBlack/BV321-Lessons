from tkinter import *
import random as r
w = Tk()
c = Canvas(w, width=800, height=600, bg="white")
c.pack()
list = [r.randint(0, 60) for i in range(30)]
x = 10
i = 0
def drawLine(index):
    global x
    el = list[index]
    c.create_rectangle(x, 600, x+10, 600-el*10, fill="green")
    x += 20
def drawAll():
    global i
    drawLine(i)
    i+=1
    if i < 30:
        w.after(10, drawAll)
def draw():
    global i, x
    c.create_rectangle(0, 0,800, 600, fill="white")
    i = 0;    x = 10
    drawAll()
w.after(1000, draw)
w.after(2000, draw)
w.mainloop()