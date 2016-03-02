import random
import time
import cards

time.sleep(1)






def check_outs(hand, deck):
    outs_count = 0
    #cards.print_cards(hand)
    #raw_input()
    for card in deck.set:
            hand.append(card)
            if cards.check_comb(hand) in cards.good_comb:
                #print card,  cards.check_comb(hand)      
                outs_count+=1
            hand.pop()
    return outs_count
    

        
    
mas = [0 for i in range(30)]
deck = cards.Deck()

for i in range(1000):
    
    deck.reCreate()
    hand = [deck.get_card() for i in range(5)]
    print check_outs(hand, deck)
    '''
    try:
        mas[check_outs(hand, deck)] += 1
        print mas
    except:
        print check_outs(hand, deck)
    '''
'''
hand = [cards.Card(12,3),cards.Card(11,3),cards.Card(3,3),cards.Card(9,0),cards.Card(10,1)]
print cards.check_comb(hand)
for card in hand:
    deck.remove_card(card)
'''



'''

    if len(hand) ==5:
        maps = deck.get_two_cards()
        for two_cards in maps:
            hand.append(two_cards[0])
            hand.append(two_cards[1])
            if cards.check_comb(hand) in cards.good_comb:
                print two_cards        
                outs_count+=1
            hand.pop()
            hand.pop()
        return outs_count




list_of_rounds =[0 for i in range(100)]
print list_of_rounds
cards.time_stamp = time.time()
deck = cards.Deck()
rounds = 0
comb_count = 0
mas = []
while True:
    rounds +=1
    deck.reCreate()
    hand = [deck.get_card() for i in range(7)]
    if cards.combinations.index(cards.check_comb(hand)) == 6:
        comb_count += 1
        #print comb_count,":", rounds, time.time()-time_stamp
        mas.append(rounds)
        try:
            list_of_rounds[rounds] += 1
        except:
            pass
        rounds = 0
        
    if comb_count == 300:
        break
print list_of_rounds
average = 0
sum = 0    
for n in mas:
    sum = sum + n
average = sum / len(mas)
print "Average ",average

mas = [0.0 for i in range(len(combinations))]

rounds = 0
for i in range(10000):
    rounds += 1
    deck = Deck()
    deck.reCreate()

    hand = [deck.get_card() for i in range(7)]
    print combinations.index(check_comb(hand))
    mas[ combinations.index(check_comb(hand)) ] += 1.0
    mas = [point / rounds for point in mas]
print mas
print '\n'
'''








