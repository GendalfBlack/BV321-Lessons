# вкадені цикли
x = int(input("ширина: "))
y = int(input("висота: "))

for i in range(y):
    for j in range(x):
        if i == 0 or j == 0 or i == y - 1 or j == x - 1:
            print("*", end="")
        else:
            print("-", end="")
    print()

