# Canvas та івенти. Функції

from tkinter import *
from visualize import *

list = [] # список для майбутніх чисел на діаграмі

w = Tk() # створення вікна програми

c = Canvas(w, width=400, height=400, bg="white") # створення канваса для малювання діаграми
c.grid(row=0, column=0, rowspan=20) # канвас на весь екран в висоту (rowspan=20)

e = Entry(w, width=30) # створення поля для введення чисел
e.grid(row=0, column=1) # наступний стовпчик після канваса

b = Button(w, text="Додати", command=lambda: addElement(e.get(), l, c, list))
# створення кнопки для додавання чисел в список з викликом функції з іншого файлу
b.grid(row=0, column=2) # наступний стовпчик після поля введення

l = Label(w, text="Числа:\n", justify=LEFT, wraplength=250) # створення напису що буде показувати числа
# justify - вирівнювання текста по лівому краю.
# wraplength=250 - після 250 пікселів текст буде перенесено на новий рядок
l.grid(row=2, column=1, rowspan=19, columnspan=2, sticky=NW) # наступний рядок після поля для введення

w.mainloop()# відкриття вікна на екрані