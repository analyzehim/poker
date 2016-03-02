import random


card_values=['2', #0
             '3', #1
             '4', #2
             '5', #3
             '6', #4
             '7', #5
             '8', #6
             '9', #7
             '10',#8
             'J', #9
             'Q', #10
             'K', #11
             'A', #12
             ]

card_suits=['Clubs',     #0
            'Diamonds',  #1
            'Hearts',    #2
            'Spades',    #3
            ]


class Card:
    value=card_values[12]
    suit=card_suits[3]
    def __eq__(self, other):
        if ((self.value == other.value) and
            (self.suit == other.suit)):
            return True
        return False
    def __init__(self, value, suit):
            self.suit=card_suits[int(suit)]
            self.value=card_values[int(value)]
    def __str__(self):
        return str(self.value)+" "+str(self.suit)
    
def generate_card():     
    return Card(random.randint(0,12),random.randint(0,3))


class Deck:
    set = []
    size = 0
    def check_card(self, card):
        for cardDeck in self.set:
            if ((cardDeck.value == card.value) and (cardDeck.suit == card.suit)):
                return True
        return False
    def __eq__(self, other):
        if ((self.set == other.set) and
            (self.size == other.size)):
            return True
        return False        
    def __init__(self):
        while True:
            if len(self.set)==52:
                self.size = 52
                break
            card = generate_card()
            if self.check_card(card) == False:
                self.set.append(card)
    def reCreate(self):
        self.set = []
        while True:
            if len(self.set)==52:
                self.size = 52
                break
            card = generate_card()
            if self.check_card(card) == False:
                self.set.append(card)
    def __str__(self):
        ans =''
        for card in self.set:
            ans += str(card) + '\n'
        return ans[:-1]
    def shuffle(self):
        self.set = shuffle(self.set)
    def get_card(self):
        if self.size>1:
            self.size -=1
            return self.set.pop()
        else:
            print "No cards"
            return 0
        
    def remove_card(self, card):
        try:
            self.set.remove(card)
            self.size -=1
            return 1
        except:
            return -1
    def get_two_cards(self):
        mas =[]
        for card1 in self.set:
            for card2 in self.set:
                if (card1 != card2):
                    mas.append([card1 , card2])
        return mas
        
        
def print_cards(card_list):
    ans = ''
    for card in card_list:
        print card.value,card.suit[0:1]









