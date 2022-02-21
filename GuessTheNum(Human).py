import random

print("Enter range from which you want to guess the number")
n = int(input())
num = random.randint(1, n)
g = ng = 0
while g != num:
    print("Enter your guess: ", end="")
    g = int(input())
    ng += 1
    if g > num:
        print("Too High!!")
    elif g < num:
        print("Too Low!!")
    else:
        print("Congratulations, you guessed the number correctly in", ng, "guesses")