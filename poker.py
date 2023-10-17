import random
import copy

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
        self.betting = 0
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
    def __str__(self):
        if not self.cards:
            return "No cards on the table"
        else:
            return ", ".join(map(str, self.cards))
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
        self.tail = None
    def Append(self, data, chips):
        new_node = Node(data, chips)
        new_node.hand = Hand()  # Create a Hand object for the player
        if self.head is None:
            self.head = new_node
            self.tail = new_node  # Update the tail to the first node in a single-node list
            new_node.next = self.head
        else:
            self.tail.next = new_node  # Update the next of the current tail node
            new_node.next = self.head  # Update the next of the new node
            self.tail = new_node  # Update the tail to the new node

        new_node.hand.chips = chips
    
    def check_node(self):
        current = self.head
        while current:
            if current.flag == "folds":
                self.delete_node(current)
            elif current.next == self.head:
                break
            current = current.next
            
    
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
                current_player.hand.status = "big blind"
            else:
                # Handle the case where the player doesn't have enough chips to post the big blind
                print(f"{current_player.data} doesn't have enough chips to post the big blind.")
                
                current_player.flag = "folds"
                print(f"{current_player.data} folds.")
        elif current_player.hand.status == "Small Blind":
            small_blind = 5  # Small blind amount
            if current_player.chips >= small_blind:
                current_player.chips -= small_blind
                table.pots += small_blind
                print(f"{current_player.data} posts the small blind.")
                current_player.hand.status = "small blind"
            else:
                # Handle the case where the player doesn't have enough chips to post the small blind
                print(f"{current_player.data} doesn't have enough chips to post the small blind.")
                
                current_player.flag = "folds"
                print(f"{current_player.data} folds.")

        

        # Implement your betting logic here
        if current_player.chips > 0:
            while True:
                try:
                    print(f'Pots : {table.pots}')
                    print(f'Current Bet : {current_bet}')
                    print(f"{current_player.data}'s Chips: {current_player.chips}")
                    print(f"{current_player.hand.status}")
                    print_player_hands(current_cll)
                    print(f'Enter 1 for folds. ')
                    print(f'Enter 2 for call. ')
                    print(f'Enter 3 for bet. ')
                    chk = int(input(f"{current_player.data}, enter your choice : "))
                    while chk != 1 and chk != 2 and chk != 3 :
                        chk = int(input(f"{current_player.data}, enter your choice : "))
                        
                    if chk == 1:
                        current_player.hand.flag = "folds"
                        print(f'player {current_player.data} is already folds')
                    elif chk == 2:
                        if current_bet > current_player.chips :
                            print(f'chips not enough')
                            current_player.hand.flag = "folds"
                            print(f'player {current_player.data} is already folds')
                        else:
                            print(f'player {current_player.data} is already call')
                            
                            if current_player.hand.status == "big blind" :
                                current_player.chips -= 0
                                current_player.hand.flag = "call"
                                current_player.hand.betting = current_bet
                            elif current_player.hand.status == "small blind" :
                                current_player.chips -= 5
                                table.pots += 5
                                current_player.hand.flag = "call"
                                current_player.hand.betting = current_bet
                            else :
                                current_player.chips -= current_bet
                                table.pots += current_bet
                                current_player.hand.flag = "call"
                                current_player.hand.betting = current_bet
                            
                    elif chk == 3 :
                        bet = int(input("Enter your bet : "))
                        if bet > current_player.chips :
                            while True :
                                print(f"your bet it's most then your pots size")
                                bet = int(input("Enter your bet : "))
                                if bet < current_player.chips or bet == 0:
                                    break
                        
                        current_player.hand.flag = "bet"
                        current_player.hand.betting = bet
                        current_player.chips -= bet
                        if current_player.hand.status == "big blind":
                            current_player.chips += 10
                        elif    current_player.hand.status == "small blind":
                            current_player.chips += 5
                        table.pots += bet
                        current_cll.head = current_player.next
                        current_cll.tail = current_player
                        game_betting_for_pf(current_cll,bet,table)
                        
                    print("###################################################################")    
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            # Deduct the bet amount from the player's chips

                
                
        # Move to the next player
        bet = 0
        if current_player.hand.status == "Dealer":
            break
        current_player = current_player.next
        # Check if all players have placed their bets




