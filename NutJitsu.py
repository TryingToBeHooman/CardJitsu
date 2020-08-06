import random, os, time

#   Print Player Info  ________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

f = open('C:/Users/warre/Desktop/Python/Card Jitsu/wins.txt','r')
g = open('C:/Users/warre/Desktop/Python/Card Jitsu/belts.txt','r')
e = open('C:/Users/warre/Desktop/Python/Card Jitsu/achievements.txt','r')
cool = f.read()
cool2 = g.read()
cool3 = e.read()
print('You Have', cool, 'Wins')
print('You Have The', cool2)
print('Achievements:', cool3)

#   Cool Win  ______________________________________________________________________________________________________________________________________________________________________________________________________

file_dict = {}
file_dict["wins"] = cool

file_dict["belts"] = ""
file_dict["achieve"] = ""
e.close()
f.close()
g.close()

#   Start Game  ________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

continue_ = input('Press Enter To Start Playing >>>  ')

#   Player Info  ________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

player_cards = []
enemy_cards = []
wins = 0

#   Card Types  ________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

fire = 'Fire'
snow = 'Snow'
water = 'Water'
all_cards = [fire, water, snow]

#____________________________________________________________________________________________________________________________________________________________________________________

flag = True

os.system('clear')

#____________________________________________________________________________________________________________________________________________________________________________________


#   card should be fire, water, or snow
#   0 = weak, 1 = strong, 2 = neither
class Card:
    def __init__(self, type, power):
        self.power = power
        self.type = type
    def compare(self, other):
        if self.type == other.type:
            return 2
        elif self.type == fire:
            if other.type == snow:
                return 1
            return 0
        elif self.type == snow:
            if other.type == water:
                return 1
            return 0
        elif self.type == water:
            if other.type == fire:
                return 1
            return 0
        return 0

power_range = range(1, 16)

def create_cards(cardArray):
    for i in range(25):
        card_type = random.choice(all_cards)
        power = random.choice(power_range)
        card = Card(card_type, power)
        cardArray.append(card)

def display_cards(cardArray):
    for i in range(len(cardArray)):
        power = cardArray[i].power
        type = cardArray[i].type
        print('Card', str(i+1), 'is a', 'Power {}'.format(power), type, 'Card')

create_cards(player_cards)
create_cards(enemy_cards)

while flag:

    os.system('clear')
    display_cards(player_cards)

#   Get Player Input  ____________________________________________________________________________________________________________________________________________________________________________________

    chosen_index = -1
    while chosen_index == -1:
        player_input = input('What Card Do You Choose? >>>  ')
        if player_input.isdigit():
            if int(player_input) <= len(player_cards) and int(player_input) > 0:
                chosen_index = int(player_input) -1
            else:
                print('Invalid input')
        else:
                print('Invalid input')
    
    card = player_cards[chosen_index]
    
#   Player Place Card  ____________________________________________________________________________________________________________________________________________________________________________________

    print()
    print('You Placed A Power', card.power, card.type, 'Card')
    print()

#   Enemy Input  ____________________________________________________________________________________________________________________________________________________________________________________

    enemy_index = random.choice(range(0, len(enemy_cards)-1 ))

    enemy_card = enemy_cards[enemy_index]

#   Enemy Place Card  ____________________________________________________________________________________________________________________________________________________________________________________

    print()
    print('The Enemy Placed A Power', enemy_card.power, enemy_card.type, 'Card')
    print()

#   Player Beat Enemy Thing  ____________________________________________________________________________________________________________________________________________________________________________________    


#   Player Water Beat Fire  ____________________________________________________________________________________________________________________________________________________________________________________

    type = card.compare(enemy_card)

    if type==1:
        print()
        print('You Win!')
        print()
        del enemy_cards[enemy_index]
    elif type==0:
        print()
        print('You Lose!')
        print()
        del player_cards[chosen_index]
    else:
        if card.power == enemy_card.power:
            print()
            print("It's A Tie!")
            print()
        elif card.power > enemy_card.power:
            print()
            print('You Win!')
            print()
            del enemy_cards[enemy_index]
        else:
            print()
            print('You Lose!')
            print()
            del player_cards[chosen_index]

#   Print How Much Cards Player And Enemy Have  ____________________________________________________________________________________________________________________________________________________________________________________

    print('You Have {} Cards'.format(len(player_cards)))
    print('Your Opponent Has {} Cards'.format(len(enemy_cards)))

#   Detect If Player Wins Or Loses The Game  ____________________________________________________________________________________________________________________________________________________________________________________

    if len(player_cards) == 0:
        print('You Lost :(')
        flag = False

    elif len(enemy_cards) == 0:
        print('You Won!!!')
        flag = False

#   Write Wins  ____________________________________________________________________________________________________________________________________________________________________________________

        wins = int(file_dict["wins"])
        wins = wins + 1
        file_dict["wins"] = wins

#_______________________________________________________________________________________________________________________________________________________________________________________________________   

    continue_ = input('Press Enter To Continue >>>  ')
    os.system('clear')

#   Write Wins  _____________________________________________________________________________________________________________________________________________________________________________________

wins = file_dict['wins']
f = open('C:/Users/warre/Desktop/Python/Card Jitsu/wins.txt', 'w')
f.write(str(wins))
f.close()

#   Write Belts  ________________________________________________________________________________________________________________________________________________________________________

belts = file_dict['belts']
f = open('C:/Users/warre/Desktop/Python/Card Jitsu/belts.txt', 'w')
f.write(str(belts))
f.close()

wins = int(file_dict["wins"])
belt = file_dict['belts']

#   Belt Things  ______________________________________________________________________________________________________________________________________________________________________________________

if int(wins) == 5:
    file_dict['belts'] = 'White Belt'
    print('You Have Obtained The White Belt!!!!')

elif int(wins) == 13:
    file_dict['belts'] = 'Yellow Belt'
    print('You Have Obtained The Yellow Belt!!!!')

elif int(wins) == 21:
    file_dict['belts'] = 'Orange Belt'
    print('You Have Obtained The Orange Belt!!!!')

elif int(wins) == 30:
    file_dict['belts'] = 'Green Belt'
    print('You Have Obtained The Green Belt!!!!')

elif int(wins) == 40:
    file_dict['belts'] = 'Blue Belt'
    print('You Have Obtained The Blue Belt!!!!')

elif int(wins) == 52:
    file_dict['belts'] = 'Red Belt'
    print('You Have Obtained The Red Belt!!!!')

elif int(wins) == 64:
    file_dict['belts'] = 'Purple Belt'
    print('You Have Obtained The Purple Belt!!!!')

elif int(wins) == 76:
    file_dict['belts'] = 'Coffee Belt'
    print('You Have Obtained The Coffee Belt!!!!')
    
elif int(wins) == 88:
    file_dict['belts'] = 'Black Belt'
    print('You Have Obtained The Black Belt!!!!')
    print('You Are Now A Card Jitsu Master!!!')