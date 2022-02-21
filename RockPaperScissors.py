import random

op = ["Rock", "Paper", "Scissor"]


def result(n, m):
    if (n == 1 and m == 2):
        return m
    elif (n == 1 and m == 3):
        return n
    elif (n == 2 and m == 1):
        return n
    elif (n == 2 and m == 3):
        return m
    elif (n == 3 and m == 1):
        return m
    elif (n == 3 and m == 2):
        return n
    else:
        return 7


def dis(n):
    if n == 1:
        print("Rock")
    elif n == 2:
        print("Paper")
    else:
        print("Scissors")


n = m = 0
nn = mm = 0
print("This game of rock, paper, scissors is a race to 3. First one to win three times wins the game.")
while nn < 3 and mm < 3:
    print("Enter 1 to select Rock, 2 to select paper, 3 to select scissor")
    n = int(input())
    while(True):
        if n < 1 or n > 3:
            n = int(input("Enter either 1, 2 ro 3: "))
        else:
            break
    m = random.randint(1, 3)
    print("You selected: ", end="")
    dis(n)
    print("Computer selected: ", end="")
    dis(m)
    if (result(n, m) == n):
        print("You won this round")
        nn += 1
    elif (result(n, m) == m):
        print("You Lost this round")
        mm += 1
    else:
        print("Tie Round")
    print("Scores", nn, ":", mm)
    print("\n")

print("\n\n")

if (nn == 3):
    print("Good Job! You've won")
else:
    print("Oh No! Better luck next time")
