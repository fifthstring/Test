
end = '\033[0m'
bold = '\033[1m'
score = [100]


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


getch = _GetchUnix()
print(bold + 'WELCOME TO ROGUELIKE WAYFARER!' + end)

print(
    "Movement:wasd\nOpen Chest:o\nInventory:i\nGo Back:l\nHelp:h\nEquip:u\nSHOP:b\nGAME OVER:g"
)

print('All good? type y')

while True:
    x = getch.__call__()
    if x == 'y':
        break

codes = ['\033[31;107m', '\033[30;47m']

import time, os, random, math, sys
from functio import show

player = {
    'health': 100,
    'successrate': 10,
    'defense': 10,
    'crit': 20,
    'attack': 10,
    'money': 10,
    'maxhealth': 100,
    'level': 0
}
buff = [0]

names = [
    'unga', 'bunga', 'ooga', 'booga', 'beni', 'harg', 'shanka', 'drogo',
    'jogo', 'azog', 'belwas', 'borg', 'borf', 'zorg', 'polon', 'khal'
]
epithets = [
    'destroyer', 'defiler', 'evil', 'ghastly', 'bunga', 'booga', 'horrific',
    'cruel', 'great', 'strong', 'weak', 'slow', 'quick', 'speedy', 'orangutan'
]


def attack(rate, damage, crit, defense):
    if rate > 100: rate = 100
    if crit > 100: crit = 100
    number = random.randint(0, 100)

    if number > rate:
        return 0
    else:
        critc = random.randint(1, 100)
        if critc < crit:
            damage *= 2

        defense = round(defense / 5)
        damage -= defense
        if damage < 0:
            damage = 0
        return damage


skip = True


def fight():
    for i in equipped.keys():
        if equipped[i]['itemType'] == 'weapon':
            print('equipped weapon:', i)
            weapon = equipped[i]
            weaponn = i
        if equipped[i]['itemType'] == 'armor':
            print('equipped armor:', i)
            armor = equipped[i]
            armorn = i
    name = random.choice(names) + ' the ' + random.choice(epithets)

    stats = {
        'health': random.randint(80, 110) + buff[0] * 3,
        'attack': random.randint(10, 30) + buff[0],
        'successrate': random.randint(50, 70) + buff[0],
        'defense': random.randint(0, 30) + buff[0],
        'critchance': random.randint(0, 30) + buff[0]
    }
    if stats['successrate'] > 99: stats['successrate'] = 100
    if stats['critchance'] > 99:
        stats['critchance'] = 100
    os.system('clear')
    show(filename='bunga.png')
    print('''\033[30;47m
  ______ _       _     _   
 |  ____(_)     | |   | |  
 | |__   _  __ _| |__ | |_ 
 |  __| | |/ _` | '_ \| __|
 | |    | | (_| | | | | |_ 
 |_|    |_|\__, |_| |_|\__|
            __/ |          
           |___/           
\033[0m''')
    time.sleep(1)
    damage = 0
    first = random.randint(1, 2)
    if first == 1:
        print(name, 'sneak attacked you')
        time.sleep(2)
        damage = attack(stats['successrate'], stats['attack'],
                        stats['critchance'],
                        player['defense'] + armor['strength'])
        print('IT DOES', damage, 'DAMAGE')
        player['health'] -= damage

    damage2 = 0
    damage1 = damage
    while True:
        skip = False
        os.system('clear')
        show(filename='bunga.png')
        print('YOUR HEALTH:', player['health'], '(' + str(damage1 * -1) + ')')
        print(name + "'s HEALTH", stats['health'],
              '(' + str(damage2 * -1) + ')')
        damage1 = damage2 = 0
        possible = []
        for i in items.keys():
            if items[i]['itemType'] == 'healing':
                possible.append(i)
        if len(possible) == 0: print('ATTACK (a)? You have no items')

        else: print('ATTACK (a)) or use an ITEM? (i)')

        if player['health'] <= 0:
            print(
                'you narrowly escape, but drop half your money in the process')
            player['money'] = round(player['money'] / 2)
            player['health'] = player['maxhealth']
            print('You now have', player['money'], 'money')
            while True:
                x = getch.__call__()
                if parseInput(x, 'menu') == 'l':
                    break
            break

        if stats['health'] <= 0:
            print('you have killed', name)
            player['money'] += 5 + buff[0] * 2 + random.randint(0, buff[0] * 2)
            print('You now have', player['money'], 'money')
            buff[0] += 2
            score[0] += 2
            player['health'] = round(3 / 4 * player['maxhealth'])
            while True:
                x = getch.__call__()
                if parseInput(x, 'menu') == 'l':
                    break
            break

        while True:
            inp = getch.__call__()
            if inp == 'a':

                print('YOU ATTACK', name)
                damage = attack(player['successrate'] + weapon['successrate'],
                                player['attack'] + weapon['strength'],
                                stats['critchance'], stats['defense'])
                print('YOU DEAL', damage, 'DAMAGE')
                stats['health'] -= damage
                damage2 = damage
                break
            elif inp == 'i' and len(possible) > 0:

                possible = []
                for i in items.keys():
                    if items[i]['itemType'] == 'healing':
                        possible.append(i)
                        print(
                            str(len(possible)) + ':', i + ':',
                            items[i]['amount'])

                while True:
                    x = input('Pick the number you want equipped or leave(a)')

                    try:
                        x = int(x)
                    except:
                        if x == 'a':
                            skip = True
                            break
                        else:
                            continue

                    if x > len(possible):
                        print('invalid')
                        continue

                    med = items[possible[x - 1]]
                    if items[possible[x - 1]]['amount'] > 2:
                        items[possible[x - 1]]['amount'] -= 1
                    else:
                        del items[possible[x - 1]]

                    damage1 -= med['strength']
                    player['health'] = med['strength'] + player['health']
                    if player['health'] > player['maxhealth']:
                        player['health'] = player['maxhealth']

                    break
                break

        if skip == False:
            damage = attack(stats['successrate'], stats['attack'],
                            stats['critchance'],
                            player['defense'] + armor['strength'])
            player['health'] -= damage
            damage1 += damage


#show(filename='startscreen.jpg')
#time.sleep(5)

end = '\033[0m'
bold = '\033[1m'

visitedRooms = []
pre = [0]

equipped = {
    'knife': {
        'itemType': 'weapon',
        'strength': 12,
        'successrate': 75,
        'cost': 10,
        'dropRate': 100,
        'amount': 1
    },
    'leather armor': {
        'itemType': 'armor',
        'strength': 12,
        'cost': 10,
        'dropRate': 100,
        'amount': 1
    }
}

items = {
    'medicine': {
        'itemType': 'healing',
        'strength': 50,
        'successrate': 75,
        'cost': 7,
        'dropRate': 70,
        'amount': 1
    }
}

dim = [100, 100]
world = [["-" for i in range(dim[0])] for i in range(dim[1])]
coords = [20, 20]
rooms = {}
roomcoords = []
room = []
once = [False]
p = []


def update():

    pass


# Display current location (dynamic, based on coords)
def display():

    vx = 30
    vy = 24
    # Working out the 20 by 10 section  of the dungeon to display
    x = [coords[0] - int(vx / 2), coords[0] + int(vx / 2)]
    if x[0] < 0:
        x[0] = 0
        x[1] = vx
    if x[1] > dim[0]:
        x[0] = dim[0] - vx
        x[1] = dim[0]
    y = [coords[1] - int(vy / 2), coords[1] + int(vy / 2)]
    #print(x, '\n', y)
    if y[0] < 0:
        y[0] = 0
        y[1] = vy
    if y[1] > dim[1]:
        y[0] = dim[1] - vy
        y[1] = dim[1]
    #x = [0,40]
    #y = [10,40]
    #Displaying dungeon

    has = False
    for i in range(len(world)):
        for j in range(len(world[i])):
            if i > y[0] and i < y[1]:
                if j > x[0] and j < x[1]:
                    if world[i][j] == '-':
                        print('\033[48;2;0;0;0m  \033[0m', end='')

                    elif j == coords[0] and i == coords[1]:
                        print('\033[48;2;200;0;0m**\033[0m', end='')

                    elif [j, i] in visitedRooms:

                        print('\033[48;2;200;200;0m  \033[0m', end='')
                    elif world[i][j] == 'R':

                        print('\033[48;2;0;200;0m  \033[0m', end='')

                    elif world[i][j] == 'P':
                        print("\033[48;2;255;255;255m  \033[0m", end='')

                    else:
                        print(world[i][j])

                        print(world[i][j], end='')

                    has = True
        if has == True:
            print('')
        has = False


# Generates positions for the rooms


