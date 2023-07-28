def equation(a, b, c):
    d = b * b - 4 * a * c
    if d < 0: return []
    elif d == 0: return [-b/(2*a)]
    else:
        return [ (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)]

print(equation(int(input("Введіть а: ")), int(input("Введіть b: ")), int(input("Введіть c: "))))

