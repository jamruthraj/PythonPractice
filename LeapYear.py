y = int(input())
if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")
