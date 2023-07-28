# - аргументи спаковані у словник (будь-яка кількість агрументів передана за допомогою
# ключових слів

def rect(**kargs):
    if 'height' not in kargs.keys():
        print("Бракує висоти прямокутника")
        return
    if 'width' not in kargs.keys():
        print("Бракує ширини прямокутника")
        return
    for i in range(kargs['height']):
        for j in range(kargs['width']):
            print('*', end="")
        print()

rect(width=10, height=5)