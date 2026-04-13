import random

board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
gameOn = True
player_1_turn = True

def draw_board():
    print(" |0|1|2")
    for i in range(3):
        print(i, end="")
        for j in range(3):
            print(f"|{board[i][j]}", end = "")
        print()

def read_input():
    row = int(input("Add meg a sor indexét: "))
    col = int(input("Add meg az oszlop indexét: "))
    while row < 0 or row >= 3 or col >= 3 or col < 0 or board[row][col] != "-":
        if row < 0 or row >= 3 or col >= 3 or col < 0:
            print("A sornak és az oszlopnak is 0 és 2 között kell lennie!")
        else:
            print("Ez a hely már foglalt!")
        row = int(input("Add meg a sor indexét: "))
        col = int(input("Add meg az oszlop indexét: "))

    return row, col

def computer_input():
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    while board[row][col] != "-":
        row = random.randint(0, 2)
        col = random.randint(0, 2)
    return row, col

def place_mark(row, col):
    if player_1_turn:
        board[row][col] = "X"
    else:
        board[row][col] = "O"

def is_full():
    has_dash = False
    for row in board:
        for cell in row:
            if cell == "-":
                has_dash = True
    return not has_dash

def check_board():
    # Sorok ellenőrzése:
    for i in range(3): # 0, 1, 2
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][1] != "-":
            return board[i][0]
    # Oszlopok ellenőrzése:
    for j in range(3):
        if board[0][j] == board[1][j] and board[1][j] == board[2][j] and board[0][j] != "-":
            return board[0][j]
    # Átlók ellenőrzése
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] != "-":
        return board[1][1]
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[1][1] != "-":
        return board[1][1]
    return None
    
# Addig meg a játék, amíg valaki nem nyer, vagy döntetlen, nem lesz
while gameOn:
    print()
    draw_board()
    if player_1_turn:
        row, col = read_input()
    else:
        row, col = computer_input()
    place_mark(row, col)
    winner = check_board() # "X", "O", None
    if winner: # "X", "O" (nem None)
        print(f"Az {winner} játékos nyert!")
        gameOn = False
        break
    if is_full():
        print("Döntetlen!")
        gameOn = False
        break
    player_1_turn = not player_1_turn

draw_board()
