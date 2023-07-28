from tkinter import *


def deleteItem(elements):
    elements["check"].destroy()
    elements["label"].destroy()
    elements["edit"].destroy()
    elements["delete"].destroy()


def createItem(w, row, text, elements):
    var = IntVar()
    c = Checkbutton(w, variable=var)
    c.grid(row=row, column=0)
    l = Label(w, text=text)
    l.grid(row=row, column=1, columnspan=5)
    edit = Button(w, text="Редагувати")
    edit.grid(row=row, column=6)
    delete = Button(w, text="Видалити")
    delete.grid(row=row, column=7)
    e = Entry(w)
    ok = Button(w, text="OK")

    elements["check"] = c
    elements["label"] = l
    elements["edit"] = edit
    elements["delete"] = delete
    elements["entry"] = e
    elements["ok"] = ok
    elements["row"] = row
    elements["var"] = var
    delete.config(command=lambda: deleteItem(elements))
    edit.config(command=lambda: openEdit(elements))
    ok.config(command=lambda: closeEdit(elements))
    c.config(command=lambda: checkButton(elements))

def openEdit(elements):
    elements["entry"].grid(row=elements["row"]+1, column=1, columnspan=5)
    elements["ok"].grid(row=elements["row"]+1, column=6, columnspan=2)
    elements["delete"].config(state=DISABLED)
    elements["edit"].config(state=DISABLED)
    elements["entry"].insert(0, elements["label"]["text"])

def closeEdit(elements):
    elements["delete"].config(state=NORMAL)
    elements["edit"].config(state=NORMAL)
    elements["label"]["text"] = elements["entry"].get()
    elements["entry"].destroy()
    elements["ok"].destroy()

def checkButton(elements):
    if elements["var"].get():
        elements["label"].config(bg="green")
    else:
        elements["label"].config(bg="grey94")



        