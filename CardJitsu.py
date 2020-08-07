import random, os, time

#   Print Player Info  ________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


winsFile = os.getcwd() + "\\stats\\wins.txt"
beltFile = os.getcwd() + "\\stats\\belts.txt"
achievementsFile = os.getcwd() + "\\stats\\achievements.txt"

fWins = ''
fBelt = ''
fAchievements = ''

aPlay = '\tOpen the game for the first time\n'
aTieRound = '\tTie a round\n'
aWinRound = '\tWin a round\n'
aLoseRound = '\tLose a round\n'
aWinGame = '\tWin a Game\n'
aLoseGame = '\tLose a Game\n'
aCJMaster = '\tBecome a Card Jitsu master\n'
aRepeater = '\tPlay the same card type 5 times in a row\n'

trackRepeatAmount = 0
trackRepeatType = ''


try:
    with open(winsFile, 'r') as file:
        fWins = file.read()
        file.close()
except FileNotFoundError:
    fWins = '0'
    file = open(winsFile, 'w')
    file.write(fWins)
    file.close()

try:
    with open(beltFile, 'r') as file:
        fBelt = file.read()
        file.close()
except FileNotFoundError:
    fBelt = 'White Belt'
    file = open(beltFile, 'w')
    file.write(fBelt)
    file.close()

try:
    with open(achievementsFile, 'r') as file:
        fAchievements = file.read()
        file.close()
except FileNotFoundError:
    fAchievements = aPlay
    file = open(achievementsFile, 'w')
    file.write(fAchievements)
    file.close()
    print('You got the achievement: ' + aPlay)

def tryAddAchievement(achieve):
    file = open(achievementsFile, 'r')
    noDupe = True
    for line in file.readlines():
        if line == achieve:
            noDupe = False
            break
    if noDupe:
        file.close()
        file = open(achievementsFile, 'a')
        print('You got the achievement: ' + achieve)
        file.write(achieve)
    file.close()

print('You Have', fWins, 'Wins')
print('You Have The', fBelt)
print('Achievements:\n', fAchievements)

#   Start Game  ________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

continue_ = input('Press Enter To Start Playing >>>  ')

#   Player Info  ________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

player_cards = []
enemy_cards = []

#   Card Types  ________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

fire = 'Fire'
snow = 'Snow'
water = 'Water'
all_cards = [fire, water, snow]

#   card should be fire, water, or snow
#   0 = weak, 1 = strong, 2 = neither
class Card:
    def __init__(self, type, power):
        self.power = power
        self.type = type
    def compare(self, other):
        if self.type == other.type:
            if self.power == other.power:
                return 2
            elif self.power > other.power:
                return 1
            else:  
                return 0
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
        return 3

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

playing = True
print('\n\n\n\n\n\n\n\n')

while playing:

    print('\n\n\n\n\n\n\n\n')
    display_cards(player_cards)

#   Player Card  ____________________________________________________________________________________________________________________________________________________________________________________

    player_index = -1
    while player_index == -1:
        typedInput = input('\nWhat Card Do You Choose? >>>  ')
        if typedInput.isdigit():
            if int(typedInput) <= len(player_cards) and int(typedInput) > 0:
                player_index = int(typedInput) -1
            else:
                print('Invalid typedInput')
        else:
                print('Invalid typedInput')
                
    player_card = player_cards[player_index]

    print('\n\nYou Placed A Power', player_card.power, player_card.type, 'Card')

    if trackRepeatAmount == 4:
        tryAddAchievement(aRepeater)
    elif player_card.type == trackRepeatType:
        trackRepeatAmount += 1
    else:
        trackRepeatType = player_card.type
        trackRepeatAmount = 0

#   Enemy Card  ____________________________________________________________________________________________________________________________________________________________________________________

    enemy_index = random.choice(range(0, len(enemy_cards)-1 ))
    enemy_card = enemy_cards[enemy_index]

    print('The Enemy Placed A Power', enemy_card.power, enemy_card.type, 'Card\n\n')

    type = player_card.compare(enemy_card)

    if type==1:
        tryAddAchievement(aWinRound)
        print('You Win!\n')
        del enemy_cards[enemy_index]
    elif type==0:
        tryAddAchievement(aLoseRound)
        print('You Lose!\n')
        del player_cards[player_index]
    else:
        tryAddAchievement(aTieRound)
        print("It's A Tie!\n")
    
    print('You Have {} Cards'.format(len(player_cards)))
    print('Your Opponent Has {} Cards'.format(len(enemy_cards)))

#   no cards = big L  ____________________________________________________________________________________________________________________________________________________________________________________

    if len(player_cards) == 0:
        tryAddAchievement(aLoseGame)
        print('You Lost :(')
        playing = False

    elif len(enemy_cards) == 0:
        tryAddAchievement(aWinGame)
        print('You Won!!!')
        playing = False
        #   Write Wins
        wins = int(fWins) + 1
        fWins = str(wins)
        f = open(winsFile, 'w')
        f.write(fWins)
        f.close()

        #   Belt Things ____________________________________________________________________________________________________________________________________________________________________________________
        write = False
        if int(wins) == 5:
            fBelt = 'White Belt'
            write = True
        elif int(wins) == 13:
            fBelt = 'Yellow Belt'
            write = True
        elif int(wins) == 21:
            fBelt = 'Orange Belt'
            write = True
        elif int(wins) == 30:
            fBelt = 'Green Belt'
            write = True
        elif int(wins) == 40:
            fBelt = 'Blue Belt'
            write = True
        elif int(wins) == 52:
            fBelt = 'Red Belt'
            write = True
        elif int(wins) == 64:
            fBelt = 'Purple Belt'
            write = True
        elif int(wins) == 76:
            fBelt = 'Coffee Belt'
            write = True
        elif int(wins) == 88:
            fBelt = 'Black Belt'
            write = True

        if write:
            if fBelt=='Black Belt':
                tryAddAchievement(aCJMaster)
                print('You Have Obtained The Black Belt!!!!')
                print('You Are Now A Card Jitsu Master!!!')
            else:
                print('You Have Obtained The ', fBelt, '!!!!')
            f = open(beltFile, 'w')
            f.write(fBelt)
            f.close()
    
<<<<<<< HEAD:NutJitsu.py
    unused_variable_for_pausing = input('\nPress Enter To Continue >>>  ')
    print('\n\n\n\n\n\n\n\n')
=======
    continue_ = typedInput('Press Enter To Continue >>>  ')
    print('\n\n\n\n\n\n\n\n')
>>>>>>> aee304521e691106d5526fcdc8a6a909ba210450:CardJitsu.py
