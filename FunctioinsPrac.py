def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            return b
        return a
    else:
        if a > b:
            return a
        return b


def animal_crackers(n):
    mylist = n.lower().split()
    if mylist[0][0] == mylist[1][0]:
        print("True")
    else:
        print("False")


def makes_twenty(n1, n2):
    if n1 == 20 or n2 == 20:
        return True
    elif n1 + n2 == 20:
        return True
    return False


def old_macdonald(n):
    ns = ""
    for i in range(len(n)):
        if i == 0 or i == 3:
            ns += n[i].upper()
        else:
            ns += n[i].lower()
    print(ns)


def master_yoda(n):
    YList = n.split()
    RevList = YList[::-1]
    print(RevList)


def almost_there(n):
    if n > 89 or n < 111 or n > 189 or n < 211:
        return True
    return False


def has_33(intlist):
    for i in range(0, len(intlist) - 1):
        if intlist[i] == intlist[i + 1] == 3:
            return True
    return False


def paper_doll(n):
    s = ""
    for i in range(0, len(n)):
        for j in range(0, 3):
            s += n[i]
    print(s)


def blackjack(a, b, c):
    if a + b + c < 21:
        return a + b + c
    else:
        if a == 11 or b == 11 or c == 11:
            return a + b + c - 10
        return "Bust"


def summer_69(*args):
    mylist = args
    si = mylist.index(6)
    sn = mylist.index(9)
    mulist = mylist[0:si] + mylist[sn + 1:]
    print(sum(mulist))


def spy_number(intlist):
    for i in range(len(intlist)):
        if intlist[i] == 0:
            for j in range(i, len(intlist)):
                if intlist[j] == 0:
                    for k in range(j, len(intlist)):
                        if intlist[k] == 7:
                            return True
    return False


def count_primes(n):
    count = 0
    for i in range(n + 1):
        faccount = 0
        for j in range(1, i + 1):
            if i % j == 0:
                faccount += 1
        if faccount == 2:
            count += 1
    print("Number of Prime Numbers =", count)


def vos(r):
    return (22 / 7) * (4 / 3) * r ** 3


def check(a, b, c):
    if c > a >= b:
        return True
    return False


def up_low(s):
    up = low = 0
    for l in s:
        if l.isupper():
            up += 1
        elif l.islower():
            low += 1
    print(up, low)


def unique(olist):
    nlist = []
    ch = 84989464848
    for n in olist:
        if ch != n:
            nlist.append(n)
            ch = n
    print(nlist)


def mult(nlist):
    product = 1
    for n in nlist:
        product *= n
    print(product)


def palindrome(s):
    s = s.replace(" ", "")
    n = s[::-1]
    if n.lower() == s.lower():
        print("True")
    else:
        print("False")