def spawnPlayer():
    potential = [random.randint(2, dim[0] - 2), random.randint(2, dim[1] - 2)]
    neighbors = [[potential[0] - 1, potential[1]],
                 [potential[0] + 1, potential[1]],
                 [potential[0], potential[1] + 1],
                 [potential[0], potential[1] - 1]]
    covered = 0
    for i in neighbors:
        if world[i[1]][i[0]] == 'R' or world[i[1]][i[0]] == 'P':
            covered += 1

    if covered >= 3 and world[potential[1]][potential[0]] == 'P':
        coords[0] = potential[0]
        coords[1] = potential[1]
    else:

        spawnPlayer()


def generateRoom():
    # Generates potential position
    potential = [random.randint(2, dim[0] - 2), random.randint(2, dim[1] - 2)]
    #Works out neighboring tiles (dungeon can't generate there)
    neighbors = [[potential[0] - 1, potential[1]],
                 [potential[0] + 1, potential[1]],
                 [potential[0], potential[1] + 1],
                 [potential[0], potential[1] - 1],
                 [potential[0], potential[1]]]
    #places dungeon
    covered = False
    for i in neighbors:
        if world[i[1]][i[0]] == 'R':
            covered = True
    if covered == False:
        choice = random.choice(list(roomtypes.keys()))
        world[potential[1]][potential[0]] = "R"
        rooms[str(potential)] = choice
        roomcoords.append(potential)


def dostuff(choices, i, m):
    drawStack = []
    chosen = [choices[i], choices[i + m]]
    if chosen[0][0] > chosen[1][0]:
        lowestX = chosen[1]
    else:
        lowestX = chosen[0]

    if chosen[0][1] > chosen[1][1]:
        lowestY = chosen[1]
    else:
        lowestY = chosen[0]

    r = random.randint(1, 2)
    if r == 1:
        for i in range(abs(chosen[0][0] - chosen[1][0])):
            drawStack.append([lowestX[0] + i, lowestX[1]])
        for i in range(abs(chosen[0][1] - chosen[1][1])):
            drawStack.append([lowestY[0], lowestY[1] + i])
    else:
        for i in range(abs(chosen[0][1] - chosen[1][1])):
            drawStack.append([lowestY[0], lowestY[1] + i])

        for i in range(abs(chosen[0][0] - chosen[1][0])):
            drawStack.append([lowestX[0] + i, lowestX[1]])

    for i in range(len(drawStack)):
        if drawStack[i] not in roomcoords:
            coords = drawStack[i]
            #print(coords)
            world[coords[1]][coords[0]] = "P"

            target = i + 1
            if target == len(drawStack): target -= 1

            if world[drawStack[target][1] +
                     1][drawStack[target][0]] == 'P' and world[
                         drawStack[target][1] + 1][drawStack[target][0] +
                                                   1] == 'P':
                break

            if world[drawStack[target][1] -
                     1][drawStack[target][0]] == 'P' and world[
                         drawStack[target][1] - 1][drawStack[target][0] +
                                                   1] == 'P':
                break

            if world[drawStack[target][1]][
                    drawStack[target][0]] == 'P' or world[
                        drawStack[target][1]][drawStack[target][0]] == 'R':
                break


def generatePaths(potX=random.randint(2, dim[0] - 2),
                  potY=random.randint(2, dim[1] - 2),
                  counter=0):

    for i in range(len(roomcoords) - 1):
        dostuff(roomcoords, i, 1)
        dostuff(roomcoords, i, -1)
        dostuff(roomcoords, i, -2)
        #dostuff(roomcoords,i,-3)
        #dostuff(roomcoords,i,-4)


def deleteIncorrectRooms():
    for i in range(len(world)):
        for j in range(i):
            if world[i][j] == 'R':
                potential = [i, j]
                neighbors = [[potential[0] - 1, potential[1]],
                             [potential[0] + 1, potential[1]],
                             [potential[0], potential[1] + 1],
                             [potential[0], potential[1] - 1],
                             [potential[0], potential[1]]]
                empty = True
                for k in neighbors:
                    if world[k[0]][k[1]] == 'P':
                        empty = False

                if empty == True:
                    world[potential[1]][potential[0]] == '-'

                    temp = potential[0]
                    potential[0] = potential[1]
                    potential[1] = temp

                    roomcoords.remove(potential)


#Treasure room
treasure = {
    'knife': {
        'itemType': 'weapon',
        'strength': 12,
        'successrate': 75,
        'cost': 15,
        'dropRate': 200,
        'amount': 1
    },
    'medicine': {
        'itemType': 'healing',
        'strength': 50,
        'successrate': 75,
        'cost': 20,
        'dropRate': 70,
        'amount': 1
    },
    'panacea': {
        'itemType': 'healing',
        'strength': 75,
        'successrate': 75,
        'cost': 40,
        'dropRate': 70,
        'amount': 1
    },
    'perfect panacea': {
        'itemType': 'healing',
        'strength': 200,
        'successrate': 75,
        'cost': 100,
        'dropRate': 70,
        'amount': 1
    },
    'talwar': {
        'itemType': 'weapon',
        'strength': 32,
        'successrate': 70,
        'cost': 99,
        'dropRate': 10,
        'amount': 1
    },
    'arakh': {
        'itemType': 'weapon',
        'strength': 35,
        'successrate': 75,
        'cost': 120,
        'dropRate': 20,
        'amount': 1
    },
    'longsword': {
        'itemType': 'weapon',
        'strength': 16,
        'successrate': 60,
        'cost': 30,
        'dropRate': 100,
        'amount': 1
    },
    'greatsword': {
        'itemType': 'weapon',
        'strength': 26,
        'successrate': 45,
        'cost': 35,
        'dropRate': 75,
        'amount': 1
    },
    'steel spear': {
        'itemType': 'weapon',
        'strength': 30,
        'successrate': 80,
        'cost': 90,
        'dropRate': 4,
        'amount': 1
    },
    'dragonsteel sword': {
        'itemType': 'weapon',
        'strength': 70,
        'successrate': 70,
        'cost': 150,
        'dropRate': 2,
        'amount': 1
    },
    'glamdring': {
        'itemType': 'weapon',
        'strength': 80,
        'successrate': 80,
        'cost': 250,
        'dropRate': 1,
        'amount': 1
    },
    'wooden bow': {
        'itemType': 'weapon',
        'strength': 8,
        'successrate': 90,
        'cost': 20,
        'dropRate': 200,
        'amount': 1
    },
    'nether stone bow': {
        'itemType': 'weapon',
        'strength': 12,
        'successrate': 90,
        'cost': 30,
        'dropRate': 80,
        'amount': 1
    },
    'yew yew longbow': {
        'itemType': 'weapon',
        'strength': 15,
        'successrate': 90,
        'cost': 40,
        'dropRate': 50,
        'amount': 1
    },
    'flower of justice': {
        'itemType': 'weapon',
        'strength': 25,
        'successrate': 99,
        'cost': 80,
        'dropRate': 10,
        'amount': 1
    },
    'obamium sword': {
        'itemType': 'weapon',
        'strength': 420,
        'successrate': 100,
        'cost': 25000,
        'dropRate': 1,
        'amount': 1
    },
    'leather armor': {
        'itemType': 'armor',
        'strength': 12,
        'cost': 10,
        'dropRate': 100,
        'amount': 1
    },
    'chainmail': {
        'itemType': 'armor',
        'strength': 16,
        'cost': 20,
        'dropRate': 20,
        'amount': 1
    },
    'platemail': {
        'itemType': 'armor',
        'strength': 20,
        'cost': 40,
        'dropRate': 50,
        'amount': 1
    },
    'knight armor': {
        'itemType': 'armor',
        'strength': 40,
        'cost': 80,
        'dropRate': 3,
        'amount': 1
    },
    'berserker armor': {
        'itemType': 'armor',
        'strength': 50,
        'cost': 120,
        'dropRate': 1,
        'amount': 1
    },
    'dragon armor': {
        'itemType': 'armor',
        'strength': 70,
        'cost': 200,
        'dropRate': 1,
        'amount': 1
    },
    'titan armor': {
        'itemType': 'armor',
        'strength': 100,
        'cost': 300,
        'dropRate': 1,
        'amount': 1
    }
}
total = 0
for i in treasure:
    #print(i)
    total += treasure[i]['dropRate']


def getItems(c='weapon'):
    l = []
    for i in items.keys():
        if items[i]['itemType'] == c:
            l.append(i)
    return l


def getShopItems(c='weapon'):
    l = []
    for i in treasure.keys():
        if treasure[i]['itemType'] == c:
            l.append(i)
    return l


