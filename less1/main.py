'''
print("Hello world") # команда виведення данних в консоль
# "text" будь-яка інформація записана в лапках являється ТЕКСТОВИМ ЛІТЕРАЛОМ
print(1) # print може виводити будь-який ТИП ДАНИХ (текст/число тощо)
# 1 будь-яке число являється ЧИСЕЛЬНИМ ЛІТЕРАЛОМ
print(1, 2, "фвіфі") # через кому можна вивести декілька значень

# Задача 1: Вивести всі степіні числа 2 в рядок через кому від 1 до 10.
print(2**2, 2**3, 2**4, 2**5, 2**6, 2**7, 2**8, 2**9, 2**10, sep=", ")
# sep= параметр що дозволяє визначити що буде між елементами які виводяться
# за замовчуванням sep=" "
'''
'''
# Задача 2: Вивести в консоль квадрат з зірочок 5*5
#print("**********\n**********\n**********\n**********\n**********\n")
# ESCAPE-послідовності - сполучення символа оберненеого слешу \ та букви
# що впливає на виведення на екран
# \t - відступ(табуляція)
# \n - перенос рядка
# \" - вивести лапки в коносль
# \' - вивести лапки в коносль
# \\ - вивести лапки в коносль
# \b - повернутись на 1 символ назад по вже виведеному тексту і далі друкувати
#      поверх існуючого текста
# +,-,*,/,  ** - підняття в степінь,  % - знаходження остачі,  // - знаходження цілого
print(5+5) print(5-5) print(5*5) print(5/5) print(5**5) print(7%3) print(7//3)'''
# print("Sasha"*1000) # рядок можна помножити на число (скопіювати n разів)
# Задача 3: Вивести кольори райдуги в консоль з нового рядка згідно прикладу:
'''
червоний оранжевий
         жовтий зелений
                блакитний синій
                          фіолетовий
'''
'''
# print("червоний оранжевий\n"," "*7,"жовтий зелений\n"," "*14,"блакитний синій\n"," "*24,"фіолетовий")

# Задача 4: За допомогою 5 print вивести 5 різних чисел в рядок
print(1, end=" ") # end= параметр що дозволяє змінити на що закінчується рядок
print(2, end=" ") #      за замовчуванням \n
print(3, end=" ")
print(4, end=" ")
print(5, end=" ")
'''
'''
# ЗМІННА
#cash = 100
#reciept = 30
#change = cash-reciept
#print(change)

# змінна створюється за допомогою назви та початкового значення
x = 100 # змінна що зберігає ціле число
f = 10.2 # не ціле число
t = "Hello" # рядок/текст
b = True # логічне значення

s = 10/5 # ділення залишає у відповіді НЕ ЦІЛЕ ЧИСЛО
s2 = 10//5 # ділення без остачі залишає у відповіді НЕ ЦІЛЕ ЧИСЛО
print(s2)
'''
'''
# Задача 5: Дано: кількість місяців, сумма абонентської плати, початкова кількість грошей.
# Визначити кошти після пройденого часу

m = 10
a = 125.50
c = 2131.20
x = c - a * m
print(f"Було грошей: {c} абонплата:{a} місяців: {m}\nсумма в кінці: {x:.2f}")
# форматований рядок спрощує вставлення змінних в текст, має починатися з f"" і всі змінні мають бути
# у фігурних дужках. Якщо написати x:.Nf -> змінна з нецілим значенням буде виведена з N знаками після коми

# Задача 6: Дано: довжина(h) та ширина(w) стіни, об'єм(V) фарби на м^2. Порахувати скільки треба фарби(x)
# на всю стіну вивести на екран результат.
h = 10
w = 10
v = 0.4
print(f"Необхідна кількість{h * w * v:.2f}")
'''

# КОМАНДА ДЛЯ ЗАПИСУ В ЗМІННУ ТЕКСТУ
# name = input("Напишіть своє ім'я: ")
# Команда input зупиняє програму та створює очікування введення з консолі. приймає введення
# після натискання клавіши Enter. ЗНАЧЕННЯ ЗАВЖДИ ТЕКСТОВЕ
#print("Вітаємо!", name)

# КОМАНДА ДЛЯ ЗАПИСУ В ЗМІННУ ЦІЛОГО ЧИСЛА
#i_number = int(input("Напишіть число: "))

# КОМАНДА ДЛЯ ЗАПИСУ В ЗМІННУ НЕЦІЛОГО ЧИСЛА
#f_number = float(input("Напишіть число: "))

# Задача 6: Користувач вводить два числа з клавіатури, програма показує їх сумму
'''a = int(input("Напишіть перше число: "))
b = int(input("Напишіть друге число: "))
c = a + b
print(f"{a}+{b}={c}")
'''
# Задача 7: Користувач пише в змінну (word) слово, що хоче вивести, а в змінну (n)
# скільки разів це слово має з'явитись в консолі.

word = input("Напишіть своє слово: ")
n = int(input("Напишіть число разів: "))
answ = (word + " ")* n
print(answ)