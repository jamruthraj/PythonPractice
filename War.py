import random

#
values = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
          "jack": 11, "queen": 12, "king": 13, "ace": 14}
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


#
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

#
class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove(self):
        return self.all_cards.pop(0)

    def add(self, cards):
        if type(cards) == list:
            self.all_cards.extend(cards)
        else:
            self.all_cards.append(cards)

    def __str__(self):
        return self.name + " has " + str(len(self.all_cards)) + " cards"

#
deck = Deck()
deck.shuffle()
print("Enter name of player 1")
n1 = input()
p1 = Player(n1)
print("Enter name of player 2")
n2 = input()
p2 = Player(n2)
for x in range(52):
    if x % 2 == 0:
        p1.add(deck.all_cards[x])
    else:
        p2.add(deck.all_cards[x])
r = 0
game = True
while game:
    r += 1
    print("Round =", r)
    if len(p1.all_cards) == 0:
        print(n1, "is out of cards,", n2, "is the winner")
        break
    elif len(p2.all_cards) == 0:
        print(n2, "is out of cards,", n1, "is the winner")
        break
    p1cards = []
    p2cards = []
    p1cards.append(p1.remove())
    p2cards.append(p2.remove())
    while True:

        if p1cards[-1].value > p2cards[-1].value:
            print(n1, "won round", r)
            p1.add(p1cards)
            p1.add(p2cards)
            break
        elif p1cards[-1].value < p2cards[-1].value:
            print(n2, "won round", r)
            p2.add(p2cards)
            p2.add(p1cards)
            break
        else:
            print("War!")
            if len(p1.all_cards) < 3:
                print(n1, "is unable ti declare war,", n2, "wins")
                game = False
                break
            elif len(p2.all_cards) < 3:
                print(n2, "is unable to declare war", n1, "wins")
                game = False
                break
            else:
                for x in range(3):
                    p1cards.append(p1.remove())
                    p2cards.append(p2.remove())

