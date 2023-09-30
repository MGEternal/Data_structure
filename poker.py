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

class Node:
    def __init__(self, data, chips, next=None):
        self.data = data
        self.chips = chips
        if next is not None:
            self.next = next
        else:
            self.next = None

class Circular_link_list:
    def __init__(self):
        self.head = None

    def Append(self, data, chips):
        new_node = Node(data, chips)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            new_node.hand = Hand()  # Create a Hand object for the player
        else:
            current = self.head
            while True:
                if current.next == self.head:
                    current.next = new_node
                    new_node.next = self.head
                    new_node.hand = Hand()  # Create a Hand object for the player
                    break
                else:
                    current = current.next
        new_node.hand.chips = chips
        
    def __str__(self):
        if self.head is None:
            return "Empty Circular Linked List"
        else:
            values = []
            current = self.head
            while True:
                values.append(f"{current.data} ({current.chips} chips)")
                current = current.next
                if current == self.head:
                    break
            return " -> ".join(values)

class Node:
    def __init__(self, data, chips, next=None):
        self.data = data
        self.chips = chips
        if next is not None:
            self.next = next
        else:
            self.next = None

def setting_game(circular_link_list):
    global set_buyin 
    set_buyin = int(input("Enter amount of buy-in: "))
    players = int(input("Enter number of players: "))
    for i in range(players):
        i = i + 1
        name = input(f"Enter name of player {i}: ")
        circular_link_list.Append(name, set_buyin)
    return Deck()  # Return a deck after initializing players

def deal_cards(deck, circular_link_list):
    current_player = circular_link_list.head
    while True:
        card = deck.deal_card()
        current_player.hand.add_card(card)
        current_player = current_player.next
        if current_player == circular_link_list.head:
            break

def print_player_hands(circular_link_list):
    current_player = circular_link_list.head
    while True:
        print(f"{current_player.data}'s Hand: {current_player.hand}")
        current_player = current_player.next
        if current_player == circular_link_list.head:
            break

def calculate_hand_value(hand):
    value = 0
    for card in hand.cards:
        value += VALUES[card.rank]
    return value

# Function to sort players based on hand value
def sort_players_by_hand_value(circular_link_list):
    players = []
    current_player = circular_link_list.head
    while True:
        player = (current_player.data, current_player.hand)
        players.append(player)
        current_player = current_player.next
        if current_player == circular_link_list.head:
            break

    def sort_key(player):
        hand_value = calculate_hand_value(player[1])
        card_suit = player[1].cards[0].suit  # Assuming all cards have the same suit
        return (-hand_value, SUITS.index(card_suit))

    players.sort(key=sort_key)
    return players

# Function to create a new Circular_link_list based on sorted players
def create_sorted_circular_link_list(players):
    sorted_cll = Circular_link_list()
    for player_data, _ in players:
        sorted_cll.Append(player_data, set_buyin)  # The second argument (chips) is not relevant here
    return sorted_cll
set_buyin = "0"
cll = Circular_link_list()
deck = setting_game(cll)
deal_cards(deck, cll)
print_player_hands(cll)

# Sort players by hand value
sorted_players = sort_players_by_hand_value(cll)

# Create a new Circular_link_list with sorted players
sorted_cll = create_sorted_circular_link_list(sorted_players)
print("\nSorted Circular Linked List:")
print(sorted_cll)