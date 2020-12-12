mylist = []
m = 0
sm = 0
print("Enter 5 numbers")
for x in range(5):
    z = int(input())
    mylist.append(z)
m = list[0]
for y in range(5):
    if m < list[y]:
        sm = m
        m = list[y]
print("Second Largest num =", sm)
