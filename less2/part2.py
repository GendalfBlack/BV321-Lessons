import random as rnd

number = rnd.randint(1, 10) # функція створить випадкове число від 1 до 10
print("Введіть своє число: ", end="")
x = int(input())
if x == number:
    print("Ви вгадали!")
elif x > number:
    print("Треба було менше!")
else:
    print("Треба було більше!")

print("Дякую за гру!")



