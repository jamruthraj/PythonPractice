import random

values = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
          "jack": 10, "queen": 10, "king": 10, "ace": 11}
suits = ("Diamonds", "Spades", "Hearts", "Clubs")
ranks = ("two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace")


#
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal(self):
        return self.all_cards.pop()


class Bank:

    def __init__(self, name, bal):
        self.name = name
        self.bal = bal

    def add(self, amt):
        self.bal += amt

    def rem(self, amt):
        while self.bal < amt:
            print("Amount not sufficient, enter amt less than", self.bal)
            amt = int(input())
        self.bal -= amt

    def checkbal(self):
        return self.bal


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "ace":
            self.aces += 1

    def acehandle(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


def hit(hand):
    single = deck.deal()
    hand.add(single)
    hand.acehandle()


def hit_stand():
    global game
    while True:
        x = input("Enter H to hit and S to stand: ")
        if x[0].lower() == 'h':
            hit(ph)
            print(n, "you got", ph.cards[-1])
        elif x[0].lower() == 's':
            print("Dealer's Turn")
            hit(dh)
            break


def player_bust():
    print("It is a Bust", n)


def player_win(amt):
    print(n, "You Win")
    pb.add(amt=2 * amt)


def dealer_bust(amt):
    print(n, "you win, dealer bust")
    pb.add(amt=2 * amt)


def dealer_win():
    print("Dealer wins")


deck = Deck()
deck.shuffle()
print("Enter your name")
n = input()
print("Enter your initial balance")
b = int(input())
pb = Bank(n, b)
game = True
while game:
    if pb.checkbal() == 0:
        print("Money Over")
        break
    print("Enter amount to place a bet")
    bet = int(input())
    print("\n" * 3)
    ph = Hand()
    pb.rem(bet)
    ph.add(deck.deal())
    ph.add(deck.deal())
    dh = Hand()
    dh.add(deck.deal())
    dh.add(deck.deal())
    print(n, "you have", ph.cards[0], "and", ph.cards[1], "that totals to", ph.value)
    print("Computer deals has", dh.cards[0], "and another card")
    while game:
        hit_stand()
        if ph.value > 21:
            player_bust()
        break
    if ph.value <= 21:
        while dh.value <= 17:
            hit(dh)
        print("\n" * 3)
        print("YourCards")
        for o in range(len(ph.cards)):
            print(ph.cards[o])
        print("")
        print("Dealer's Cards")
        for m in range(len(dh.cards)):
            print(dh.cards[m])
        print("")
        if dh.value > 21:
            dealer_bust(bet)
        elif dh.value > ph.value:
            dealer_win()
        elif ph.value > dh.value:
            player_win(bet)

    print("")
    print("You have", pb.checkbal())
    print("Do you wish to continue? Y or N")
    aaa = input()
    print("\n" * 2)
    if aaa[0].lower() == 'y':
        continue
    else:
        break

print("Have a nice day")
