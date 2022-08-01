import random
import time

ranks = ("6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("Diamonds ♦", "Clubs ♣", "Spades ♠", "Hearts ♥")
values = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11,
}

#********************************************************************
class Card:
    def __init__(self, ranks, suits):
        self.ranks = ranks
        self.suits = suits

    def __str__(self):
        return self.ranks + " of " + self.suits

    def value(self):
        if self.ranks in ['J', 'Q', 'K']:
            return 10
        elif self.ranks == 'A':
            return 1, 11
        else:
            return int(self.ranks)

#********************************************************************
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suits, ranks))


    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

#********************************************************************
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(Card)
        self.value += [card.value]

#********************************************************************
def hit(deck, hand):
    hand.add_card(deck.deal())

def stop():
    return False
#********************************************************************

def run_game():
    while True:
        print()
        print("*****************************************")
        print("Welcome to the Vladimir's casino! Today, we are playing BLACK JACK! Would you like to join us? yes OR no?")
        to_do = input("Give me your answer: ").lower()
        while to_do not in {"yes","no"}:
            to_do = input("Speak English please, so I can understand you! yes OR no?")
        if to_do == "no":
            print()
            print("It is easy money, but do what you want!")
            break
        if to_do == "yes":
            print()
            print("That is right choice ;)")
            print()
            print(f"Table number {random.randrange(1, 10)} have a spot for you! ENJOY THE GAME;)")
            time.sleep(3)
            print("Delling...")
            time.sleep(4)
        
        deck = Deck()
        deck.shuffle()   

        print("Here is your cards, good luck!")
        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        hit = input("Would you like to hit or stop?").lower
        while hit not in {"hit", "stop"}:
            hit = input{"That is not valid answer. Would you like to hit or stop?"}
        if hit == "stop":
            stop()
        if hit == "hit":
            hit()

run_game()
