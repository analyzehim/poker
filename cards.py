import random
combinations=['Royal_Flush',    #0
              'Straight_Flush', #1
              'Four',           #2
              'Full_House',     #3
              'Flush',          #4
              'Straight',       #5
              'Three',          #6
              'Two_Pair',       #7
              'Pair',           #8
              'High_card',      #9
              ]
good_comb =  ['Royal_Flush',    #0
              'Straight_Flush', #1
              'Four',           #2
              'Full_House',     #3
              'Flush',          #4
              'Straight',       #5
              'Three',          #6
              'Two_Pair',       #7
              ]
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



def check_comb(card_list):
    if len(card_list) < 5:
        return -1
    value_list=[]
    suit_list=[]
    for card in card_list:
        value_list.append(card_values.index(card.value))
        suit_list.append(card_suits.index(card.suit))
    flag_straight = False
    flag_flush = False    
    value_list_sorted = sorted(value_list)


    for suit in range(len(card_suits)):
        if suit_list.count(suit)>=5:
            flush_suit = suit
            flag_flush = True
    '''
    
    ///////////////////////////////////
    Royal Flush
    '''    
    if flag_flush:

        if ((Card(12,flush_suit) in card_list) and
            (Card(11,flush_suit) in card_list) and
            (Card(10,flush_suit) in card_list) and
            (Card(9,flush_suit) in card_list) and
            (Card(8,flush_suit) in card_list)):
            return combinations[0]
    '''

    ///////////////////////////////////
    Straight Flush
    '''
    
    if flag_flush:

        flag = 0

        if ((Card(0,flush_suit) in card_list) and
            (Card(1,flush_suit) in card_list) and
            (Card(2,flush_suit) in card_list) and
            (Card(3,flush_suit) in card_list) and
            (Card(12,flush_suit) in card_list)):
            return combinations[1]
        for i in range(len(value_list)-1):
            if ((value_list_sorted[i+1] - value_list_sorted[i] == 1) and
                (Card(value_list_sorted[i],flush_suit) in card_list) and
                (Card(value_list_sorted[i+1],flush_suit) in card_list)):
                    
                    flag +=1
            else:
                flag =0

            if flag == 4:
                return combinations[1]

    '''

    ///////////////////////////////////
    Four
    '''
    for value in value_list:
        if value_list.count(value) == 4:
            return combinations[2]
    '''

    ///////////////////////////////////
    Full House
    '''
    flag = 0
    flag1 = 0
    for value in value_list:
        if value_list.count(value) == 2:
            flag += 1
        if value_list.count(value) == 3:
            flag1 += 1
    if (flag == 2) and (flag1 == 3):
        return combinations[3]
    '''

    ///////////////////////////////////
    Flush
    '''
    if flag_flush:
        return combinations[4]       
    '''

    ///////////////////////////////////
    Straight
    '''
    flag = 0

    if (0 in value_list_sorted and
        1 in value_list_sorted and
        2 in value_list_sorted and
        3 in value_list_sorted and
        12 in value_list_sorted):
        return combinations[5]
    for i in range(len(value_list)-1):
        if value_list_sorted[i+1] - value_list_sorted[i] == 1:
            flag +=1
        elif (value_list_sorted[i+1] == value_list_sorted[i]):
            pass
        else:
            flag =0
        if flag == 4:
            return combinations[5]

    '''

    ///////////////////////////////////
    Three
    '''
    for value in value_list:
        if value_list.count(value) == 3:
            return combinations[6]
    '''

    ///////////////////////////////////
    Two Pair
    '''
    flag = 0
    for value in value_list:
        if value_list.count(value) == 2:
            flag+=1
    if flag > 2:
        return combinations[7]
    '''

    Pair
    ///////////////////////////////////
    '''

    if flag == 2:
        return combinations[8]
    '''

    High Card
    ///////////////////////////////////
    '''
    return combinations[9]

def testing_comb():
    f = open("test.txt","r")
    for test_case in f:
        card_list = test_case.split(' ')
        real_comb =  combinations[int(card_list.pop(0))]
        hand = []
        for card_param in card_list:
            hand.append(Card(card_param.split(':')[0],card_param.split(':')[1]))
        if real_comb != check_comb(hand):
            print_cards(hand)
            print real_comb,'!=', check_comb(hand)
            print("Error")
            #print('\n')
            #print('\n')
            pass
    print ("Test OK!")
    f.close()
        

testing_comb()    








