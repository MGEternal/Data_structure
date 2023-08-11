import random

# Define constants for the game
SUITS = ['Clubs','Hearts','Diamonds','Spades']
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
        self.chips = ''
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





# Pregame function
number_played = int(input("Number of players : "))
player_list = []
for i in range(number_played):
    name = input(f'Name of player {i+1} : ')
    player_dict = {'keys': name, 'values': ""}
    player_list.append(player_dict)

deck = Deck()

for item in player_list:
    pre_game_Hand = Hand()
    pre_game_Hand.add_card(deck.deal_card())
    item['values'] = str(pre_game_Hand)  # Store the string representation of the hand

Set_buy_in = int(input("Set buy in of table : "))
score_dict = {}

for item in player_list:
    hand_str = item['values']
    hand_list = [Card(card_str.split()[0], card_str.split()[-1]) for card_str in hand_str.split(', ')]
    if all(card.rank in VALUES for card in hand_list):  # Check if all card ranks are in VALUES
        hand_suits = set(card.suit for card in hand_list)
        if len(hand_suits) == 1:  # Check if all cards have the same suit
            score_dict[item['keys']] = sum(VALUES[card.rank] for card in hand_list)

# Sort the score_dict based on values
sorted_score_list = sorted(score_dict, key=lambda x: (score_dict[x], x), reverse=True)

print(str(player_list))
print("Sorted score list:", ', '.join(sorted_score_list))

    
    


   

