import cards

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


def check_comb(card_list):
    if len(card_list) < 5:
        return -1
    value_list=[]
    suit_list=[]
    for card in card_list:
        value_list.append(cards.card_values.index(card.value))
        suit_list.append(cards.card_suits.index(card.suit))
    flag_straight = False
    flag_flush = False    
    value_list_sorted = sorted(value_list)


    for suit in range(len(cards.card_suits)):
        if suit_list.count(suit)>=5:
            flush_suit = suit
            flag_flush = True
    '''
    
    ///////////////////////////////////
    Royal Flush
    '''    
    if flag_flush:

        if ((cards.Card(12,flush_suit) in card_list) and
            (cards.Card(11,flush_suit) in card_list) and
            (cards.Card(10,flush_suit) in card_list) and
            (cards.Card(9,flush_suit) in card_list) and
            (cards.Card(8,flush_suit) in card_list)):
            return combinations[0]
    '''

    ///////////////////////////////////
    Straight Flush
    '''
    
    if flag_flush:

        flag = 0

        if ((cards.Card(0,flush_suit) in card_list) and
            (cards.Card(1,flush_suit) in card_list) and
            (cards.Card(2,flush_suit) in card_list) and
            (cards.Card(3,flush_suit) in card_list) and
            (cards.Card(12,flush_suit) in card_list)):
            return combinations[1]
        for i in range(len(value_list)-1):
            if ((value_list_sorted[i+1] - value_list_sorted[i] == 1) and
                (cards.Card(value_list_sorted[i],flush_suit) in card_list) and
                (cards.Card(value_list_sorted[i+1],flush_suit) in card_list)):
                    
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
            hand.append(cards.Card(card_param.split(':')[0],card_param.split(':')[1]))
        if real_comb != check_comb(hand):
            print_cards(hand)
            print real_comb,'!=', check_comb(hand)
            print("Error")
            #print('\n')
            #print('\n')
            pass
    print ("Test OK!")
    f.close()
        
def check_outs(hand, deck):
    outs_count = 0
    #cards.print_cards(hand)
    #raw_input()
    for card in deck.set:
            hand.append(card)
            if cards.check_comb(hand) in cards.good_comb:
                #print card,  cards.check_comb(hand)      
                outs_count += 1
            hand.pop()
    return outs_count

testing_comb()    
