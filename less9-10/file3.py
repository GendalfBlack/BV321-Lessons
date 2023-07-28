# Задача 4. Користувач вводить речення в консоль, програма виводить всі слова
# з речення з нового рядка в нижньому регістрі.

text = input("Введіть речення: ")

for letter in text:
    if letter == " ":
        print()
    elif letter.isalpha():
        print(letter.lower(), end="")

print()
words = text.split(" ")
for word in words:
    print(word.lower())
    