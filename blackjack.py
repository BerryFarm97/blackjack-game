import random

def calculate_score(hand: list[str]) -> int:
    score = 0
    aces = 0

    for card in hand:
        rank = card.split()[0]
        if rank in ['Jack', 'Queen', 'King']:
            score += 10
        elif rank == 'Ace':
            score += 11
            aces += 1
        else:
            score += int(rank)
    
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1

    return score

def player_action(deck, player_hand):                   #Added player input to allow Hit or Stand function. Also use .lower() so it doesnt matter how player inputs it.
    score = calculate_score(player_hand)
    
    while True:

        choice = input("Would you like to Hit or Stand: ").lower()

        if choice == 'hit':
            player_hand.append(deck.pop())
            score = calculate_score(player_hand)
            print("Your hand:", player_hand)
            print("Total:", score)
            if score > 21:
                print("You busted with:", score)
                return score
        elif choice == 'stand':
            return score
        
        else:
            print("Invalid options. Please choose Hit or Stand.\n")
            


def main():

    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    #Build and shuffle deck
    deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
    random.shuffle(deck)

    player_hand = []
    dealer_hand = []
        #Deal initial hand
    for _ in range(2):
    
        player_hand.append(deck.pop())

        dealer_hand.append(deck.pop())

    print("\nYour hand:", player_hand)
    print("Dealer shows:", dealer_hand[0], "and [hidden]")

        #Call player turn
    player_score = player_action(deck, player_hand)
    
    print(f"\nYou ended with: {player_score}\n")

# TODO: Add dealer turn and winner comparison


if __name__ == "__main__":
    main()
