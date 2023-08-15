path = r"Z:\PKO\Python\BV321\less21-22\mytext.txt"
#name = input("Введите имя вашего файла:")

f = open(path, "a")

f.write("1")

f.close()

f = open(path, "r")

print(f.read())

f.close()


# r -> только чтение. файла не существует = ошибка