# Повторити типи даних, введення даних, оператори розгалужень
'''
# Типи даних
x = 0      # integer
f = 10.2   # float
t = "text" # string
b = True   # boolean

# input - введення даних з консолі, в дужках в input можна вказати текстовий фрагмент
#         що обов'язково відобразиться одразу перед введенням значення(підказка)
text = input("Введіть текст: ")                 # інформація записується в форматі string
integer = int(input("Введіть ціле число: "))    # integer
_float = float(input("Введіть неціле число: ")) # float
'''

import turtle as t
import random as rnd

w = t.Screen() # створити вікно для черепашки

t.fillcolor("brown")
t.begin_fill()
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.end_fill()
t.lt(180)
t.fd(100)
t.fillcolor("orange")
t.begin_fill()
t.lt(90)
t.fd(25)
t.rt(120)
t.fd(150)
t.rt(120)
t.fd(150)
t.rt(120)
t.fd(150)
t.end_fill()

t.lt(180)
t.fd(50)
t.rt(90)
t.pu()
t.fd(25)
t.pd()
t.fillcolor("blue")
t.begin_fill()
t.fd(25); t.lt(90); t.fd(25); t.lt(90);t.fd(25); t.lt(90);t.fd(25); t.lt(90)
t.end_fill()

w.exitonclick() # запустити режим очікування нажаття мишкою на будь-яку точку вікна