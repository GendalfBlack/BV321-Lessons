# списки, строки

# Список - это переменная, которая сохраняет в себе больше чем одно значение

x = 0
l = [1, 2, 3] # список из целых чисел (3 числа)
l2 = [1, 1.2, "text", True, [1, 2, 3]] # смешаный список из 5 значений разных типов

# Задача 1. Пользователь вводит числа с клавиатуры, програма выводит ему среднее значение
# среди всех чисел что он ввел до этого и числа которые образуют это значение

f = []  # пустой список
sum = 0
for i in range(10):
    n = int(input())
    f.append(n)  # добавляет один елемент в конец списка
    print(f, end=" ")
    sum += n
    print(sum/(i+1))