def parseInput(inp, room):
    if inp == 'help' or inp == 'h' or inp == '\n':
        os.system('clear')
        print(codes[1] + '''
 _____ _____ _   _ ___________ _____ _     _____ 
/  __ |  _  | \ | |_   _| ___ |  _  | |   /  ___|
| /  \| | | |  \| | | | | |_/ | | | | |   \ `--. 
| |   | | | | . ` | | | |    /| | | | |    `--. \
| \__/\ \_/ | |\  | | | | |\ \\ \_/ | |___/\__/ /
 \____/\___/\_| \_/ \_/ \_| \_|\___/\_____\____/ 
                                                 
                                                 
''' + end)
        print(
            "Movement:wasd\nOpen Chest:o\nInventory:i\nGo Back:l\nHelp:h\nEquip:u\nSHOP:b\nGAME OVER:g"
        )

        while True:
            x = getch.__call__()
            if parseInput(x, 'menu') == 'l':
                break

    if inp == 'b':

        os.system('clear')
        print(codes[1] + '''
  ____                  _______      _ _ 
 |  _ \                / / ____|    | | |
 | |_) |_   _ _   _   / | (___   ___| | |
 |  _ <| | | | | | | / / \___ \ / _ | | |
 | |_) | |_| | |_| |/ /  ____) |  __| | |
 |____/ \__,_|\__, /_/  |_____/ \___|_|_|
               __/ |                     
              |___/                      
''' + end)
        print('MONEY:', player['money'])

        counter = 0
        for i in treasure.keys():
            counter += 1

            if treasure[i]['itemType'] == 'weapon':
                print(counter, '  ', i, 'Successrate:',
                      treasure[i]['successrate'], 'Damage:',
                      treasure[i]['strength'], 'Cost:', treasure[i]['cost'])

            elif treasure[i]['itemType'] == 'armor':
                print(counter, '  ', i, 'Amount:', treasure[i]['amount'],
                      'Defense:', treasure[i]['strength'], 'Cost:',
                      treasure[i]['cost'])

            elif treasure[i]['itemType'] == 'healing':
                print(counter, '  ', i, 'Amount:', treasure[i]['amount'],
                      'Defense:', treasure[i]['strength'], 'Cost:',
                      treasure[i]['cost'])
        while True:
            print()
            x = input(
                'Input the number you want to buy\nInput s to sell duplicate armor and weapons\nInput a to leave the shop'
            )
            if x == 's':
                gains = 0
                for key in items.keys():
                    if items[key]['amount'] > 1 and items[key][
                            'itemType'] != 'healing':
                        number_sold = items[key]['amount'] - 1
                        items[key]['amount'] -= number_sold
                        print('sold', number_sold, '*', key)
                        cost = round(items[key]['cost'] / 10)
                        gains += cost * number_sold

                print('You have gained:', gains, 'money')
                player['money'] += gains
                print('You now have', player['money'], 'money')
                while True:
                    x = getch.__call__()
                    if parseInput(x, 'menu') == 'l':
                        break
                break

            if x == 'a': break
            try:
                x = int(x)
            except:
                continue

            if x > len(treasure):
                continue

            item = list(treasure.keys())[x - 1]
            if player['money'] >= treasure[item]['cost']:
                print('You bought the', item)
                score[0] += int(round(treasure[item]['cost'] / 5))
                player['money'] -= treasure[item]['cost']

            if item in items.keys():
                items[item]['amount'] += 1
            else:
                items[item] = treasure[item]

    if inp == 'u':

        while True:

            os.system('clear')
            print(codes[1] + '''
  ______            _       
 |  ____|          (_)      
 | |__   __ _ _   _ _ _ __  
 |  __| / _` | | | | | '_ \ 
 | |___| (_| | |_| | | |_) |
 |______\__, |\__,_|_| .__/ 
           | |       | |    
           |_|       |_|    
''' + end)
            for i in equipped.keys():
                if equipped[i]['itemType'] == 'weapon':
                    print('equipped weapon:', i)
                    weapon = equipped[i]
                    weaponn = i
                if equipped[i]['itemType'] == 'armor':
                    print('equipped armor:', i)
                    armor = equipped[i]
                    armorn = i

            print('Change Weapon:1\nChange Armor:2\nExit:3')

            x = getch.__call__()
            try:
                x = int(x)
            except:
                continue
            if x == 3: break
            if x == 2:
                if len(getItems('armor')) > 0:
                    possible = []
                    for i in items.keys():
                        if items[i]['itemType'] == 'armor':
                            possible.append(i)
                            print(str(len(possible)) + ':', i)
                    while True:
                        print()
                        x = input(
                            'Pick the number you want equipped or a to leave')
                        try:
                            x = int(x)
                        except:
                            if x == 'a': break
                            else:
                                print('invalid')
                                continue

                        if len(possible[x - 1]) < x or armorn == possible[x -
                                                                          1]:
                            print('invalid')
                            continue

                        toequip = items[possible[x - 1]]
                        equipped[possible[x - 1]] = toequip
                        equipped[possible[x - 1]]
                        items[possible[x - 1]]['amount'] -= 1
                        if items[possible[x - 1]]['amount'] <= 0:
                            del items[possible[x - 1]]

                        if armorn in items.keys():
                            items[armorn]['amount'] += 1
                        else:
                            items[armorn] = armor

                        del equipped[armorn]

                        break
                    break
            if x == 1:
                if len(getItems('weapon')) > 0:
                    possible = []
                    for i in items.keys():
                        if items[i]['itemType'] == 'weapon':
                            possible.append(i)
                            print(str(len(possible)) + ':', i)
                    while True:
                        print()
                        x = input(
                            'Pick the number you want equipped or a to leave')
                        try:
                            x = int(x)
                        except:
                            if x == 'a': break
                            else:
                                print('invalid')
                                continue

                        if len(possible[x - 1]) < x or weaponn == possible[x -
                                                                           1]:
                            print('invalid')
                            continue

                        toequip = items[possible[x - 1]]
                        equipped[possible[x - 1]] = toequip
                        equipped[possible[x - 1]]
                        items[possible[x - 1]]['amount'] -= 1
                        if items[possible[x - 1]]['amount'] <= 0:
                            del items[possible[x - 1]]

                        if weaponn in items.keys():
                            items[weaponn]['amount'] += 1
                        else:
                            items[weaponn] = weapon

                        del equipped[weaponn]

                        break
                    break

    if inp == 'i':
        os.system('clear')
        print(codes[1] + '''
  _____            
 |_   _|           
   | |  _ ____   __
   | | | '_ \ \ / /
  _| |_| | | \ V / 
 |_____|_| |_|\_/  
                   
                   
''' + end)

        print(bold + '\nStats' + end)
        for i in player.keys():
            print(i + ':', player[i])
        print(bold + '\nEquipped' + end)
        for i in equipped.keys():
            equipped[i]['amount'] = 1
            if equipped[i]['itemType'] == 'weapon':
                print(i, 'Amount:', equipped[i]['amount'], 'Successrate:',
                      equipped[i]['successrate'], 'Damage:',
                      equipped[i]['strength'])
            elif equipped[i]['itemType'] == 'armor':
                print(i, 'Amount:', equipped[i]['amount'], 'Defense:',
                      equipped[i]['strength'])

        print(bold + '\nWeapons' + end)

        weapons = getItems('weapon')
        armor = getItems('armor')
        other = getItems('healing')

        for i in weapons:
            print(i, 'Amount:', items[i]['amount'], 'Successrate:',
                  items[i]['successrate'], 'Damage:', items[i]['strength'])

        print(bold + '\nArmor' + end)

        for i in armor:
            print(i, 'Amount:', items[i]['amount'], 'Defense:',
                  items[i]['strength'])

        print(bold + '\nOther' + end)
        for i in other:
            print(i, 'Amount:', items[i]['amount'], 'Healing:',
                  items[i]['strength'])

        while True:
            x = getch.__call__()
            if parseInput(x, 'menu') == 'l':
                break

    elif room == 'menu':
        if inp == 'l':
            return 'l'
    elif room == 'treasureroom':
        if inp == 'e':
            return 'e'
        if inp == 'o':
            treasures = []
            for i in range(3):
                choice = random.randint(1, total)
                #print(choice)
                cumulative = 0
                for i in treasure:
                    cumulative += treasure[i]['dropRate']
                    if choice < cumulative:
                        treasures.append(i)
                        break
            #print(treasures)
            print('YOU RECEIVED:')
            for i in treasures:
                print(i)
            while True:
                x = getch.__call__()
                if parseInput(x, 'menu') == 'l':
                    break

            return treasures

    elif room == 'none':

        if inp == 'a': x = valid([coords[0] - 1, coords[1]], x=-1)
        if inp == 'd': x = valid([coords[0] + 1, coords[1]], x=1)
        if inp == 'w': x = valid([coords[0], coords[1] - 1], y=-1)
        if inp == 's': x = valid([coords[0], coords[1] + 1], y=1)

    else:
        return 'invalid'


def troll():
    os.system('clear')
    if random.randint(1, 2) == 1:
        for i in range(5):
            show(filename='image26.jpg')
            time.sleep(0.05)
            os.system('clear')

            show(filename='image27.jpg')
            time.sleep(0.05)
            os.system('clear')

    else:
        show(filename='download.jpeg')
        print("You've been Gnomed")
        while True:
            x = getch.__call__()
            if parseInput(x, 'menu') == 'l':
                break


