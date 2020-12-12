board1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
p1 = ""
board = [" "] * 10


def display_board1(boarddd):
    print(boarddd[0] + " | " + boarddd[1] + " | " + boarddd[2])
    print("-" + " | " + "-" + " | " + "-")
    print(boarddd[3] + " | " + boarddd[4] + " | " + boarddd[5])
    print("-" + " | " + "-" + " | " + "-")
    print(boarddd[6] + " | " + boarddd[7] + " | " + boarddd[8])


def user_input(inp):
    while not inp.isdigit():
        inp = input("Please enter a valid position(1 to 9) : ")
    while int(inp) not in range(1, 10):
        inp = input("Please enter a valid position(1 to 9) : ")
    return int(inp)


def user_interaction():
    global p1
    print("Hi")
    p1 = input("Player 1, choose X or O : ")
    while p1 != "X" and p1 != "O":
        p1 = input("Invalid input, please choose X or O : ")


def playx():
    x = input("Enter the position to place X(1 to 9) : ")
    x = user_input(x)
    while board[x - 1] != " ":
        y = input("Position already occupied, please choose another one : ")
        x = user_input(y)
    board[x - 1] = "X"
    display_board1(board)


def playo():
    o = input("Enter the position to place O(1 to 9) : ")
    o = user_input(o)
    while board[o - 1] != " ":
        y = input("Position already occupied, please choose another one : ")
        o = user_input(y)
    board[o - 1] = "O"
    display_board1(board)


user_interaction()
display_board1(board1)
for h in range(1, 3):
    playx()

    playo()
playx()

for h in range(3, 10):
    if board[0] == board[1] == board[2] != " ":
        if p1 == board[2]:
            print("Player 1 wins")
        else:
            print("Player 2 wins")
        break
    elif board[0] == board[3] == board[6] != " ":
        if p1 == board[3]:
            print("Player 1 wins")
        else:
            print("Player 2 wins")
        break
    elif board[0] == board[4] == board[8] != " ":
        if p1 == board[4]:
            print("Player 1 wins")
        else:
            print("Player 2 wins")
        break
    elif board[3] == board[4] == board[5] != " ":
        if p1 == board[3]:
            print("Player 1 wins")
        else:
            print("Player 2 wins")
        break
    elif board[6] == board[7] == board[8] != " ":
        if p1 == board[6]:
            print("Player 1 wins")
        else:
            print("Player 2 wins")
        break
    elif board[1] == board[4] == board[7] != " ":
        if p1 == board[1]:
            print("Player 1 wins")
        else:
            print("Player 2 wins")
        break
    elif board[2] == board[5] == board[8] != " ":
        if p1 == board[2]:
            print("Player 1 wins")
        else:
            print("Player 2 wins")
        break
    elif board[2] == board[4] == board[6] != " ":
        if p1 == board[2]:
            print("Player 1 wins")
        else:
            print("Player 2 wins")
        break
    else:
        if h % 2 == 0:
            playx()
        else:
            playo()
        check = True
        for i in range(0, 10):
            if board[i] == " ":
                check = False
        if check:
            print("Match Draw")
            break