################################################################
def game_betting_for_pf(current_cll, last_bet, table):
    
    current_player = current_cll.head
    
    # Initialize the current_bet to 10
    current_bet = last_bet  # Initial bet set to 10

    while True:
        # Deal the player's cards
        if current_cll.tail == current_player:
            break
        if current_player.hand.flag == "folds":
            current_player = current_player.next
            continue
        
        if current_player.hand.status == "Big Blind":
            big_blind = 10  # Big blind amount
            if current_player.chips >= big_blind:
                current_player.chips -= big_blind
                table.pots += big_blind
                print(f"{current_player.data} posts the big blind.")
                current_player.hand.status = "big blind"
            else:
                # Handle the case where the player doesn't have enough chips to post the big blind
                print(f"{current_player.data} doesn't have enough chips to post the big blind.")
                
                current_player.flag = "folds"
                print(f"{current_player.data} folds.")
        elif current_player.hand.status == "Small Blind":
            small_blind = 5  # Small blind amount
            if current_player.chips >= small_blind:
                current_player.chips -= small_blind
                table.pots += small_blind
                print(f"{current_player.data} posts the small blind.")
                current_player.hand.status = "small blind"
            else:
                # Handle the case where the player doesn't have enough chips to post the small blind
                print(f"{current_player.data} doesn't have enough chips to post the small blind.")
                
                current_player.flag = "folds"
                print(f"{current_player.data} folds.")
        else:
        # Implement your betting logic here
            if current_player.chips > 0:
                while True:
                    try:
                        print_player_hands(current_cll)
                        print(f'Pots : {table.pots}')
                        print(f'Current Bet : {current_bet}')
                        print(f"{current_player.data}'s Chips: {current_player.chips}")
                        print(f"{current_player.data}'s Hand: {current_player.hand}")
                        print(f'Enter 1 for folds. ')
                        print(f'Enter 2 for call. ')
                        print(f'Enter 3 for bet. ')
                        chk = int(input(f"{current_player.data}, enter your choice : "))
                        while chk != 1 and chk != 2 and chk != 3 :
                            chk = int(input(f"{current_player.data}, enter your choice : "))
                            
                        if chk == 1:
                            current_player.hand.flag = "folds"
                            print(f'player {current_player.data} is already folds')
                        elif chk == 2:
                            if current_bet > current_player.chips :
                                print(f'chips not enough')
                                current_player.hand.flag = "folds"
                                print(f'player {current_player.data} is already folds')
                            else:
                                print(f'player {current_player.data} is already call')
                                current_player.chips -= (current_bet-current_player.hand.betting)
                                table.pots += (current_bet-current_player.hand.betting)
                                current_player.hand.flag = "call"
                                current_player.hand.betting += (current_bet-current_player.hand.betting)
                                
                        elif chk == 3 :
                            bet = int(input("Enter your bet : "))
                            if bet > current_player.chips :
                                while True :
                                    print(f"your bet it's most then your pots size")
                                    bet = int(input("Enter your bet : "))
                                    if bet < current_player.chips or bet == 0:
                                        break
                            current_player.hand.flag = "bet"
                            current_player.hand.betting = bet
                            current_player.chips -= (bet-current_player.hand.betting)
                            table.pots += (bet-current_player.hand.betting)
                            current_cll.head = current_player.next
                            current_cll.tail = current_player
                            game_betting_for_pf(current_cll,bet,table)
                            
                        print("###################################################################")    
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

                # Deduct the bet amount from the player's chips
                
            # Move to the next player
            
            
            current_player = current_player.next
        

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
print_player_hands(sorted_cll)
pre_flop(sorted_cll,deck,table)
print(table.pots)
table.add_card(deck.deal_card())
table.add_card(deck.deal_card())
table.add_card(deck.deal_card())
print(table)

## need next turn


