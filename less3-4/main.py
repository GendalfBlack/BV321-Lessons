import turtle as t      # импорт библиотеки

w = t.Screen()          # создание окна для отображения

# i -> иттератор, переменная которая даёт счет
# сколько етапов(иттераций) цикла было проделано
for i in range(4):
    t.fd(100)
    t.lt(90)

w.exitonclick()         # специальная функция для вихода по клику на окно