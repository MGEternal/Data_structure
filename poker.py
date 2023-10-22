import random
import copy

# Define constants for the game
class checkCard (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('S', 'D', 'H', 'C')

  def __init__ (self, rank, suit):
    self.rank = rank
    self.suit = suit

  def __str__ (self):
    if self.rank == 14:
      rank = 'A'
    elif self.rank == 13:
      rank = 'K'
    elif self.rank == 12:
      rank = 'Q'
    elif self.rank == 11:
      rank = 'J'
    else:
      rank = self.rank
    return str(rank) + self.suit

  def __eq__ (self, other):
    return (self.rank == other.rank)

  def __ne__ (self, other):
    return (self.rank != other.rank)

  def __lt__ (self, other):
    return (self.rank < other.rank)

  def __le__ (self, other):
    return (self.rank <= other.rank)

  def __gt__ (self, other):
    return (self.rank > other.rank)

  def __ge__ (self, other):
    return (self.rank >= other.rank)
   

class Deck (object):
  def __init__ (self):
    self.deck = []
    for suit in checkCard.SUITS:
      for rank in checkCard.RANKS:
        card = checkCard (rank, suit)
        self.deck.append(card)

  def shuffle (self):
    random.shuffle (self.deck)

  def __len__ (self):
    return len (self.deck)

  def deal (self):
    if len(self) == 0:
      return None
    else:
      return self.deck.pop(0)

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
    def __iter__(self):
        return iter(self.cards)

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
        card = deck.deal()
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
    for card in hand:
        value += card.rank
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
        return (-hand_value, checkCard.SUITS.index(card_suit))



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
    flag_bet = False
    current_player = current_cll.head
    
    # Initialize the current_bet to 10
    current_bet = 10  # Initial bet set to 10

    while True:
        # Deal the player's cards
        card1 = deck.deal()
        card2 = deck.deal()
        current_player.hand.add_card(card1)
        current_player.hand.add_card(card2)
        print("############################ Pre Flop ###########################")
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
                                if current_player.hand.status == "big blind":
                                    current_player.hand.status = "big"
                                    current_player.chips += 10
                                elif    current_player.hand.status == "small blind":
                                    current_player.hand.status = "small"
                                    current_player.chips += 5
                            
                    elif chk == 3 :
                        bet = int(input("Enter your bet : "))
                        while True :
                                if bet > current_bet:
                                    break
                                print(f"your bet it's most then last bet")
                                bet = int(input("Enter your bet : "))
                        
                        current_player.hand.flag = "bet"
                        current_player.hand.betting = bet
                        current_player.chips -= bet
                        if current_player.hand.status == "big blind":
                            current_player.hand.status = "big"
                            current_player.chips += 10
                        elif    current_player.hand.status == "small blind":
                            current_player.hand.status = "small"
                            current_player.chips += 5
                        table.pots += bet
                        current_cll.head = current_player.next
                        current_cll.tail = current_player
                        game_betting_for_pf(current_cll,bet,table)
                        flag_bet = True
                        break
                    print("###################################################################")    
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            # Deduct the bet amount from the player's chips

                
                
        # Move to the next player
        bet = 0
        if flag_bet :
           break
        if current_player.next == current_cll.head:
            break
        current_player = current_player.next
        # Check if all players have placed their bets




################################################################
def game_betting_for_pf(current_cll, last_bet, table):
    flag_bet = False
    current_player = current_cll.head
    
    # Initialize the current_bet to 10
    current_bet = last_bet  # Initial bet set to 10

    while True:
        # Deal the player's cards
        
        if current_player.hand.flag == "folds":
            current_player = current_player.next
            continue
        print("########################## game_betting_for_pf ###################################")
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
                                if current_player.hand.status == "big blind":
                                    current_player.hand.status = "big"
                                    current_player.chips += 10
                                elif    current_player.hand.status == "small blind":
                                    current_player.hand.status = "small"
                                    current_player.chips += 5
                        elif chk == 3 :
                            bet = int(input("Enter your bet : "))
                            while True :
                                if bet > current_bet:
                                    break
                                print(f"your bet it's most then last bet")
                                bet = int(input("Enter your bet : "))
                            current_player.hand.flag = "bet"
                            current_player.hand.betting = bet
                            current_player.chips -= (bet-current_player.hand.betting)
                            if current_player.hand.status == "big blind":
                                current_player.hand.status = "big"
                                current_player.chips += 10
                            elif    current_player.hand.status == "small blind":
                                current_player.hand.status = "small"
                                current_player.chips += 5
                            table.pots += (bet-current_player.hand.betting)
                            current_cll.head = current_player.next
                            current_cll.tail = current_player
                            game_betting_for_pf(current_cll,bet,table)
                            flag_bet = True
                            break
                            
                        print("###################################################################")    
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

                # Deduct the bet amount from the player's chips
                
            # Move to the next player
            
            if flag_bet :
                break
            if current_player.next == current_cll.tail:
                break
            current_player = current_player.next
        
def betting_round(current_cll, last_bit, table):
    current_player = current_cll.head
    current_bet = last_bit  # Initial bet set to 10
    flag_bet = False 
    while True:
        # Deal the player's cards
        if current_player.hand.flag == "bet":
            break
        if current_player.hand.flag == "folds":
            current_player = current_player.next
            continue
        print("######################################################")
        print(f"Cards on table : {table}")
        print("######################################################")
        print("######################## betting_round ##############################")
        print(f"{current_player.data}'s Hand: {current_player.hand}")

        # Check if the player should contribute as big blind or small blind based on their status
        

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
                            
                            
                            current_player.chips -= current_bet
                            table.pots += current_bet
                            current_player.hand.flag = "call"
                            current_player.hand.betting = current_bet
                            if current_player.hand.status == "big blind":
                                current_player.hand.status = "big"
                                current_player.chips += 10
                            elif    current_player.hand.status == "small blind":
                                current_player.hand.status = "small"
                                current_player.chips += 5
                    elif chk == 3 :
                        bet = int(input("Enter your bet : "))
                        while True :
                                if bet > current_bet:
                                    break
                                print(f"your bet it's most then last bet")
                                bet = int(input("Enter your bet : "))
                        
                        current_player.hand.flag = "bet"
                        current_player.hand.betting = bet
                        current_player.chips -= bet
                        if current_player.hand.status == "big blind":
                            current_player.hand.status = "big"
                            current_player.chips += 10
                        elif    current_player.hand.status == "small blind":
                            current_player.hand.status = "small"
                            current_player.chips += 5
                        table.pots += bet
                        current_cll.head = current_player.next
                        current_cll.tail = current_player
                        betting_game(current_cll,bet,table)
                        flag_bet = True
                        break
                    print("###################################################################")    
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            # Deduct the bet amount from the player's chips

                
                
        # Move to the next player
        bet = 0
        if flag_bet :
            break
        if current_player.next == current_cll.head:
            break
        current_player = current_player.next

def betting_game(current_cll,last_bit,table):
    
    current_player = current_cll.head
    current_bet = last_bit  # Initial bet set to 10
    flag_bet = False
    while True:
        # Deal the player's cards
        if current_player.hand.flag == "bet":
            break
        if current_player.hand.flag == "folds":
            current_player = current_player.next
            continue

        print("######################################################")
        print(f"Cards on table : {table}")
        print("######################################################")
        print("########################## betting_game ###################################")
        print(f"{current_player.hand.flag}")
        print(f"{current_player.hand.status}")
        print(f"{current_player.data}'s Hand: {current_player.hand}")

        # Check if the player should contribute as big blind or small blind based on their status
        

        # Implement your betting logic here
        if current_player.chips > 0:
            while True:
                try:
                    print(f'Pots : {table.pots}')
                    print(f'Current Bet : {current_bet}')
                    print(f"{current_player.data}'s Chips: {current_player.chips}")
                    
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
                            current_player.chips -= current_bet
                            table.pots += current_bet
                            current_player.hand.flag = "call"
                            current_player.hand.betting = current_bet
                            if current_player.hand.status == "big blind":
                                current_player.hand.status = "big"
                                current_player.chips += 10
                            elif    current_player.hand.status == "small blind":
                                current_player.hand.status = "small"
                                current_player.chips += 5
                    elif chk == 3 :
                        bet = int(input("Enter your bet : "))
                        while True :
                                if bet > current_bet:
                                    break
                                print(f"your bet it's most then last bet")
                                bet = int(input("Enter your bet : "))
                        
                        current_player.hand.flag = "bet"
                        current_player.hand.betting = bet
                        current_player.chips -= bet
                        if current_player.hand.status == "big blind":
                            current_player.hand.status = "big"
                            current_player.chips += 10
                        elif    current_player.hand.status == "small blind":
                            current_player.hand.status = "small"
                            current_player.chips += 5
                        table.pots += bet
                        current_cll.head = current_player.next
                        current_cll.tail = current_player
                        flag_bet = True
                        b = betting_game(current_cll,bet,table)
                        flag_bet = True
                        print("bettinggggggggg")
                        break
                    print("###################################################################")    
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            # Deduct the bet amount from the player's chips

                
                
        # Move to the next player
        bet = 0
        if flag_bet :
            break
        if current_player.next == current_cll.tail:
            break
        
        current_player = current_player.next
        

def Point(hand):                         #point()function to calculate partial score
    sortedHand=sorted(hand,reverse=True)
    c_sum=0
    ranklist=[]
    for card in sortedHand:
      ranklist.append(card.rank)
    c_sum=ranklist[0]*13**4+ranklist[1]*13**3+ranklist[2]*13**2+ranklist[3]*13+ranklist[4]
    return c_sum

def isRoyal ( hand):  
    global list_point             #returns the total_point and prints out 'Royal Flush' if true, if false, pass down to isStraightFlush(hand)
    sortedHand=sorted(hand,reverse=True)
    flag=True
    h=10
    Cursuit=sortedHand[0].suit
    Currank=14
    point = Point(sortedHand)
    total_point=h*13**5+point
    for card in sortedHand:
      if card.suit!=Cursuit or card.rank!=Currank:
        flag=False
        break
      else:
        Currank-=1
    if flag:
        #print('Royal Flush')
        list_point.append(total_point)    
    else:
      isStraightFlush(sortedHand)
    

def isStraightFlush ( hand): 
    global list_point      #returns the total_point and prints out 'Straight Flush' if true, if false, pass down to isFour(hand)
    sortedHand=sorted(hand,reverse=True)
    flag=True
    h=9
    Cursuit=sortedHand[0].suit
    Currank=sortedHand[0].rank
    point = Point(sortedHand)
    total_point=h*13**5+point
    for card in sortedHand:
      if card.suit!=Cursuit or card.rank!=Currank:
        flag=False
        break
      else:
        Currank-=1
    if flag:
      #print ('Straight Flush')
      list_point.append(total_point)
    else:
      isFour(sortedHand)

def isFour ( hand):   
    global list_point               #returns the total_point and prints out 'Four of a Kind' if true, if false, pass down to isFull()
    sortedHand=sorted(hand,reverse=True)
    flag=True
    h=8
    Currank=sortedHand[1].rank               #since it has 4 identical ranks,the 2nd one in the sorted listmust be the identical rank
    point = Point(sortedHand)
    total_point=h*13**5+point
    for card in sortedHand:
      if card.rank==Currank:
        count+=1
    if not count<4:
      flag=True
      #print('Four of a Kind')
      list_point.append(total_point)

    else:
      isFull(sortedHand)
    
def isFull ( hand):  
    global list_point                   #returns the total_point and prints out 'Full House' if true, if false, pass down to isFlush()
    sortedHand=sorted(hand,reverse=True)
    flag=True
    h=7
    point = Point(sortedHand)
    total_point=h*13**5+point
    mylist=[]                                 #create a list to store ranks
    for card in sortedHand:
      mylist.append(card.rank)
    rank1=sortedHand[0].rank                  #The 1st rank and the last rank should be different in a sorted list
    rank2=sortedHand[-1].rank
    num_rank1=mylist.count(rank1)
    num_rank2=mylist.count(rank2)
    if (num_rank1==2 and num_rank2==3)or (num_rank1==3 and num_rank2==2):
      flag=True
      #print ('Full House')
      list_point.append(total_point)
      
    else:
      flag=False
      isFlush(sortedHand)

def isFlush ( hand):      
    global list_point                   #returns the total_point and prints out 'Flush' if true, if false, pass down to isStraight()
    sortedHand=sorted(hand,reverse=True)
    flag=True
    h=6
    point = Point(sortedHand)
    total_point=h*13**5+point
    Cursuit=sortedHand[0].suit
    for card in sortedHand:
      if not(card.suit==Cursuit):
        flag=False
        break
    if flag:
      #print ('Flush')
      list_point.append(total_point)
      
    else:
      isStraight(sortedHand)

def isStraight ( hand):
    global list_point
    sortedHand=sorted(hand,reverse=True)
    flag=True
    h=5
    point = Point(sortedHand)
    total_point=h*13**5+point
    Currank=sortedHand[0].rank                        #this should be the highest rank
    for card in sortedHand:
      if card.rank!=Currank:
        flag=False
        break
      else:
        Currank-=1
    if flag:
      #print('Straight')
      list_point.append(total_point)
      
    else:
      isThree(sortedHand)
        
def isThree ( hand):
    global list_point
    sortedHand=sorted(hand,reverse=True)
    flag=True
    h=4
    point = Point(sortedHand)
    total_point=h*13**5+point
    Currank=sortedHand[2].rank                    #In a sorted rank, the middle one should have 3 counts if flag=True
    mylist=[]
    for card in sortedHand:
      mylist.append(card.rank)
    if mylist.count(Currank)==3:
      flag=True
      #print ("Three of a Kind")
      list_point.append(total_point)
      
    else:
      flag=False
      isTwo(sortedHand)
        
def isTwo ( hand): 
    global list_point                          #returns the total_point and prints out 'Two Pair' if true, if false, pass down to isOne()
    sortedHand=sorted(hand,reverse=True)
    flag=True
    h=3
    point = Point(sortedHand)
    total_point=h*13**5+point
    rank1=sortedHand[1].rank                        #in a five cards sorted group, if isTwo(), the 2nd and 4th card should have another identical rank
    rank2=sortedHand[3].rank
    mylist=[]
    for card in sortedHand:
      mylist.append(card.rank)
    if mylist.count(rank1)==2 and mylist.count(rank2)==2:
      flag=True
      #print ("Two Pair")
      list_point.append(total_point)
      
    else:
      flag=False
      isOne(sortedHand)
  
def isOne ( hand):  
    global list_point                            #returns the total_point and prints out 'One Pair' if true, if false, pass down to isHigh()
    sortedHand=sorted(hand,reverse=True)
    flag=True
    h=2
    point = Point(sortedHand)
    total_point=h*13**5+point
    mylist=[]                                       #create an empty list to store ranks
    mycount=[]                                      #create an empty list to store number of count of each rank
    for card in sortedHand:
      mylist.append(card.rank)
    for each in mylist:
      count=mylist.count(each)
      mycount.append(count)
    if mycount.count(2)==2 and mycount.count(1)==3:  #There should be only 2 identical numbers and the rest are all different
      flag=True
      #print ("One Pair")
      list_point.append(total_point)
      
    else:
      flag=False
      isHigh(sortedHand)

def isHigh ( hand):      
    global list_point                    #returns the total_point and prints out 'High Card' 
    sortedHand=sorted(hand,reverse=True)
    flag=True
    h=1
    point = Point(sortedHand)
    total_point=h*13**5+point
    mylist=[]                                       #create a list to store ranks
    for card in sortedHand:
      mylist.append(card.rank)
    #print ("High Card")
    list_point.append(total_point)


list_point = []
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
deck.shuffle()
table = Table()
print_player_hands(sorted_cll)
pre_flop(sorted_cll,deck,table)
print(table.pots)

table.add_card(deck.deal())
table.add_card(deck.deal())
table.add_card(deck.deal())
current_player = sorted_cll.head
while True:
    if current_player.hand.flag == "folds":
        current_player = current_player.next
        continue
    current_player.hand.flag == ""
    current_player = current_player.next
    if current_player==sorted_cll.head:
        break
betting_round(sorted_cll,0,table)
print(table.pots)
table.add_card(deck.deal())
current_player = sorted_cll.head
while True:
    if current_player.hand.flag == "folds":
        current_player = current_player.next
        continue
    current_player.hand.flag == ""
    current_player = current_player.next
    if current_player==sorted_cll.head:
        break
betting_round(sorted_cll,0,table)
table.add_card(deck.deal())
current_player = sorted_cll.head
while True:
    if current_player.hand.flag == "folds":
        current_player = current_player.next
        continue
    current_player.hand.flag == ""
    current_player = current_player.next
    if current_player==sorted_cll.head:
        break
betting_round(sorted_cll,0,table)
print(f"Final Pots : {table.pots}")
current_player = sorted_cll.head
while True:
    current_hand = []
    if current_player.hand.flag != "folds":
        current_hand.append()
        list1 = [current_hand.hand.cards[0],current_hand.hand.cards[1],table.cards[0],table.cards[1],table.cards[2]]
        list2 = [current_hand.hand.cards[1],table.cards[0],table.cards[1],table.cards[2],table.cards[3]]
        list3 = [table.cards[0],table.cards[1],table.cards[2],table.cards[3],table.cards[4]]
        list4 = [current_hand.hand.cards[0],current_hand.hand.cards[1],table.cards[0],table.cards[1],table.cards[3]]
        list5 = [current_hand.hand.cards[1],table.cards[0],table.cards[1],table.cards[2],table.cards[4]]
        list6 = [current_hand.hand.cards[0],table.cards[0],table.cards[1],table.cards[2],table.cards[4]]
        list7 = [current_hand.hand.cards[0],current_hand.hand.cards[4],table.cards[0],table.cards[1],table.cards[3]]
        current_hand.append(list1)
        current_hand.append(list2)
        current_hand.append(list3)
        current_hand.append(list4)
        current_hand.append(list5)
        current_hand.append(list6)
        current_hand.append(list7)
        maxpoint=max(list_point)
        maxindex=list_point.index(maxpoint)
        print ('\nHand %d wins'% (maxindex+1))
        
    if current_player == sorted_cll.head:
       break
    current_player = current_player.next


