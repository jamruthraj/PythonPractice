print("Enter the number of digits of your number")
n = int(input())
print("I will generate a number, press 1 if my guess is too high, 2 if my guess is too low and 3 if I guessed it right")
ng = 0

def guess(l, h):
    g = int((l+h)/2)
    print("My guess:", g)
    print("Thoughts?")
    global ng
    ng += 1
    t = int(input())
    if t == 1:
        guess(l, g)
    elif t == 2:
        guess(g, h)
    else:
        print("Yay! I got it right in", ng, "guesses")

guess(0, 10 ** n)