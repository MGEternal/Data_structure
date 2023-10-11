import random
import time

# Define constants for the game
SUITS = ['Clubs', 'Hearts', 'Diamonds', 'Spades']
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

# Define a Hand class to store a player's cards
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

# Define a Card_table class to store community cards
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

    def find_node(self, player_data):
        current = self.head
        while True:
            if current.data == player_data:
                return current
            current = current.next
            if current == self.head:
                break
        return None

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
    
    if current_player is None:
        print("No players in the circular linked list.")
        return

    while True:
        if current_player is not None:
            player_info = f"{current_player.data} ({current_player.chips} chips"
            if current_player.hand.status:
                player_info += f" | Status: {current_player.hand.status}"
            player_info += ")"
            values.append(player_info)
        
        if current_player.next == circular_link_list.head:
            break
        current_player = current_player.next
    
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

    # Filter out players with no cards in their hand
    players = [(player_data, hand) for player_data, hand in players if hand.cards]

    def sort_key(player):
        hand_value = calculate_hand_value(player[1])
        if player[1].cards:  # Check if the player has cards in their hand
            card_suit = player[1].cards[0].suit  # Assuming all cards have the same suit
        else:
            card_suit = None
        return (-hand_value, SUITS.index(card_suit) if card_suit else -1)

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


def game_round_betting(current_cll, deck):
    current_player = current_cll.head

    # Deal two cards to each player's hand
    for _ in range(2):
        while True:
            card = deck.deal_card()
            current_player.hand.add_card(card)
            current_player = current_player.next
            if current_player == current_cll.head:
                break

    # Initialize the current_bet to zero
    current_bet = 0

    while True:
        # Display current player's hand and chips
        print(f"{current_player.data}'s Hand: {current_player.hand}")
        print(f"{current_player.data}'s Chips: {current_player.chips}")

        # Implement your betting logic here
        if current_player.chips > 0:
            while True:
                try:
                    bet = int(input(f"{current_player.data}, enter your bet (0 to check/fold): "))
                    if current_bet == 0:
                        if bet == 0:
                            current_player.flag = "call"
                            print(f"{current_player.data} check.")
                        elif bet > 0:
                            current_bet = bet
                            current_player.flag = "bet"
                            print(f"{current_player.data} bet.")
                        else:
                            print("Invalid bet. Please enter a valid bet.")
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
                            elif bet > current_bet :
                                current_player.flag = "bet"
                                print(f"{current_player.data} bet.")
                                chk = False
                            elif bet < current_bet :
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
        # Move to the next player
        current_player = current_player.next
        # Check if all players have placed their bets
        if current_cll.check_flags:
            break


set_buyin = "0"
cll = Circular_link_list()
deck = setting_game(cll)
print("############################################")
# Sort players by hand value
sorted_players = sort_players_by_hand_value(cll)

# Create a new Circular_link_list with sorted players
sorted_cll = create_sorted_circular_link_list(sorted_players)
deck = Deck()
print_player_hands(sorted_cll)


class PokerGame:
    def __init__(self):
        self.deck = None
        self.community_cards = []
        self.round = 0
        self.pot = 0

    def setup_game(self):
        self.deck = Deck()
        self.community_cards = []
        self.round = 0
        self.pot = 0
        self.collect_blinds()

    def collect_blinds(self):
        small_blind_player = sorted_cll.head
        big_blind_player = small_blind_player.next

        small_blind = set_buyin // 20  # You can adjust the blind amounts
        big_blind = small_blind * 2

        # Deduct blinds from players' chips
        small_blind_player.chips -= small_blind
        big_blind_player.chips -= big_blind
        self.pot += small_blind + big_blind

        print(f"{small_blind_player.data} posts small blind (${small_blind})")
        print(f"{big_blind_player.data} posts big blind (${big_blind})")

    def deal_community_cards(self, num_cards):
        for _ in range(num_cards):
            card = self.deck.deal_card()
            self.community_cards.append(card)

    def print_community_cards(self):
        if self.community_cards:
            print("Community Cards:")
            for card in self.community_cards:
                print(card)
        else:
            print("No community cards yet.")

    def clear_community_cards(self):
        self.community_cards = []

    def determine_winner(self):
        players = sort_players_by_hand_value(sorted_cll)
        winning_hand_value = calculate_hand_value(players[0][1])
        winners = []

        for player_data, hand in players:
            if calculate_hand_value(hand) == winning_hand_value:
                winners.append(player_data)

        return winners

    def play_round(self):
        print("\n############################################")
        print(f"Round {self.round + 1}")
        print(f"Current Pot: ${self.pot}")
        self.deal_community_cards(3 if self.round == 0 else 1)
        self.print_community_cards()
        game_round_betting(sorted_cll, self)

    def play_game(self):
        while True:
            self.setup_game()
            for _ in range(4):  # Adjust the number of rounds as needed
                self.play_round()
                self.clear_community_cards()

            winners = self.determine_winner()
            if len(winners) == 1:
                print(f"{winners[0]} wins the pot of ${self.pot} with {calculate_hand_value(sorted_cll.head.hand)}")
                # Distribute the pot to the winner
                sorted_cll.head.chips += self.pot
            else:
                print("It's a tie!")
                # Split the pot among winners
                share = self.pot // len(winners)
                for winner in winners:
                    player = sorted_cll.find_node(winner)
                    player.chips += share

            play_again = input("Do you want to play another round? (yes/no): ").lower()
            if play_again != "yes":
                break

if __name__ == "__main__":
    cll = Circular_link_list()
    deck = setting_game(cll)
    game = PokerGame()
    game.play_game()
