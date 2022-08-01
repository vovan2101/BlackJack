import random
import time

suits = ("Spades ♠", "Clubs ♣", "Hearts ♥", "Diamonds ♦")
ranks = (
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "J",
    "Q",
    "K",
    "A",
)
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

playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]


def hit(deck, hand):
    hand.add_card(deck.deal())


def hit_or_stop(deck, hand):
    global playing

    while True:
        x = input("\nWould you like to h or s? ").lower()

        if x == "h":
            hit(deck, hand)  # hit() function defined above

        elif x == "s":
            print("Player stops. Dealer is playing.")
            playing = False

        else:
            print("Speak English PLS.Enter h or s.")
            continue
        break


def show_some(player, dealer):
    print("Player's Hand:", *player.cards, sep="\n ")
    print("Player's Hand =", player.value)
    print("\nDealer's Hand:")
    print("","<card hidden>")
    print("",dealer.cards[1])


def show_all(player, dealer):
    print("\nPlayer's Hand:", *player.cards, sep="\n ")
    print("Player's Hand =", player.value)
    print("\nDealer's Hand:", *dealer.cards, sep="\n ")
    print("Dealer's Hand =", dealer.value)


def player_busts(player, dealer):
    print("\n--- Player busts! ---")


def player_wins(player, dealer):
    print("\n--- Player has **BLACKJACK**! You win! ---")


def dealer_busts(player, dealer):
    print("\n--- Dealer busts! You win! ---")


def dealer_wins(player, dealer):
    print("\n--- Dealer wins! ---")


def push(player, dealer):
    print("\nIts a tie!")


# GAMEPLAY!

while True:
    print("\n----------------------------------------------------------------")
    print("                ♠♣♥♦ WELCOME TO BLACKJACK! ♠♣♥♦")
    print("                          Lets Play!")
    print("----------------------------------------------------------------")
    print(
    )

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    show_some(player_hand, dealer_hand)

    while playing:

        hit_or_stop(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        time.sleep(2)
        print("\n----------------------------------------------------------------")
        print("                     ★ Final Results ★")
        print("----------------------------------------------------------------")

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand)

        else:
            push(player_hand, dealer_hand)

    new_game = input("\nPlay another hand? y or n ").lower()
    while new_game not in "y" "n":
        new_game = input("Invalid Input. Please enter y or n ").lower()
    if new_game == "y":
        playing = True
        continue
    else:
        print("\n------------------------Thanks for playing!---------------------\n")
        break