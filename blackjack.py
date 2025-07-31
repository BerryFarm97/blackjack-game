import random
import time

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
            
def dealer_action(deck, dealer_hand):
    score = calculate_score(dealer_hand)
    print("Dealer has:", score)
    time.sleep(1)
    while score < 17:
        dealer_hand.append(deck.pop())
        score = calculate_score(dealer_hand)
        print("Dealer has:", score)
        time.sleep(1)
    print("Dealer's final hand:", dealer_hand)
    return score

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
    if player_score > 21:
        dealer_score = calculate_score(dealer_hand)
        print("You busted. Dealer wins.")
        return
    else:
        dealer_score = dealer_action(deck, dealer_hand)

        if player_score > dealer_score and player_score <= 21:
            print("You win.")
        elif player_score < dealer_score and dealer_score <= 21:
            print("Dealer won.")
        elif player_score < dealer_score and dealer_score > 21:
            print("Dealer busts! You win.")
        else:
            print("It's a tie! You push.")

if __name__ == "__main__":
    main()
