# Задача 1. Створити програму, що на початку дає вибір користувачу згенерувати 10 чисел
# випадково, чи ввести їх вручну, чи завантижити з файлу. Після чого числа зберігаються у файл.

import random as rnd
print("Виберіть один з варіантів: ")
print("1. Згенерувати 10 чисел випадково")
print("2. Вручну ввести 10 чисел")
print("3. Завантажити з файлу")
list = []
selection = input()
if selection == "1":
    list = [rnd.randint(-10,10) for i in range(10)]
    # for i in range(10):
    #   list.append(rnd.randint(-10,10))
elif selection == "2":
    for i in range(10):
        list.append(int(input(f"Введіть {i+1} число: ")))
else:
    f = open("numbers.txt", "a+"); f.seek(0)
    info = f.readlines()
    f.close()
    if len(info) == 10:
        list = [int(info[i]) for i in range(10)]
        # for i in range(10):
        #   list.append(int(info[i]))
print(list)
f = open("numbers.txt", "w")
for i in range(10):
    f.write(str(list[i]))
    if i != 9: f.write('\n')
f.close()
