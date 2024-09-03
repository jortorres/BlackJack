import random

# Define the card deck
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# Function to create a deck of cards
def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

# Function to calculate the total value of a hand
def calculate_hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        value += values[card[0]]
        if card[0] == 'Ace':
            aces += 1
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

# Function to display a hand
def display_hand(hand, name):
    print(f"{name}'s hand: {', '.join([f'{rank} of {suit}' for rank, suit in hand])}")

# Function for the player to play their hand
def player_turn(deck, player_hand):
    while True:
        display_hand(player_hand, "Player")
        if calculate_hand_value(player_hand) > 21:
            print("Player busts! You lose.")
            return False
        choice = input("Do you want to hit or stand? (h/s): ").lower()
        if choice == 'h':
            player_hand.append(deck.pop())
        elif choice == 's':
            break
    return True

# Function for the dealer to play their hand
def dealer_turn(deck, dealer_hand):
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    display_hand(dealer_hand, "Dealer")
    if calculate_hand_value(dealer_hand) > 21:
        print("Dealer busts! You win.")
        return False
    return True

# Function to determine the winner
def determine_winner(player_hand, dealer_hand):
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    if player_value > dealer_value:
        print("Player wins!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")

# Main game function
def blackjack_game():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    if not player_turn(deck, player_hand):
        return

    if not dealer_turn(deck, dealer_hand):
        return

    determine_winner(player_hand, dealer_hand)

# Start the game
if __name__ == "__main__":
    while True:
        blackjack_game()
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break