def rest():
    os.system('clear')
    show(filename='RICK.jpeg')
    player['maxhealth'] += 2
    player['level'] += 1
    player['defense'] += 1
    player['attack'] += 1
    if player['level'] % 2 == 0:
        player['successrate'] += 1
    if player['level'] % 4 == 0:
        player['crit'] += 1

    score[0] += 5
    player['health'] = player['maxhealth']
    print(codes[1] + '''
  _                    _   _    _ _____  _ 
 | |                  | | | |  | |  __ \| |
 | |     _____   _____| | | |  | | |__) | |
 | |    / _ \ \ / / _ | | | |  | |  ___/| |
 | |___|  __/\ V |  __| | | |__| | |    |_|
 |______\___| \_/ \___|_|  \____/|_|    (_)
                                           
                                           
''' + end)

    print(bold + 'LEVEL UP! BASE STATS INCREASED! HEALTH RESTORED' + end)
    while True:
        x = getch.__call__()
        if parseInput(x, 'menu') == 'l':
            break


t = [298]


def riddleroom():
    os.system('clear')
    print(codes[1] + '''
  _____  _     _     _ _            
 |  __ \(_)   | |   | | |           
 | |__) |_  __| | __| | | ___       
 |  _  /| |/ _` |/ _` | |/ _ \      
 | | \ \| | (_| | (_| | |  __/_ _ _ 
 |_|  \_|_|\__,_|\__,_|_|\___(_(_(_)
                                    
                                    
''' + end)
    index = random.randint(0, t[0])
    
    x = riddles.pop(index)
    t[0] -= 1
    while True:
        print(x[0])
        y = input('Just enter the answer word or letter. enter end to give up')
        if y.lower() == 'end':
            print('You give up!')
            print('The answer was', x[1].lower())
            while True:
                x = getch.__call__()
                if parseInput(x, 'menu') == 'l':
                    break
            break

        if y.lower() == x[1].lower():
            print('Correct!')
            money = random.randint(1, 100)
            if money == 2:
                print('YOU WON THE JACKPOT! 100000 COINS!')

                player['money'] += 100000
            else:
                coins = random.randint(1, 10 + buff[0])
                player['money'] += coins
                print('You received', coins, 'coins')
                score[0] += coins

            while True:
                x = getch.__call__()
                if parseInput(x, 'menu') == 'l':
                    break
            break


def treasureroom():
    os.system('clear')
    show(filename='treasurechest.png')
    print('''\033[30;47m
  _______                                _ 
 |__   __|                              | |
    | |_ __ ___  __ _ ___ _   _ _ __ ___| |
    | | '__/ _ \/ _` / __| | | | '__/ _ | |
    | | | |  __| (_| \__ | |_| | | |  __|_|
    |_|_|  \___|\__,_|___/\__,_|_|  \___(_)
                                           \033[0m''')
    while True:

        c = getch.__call__()
        out = parseInput(c, 'treasureroom')
        p
        if out == 'e':
            break
        elif type(out) == list:
            for i in out:
                if i in items:
                    items[i]['amount'] += 1
                else:
                    items[i] = treasure[i]
            break
        else:
            pass


def fightroom():
    pass


roomtypes = {
    'Treasure Room': [],
    'Trap Room': [],
    'Puzzle Room': [],
    'Enemy Room': [],
    'Start Room': [],
    'Boss Room': []
}

decorations = {
    'Old Painting':
    [['streaked with blood', 'covered in dust'],
     ['depicting a battle', 'depicting a monster', 'depicting a dragon']],
    'Crack': {'huge', 'big', 'deep', 'filthy'},
    'Symbol': {'demonic', 'grand', 'ornate', 'circular'}
}

for i in range(int((dim[0] * dim[1]) / 10)):
    generateRoom()
    #display()

generatePaths()
spawnPlayer()
#deleteIncorrectRooms()


def valid(inp, x=0, y=0):

    if inp in roomcoords:
        c = random.randint(1, 15)
        if c < 1:
            treasureroom()
        elif c < 3:
            troll()
            treasureroom()
        elif c < 6:
            rest()
        elif c == 7:
            parseInput('b', 'none')
        elif c == 8:
            parseInput('i', 'wefwef')
        elif c == 9:
            parseInput('u', 'wefwef')

        else:
            riddleroom()

        coords[0] = inp[0]
        coords[1] = inp[1]
        visitedRooms.append([coords[0], coords[1]])
        roomcoords.remove(coords)
        return

    if world[inp[1]][inp[0]] == 'P' or world[inp[1]][inp[0]] == 'R':
        coords[0] = inp[0]
        coords[1] = inp[1]

        x = random.randint(1, 10)
        if x == 6:
            fight()

        return 'move'

    return 'invalid'


def reset(inp, p):
    world[inp[1]][inp[0]] = p


move = False

has_moved = 0

