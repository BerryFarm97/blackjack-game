import random as ran


def main():

    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
    ran.shuffle(deck)

    player_hand = []
    dealer_hand = []

    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())

    print("Your hand:", player_hand)
    print("Dealer shows:", dealer_hand[0], "and [hidden]")

if __name__ == "__main__":
    main()
