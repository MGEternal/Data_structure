import random

# Define constants for the game
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13,
          'Ace': 14}

# Define a Card class
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Define a Deck class
class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in RANKS for suit in SUITS]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

# Define a Hand class to store player's cards
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

class Card_table:
    def __init__(self):
        self.cards = []
    def add_card(self, card):
        self.cards.append(card)
# Function to compare hands and determine the winner

def compare_hands(hand1, hand2):
    hand1_values = [VALUES[card.rank] for card in hand1.cards]
    hand2_values = [VALUES[card.rank] for card in hand2.cards]
    return sum(hand1_values) - sum(hand2_values)




# Main game function
def play_poker():
    deck = Deck()
    dict_players = dict
    num_players = int(input("Number of players : "))
    table = Card_table()
    def add_card_to_hand(hand):
        for _ in range(2):
            hand.add_card(deck.deal_card())
        return hand
    
    for i in range(num_players):
        name = f'player{i}'
        dict_players.append()
    
    for _ in range(3):
        table.add_card(deck.deal_card())
    
    # Deal two cards to each player
    



    # Compare hands to determine the winner
    for i in table.cards:
        print(i)

   

# Start the game
if __name__ == "__main__":
    play_poker()
