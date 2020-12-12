# [1]
st = "Print only the words that start with s in this sentence"
for word in st.split():
    # if word[0] == 's':
    if word.startswith('s'):
        print(word)
print("\n\n")

# [2]
for num in range(0, 10, 2):
    print(num)
print("\n\n")

# [3]
MyList = [x for x in range(1, 50) if (x % 3 == 0)]
print(MyList, "\n\n")

# [4]
sent = "Print every word in this sentence than has even number of letters"
for word in sent.split():
    if len(word) % 2 == 0:
        print(word)
print("\n\n")

# [5]
for y in range(1, 100):
    if y % 3 == 0 and y % 5 != 0:
        print("Fizz")
    elif y % 5 == 0 and y % 3 != 0:
        print("Buzz")
    elif y % 3 == 0 and y % 5 == 0:
        print("FizzBuzz")
    else:
        print(y)
print("\n\n")

# [6]
first = "Create a list of the first letters of every word in this string"
List = [word[0] for word in first.split()]
print(List)
