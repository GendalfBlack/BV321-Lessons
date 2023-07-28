# Сортування, рядки

# Бульбашкове, вставками, вибіркою
import random as r
list = [r.randint(-10,10) for i in range(10)]

for i in range(len(list)):  # сортування вибіркою
    min = i
    for j in range(i + 1, len(list), 1):
        if list[j] < list[min]:
            min = j
    list[i], list[min] = list[min], list[i]
