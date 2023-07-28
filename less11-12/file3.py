def line(symbol="-", length=50):
    print(symbol*length)

line()
a = int(input("Введіть а: "))
b = int(input("Введіть b: "))
c = int(input("Введіть c: "))
line()
def numberPrint(n, text="", plus=True): # def - оператор створення функції
    result = ""                         # numberPrint - назва функції
    if n == 0: return result            # (n, text) - аргументи, що передаються у функцію
    elif n > 0 and plus: result += "+"+str(n)+text
    else: result += str(n)+text
    return result

print(numberPrint(a, "*x^2", False)+numberPrint(b, "*x")+numberPrint(c)+"=0")
line()
d = b * b - 4 * a * c

if d < 0: print("Коренів немає")
elif d == 0: print("x =",-b/(2*a))
else:
    print("x1 =", (-b + d ** 0.5) / (2 * a))
    print("x2 =", (-b - d ** 0.5) / (2 * a))
line()