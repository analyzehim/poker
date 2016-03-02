import random
import time
import cards
import poker
from cards import print_cards

deck = cards.Deck()

print deck




'''
try:
    time_stamp = time.time()
    mas = []
    hands_map = deck.get_maps()
    steps =0
    good_count = 0
    for hand in hands_map:
        if (hand[0].suit == 'Clubs' or
        hand[1].suit =='Clubs' or
        hand[0].suit == 'Diamonds' or
        hand[1].suit =='Diamonds'):
            continue
        if hand[0].suit != 'Spades':
            continue
            
        
        steps +=1

        if steps ==4:
            break


        count = 0.0
        comb_count = 0.0
        for i in range(500):
            deck.reCreate()
            deck.remove_card(hand[0])
            deck.remove_card(hand[1])
            river = [deck.get_card() for i in range(5)]
            if cards.check_comb(river + hand) in cards.good_comb:
                comb_count += 1.0
            count += 1.0
        coef = comb_count/count
        
        if coef <= 0.38:
            mas.append([hand, coef])
            good_count+=1
        print steps, coef, good_count
        #print comb_count/count
    print time.time() - time_stamp
    f = open("2.txt", "w")
    mas = sorted(mas, key =  itemgetter(1))
    for i in mas:
        ans = str(i[1]) + ": " 
        ans += i[0][0].value+" " +i[0][0].suit[0:1]+" "
        ans += i[0][1].value+" " +i[0][1].suit[0:1]
        f.write(ans)
        f.write('\n')
        print ans
        #print i[1]
        #cards.print_cards(i[0])
    f.close()

except:
    mas = sorted(mas, key =  itemgetter(1), reverse=True)
    for i in mas:
        print 1
        print i[1]
        cards.print_cards(i[0])
        print '\n'





    


deck = cards.Deck()
rounds = 0
comb_count = 0
mas = []
def average_rounds_of_comb (players, comb, accuracy):
    rounds = 0
    comb_count = 0
    while True:
        
        rounds +=1
        
        deck.reCreate()
        hands = []
        for player in range(players):
            hand = [deck.get_card() for i in range(2)]
            hands.append(hand)

        flop = [deck.get_card() for i in range(5)]
        
        for player in range(players):
            hands[player] = hands[player] + flop
            
        hands_comb =[]
        
        for i in range(players):
            hands_comb.append(cards.combinations.index(cards.check_comb(hands[i])))

        if  comb in hands_comb:

            comb_count += 1

            mas.append(rounds)
            rounds = 0            
        if comb_count == accuracy:
            break

    average = 0
    sum = 0    
    for n in mas:
        sum = sum + n
    average = sum / len(mas)
    return average

comb = 2
iterations = 200
players = 6
average = average_rounds_of_comb(players, comb, iterations)
print (cards.combinations[comb] + ": " + str(players) + " players, " + str(iterations) + " iterations, average: " + str(average))

for i in range(3):
    f = open("average.txt","a")
    comb = 5
    iterations = 1000
    average =  average_rounds_of_comb(comb, iterations)
    f.write(cards.combinations[comb] + ": "+str(iterations) + " iterations, average: " + str(average)+'\n')
    f.close()


for i in range(1000):
    
    deck.reCreate()
    hand = [deck.get_card() for i in range(5)]
    print check_outs(hand, deck)

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








