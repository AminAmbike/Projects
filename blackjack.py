import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

playing = True


class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        self.deck = []
        for i in suits:
            for j in ranks:
                self.deck.append(Card(i,j))


    def __str__(self):
        deck_comp = ''
        for i in self.deck:
            deck_comp += '\n ' +card._str_()
        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        lone_card = self.deck.pop()
        return lone_card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces= 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            

class Chips:

    def __init__(self):
        self.total = 100
        self.bet=0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def place_bet(chips):

    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet?"))
        except ValueError:
            print ("sorry, a bet must be an integer!")
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed", chips.total)
            else:
                break


def hit(deck,hand):

    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck,hand):
    global playing

    while True:
        x = input("Would you like to hit or stand? Enter 'h' or 's' ")

        if x[0].lower() == 'h':
            hit(deck,hand)

        elif x[0].lower() == 's':
            print("You've chosen to stand, Dealer's turn.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden> ")
    print(' ', dealer.cards[1])
    print("\nYour Hand: ", *player.cards, sep='\n ')


def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nYour Hand:", *player.cards, sep='\n ')
    print("Your Hand =",player.value)


def player_busts(player,dealer,chips):
    print("\nYou've BUSTED!!!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("\nYou WIN!!!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("\nDealer WINS!!!")
    chips.lose_bet()

def push(player,dealer):
    print("\nYou and the dealer have tied! It's a push!")


while True:

    print("\nWelcome to BlackJack by Amin Ambike!. The object of the game is to get as close to 21 as you can without going over.")
    print("\nThe Dealer hits until they reaches 17. Aces count as 1 or 11. Enjoy :) ")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    place_bet(player_chips)

    show_some(player_hand,dealer_hand)

    while playing:

        hit_or_stand(deck,player_hand)

        show_some(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

        show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif deler_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)

    print("\nYour winnings are: ", player_chips.total)

    new_game = input("would you like top play another hand? Enter 'y' or 'n': ")

    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("I hope you've had fun. Goodbye :)")
        break
    

    





    
    


    
















        
