class Account:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"Owner : {self.name} \nBalance : {self.value}"

    def deposit(self, dep):
        self.value += dep

    def withdraw(self, wit):
        if self.value < wit:
            print("Insufficient Funds")
        else:
            self.value -= wit


acc = Account("Amruth", 500)
acc.deposit(500)
acc.withdraw(200)
print(acc)
