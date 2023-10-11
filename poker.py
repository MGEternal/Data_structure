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
        self.status = None
        self.flag = None
        self.chips = ''
    def add_card(self, card):
        self.cards.append(card)
    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

class Table:
    def __init__(self):
        self.cards = []
        self.pots = 0
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
    
    def check_flags(self):
        if self.head is None:
            return False

        current = self.head
        first_bet_flag = None  # To track the first node with a "bet" flag
        all_call_flags = True  # To track if all nodes have "call" flags

        while True:
            if current.flag == "bet":
                if first_bet_flag is None:
                    first_bet_flag = current
                else:
                    return False  # More than one node has a "bet" flag

            if current.flag != "call":
                all_call_flags = False

            current = current.next
            if current == self.head:
                break

        if first_bet_flag is not None:
            return all_call_flags
        else:
            return True 
    
    def add_status(self, player_data, status):
        current = self.head
        while True:
            if current.data == player_data:
                current.hand.status = status
                break
            current = current.next
            if current == self.head:
                break
    
    def delete_node(self, player_data):
        if self.head is None:
            return

        # Case 1: If the head node needs to be deleted
        if self.head.data == player_data:
            current = self.head
            while current.next != self.head:
                current = current.next
            if self.head == self.head.next:  # Only one node in the list
                self.head = None
            else:
                current.next = self.head.next
                self.head = self.head.next
        else:
            current = self.head
            prev = None
            while True:
                if current.data == player_data:
                    prev.next = current.next
                    if current == self.head:
                        self.head = current.next
                    break
                prev = current
                current = current.next
                if current == self.head:
                    break
           
    def __str__(self):
        if self.head is None:
            return "Empty Circular Linked List"
        else:
            values = []
            current = self.head
            while True:
                player_info = f"{current.data} ({current.chips} chips)"
                if current.hand.status:
                    player_info += f" - Status: {current.hand.status}"
                else:
                    player_info += " - Status: None"
                values.append(player_info)
                current = current.next
                if current == self.head:
                    break
        return " -> ".join(values)




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
    values = []
    while True:
        player_info = f"{current_player.data} ({current_player.chips} chips"
        if current_player.hand.status:
            player_info += f" | Status: {current_player.hand.status}"
        player_info += ")"
        values.append(player_info)
        current_player = current_player.next
        if current_player == circular_link_list.head:
            break
    player_info = " -> ".join(values)
    print(player_info)


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

def create_sorted_circular_link_list(players):
    sorted_cll = Circular_link_list()
    num_players = len(players)
    
    for i, (player_data, _) in enumerate(players):
        sorted_cll.Append(player_data, set_buyin)  # Create the sorted list without statuses
    
    # Now, assign statuses to the players
    for i, (_, status) in enumerate(players):
        if i == num_players - 1:
            sorted_cll.add_status(players[i][0], "Dealer")
        elif i == num_players - 2:
            sorted_cll.add_status(players[i][0], "Big Blind")
        elif i == num_players - 3:
            sorted_cll.add_status(players[i][0], "Small Blind")
    
    return sorted_cll





def pre_flop(current_cll, deck, table):
    current_player = current_cll.head

    # Initialize the current_bet to 10
    current_bet = 10  # Initial bet set to 10

    while True:
        # Deal the player's cards
        card1 = deck.deal_card()
        card2 = deck.deal_card()
        current_player.hand.add_card(card1)
        current_player.hand.add_card(card2)
        print(f"{current_player.data}'s Hand: {current_player.hand}")

        # Check if the player should contribute as big blind or small blind based on their status
        if current_player.hand.status == "Big Blind":
            big_blind = 10  # Big blind amount
            if current_player.chips >= big_blind:
                current_player.chips -= big_blind
                table.pots += big_blind
                print(f"{current_player.data} posts the big blind.")
            else:
                # Handle the case where the player doesn't have enough chips to post the big blind
                print(f"{current_player.data} doesn't have enough chips to post the big blind.")
                current_cll.delete_node(current_player.data)
                current_player.flag = "folds"
                print(f"{current_player.data} folds.")
        elif current_player.hand.status == "Small Blind":
            small_blind = 5  # Small blind amount
            if current_player.chips >= small_blind:
                current_player.chips -= small_blind
                table.pots += small_blind
                print(f"{current_player.data} posts the small blind.")
            else:
                # Handle the case where the player doesn't have enough chips to post the small blind
                print(f"{current_player.data} doesn't have enough chips to post the small blind.")
                current_cll.delete_node(current_player.data)
                current_player.flag = "folds"
                print(f"{current_player.data} folds.")

        print_player_hands(current_cll)

        # Implement your betting logic here
        if current_player.chips > 0:
            while True:
                try:
                    print(f"{current_player.data}'s Chips: {current_player.chips}")
                    bet = int(input(f"{current_player.data}, enter your bet (0 to check/fold): "))
                    if current_bet == 10:  # Check if the current bet is equal to the initial bet (10)
                        if bet ==  10 or current_player.hand.status == "Small Blind" and bet == 5 or bet == 0 and current_player.hand.status == "Big Blind":
                            current_player.flag = "call"
                            print(f"{current_player.data} check.")
                        elif bet > 0:
                            current_bet = bet
                            current_player.flag = "bet"
                            print(f"{current_player.data} bet.")
                    elif bet == 0:
                        current_cll.delete_node(current_player.data)
                        current_player.flag = "folds"
                        print(f"{current_player.data} folds.")
                    elif bet < current_bet:
                        chk = True
                        while chk:
                            print(f"You have bet less than the current bet ({current_bet}). Please enter a higher bet.")
                            bet = int(input(f"{current_player.data}, enter your bet (0 to check/fold): "))
                            
                            if bet == 0:
                                print(f"{current_player.data} folds.")
                                current_player.flag = "folds"
                                chk = False
                            elif bet == current_bet:
                                current_player.flag = "call"
                                print(f"{current_player.data} call.")
                                chk = False
                            elif bet > current_bet:
                                current_player.flag = "bet"
                                print(f"{current_player.data} bet.")
                                chk = False
                            elif bet < current_bet:
                                chk = True
                    elif bet > current_player.chips:
                        print("Invalid bet. You don't have enough chips.")
                    else:
                        current_bet = bet
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            # Deduct the bet amount from the player's chips
            if bet != 0:
                current_player.chips -= bet
                table.pots += bet
        # Move to the next player
        if current_player.hand.status == "Dealer":
            break
        current_player = current_player.next
        # Check if all players have placed their bets
        

        


set_buyin = "0"
cll = Circular_link_list()
deck = setting_game(cll)
deal_cards(deck, cll)
print("############################################")
# Sort players by hand value
sorted_players = sort_players_by_hand_value(cll)

# Create a new Circular_link_list with sorted players
sorted_cll = create_sorted_circular_link_list(sorted_players)
deck = Deck()
table = Table()

pre_flop(sorted_cll,deck,table)


