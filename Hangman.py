import random

words = ["apple", "mango", "orange", "watermelon", "papaya", "guava", "kiwi", "grapes",
         "mercedes", "ford", "bottle", "mouse",  "phone", "remote", "charger", "brush"]


def blanks(s):
    letters = []
    for j in range(0, len(s) // 2):
        x = random.randint(0, len(s) - 1)
        if s[x] != '_':
            letters.append(s[x])
            s = s.replace(s[x], '_', 1)
    return s


def nob(aw):
    nb = 0
    for i in aw:
        if i == '_':
            nb += 1
    return nb


def display(bw):
    print("\t", end="")
    for i in bw:
        print(i, end=" ")
    print("\n\t", end="")
    for i in range(0, len(bw)):
        print(i + 1, end=" ")
    print()


def play(bw, nw, nb):
    tries = 5
    while tries > 0 or nb > 0:
        pos = int(input("Enter the position, where you want to guess the letter: "))
        while(True):
            if bw[pos-1] != "_" or pos > len(bw):
                pos = int(
                    input("Enter only the position of blank where you want to guess the letter"))
            else:
                break
        let = input("Enter the letter: ").lower()
        if nw[pos - 1] == let:
            print("Correct Guess")
            bw = bw[0:pos - 1] + let + bw[pos:]
            nb -= 1
        elif nw[pos - 1] != let:
            print("Wrong Guess!! You have", tries - 1, "guesses remaining")
            tries -= 1
        if tries != 0 or nb != 0:
            display(bw)
        if nb == 0:
            return 0
        if tries == 0:
            return 1


print("--------------Hangman-------------")
while True:
    word = words[random.randint(0, len(words) - 1)]
    print("You will have 5 guesses to guess all the missing letters")
    print("You have to guess the missing letters and complete the word given below")
    w = blanks(word)
    display(w)
    res = play(w, word, nob(w))
    if res:
        print("You ran out of tries :(")
    else:
        print("Yay! You guesses the letters of the word correctly")
    ch = int(input("Press 1 if you want to play again, 2 if you want to quit: "))
    if ch == 1:
        continue
    break

print("Thanks for playing")