riddles = [
    [
        "With thieves I consort, With the Vilest, in short, I'm quite at ease in depravity, Yet all divines use me, And savants can't lose me, For I am the century of gravity.",
        'V'
    ],
    [
        'I move without wings, Between silken string, I leave as you find, My substance behind.',
        'Spider'
    ], ['What flies forever, Rests never?', 'Wind'],
    [
        'I appear in the morning. But am always there. You can never see me. Though I am everywhere. By night I am gone, though I sometimes never was. Nothing can defeat me. But I am easily gone.',
        'Sunlight'
    ], ['I crawl on the earth. And rise on a pillar.', 'Shadow'],
    [
        'They are many and one, they wave and they drum, Used to cover a state, they go with you everywhere.',
        'Hands'
    ],
    [
        'What must be in the oven yet can not be baked? Grows in the heat yet shuns the light of day? What sinks in water but rises with air? Looks like skin but is fine as hair?',
        'Yeast'
    ],
    [
        'I have holes on the top and bottom. I have holes on my left and on my right. And I have holes in the middle, Yet I still hold water.',
        'Sponge'
    ], ['What can be swallowed, But can also swallow you?', 'Pride'],
    [
        'You get many of me, but never enough. After the last one, your life soon will snuff. You may have one of me but one day a year, When the last one is gone, your life disappears.',
        'Birthday'
    ], ['I run around the city, but I never move.', 'Wall'],
    [
        'As a whole, I am both safe and secure. Behead me, I become a place of meeting. Behead me again, I am the partner of ready. Restore me, I become the domain of beasts.',
        'Stable'
    ],
    [
        'Two horses, swiftest traveling, harnessed in a pair, and grazing ever in places. Distant from them.',
        'Eyes'
    ],
    [
        'At the sound of me, men may dream. Or stamp their feet. At the sound of me, women may laugh. Or sometimes weep.',
        'Music'
    ],
    [
        "To unravel me you need a simple key, no key that was made by locksmith's hand. But a key that only I will understand.",
        'Riddle'
    ], ['Long and think, red within, with a nail at the end.', 'Finger'],
    [
        "I'm sometimes white and always wrong. I can break a heart and hurt the strong. I can build love or tear it down. I can make a smile or bring a frown.",
        'Lie'
    ],
    [
        'You can tumble in it, roll in it, burn it, animal eat it. Used to cover floors, still used beyond stall doors. Freshens whatever it is placed on. Absorbs whatever is poured into it.',
        'Hay'
    ],
    [
        "I come in winter. I cannot see, hear, or feel. I can't eat, But you can eat parts of me.",
        'Snowman'
    ],
    [
        "Sometimes I am loud. And viewed with distaste. Poke out my 'eye', then I'm on the front of your face.",
        'Noise'
    ], ['What is it that has four legs, one head, and a foot?', 'Bed'],
    [
        'What makes a loud noise when changing its jacket. Becomes larger but weighs less?',
        'Popcorn'
    ],
    [
        'I am always hungry, I must always be fed. The finger I lick will soon turn red.',
        'Fire'
    ],
    [
        'Something wholly unreal, yet seems real to I. Think my friend, tell me where does it lie?',
        'Mind'
    ],
    [
        'No matter how little or how much you use me, you change me every month.',
        'Calendar'
    ], ['What can burn the eyes, sting the mouth, yet be consumed?', 'Salt'],
    ['What an fill a room but takes up no space?', 'Light'],
    [
        'It occurs once in every minute. Twice in every moment and yet never in one hundred thousand years.',
        'M'
    ],
    [
        'With pointed fangs it sits in wait. With piercing force it doles out fate, over bloodless victims proclaiming its might. Eternally joining in a single bite.',
        'Stapler'
    ],
    [
        '"It holds most knowledge that has ever been said. But is not the brain, is not the head. To feathers and their masters, it\'s both bane and boon\x85One empty, and one full."',
        'Paper'
    ],
    [
        "Upon me you can tread, though softly under cover. And I will take you places, that you have yet to discover. I'm high, and I'm low, though flat in the middle. And though a joy to the children, adults think of me little.",
        'Stairs'
    ],
    [
        'A mile from end to end, yet as close to as a friend. A precious commodity, freely given. Seen on the dead and on the living. Found on the rich, poor, short and tall. But shared among children most of all.',
        'Smile'
    ],
    [
        "I have a hundred legs, but cannot stand. I have a long neck, but no head. I cannot see. I'm neat and tidy as can be.",
        'Broom'
    ],
    [
        "Flat as a leaf, round as a ring. Has two eyes, can't see a thing.",
        'Button'
    ],
    [
        "I don't think or eat or slumber. Or move around or fear thunder. Just like you I look the same but I can't harm you or be your bane.",
        'Doll'
    ],
    [
        'In marble halls as white as milk, lined with a skin as soft as silk. Within a fountain crystal-clear. A golden apple doth appear. No doors there are to this stronghold, yet thieves break in and steal the gold.',
        'Egg'
    ], ['What is it that you must give before you can keep it.', 'Word'],
    [
        'I dig out tiny caves and store gold and silver in them. I also build bridges of silver and make crowns of gold. They are the smallest you could imagine. Sooner or later everybody needs my help. Yet many people are afraid to let me help them.',
        'Dentist'
    ],
    [
        'What is long and slim, works in light. Has but one eye, and an awful bite?',
        'Needle'
    ],
    [
        'What lies in a tunnel of darkness. That can only attack when pulled back?',
        'Bullet'
    ], ['What has six faces and twenty-one eyes?', 'Die'],
    [
        'Until I am measured. I am not known, yet how you miss me when I have flown.',
        'Time'
    ],
    [
        'Three lives have I. Gentle enough to soothe the skin. Light enough to caress the sky. Hard enough to crack rocks.',
        'Water'
    ],
    [
        'I wear a red robe, with staff in hand, and a stone in my throat.',
        'Cherry'
    ],
    [
        'A warrior amongst the flowers, he bears a thrusting sword. He uses it whenever he must, to defend his golden hoard.',
        'Bee'
    ], ['I hide but my head is outside.', 'Nail'],
    [
        'A house full, a yard full, a chimney full, no one can get a spoonful.',
        'Smoke'
    ],
    [
        'You can spin, wheel and twist. But this thing can turn without moving.',
        'Milk'
    ],
    [
        "Halo of water, tongue of wood. Skin of stone, long I've stood. My fingers short reach to the sky. Inside my heart men live and die.",
        'Castle'
    ],
    [
        'When they are caught, they are thrown away. When they escape, you itch all day.',
        'Fleas'
    ],
    [
        'What does man love more than life, fear more than death or mortal strife. What the poor have, the rich require, and what contented men desire. What the miser spends, and the spendthrift saves. And all men carry to their graves.',
        'Nothing'
    ],
    [
        "In we go, out we go. All around and in a row. Always, always steady flow. When we'll stop, you'll never known. In we go, out we go.",
        'Tides'
    ],
    [
        "A cloud was my mother, the wind is my father. My son is the cool stream, and my daughter is the fruit of the land. A rainbow is my bed, the earth my final resting place. And I'm the torment of man.",
        'Rain'
    ],
    [
        'Born of earth, but with none of its strength. Molded by flame, but with none of its power. Shaped',
        'Glass'
    ],
    [
        'Remove the outside. Cook the inside. Eat the outside. Throw away the inside.',
        'Corn'
    ],
    [
        'This is in a realm of true and in a realm false, but you experience me as you turn and toss.',
        'Dream'
    ],
    [
        'There is an ancient invention. Still used in some parts of the world today. That allows people to see through walls.',
        'Window'
    ],
    [
        'Some live in me, some live on. And some shave me to stride upon. I rarely leave my native land. Until my death I always stand. High and low I may be found. Both above and below ground.',
        'Tree'
    ],
    [
        'Metal or bone I may be, many teeth I have and always bared. Yet my bite harms no one. And ladies delight in my touch.',
        'Comb'
    ],
    [
        "I am a fire's best friend. When fat, my body fills with wind. When pushed to thin, through my nose I blow. Then you can watch the embers glow.",
        'Bellows'
    ],
    [
        "Every dawn begins with me. At dusk I'll be the first you see, and daybreak couldn't come without. What midday centers all about. Daises grow from me, I'm told. And when I come, I end all code, but in the sun I won't be found. Yet still, each day I'll be around.",
        'D'
    ],
    [
        'You heart it speak, for it has a hard tongue. But it cannot breathe, for it has not a lung.',
        'Bell'
    ],
    [
        'I cut through evil like a double edged sword, and chaos flees at my approach. Balance I single-handedly upraise, through battles fought with heart and mind, instead of with my gaze.',
        'Justice'
    ],
    [
        'The eight of us move forth and back. To protect our king from the foes attack.',
        'Pawns'
    ],
    [
        'He has one and a person has two. A citizen has three. And a human being has four. A personality has five. And an inhabitant of earth has six.',
        'Syllable'
    ],
    [
        'If you break me, I do not stop working. If you touch me, I may be snared. If you lose me, nothing will matter.',
        'Heart'
    ], ["What's in the middle of nowhere?", 'H'],
    [
        'What force and strength cannot get through. I, with a gentle touch, can do. Many in the street would stand. Were I not a friend at hand.',
        'Key'
    ],
    [
        'Often held but never touched. Always wet but never rusts. Often bits but seldom bit. To use it well you must have wit.',
        'Tongue'
    ],
    [
        "As round as an apple. As deep as a cup. All the king's horses can't pull it up.",
        'Well'
    ],
    [
        'He stands beside the road. In a purple cap at tattered green cloak. Those who touch him, curse him.',
        'Thistle'
    ],
    [
        'Power enough to smash ships and crush roofs. Yet it still must fear the sun.',
        'Ice'
    ], ['What surrounds the world, yet dwells within a thimble?', 'Space'],
    [
        'I cannot be other than what I am, until the man who made me dies. Power and glory will fall to me finally. Only when he last closes his eyes.',
        'Prince'
    ],
    [
        'What is it that makes tears without sorrow. And takes its journey to heaven?',
        'Smoke'
    ],
    [
        'Inside a great blue castle lives a shy young maid. She blushes in the morning and comes not out at night.',
        'Sun'
    ],
    [
        'This thing runs but cannot walk, sometimes sings but never talks. Lacks arms, has hands; lacks a head but has a face.',
        'Clock'
    ],
    [
        'A word I know, six letters it contains. Subtract just one and twelve remains.',
        'Dozens'
    ], ["I am the yellow hem of the sea's blue skirt.", 'Beach'],
    [
        'A skin have I, more eyes than one. I can be very nice when I am done.',
        'Potato'
    ],
    [
        'I have four legs but no tail. Usually I am heard only at night.',
        'Frog'
    ],
    ['A tiny bead, like fragile glass, strung along a cord of grass.', 'Dew'],
    [
        'Break it and it is better, immediately set and harder to break again.',
        'Record'
    ],
    [
        'Each morning I appear to lie at your feet, all day I follow no matter how fast you run. Yet I nearly perish in the midday sun.',
        'Shadow'
    ],
    ["What do you throw out to use and take in when you're done?", 'Anchor'],
    [
        'What is it which builds things up? Lays mountains low? Dries up lakes, and makes things grow? Cares not a whim about your passing? And is like few other things, because it is everlasting?',
        'Time'
    ],
    [
        'I am the fountain from which no one can drink. For many I am considered a necessary link. Like gold to all I am sought for, but my continued death brings wealth for all to want more.',
        'Oil'
    ],
    [
        "Sleeping during the day, I hide away. Watchful through the night, I open at dawn's light. But only for the briefest time, do I shine. And then I hide away. And sleep through the day.",
        'Sunrise'
    ],
    [
        'A seed am I, three letters make my name. Take away two and I still sound the same.',
        'Pea'
    ],
    [
        'In the middle of night, I surround the gong. In the middle of sight, I end the song.',
        'G'
    ],
    [
        "Look into my face and I'm everybody. Scratch my back and I'm nobody.",
        'Mirror'
    ],
    [
        'Two brothers we are, great burdens we bear. All day we are bitterly pressed. Yet this I will say, we are full all the day, and empty when go to rest.',
        'Boots'
    ],
    [
        'They can be harbored, but few hold water. You can nurse them, but only by holding them against someone else. You can carry them, but not with your arms. You can bury them, but not in the earth.',
        'Grudge'
    ],
    [
        'What is it that was given to you, belongs only to you. And yet your friends use it more than you do?',
        'Name'
    ],
    [
        "By Moon or by Sun, I shall be found. Yet I am undone, if there's no light around.",
        'Shadow'
    ],
    ['What do you use to hoe a row, slay a foe, and wring with woe?', 'Hands'],
    [
        'We travel much, yet prisoners are, and close confined to boot. Yet with any horse, we will keep the pace, and will always go on foot.',
        'Spurs'
    ],
    [
        'Without a bridle, or a saddle, across a thing I ride a-straddle. And those I ride, by help of me, though almost blind, are made to see.',
        'Glasses'
    ],
    [
        'I fly through the air on small feathered wings, seeking out life and destroying all things.',
        'Arrow'
    ], ['I am the red tongue of the earth, that buries cities.', 'Lava'],
    [
        'I look at you, you look at me, I raise my right, you raise your left.',
        'Mirror'
    ],
    [
        'What is the thing which, once poured out, cannot be gathered again?',
        'Rain'
    ],
    [
        'It is a part of us, and then replaced. It escapes out bodies, to a better place. The world becomes its sizeable home. Its passions unrestraint, the planet it roams.',
        'Water'
    ],
    [
        "What word starts with 'E', ends with 'E', but only has one letter? It is not the letter 'E'.",
        'Envelope'
    ],
    [
        "A hole in a pole, though I fill a hole in white. I'm used more by the day, and less by the night.",
        'Eye'
    ],
    [
        'I fly, yet I have no wings. I cry, yet I have no eyes. Darkness follows me. Lower light I never see.',
        'Cloud'
    ], ["I'm full of holes, yet I'm full of water.", 'Sponge'],
    [
        "Long and slinky like a trout, never sings till it's guts come out.",
        'Gun'
    ], ['What animal keeps the best time?', 'Watchdog'],
    ['What kind of room has no windows or doors?', 'Mushroom'],
    [
        'I have legs but walk not, a strong back but work not. Two good arms but reach not. A seat but sit and tarry not.',
        'Chair'
    ],
    [
        "It's in your hand though you can not feel it. Only you and time can reveal it.",
        'Fate'
    ],
    [
        "Not born, but from a Mother's body drawn. I hang until half of me is gone. I sleep in a cave until I grow old. Then valued for my hardened gold.",
        'Cheese'
    ],
    [
        'I am the outstretched fingers that seize and hold the wind. Wisdom flows from me in other hands. Upon me are sweet dreams dreamt, my merest touch brings laughter.',
        'Feather'
    ],
    [
        'Hands she has but does not hold. Teeth she has but does not bite. Feet she has but they are cold. Eyes she has but without sight.',
        'Doll'
    ], ['Only two backbones and thousands of ribs.', 'Railroad'],
    ["Hard iron on horse. Cow's hide on man.", 'Shoe'],
    [
        'What word is the same written forward, backward and upside down?',
        'Noon'
    ],
    [
        'I cannot be felt, seen or touched. Yet I can be found in everybody. My existence is always in debate. Yet I have my own style of music.',
        'Soul'
    ],
    [
        "I am seen in the water. If seen in the sky, I am in the rainbow, a jay's feather, and lapis lazuli.",
        'Blue'
    ],
    [
        'You use it between your head and your toes, the more it works the thinner it grows.',
        'Soap'
    ],
    [
        'Fatherless and motherless. Born without sin, roared when it came into the world. And never spoke again.',
        'Thunder'
    ],
    [
        'Where can you find roads without cars, forests without trees and cities without houses?',
        'Map'
    ],
    [
        "A leathery snake, with a stinging bite. I'll stay coiled up, unless I must fight.",
        'Whip'
    ],
    [
        'Take one out and scratch my head, I am now black but once was red.',
        'Match'
    ],
    [
        'Mountains will crumble and temples will fall. And no man can survive its endless call.',
        'Time'
    ],
    [
        'What has wings, but can not fly. Is enclosed, but can outside also lie. Can open itself up, or close itself away. Is the place of kings and queens and doggerel of every means. What is it upon which I stand? Which can lead us to different lands.',
        'Stage'
    ],
    [
        "I'm the source of all emotion, but I'm caged in a white prison.",
        'Heart'
    ],
    [
        "I am the tool, for inspiring many. Buy me in the store, for not much more than a penny. Don't overuse me, or my usefulness will go.",
        'Pen'
    ],
    [
        'What goes through a door but never goes in. And never comes out?',
        'Keyhole'
    ], ['What goes up when the rain comes down?', 'Umbrella'],
    ["I occur twice in eternity. And I'm always within sight.", 'T'],
    [
        'Twigs and spheres and poles and plates. Join and bind to reason make.',
        'Skeleton'
    ],
    [
        'The sun bakes them, the hand breaks them, the foot treads on them, and the mouth tastes them.',
        'Grapes'
    ],
    [
        "I have many feathers to help me fly. I have a body and head, but I'm not alive. It is your strength which determines how far I go. You can hold me in your hand, but I'm never thrown.",
        'Arrow'
    ],
    [
        "What's black when you get it, red when you use it, and white when you're all through with it?",
        'Charcoal'
    ],
    [
        'What has four legs in the morning, two legs in the afternoon, and three legs in the evening?',
        'Man'
    ], ["Take off my skin, I won't cry, but you will.", 'Onion'],
    ['Hold the tail, while I fish for you.', 'Net'],
    [
        'I am so simple that I can only point. Yet I guide men all over the world.',
        'Compass'
    ], ['Iron roof, glass walls, burns and burns and never falls.', 'Lantern'],
    [
        "Late afternoons I often bathe. I'll soak in water piping hot. My essence goes through. My see through clothes. Used up am I - I've gone to pot.",
        'Teabag'
    ],
    [
        "What can't you see, hear or feel, until its too late. What shadows love, and shopkeepers hate?",
        'Thief'
    ],
    [
        'What can bring back the dead. Make us cry, make us laugh, make us young. Born in an instant yet lasts a life time?',
        'Memory'
    ],
    [
        'I have a neck but no head. I have a body but no arm. I have a bottom but no leg.',
        'Bottle'
    ],
    [
        "A thousand colored folds stretch toward the sky. Atop a tender strand, rising from the land, until killed by maiden's hand. Perhaps a token of love, perhaps to say goodbye.",
        'Flower'
    ],
    [
        'Gold in a leather bag, swinging on a tree, money after honey in its time. Ills of a scurvy crew cured by the sea, reason in its season but no rhyme.',
        'Orange'
    ],
    [
        'A slow, solemn square-dance of warriors feinting. One by one they fall, warriors fainting, thirty-two on sixty-four.',
        'Chess'
    ], ['He has married many women but has never married.', 'Priest'],
    [
        'In your fire you hear me scream, creaking and whining, yet I am dead before you lay me in your hearth.',
        'Log'
    ],
    [
        'I weaken all men for hours each day. I show you strange visions while you are away. I take you by night, by day take you back. None suffer to have me, but do from my lack.',
        'Sleep'
    ],
    [
        'I saw a strange creature. Long, hard, and straight, thrusting into a round, dark opening. Preparing to discharge its load of lives. Puffing and squealing noises accompanied it, then a final screech as it slowed and stopped.',
        'Train'
    ],
    [
        'Large as a mountain, small as a pea, endlessly swimming in a waterless sea.',
        'Asteroid'
    ],
    [
        'I do not breathe, but I run and jump. I do not eat, but I swim and stretch. I do not drink, but I sleep and stand. I do not think, but I grow and play. I do not see, but you see me everyday.',
        'Leg'
    ],
    [
        'When liquid splashes me, none seeps through. When I am moved a lot, liquid I spew. When I am hit, color I change. And color, I come in quite a range. What I cover is very complex, and I am very easy to flex.',
        'Skin'
    ],
    ['Give it food and it will live, give it water and it will die.', 'Fire'],
    ['A nut cracker up in a tree.', 'Squirrel'],
    [
        'What happens every second, minute, month, and century. But not every hour, week, year, or decade?',
        'N'
    ],
    [
        'It has no top or bottom, but it can hold flesh, bones, and blood all at the same time.',
        'Ring'
    ],
    [
        'I am free for the taking. Through all of your life, though given but once at birth. I am less than nothing in weight, but will fell the strongest of you if held.',
        'Breath'
    ],
    [
        'My first is in blood and also in battle. My second is in acorn, oak, and apple. My third and fourth are both the same. In the center of sorrow and twice in refrain. My fifth starts eternity ending here. My last is the first of last, Oh Dear.',
        'Barrel'
    ],
    [
        "When I'm metal or wood, I help you get home. When I'm flesh and I'm blood. In the darkness I roam.",
        'Bat'
    ],
    [
        'I march before armies, a thousand salute me. My fall can bring victory, but no one would shoot me. The wind is my lover, one-legged am I. Name me and see me at home in the sky.',
        'Flag'
    ],
    [
        'Tool of thief, toy of queen. Always used to be unseen. Sign of joy, sign of sorrow. Giving all likeness borrowed.',
        'Mask'
    ],
    [
        'What five-letter word becomes shorter when you add two more letters?',
        'Short'
    ],
    [
        'What is pronounced like one letter, written with three letters. And belongs to all animals?',
        'Eye'
    ],
    ["What is it that given one, you'll have either two or none?", 'Choice'],
    [
        "It is greater than God and more evil than the devil. The poor have it, the rich need it, and if you eat it you'll die.",
        'Nothing'
    ], ['What gets bigger the more you take away from it?', 'Hole'],
    ['The more of it there is, the less you see.', 'Darkness'],
    [
        "To cross the water I'm the way, for water I'm above. I touch it not and, truth to say, I neither swim nor move.",
        'Bridge'
    ],
    [
        "As beautiful as the setting sun, as delicate as the morning dew. An angel's dusting from the stars. That can turn the Earth into a frosted moon.",
        'Snow'
    ],
    [
        'When set loose I fly away. Never so cursed as when I go astray.',
        'Fart'
    ], ['How far will a blind dog walk into a forest?', 'Halfway'],
    [
        'My first is in wield, sever bones and marrow. My second is in blade, forged in cold steel. My third is an arbalest, and also in arrows. My fourth is in power, plunged through a shield. My fifth is in honor, and also in vows. My last will put an end to it all.',
        'Weapon'
    ],
    [
        'Face with a tree, skin like the sea. A great beast I am. Yet vermin frightens me.',
        'Elephant'
    ],
    [
        'I sleep by day, I fly by night. I have no feathers to aid my flight.',
        'Bat'
    ],
    [
        "I am mother and father, but never birth or nurse. I'm rarely still, but I never wander.",
        'Tree'
    ], ['What goes in the water red, and comes out black?', 'Iron'],
    [
        'Grows from the ground, bushes and grass, leaves of yellow, red and brow, unruly plants, get the axe, trim the hedge back down.',
        'Hair'
    ], ['What can touch someone once and last them a life time?', 'Love'],
    [
        'A dragons tooth in a mortals hand, I kill, I maim, I divide the land.',
        'Sword'
    ],
    [
        "You will find me with four legs, but no hair. People ride me for hours, but I don't go anywhere without needing to be tugged. Jerked or turned on, I always manage to be ready for work.",
        'Desk'
    ], ['No sooner spoken than broken.', 'Silence'],
    [
        'Though desert men once called me God, today men call me mad. For I wag my tail when I am angry. And growl when I am glad.',
        'Cat'
    ],
    [
        'An open ended barrel, it is shaped like a hive. It is filled with the flesh, and the flesh is alive.',
        'Thimble'
    ], ['What kind of pet always stays on the floor?', 'Carpet'],
    [
        'What flies without wings? What passes all things? What mends all sorrow? What brings the morrow?',
        'Time'
    ], ['What has a neck and no head, two arms but no hands?', 'Shirt'],
    [
        'Two in a corner, one in a room, none in a house, but one in a shelter.',
        'R'
    ], ['What does no man want, yet no man want to lose?', 'Work'],
    [
        'I am the heart that does not beat. If cut, I bleed without blood. I can fly, but have no wings. I can float, but have no fins. I can sing, but have no mouth.',
        'Wood'
    ],
    [
        'Weight in my belly, trees on my back, nails in my ribs, feet I do lack.',
        'Boat'
    ], ['What is that over the head and under the hat?', 'Hair'],
    ['I bind it and it walks. I loose it and it stops.', 'Sandal'],
    [
        "My voice is tender, my waist is slender and I'm often invited to play. Yet wherever I go, I must take my bow or else I have nothing to say.",
        'Violin'
    ],
    [
        "Lovely and round, I shine with pale light, grown in the darkness, a lady's delight.",
        'Pearl'
    ],
    [
        "The strangest creature you'll ever find has two eyes in front and a hundred behind.",
        'Peacock'
    ],
    [
        'A little pool with two layers of wall around it. One white and soft and the other dark and hard. Amidst a light brown grassy lawn with an outline of a green grass.',
        'Coconut'
    ],
    [
        "I open wide and tight I shut, Sharp am I and paper-cut fingers too, so do take care, I'm good and bad, so best beware.",
        "Scissors"
    ],
    [
        'Only one color, but not one size. Stuck at the bottom, yet easily flies. Present in sun, but not in rain. Doing no harm, and feeling no pain.',
        'Shadow'
    ],
    [
        'A house of wood in a hidden place. Built without nails or glue. High above the earthen ground. It holds pale gems of blue.',
        'Nest'
    ],
    [
        'Who spends the day at the window, goes to the table for meals. And hides at night?',
        'Fly'
    ],
    [
        'The beginning of eternity, the end of time and space, the beginning of every end, the end of every place.',
        'E'
    ],
    [
        'Always old, sometimes new. Never sad, sometimes blue. Never empty, sometimes full. Never pushes, always pulls.',
        'Moon'
    ],
    [
        "I bubble and laugh and spit water in your face. I am no lady, and I don't wear lace.",
        'Fountain'
    ],
    [
        'My teeth are sharp, my back is straight, to cut things up it is my fate.',
        'Saw'
    ],
    [
        'I love to dance and twist and prance. I shake my tail, as away I sail. Wingless I fly into the sky.',
        'Kite'
    ],
    [
        'I usually wear a yellow coat. I usually have a dark head. I make marks wherever I go.',
        'Pencil'
    ],
    [
        "My life is often a volume of grief, your help is needed to turn a new leaf. Stiff is my spine and my body is pale. But I'm always ready to tell a tale.",
        'Book'
    ],
    [
        'I cost no money to use, or conscious effort to take part of. And as far as you can see, there is nothing to me. But without me, you are dead.',
        'Air'
    ],
    [
        'Soldiers line up spaced with pride. Two long rows lined side by side. One sole unit can decide, if the rows will unit or divide.',
        'Zipper'
    ], ['What measures out time. Until in time all is smashed to it?', 'Sand'],
    [
        'I turn around once. What is out will not get in. I turn around again. What is in will not get out.',
        'Key'
    ],
    ['Who is he that runs without a leg. And his house on his back?', 'Snail'],
    [
        'When the day after tomorrow is yesterday. Today will be as far from Wednesday. As today was from Wednesday. When the day before yesterday was tomorrow. What is the day after this day?',
        'Thursday'
    ],
    [
        'What has roots as nobody sees, is taller than trees. Up, up it goes, and yet never grows?',
        'Mountain'
    ], ['Come up and let us go. Go down and here we stay.', 'Anchor'],
    [
        'They have not flesh, nor feathers, nor scales, nor bone. Yet they have fingers and thumbs of their own.',
        'Gloves'
    ],
    [
        'Long slim and slender. Dark as homemade thunder. Keen eyes and peaked nose. Scares the Devil wherever it goes.',
        'Snake'
    ], ['What is put on a table, cut, but never eaten?', 'Deck'],
    ['The sharp slim blade, that cuts the wind.', 'Grass'],
    [
        '"Although my cow is dead, I still beat her\x85 What a racket she makes."',
        'Drum'
    ],
    [
        'It sat upon a willow tree, and sang softly unto me. Easing my pain and sorrow with its song. I wished to fly, but tarried long. And in my suffering, the willow was like a cool clear spring. What was it that helped me so? To spend my time in my woe.',
        'Bird'
    ],
    [
        'I have four wings but cannot fly. I never laugh and never cry. On the same spot always found, toiling away with little sound.',
        'Windmill'
    ],
    [
        "I am never quite what I appear to be. Straight-forward I seem, but it's only skin deep. For mystery most often lies beneath my simple speech. Sharpen your wits, open your eyes, look beyond my exteriors, read me backwards, forwards, upside down. Think and answer the question...What am I?",
        'Riddle'
    ],
    [
        'All about the house, with his lady he dances, yet he always works, and never romances.',
        'Broom'
    ],
    [
        "I walked and walked and at last I got it. I didn't want it. So I stopped and looked for it. When I found it, I threw it away.",
        'Thorn'
    ],
    [
        "Two in a whole and four in a pair. And six in a trio you see. And eight's a quartet but what you must get. Is the name that fits just one of me?",
        'Half'
    ], ['I drive men mad for love of me. Easily beaten, never free.', 'Gold'],
    [
        'I go around in circles, but always straight ahead. Never complain, no matter where I am led.',
        'Wheel'
    ],
    [
        'You use a knife to slice my head. And weep beside me when I am dead.',
        'Onion'
    ],
    [
        'Turns us on our backs, and open up our stomachs. You will be the wisest of men though at start a lummox.',
        'Books'
    ],
    [
        'Thousands lay up gold within this house. But no man made it. Spears past counting guard this house, but no man wards it.',
        'Beehive'
    ], ['What goes around the world and stays in a corner?', 'Stamp'],
    ['What has to be broken before it can be used?', 'Egg'],
    [
        '"Creatures of power, creatures of grade, creatures of beauty, creatures of strength. As for their lives, they set everything\'s pace. For all things must come to live. Under their emerald embrace\x85Either in their life or in their death."',
        'Trees'
    ],
    [
        "Double my number, I'm less than a score. Half of my number is less than four. Add one to my double when bakers are near. Days of the week are still greater, I fear.",
        'Six'
    ],
    [
        'In buckles or lace, they help set the pace. The farther you go, the thinner they grow.',
        'Shoes'
    ],
    [
        'When young, I am sweet in the sun. When middle-aged, I make you gay. When old, I am valued more than ever.',
        'Wine'
    ], ["Forward I'm heavy, but backwards I'm not.", 'Ton'],
    [
        "Hard to catch, easy to hold. Can't be seen, unless it's cold.",
        'Breath'
    ],
    [
        'I am two-faced but bear only one. I have no legs but travel widely. Men spill much blood over me. Kings leave their imprint on me. I have greatest power when given away, yet lust for me keeps me locked away.',
        'Coin'
    ],
    [
        'Two little holes in the side of a hill. Just as you come to the cherry-red mill.',
        'Nose'
    ],
    [
        'When you stop and look, you can always see me. If you try to touch, you cannot feel me. I cannot move, but as you near me, I will move away from you.',
        'Horizon'
    ],
    [
        "A dagger thrust at my own heart, dictates the way I'm swayed. Left I stand, and right I yield, to the twisting of the blade.",
        'Lock'
    ],
    [
        'What instrument can make any sound and be heart, but not touched or seen?',
        'Voice'
    ], ['What goes further the slower it goes?', 'Money'],
    [
        'I can run but not walk. Wherever I go, thought follows close behind.',
        'Nose'
    ],
    [
        'Used left or right, I get to travel over cobblestone or gravel. Used up, I vie for sweet success, used down, I cause men great duress.',
        'Thumb'
    ],
    [
        'What goes through the door without pinching itself? What sits on the stove without burning itself? What sits on the table and is not ashamed?',
        'Sun'
    ],
    [
        'The moon is my father. The sea is my mother. I have a million brothers. I die when I reach land.',
        'Wave'
    ], ['What always goes to bed with his shoes on?', 'Horse'],
    [
        'My thunder comes before the lightning. My lightning comes before the clouds. My rain dries all the land it touches.',
        'Volcano'
    ],
    [
        'My love, when I gaze on thy beautiful face. Careering along, yet always in place, the thought has often come into my mind. If I ever shall see thy glorious behind.',
        'Moon'
    ], ["What starts with a 'T', ends with a 'T', and has T in it?", 'Teapot'],
    [
        'Today he is there to trip you up. And he will torture you tomorrow. Yet he is also there to ease the pain, when you are lost in grief and sorrow.',
        'Alcohol'
    ],
    [
        "I can be moved. I can be rolled. But nothing will I hold. I'm red and I'm blue, and I can be other colors too. Having no head, though similar in shape. I have no eyes - yet move all over the place.",
        'Ball'
    ],
    [
        "Inside a burning house, this thing is best to make. And best to make it quickly, before the fire's too much to take.",
        'Haste'
    ],
    [
        "What is round as a dishpan, deep as a tub, and still the oceans couldn't fill it up?",
        'Sieve'
    ],
    [
        "My first is in some but not in all. My second is into but not in tall. My third in little but no in big. My fourth in port but not in pig. My whole is made in nature's way. For clothing, rugs used every day.",
        'Silk'
    ],
    [
        'Gets rid of bad ones, short and tall. Tightens when used, one size fits all.',
        'Noose'
    ], ['What gets wetter the more it dries.', 'Towel'],
    ['A little house full of meat, no door to go in and eat.', 'Nut'],
    [
        "A beggar's brother went out to sea and drowned. But the man who drowned had no brother. Who was the beggar to the man who drowned?",
        'Sister'
    ],
    [
        'I can be written, I can be spoken, I can be exposed, I can be broken.',
        'News'
    ],
    [
        'A horrid monster hides from the day, with many legs and many eyes. With silver chains it catches prey. And eats it all before it dies. Yet in every cottage does it stay. And every castle beneath the sky.',
        'Spider'
    ],
    [
        'Five hundred begins it, five hundred ends it. Five in the middle is seen. First of all figures, the first of all letters. Take up their stations between. Join all together, and then you will bring before you the name of an eminent king.',
        'David'
    ],
    [
        "Tall in the morning, short at noon, gone at night. But I'll be back soon.",
        'Shadow'
    ], ['In the night a mountain, in the morning a meadow.', 'Bed'],
    ['What can be heard and caught but never seen?', 'Remark'],
    [
        'I can sizzle like bacon, I am made with an egg. I have plenty of backbone, but lack a good leg. I peel layers like onions, but still remain whole. I can be long, like a flagpole, yet fit in a hole.',
        'Snake'
    ],
    [
        'If a man carried my burden, he would break his back. I am not rich, but leave silver in my track.',
        'Snail'
    ],
    [
        'High born, my touch is gentle. Purest white is my lace. Silence is my kingdom. Green is the color of my death.',
        'Snow'
    ],
    [
        'You heard me before, yet you hear me again, then I die. Until you call me again.',
        'Echo'
    ], ['What wears a coat in the winter and pants in the summer?', 'Dog'],
    [
        "I'm not really more than holes tied to more holes. I'm strong as good steel, though not as stiff as a pole.",
        'Chain'
    ],
    [
        "I am the third from a sparkle bright, I thrive throughout the day and night. Deep in the path of a cows white drink. I've had thousands of millions of years to think. But one of my creatures is killing me. And so the question I ask to thee, is who am I?",
        'Earth'
    ], ['Up on high I wave away but not a word can I say.', 'Flag'],
    [
        'I am whole but incomplete. I have no eyes, yet I see. You can see, and see right through me. My largest part is one fourth of what I once was.',
        'Skeleton'
    ],
    [
        "They're up near the sky, on something very tall. Sometimes they die, only then do they fall.",
        'Leaves'
    ],
    [
        "Toss me out of the window. You'll find a grieving wife. Pull me back but through the door, and watch someone give life.",
        'N'
    ],
    [
        "A time when they're green. A time when they're brown. But both of these times, cause me to frown. But just in between, for a very short while. They're perfect and yellow. And cause me to smile.",
        'Bananas'
    ],
    [
        'I build up castles. I tear down mountains. I make some men blind. I help others to see.',
        'Sand'
    ],
    [
        'Round as a button, deep as a well. If you want me to talk, you must first pull my tail.',
        'Bell'
    ],
    [
        'A house with two occupants, sometimes one, rarely three. Break the walls, eat the boarders, then throw away me.',
        'Peanut'
    ],
    [
        'My first master has four legs, my second master has two. My first I serve in life, my second I serve in death. Tough I am, yet soft beside. Against ladies cheeks I often reside.',
        'Fur'
    ],
    [
        'I have one eye. See near and far. I hold the moments you treasure and the things that make you weep.',
        'Camera'
    ],
    [
        'There are two meanings to me. With one I may need to be broken, with the other I hold on. My favorite characteristic is my charming dimple.',
        'Tie'
    ],
    [
        'With sharp edged wit and pointed poise. It can settle disputes without making a noise.',
        'Sword'
    ],
    [
        'Lighter than what I am made of, more of me is hidden than is seen. I am the bane of the mariner. A tooth within the sea.',
        'Iceberg'
    ],
    [
        'I have one, you have one. If you remove the first letter, a bit remains. If you remove the second, bit still remains. If you remove the third, it still remains.',
        'Habit'
    ],
    [
        "Kings and queens may cling to power. And the jester's got his call. But, as you may all discover. The common one outranks them all.",
        'Ace'
    ],
    [
        'Glittering points that downward thrust. Sparkling spears that never rust.',
        'Icicles'
    ],
    [
        'My first is in fish but no in snail. My second is in rabbit but no in tail. My third is in up but not in down. My fourth is in tiara but not in crown. My fifth is in tree you plainly see. My whole a food for you and me.',
        'Fruit'
    ],
    [
        'What I am filled, I can point the way. When I am empty. Nothing moves me. I have two skins. One without and one within.',
        'Gloves'
    ],
    [
        "My first is in window but not in pane. My second's in road but not in lane. My third is in oval but not in round. My fourth is in hearing but not in sound. My whole is known as a sign of peace. And from noah's ark won quick release.",
        'Dove'
    ],
    [
        "If you drop me I'm sure to crack. But give me a smile and I'll always smile back.",
        'Mirror'
    ],
    [
        'I make you weak at the worst of all times. I keep you safe, I keep you fine. I make your hands sweat. And your heart grow cold. I visit the weak, but seldom the bold.',
        'Fear'
    ],
    [
        'I run through hills. I veer around mountains. I leap over rivers. And crawl through the forests. Step out your door to find me.',
        'Road'
    ]
]

update()
os.system('clear')

while True:
    update()
    display()
    #inp = input('left,right,up or down? (wasd)')
    inp = getch.__call__()
    if inp == 'g':
        break
    parseInput(inp, 'none')

    os.system('clear')

print('SCORE:', score[0])
