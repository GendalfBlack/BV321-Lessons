# Задача 3. Користувач вводить речення та ключове слово, перевірити чи є
# це ключове слово в рядку без урахування регістру

text = input("Введіть речення: ")
word = input("Введіть слово: ")

if word.lower() in text.lower():
    print("Слово знайдено.")
else:
    print("Слово не знайдено.")
