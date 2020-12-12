name = []
num = []
while True:
    print("Enter 1 to view all contacts")
    print("Enter 2 to add a contact")
    print("Enter 3 to edit an existing contact")
    print("Enter 4 to remove an existing contact")
    print("Enter 5 to exit")
    ch = int(input())
    if ch == 1:
        if len(name) == 0:
            print("No contacts exist")
        else:
            print(name)
            print(num)
    elif ch == 2:
        print("Enter name to add")
        name.append(input())
        print("Enter number")
        num.append(int(input()))
    elif ch == 3:
        print("Press 1 to edit name")
        print("Press 2 to edit number")
        c = int(input())
        if c == 1:
            print("Enter Number to edit name")
            n = int(input())
            n1 = num.index(n)
            print("Enter new name")
            name[n1] = input()
        elif c == 2:
            print("Enter Name to edit number")
            n = input()
            n1 = num.index(n)
            print("Enter new number")
            num[n1] = input()
        else:
            print("invalid choice")
    elif ch == 4:
        print("Enter name of contact you wish to delete")
        n = input()
        n1 = num[name.index(n)]
        name.remove(n)
        num.remove(n1)
    elif ch == 5:
        break
    else:
        print("Enter a number from 1 to 5")

print("Successfully Exited")
