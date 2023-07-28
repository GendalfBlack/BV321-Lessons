# Задача 6. Зробити генератор паролів, що створить пароль бажаної величини
# використовуючи великі та маленькі англійські літери, цифри та символи
import string
import random
password = ""

s = string.digits + string.ascii_letters + string.punctuation

n = int(input("Введіть бажану довжину пароля: "))
for i in range(n):
    password += random.choice(s)

print(password)
