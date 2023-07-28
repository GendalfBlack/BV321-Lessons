# Задача 1. Користувач має ввести три числа. Ці числа являються коефіцієнтами
# квадратного рівняння. Підствивши числа в формули знайти корені рівняння.

a = int(input("Введіть а: "))
b = int(input("Введіть b: "))
c = int(input("Введіть c: "))

def numberPrint(n, text="", plus=True): # def - оператор створення функції
    result = ""                         # numberPrint - назва функції
    if n == 0: return result            # (n, text) - аргументи, що передаються у функцію
    elif n > 0 and plus: result += "+"+str(n)+text
    else: result += str(n)+text
    return result

print(numberPrint(a, "*x^2", False)+numberPrint(b, "*x")+numberPrint(c)+"=0")

d = b * b - 4 * a * c

if d < 0: print("Коренів немає")
elif d == 0: print("x =",-b/(2*a))
else:
    print("x1 =", (-b + d ** 0.5) / (2 * a))
    print("x2 =", (-b - d ** 0.5) / (2 * a))