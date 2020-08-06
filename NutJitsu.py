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

card_info = {}
enemy_card_info = {}
wins = 0

#   Card Types  ________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

fire = 'Fire'
snow = 'Snow'
water = 'Water'
all_cards = [fire, water, snow]

enemy_idx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

#____________________________________________________________________________________________________________________________________________________________________________________

flag = True

os.system('clear')

#____________________________________________________________________________________________________________________________________________________________________________________

def create_player_card():
    for i in range(1, 26):
        entry = []

        player_deck = random.choice(all_cards)

        power_range = range(1, 16)
        power = random.choice(power_range)

        entry.append(player_deck)
        entry.append(power)
        entry.append(i)
        
        key = "card" + str(i) 
        card_info[key] = entry

#________________________________________________________________________________________________________________________

def create_enemy_card():
    for k in range(1, 26):
        enemy_entry = []

        enemy_deck = random.choice(all_cards)

        power_range = range(1, 16)
        power = random.choice(power_range)

        enemy_entry.append(enemy_deck)
        enemy_entry.append(power)
        
        enemy_key = "card" + str(k) 
        enemy_card_info[enemy_key] = enemy_entry

#________________________________________________________________________________________________________________________

def display_player_card():
    for k, v in card_info.items():
        idx = v[2]
        power = v[1]
        card_type = v[0]
        print('Card', str(idx), 'Is A', 'Power {}'.format(power), card_type, 'Card')


#   Use Functions  ____________________________________________________________________________________________________________________________________________________________________________________

create_player_card()
create_enemy_card()

#   Start Main Loop  ____________________________________________________________________________________________________________________________________________________________________________________

while flag:

#   Start Game  ____________________________________________________________________________________________________________________________________________________________________________________

    os.system('clear')
    
    display_player_card()

#   Get Player Input  ____________________________________________________________________________________________________________________________________________________________________________________

    player_input = input('What Card Do You Choose? >>>  ')

    key = "card" + player_input
    value = card_info[key]

#   Player Place Card  ____________________________________________________________________________________________________________________________________________________________________________________

    print()
    print('You Placed A Power', value[1], value[0], 'Card')
    print()

#   Enemy Input  ____________________________________________________________________________________________________________________________________________________________________________________

    enemy_input = random.choice(enemy_idx)

    enemy_key = "card" + str(enemy_input)
    enemy_value = enemy_card_info[enemy_key]

#   Enemy Place Card  ____________________________________________________________________________________________________________________________________________________________________________________

    print()
    print('The Enemy Placed A Power', enemy_value[1], enemy_value[0], 'Card')
    print()

#   Player Beat Enemy Thing  ____________________________________________________________________________________________________________________________________________________________________________________    


#   Player Water Beat Fire  ____________________________________________________________________________________________________________________________________________________________________________________

    if value[0] == water and enemy_value[0] == fire:

        print() 
        print('You Win!')
        print()

        enemy_idx.remove(enemy_input)
        del enemy_card_info[enemy_key]

#   Player Fire Beat Snow  ____________________________________________________________________________________________________________________________________________________________________________________

    elif value[0] == fire and enemy_value[0] == snow:

        print()
        print('You Win!')
        print()

        enemy_idx.remove(enemy_input)
        del enemy_card_info[enemy_key]

#   Player Snow Beat Water  ____________________________________________________________________________________________________________________________________________________________________________________

    elif value[0] == snow and enemy_value[0] == water:

        print()
        print('You Win!')
        print()

        enemy_idx.remove(enemy_input)
        del enemy_card_info[enemy_key]

#   Player Water Beat Water  ____________________________________________________________________________________________________________________________________________________________________________________

    elif value[0] == water and enemy_value[0] == water:
        if value[1] > enemy_value[1]:

            print()
            print('You Win!')
            print()

            enemy_idx.remove(enemy_input)
            del enemy_card_info[enemy_key]

#   Player Fire Beat Fire  ____________________________________________________________________________________________________________________________________________________________________________________

    elif value[0] == fire and enemy_value[0] == fire:
        if value[1] > enemy_value[1]:

            print()
            print('You Win!')
            print()

            enemy_idx.remove(enemy_input)
            del enemy_card_info[enemy_key]

#   Player Snow Beat Snow  ____________________________________________________________________________________________________________________________________________________________________________________

    elif value[0] == snow and enemy_value[0] == snow:
        if value[1] > enemy_value[1]:

            print()
            print('You Win!')
            print()

            enemy_idx.remove(enemy_input)
            del enemy_card_info[enemy_key]

#   Enemy Win Thing  ____________________________________________________________________________________________________________________________________________________________________________________


#   Enemy Water Beat Fire  ____________________________________________________________________________________________________________________________________________________________________________________

    elif enemy_value[0] == water and value[0] == fire:

        print()
        print('You Lose!')
        print()

        del card_info[key]

#   Enemy Fire Beat Snow  ____________________________________________________________________________________________________________________________________________________________________________________

    elif enemy_value[0] == fire and value[0] == snow:

        print()
        print('You Lose!')
        print()

        del card_info[key]

#   Enemy Snow Beat Water  ____________________________________________________________________________________________________________________________________________________________________________________

    elif enemy_value[0] == snow and value[0] == water:

        print()
        print('You Lose!')
        print()

        del card_info[key]

#   Enemy Water Beat Water  ____________________________________________________________________________________________________________________________________________________________________________________

    elif enemy_value[0] == water and value[0] == water:
        if enemy_value[1] > value[1]:

            print()
            print('You Lose!')
            print()

            del card_info[key]

#   Enemy Fire Beat Fire  ____________________________________________________________________________________________________________________________________________________________________________________

    elif enemy_value[0] == fire and value[0] == fire:
        if enemy_value[1] > value[1]:

            print()
            print('You Lose!')
            print()

            del card_info[key]

#   Enemy Snow Beat Snow  ____________________________________________________________________________________________________________________________________________________________________________________

    elif enemy_value[0] == snow and value[0] == snow:
        if enemy_value[1] > value[1]:

            print()
            print('You Lose!')
            print()

            del card_info[key]

#   Tied Round


#   Snow Tied With Snow  ____________________________________________________________________________________________________________________________________________________________________________________

    elif enemy_value[0] == snow and value[0] == snow:
        if value[1] == enemy_value[1]:

            print()
            print("It's A Tie!")
            print()

#   Fire Tied With Fire  ____________________________________________________________________________________________________________________________________________________________________________________

    elif enemy_value[0] == fire and value[0] == fire:
        if value[1] == enemy_value[1]:

            print()
            print("It's A Tie!")
            print()

#   Water Tied With Water  ____________________________________________________________________________________________________________________________________________________________________________________

    elif enemy_value[0] == water and value[0] == water:
        if value[1] == enemy_value[1]:

            print()
            print("It's A Tie!")
            print()

#   Print How Much Cards Player And Enemy Have  ____________________________________________________________________________________________________________________________________________________________________________________

    print('You Have {} Cards'.format(len(card_info)))
    print('Your Opponent Has {} Cards'.format(len(enemy_card_info)))

#   Detect If Player Wins Or Loses The Game  ____________________________________________________________________________________________________________________________________________________________________________________

    if len(card_info) == 0:
        print('You Lost :(')
        flag = False

    elif len(enemy_card_info) == 0:
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