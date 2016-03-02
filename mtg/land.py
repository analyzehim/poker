import random
card_color={0:'Colorless',
            1:'Black',
            2:'Blue',
            3:'Green',
            4:'Red',
            5:'White',
            6:'Multicolor'}
card_types={0:'Undefined',
            1:'Land',
            2:'Creature',
            3:'Enchantment',
            4:'Instant',
            5:'Artifact',
            6:'Sorcery'}
class card:
    color=card_color[0]
    type=card_types[0]
    mana_cost=0
    def __init__(self, color, type, mana_cost):
             self.color=card_color[color]
             self.type=card_types[type]
             self.mana_cost=mana_cost
    def __str__(self):
        return str(self.color)+" "+str(self.type)+", "+str(self.mana_cost)+" mana"
    
def generate_card():     
    return card(random.randint(0,6),random.randint(2,6),random.randint(0,8))

def generate_land():
    return card(random.randint(1,5),1,0)


             
def generate_deck(number):
    deck=[]
    for i in range(number):
        deck.append(generate_card())
    return deck
def add_land(deck,number):
    for i in range(number):
        deck.append(generate_land())
    return deck

def start_game(deck):
    hand=[]
    for i in range(7):
        hand.append(deck.pop())
    return deck,hand

def turn(deck,hand):
    hand.append(deck.pop())
    return deck,hand
def count_land(list):
    count=0
    for i in list:
        if i.type==card_types[1]:
            count+=1
    return count
def generate_start(number_card, number_land):
    deck=generate_deck(number_card)
    deck=add_land(deck,number_land)
    hand=[]
    random.shuffle(deck)
    (deck,hand) = start_game(deck)
    return deck,hand
max_list=[]
coef_list=[]
def estimate_lands(number_card):
    for iteration in range(3):
        max_coef=0
        optimal_land=0
        count_bad=0
        for number_land in range(0,60):
            good=0
            bad=0
            for k in range(300):
                
                (deck,hand) = generate_start(number_card,number_land)
                count_turn=0
                if count_land(hand)>=4:
                        bad+=2
                        
                if count_land(hand)<2:
                        bad+=2
                if count_land(hand)==2 or count_land(hand)==3:
                        good+=2
                while 1:
                    
                    (deck,hand) = turn(deck,hand)
                    
                    count_turn+=1
                    for i in hand:
                        if i.type==card_types[1]:
                            index_land=i
                    try:
                        hand.remove(index_land)
                    except:
                        if (count_turn>6) or (count_turn<4):
                            bad+=1
                            break
                        else:
                            good+=1
                            break
                #print good,bad
            if max_coef< float(good)/float(bad):
                max_coef=float(good)/float(bad)
                optimal_land=number_land
                #print optimal_land,max_coef
        
        max_list.append(optimal_land)
    sum=0
    for i in max_list:
            sum+=i

    return float(sum)/len(max_list)
            
print estimate_lands(80)

                
    








