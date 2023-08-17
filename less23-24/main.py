# Програма, що зберігає інформацію про товари і надає можливість записувати нові товари
# так, щоб після відкриття додатку зберігалися усі додані товари під час попередніх
# запусків програми.

# Товар: назва, ціна, країна виробник, термін придатності

from tkinter import *

goods = []
entrys = []
w = None

def save_goods():
    f = open("database.txt", "w")
    lines = []
    for n in range(len(goods)):
        lines.append(goods[n]["Name"]+"~"
                +goods[n]["Price"]+"~"
                +goods[n]["Country"]+"~"
                +goods[n]["Date"])
    f.writelines(lines)
    f.close()

def reopen_add_window():
    w.destroy()
    create_add_window()

def create_list_window():
    global w
    w = Tk()
    labels = ["Назва", "Ціна", "Країна виробник", "Термін придатності"]
    for i in range(len(labels)):
        l = Label(w, text=labels[i], font="Arial 20")
        l.grid(row=1, column=i)
    keys = ["Name", "Price", "Country", "Date"]
    for n in range(len(goods)):
        for i in range(len(labels)):
            l = Label(w, text=goods[n][keys[i]], font="Arial 20")
            l.grid(row=n+2, column=i)
    b = Button(w, text="Додати новий товар", font="Arial 20")
    b.grid(row=0, column=0, columnspan=3)
    b.config(command=reopen_add_window)
    b2 = Button(w, text="Зберегти", font="Arial 20")
    b2.grid(row=0, column=3)
    b2.config(command=save_goods)
    w.mainloop()

def addGoods():
    new_goods = {"Name": entrys[0].get(),
                 "Price": entrys[1].get(),
                 "Country": entrys[2].get(),
                 "Date": entrys[3].get()}
    goods.append(new_goods)
    w.destroy()
    create_list_window()

def create_add_window():
    global w
    w = Tk()
    w.title("Додати новий товар")
    entrys.clear()
    labels = ["Назва", "Ціна", "Країна виробник", "Термін придатності"]
    for i in range(len(labels)):
        l = Label(w, text=labels[i], font="Arial 20", width=16, anchor=E)
        l.grid(row=i, column=0)
        e = Entry(w, font="Arial 20")
        e.grid(row=i, column=1, padx=15, pady=5)
        entrys.append(e)

    b = Button(w, text="Додати товар", font="Arial 20", width=20)
    b.grid(row=len(labels), columnspan=2, column=0,pady=15)
    b.config(command=addGoods)

    w.mainloop()

f = open("database.txt", "a+") # відкриваємо файл для читання, але в кінці після всіх даних
f.seek(0) # повернутись на початок файла
info = f.readlines()
f.close()
if len(info) == 0:
    create_add_window()
else:
    for line in info:
        if len(line.split('~')) < 4:
            continue
        parts = line.split('~')
        new_goods = {"Name": parts[0], "Price": parts[1], "Country": parts[2], "Date": parts[3]}
        goods.append(new_goods)
    create_list_window()
