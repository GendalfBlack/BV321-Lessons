# Задача 2. Гра хрестики-нулики

def print_field(grid):
    global curr_player
    print("*--*"+"-"*8+"*")
    print(f"|{curr_player} |1 |2 |3 |")
    print("*--*"+"-"*8+"*")
    for i in range(3):
        print(f"|{i + 1} |{grid[i][0]} |{grid[i][1]} |{grid[i][2]} |")
        if i < 2: print("-"*13)
        else: print("*"+"-"*11+"*")
def check_comb(combination):
    global grid
    p = combination.split(" ")
    return  grid[int(p[0])][int(p[1])] == \
            grid[int(p[2])][int(p[3])] == \
            grid[int(p[4])][int(p[5])] and \
            grid[int(p[0])][int(p[1])] != " "
def check_win(*args):
    for comb in args:
        if check_comb(comb): return True
    return False

curr_player = "X"  # поточний гравець
grid = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
while True:
    print_field(grid)
    xy = input("Напишіть координати (Наприклад: 1 2): ")
    if len(xy.split(" ")) != 2: print("Неправильна кількість цифр(або пробілів)!"); continue
    x, y = int(xy.split(" ")[0]) - 1, int(xy.split(" ")[1]) - 1
    if grid[y][x] == " ":
        grid[y][x] = curr_player
        if check_win("0 0 0 1 0 2", "1 0 1 1 1 2", "2 0 2 1 2 2",
                     "0 0 1 0 2 0", "0 1 1 1 2 1", "0 2 1 2 2 2",
                     "0 0 1 1 2 2", "0 2 1 1 2 0"): break
        if curr_player == "X": curr_player = "O"
        else: curr_player = "X"
    else: print("Введіть координати вільної клітинки!")
print_field(grid)
print(f"Переміг: {curr_player}!")



