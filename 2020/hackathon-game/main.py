import random
import time
import sys
import os


# from PIL import Image

def cls():
    os.system('clear')



class Char():
    def __init__(self):
        self.mults = []
        self.cities = []
        self.conquests = []
        self.soldierbonus= 1
        self.bonce = True
        self.eonce = True
        self.barracksevery = 0
        self.soldiers= 100
        self.enemychance = 0
        self.blastfurnace = False
        self.armory = False
        self.foodbonus = 0
        self.waterbonus = 0
        self.ironbonus = 0
        self.coalbonus = 0
        self.woodbonus = 0
        self.n = 1
        self.wood = 100
        self.iron = 20
        self.coal = 20
        self.steel = 0
        self.iron_farms= 0
        self.coal_farms = 0
        self.wood_farms = 0
        self.mult3 = 0
        self.mult = 0
        self.mult2 = 0
        self.on = True
        self.ab = 1
        self.once  = True
        self.tcount = 0
        self.icount= 0
        self.ccount = 0
        a = 1
        b = 1

        self.name = input('What do you want to call your species? (a - z only) the...\n')
        print('the world will soon fear the might of the',self.name)
        while b == 1:
            try:
                self.size = int(input('What size? 1-100\n'))  # consumes more energy #means more likly to stay alive
                if self.size > 100:
                        print('too much')
                if self.size < 1:
                        print('too little')
                else:
                        b = 0
            except ValueError:
                b = 1
                print('not a number')
        while a == 1:
            try:
                self.speed = int(input('What speed? 1-100\n'))
                if self.speed > 100:
                    print('too much')
                if self.speed < 1:
                    print('too little')
                else:
                    a = 0
            except ValueError:
                a == 1
                print('not a number')
    
        global energy
        self.v = False
        self.w = False
        self.x = False
        self.attackboost = 0
        self.energy = 100
        self.food = 20
        self.water = 20
        self.charisma = random.randint(1, 100)
        self.score = 0
        self.danger = 0
        self.turns_passed = 0
        self.currency = 10
        self.enemy = 0
        self.mine = 0
        self.baracks = 0
        self.minebought = False
        self.baracksbought = True
        self.popgrowth = 0
        self.quantityofcreatures = 1
        self.battleHP = 0
        self.turns_without_water = 0
        self.turns_without_food = 0
        self.tree_farms = 0
        self.coal_farms = 0
        self.blacksmiths = 0


		
		



    def battle(self):
        print()

    def charismatrac(self):
        self.charisma = ((self.food * 1.25) + (self.water * 1.25) + (self.energy * 0.5) + self.currency / 4)
        if self.charisma >= 100:
            self.charisma = 100
        print('\nyour charisma is', self.charisma,'\n')


    def dangerTrack(self):
        self.danger = (self.charisma) + self.turns_passed
        if self.danger >= 100:
            self.danger = 100

    def getRobbedChance(self):
        z = random.randint(0, 300)
        c = self.currency - random.randint(int(self.currency / 3), int(self.currency / 2))

        if z < self.currency:
            self.currency = self.currency - c
            print('\nYou have been robbed of',c,'money\n')
        if self.currency >= 100:
            self.currency = 100


    def RandomExploreLocations(self):
        self.treasure_location = random.randint(1,4)
        self.treasure = 0
            
    def move(self):

        self.enemychance = random.randint(1,8)
        self.e = []
        for i in self.e:
            print(self.e[i])
            #time.sleep(0.27)
        
        time.sleep(0.5 * self.n)
        
        move = input('up, down, left or right? u,d,l or r')
        self.x = 5
        self.y = 4
        self.prevx = self.x
        self.prevy = self.y
        
        if move == 'r':
            if self.treasure_location == 1:
                self.treasure = 1


        if move == 'l':
            if self.treasure_location == 2:
                self.treasure = 1

        if move == 'u':
            if self.treasure_location == 3:
                self.treasure = 1

        if move == 'd':
            if self.treasure_location == 4:
                self.treasure = 1

        if self.treasure == 1:
            self.treasure_bonus = random.randint(20,50)
            os.system('clear')
            print('You found', self.treasure_bonus, 'money!')
            self.currency += self.treasure_bonus
            time.sleep(self.n*0.5)
        else:
            #time.sleep(1)
            os.system('clear')
            print('\nUnlucky, no treasure this time\n')
            time.sleep(self.n*0.5)

        if self.enemychance == 4:
            pass
            #self.battle()

    def startTurn(self):
        self.turns_passed = self.turns_passed + 1
            # self.currency = self.currency + self.mine MAYBE OTHER BUILDINGS ASWELL
            
            #charismatrac(self)
        
    def event(self):
        self.events = {'There is a food shortage': (10,5,0), 'An enemy sneaks into the camp at night, stealing your food.': (10,0,5), 'The main hunter suffers a crippling injury and cannot hunt.': (20,5,5), 'water shortage': (20,0,10) }
    
        #  if self.energy > 50:
        #      self.events.append('injury': 30)

        if self.energy > 20:

            print()
            self.choice = random.choice(list(self.events))
            print(self.choice)

            self.choice = self.events.get(self.choice)

            self.energy -= self.choice[0]
            self.food -= self.choice[1]
            self.water -= self.choice[2]
            print('-',self.choice[0],'energy')
            print('-',self.choice[1],'food')
            print('-',self.choice[2],'water')
            time.sleep(self.n)

            
                
    def FoodWaterLoss(self):
        self.soldiers += 10 + self.barracksevery
        self.food += self.foodbonus
        self.water += self.waterbonus
        self.food = round(self.food - (self.size * 0.05 + 1))
        self.water = round(self.water - (self.size * 0.05 + 1))
        if self.food >= 100:
            self.food = 100
        if self.food <= 0:
            self.food = 0
        if self.water >= 100:
            self.water = 100
        if self.water <= 0:
            self.water = 0
        if self.energy >= 100:
            self.energy = 100
        if self.energy <= 0:
            self.energy = 0

    def Warner(self):
        if self.energy < 20:
            pass
            # print('You are running low on energy,at:', self.energy,'\n')
        if self.food < 20:
            pass
            #print('You are running low on food, at:', self.food,'\n')
        if self.water < 20:
            pass
            #print('You are running low on water, at:', self.water,)

            

    def townbuild(self):
        if self.once == True:
            self.ic = 0
            self.cc = 0
            self.fc = 0
            message = 'A tiny village'
            
            if self.wood_farms > 0:
                message = 'A small-ish village'
            if self.coal > 50:
                message = 'A prosperous village'
            if self.iron_farms > 0:
                message = 'A mining town'
            if self.steel > 0:
                message = 'An advanced town'
            
            print(message)


            self.town = []
            for i in range(11):
                self.town.append([])
            for i in range (11):
                lm = 0
                for j in range(15):
                    lm += 1
                    if lm > 2 and lm < 14 and i != 5:
                        
                        p = random.randint(1,32)
                    
                        
                        if p > 12 and p < 15:
                            if self.fc < 3:
                                
                                if i < 10:
                                    if j < 13:
                                        self.fc += 1
                                        self.town[i].append('T')

                            elif self.fc > 2:
                                self.town[i].append('.')
                        
                        elif p == 17 or p == 16:
                            if self.cc < 3:
                                
                                if i < 10:
                                    if j < 13:
                                        self.cc += 1
                                        self.town[i].append('C')
                            
                            elif self.cc > 2:
                                self.town[i].append('.')
                        
                        elif p > 17 and p < 20:
                            if self.ic < 3:
                                
                                if i < 10:
                                    if j < 13:
                                        self.ic += 1
                                        self.town[i].append('I')
                                    
                            elif self.ic > 2:
                                self.town[i].append('.')
                        else: 

                            self.town[i].append('.')

                    else:

                        self.town[i].append('.')


        
            self.once = False




            
            

        

        print('H is your home, B is a blacksmith, F is a farmer','C is a coal deposit, I is an iron deposit','T is forest')
        self.town[5][7] = 'H'



        
        
        for i in self.town:
            print( ' '.join(map(str, i)))
        
        if self.on == True:
            self.tr = []
            self.co = []
            self.ir = []

        for i in range(0,14):
            for j in range(0,11):
            
                if self.town[j][i] == 'T':
                    self.tr.append([j,i])
                    
                    
                if self.town[j][i] == 'C':
                
                    self.co.append([j,i])
                
                if self.town[j][i] == 'I':
                
                    self.ir.append([j,i])
        
        self.on = False
        
        '''
        for i in self.tr:
            
            if i[0] == 14:
            self.tr.remove([])
            self.town[i[0]][i[1]] = '.'
            i[0] = random.randint(1,13)
            self.town[i[0]][i[1]] = 'T'

            
            if i[1] == 10:
            self.town[i[0]][i[1]] = '.'
            i[0] = random.randint(1,9)
            self.town[i[0]][i[1]] = 'T'

        
        for i in self.co:
            
            if i[0] == 14:
            
            self.town[i[0]][i[1]] = '.'
            i[0] = random.randint(1,13)
            self.town[i[0]][i[1]] = 'C'
            if i[1] == 10:
            self.town[i[0]][i[1]] = '.'
            i[0] = random.randint(1,9)
            self.town[i[0]][i[1]] = 'C'

        for i in self.ir:
            
            if i[0] == 14:
            
            self.town[i[0]][i[1]] = '.'
            i[0] = random.randint(1,13)
            self.town[i[0]][i[1]] = 'I'

            if i[1] == 10:
            self.town[i[0]][i[1]] = '.'
            i[0] = random.randint(1,9)
            self.town[i[0]][i[1]] = 'I'
        '''

        
        


        
        self.ccount = 0
        self.icount = 0
        self.tcount = 0
        self.on = False
        for i in self.town:
            self.ccount += i.count('C')
            self.icount += i.count('I')
            self.tcount += i.count('T')
        print('There are',self.ccount,'unused coal deposits')
        print('There are',self.icount,'unused iron deposits')
        print('There are',self.tcount,'unused tree deposits\n')
        time.sleep(self.n)

        actions = {'establish a tree farm on one of your deposits (tree farm)':(10,10,0),'establish a coal farm on one of your deposits (coal farm)':(500,10,0),'establish an iron farm on one of your deposits (iron farm)':(1000,500,10)}

        actions2 = {'Establish an armory on a blank space (armory)':(1500,500,100),'Establish a steel-making blast furnace (furnace)':(2000,1000,500),'Establish a barracks (barracks)':(1000,500,50)}

        actions3 = {'Upgrade a wood farm (upgrade wood farm)':(550,50,0),'Upgrade a coal farm (upgrade coal farm)':(1500,50,10),'Upgrade an iron farm (upgrade iron farm)':(2000,50,50)}

        actions4 = {'Create a canal going to the town, providing water (canal)':(1500,500,50),'Create a farm in the town, providing food (farm)':(1000,0,100)}
        l = 0
        
        print('type in the word/s in the brackets')
        for i in actions:
            l += 1
            c = actions.get(i)

            print(l,i, '(' + str(c[0]),'wood,', c[1],'coal,' + str(c[2]),'iron)')
            time.sleep(0.05 * self.n)
        
        
        if self.iron >= 100 or self.v== True:
            self.v = True  
            for i in actions2:
                l += 1
                c = actions2.get(i)
                print(l,i, '(' + str(c[0]),'wood,', c[1],'coal,' + str(c[2]),'iron)')
                time.sleep(0.05 * self.n)
        if self.coal >= 50 or self.w == True:
            self.w = True
            for i in actions3:
                l += 1
                c = actions3.get(i)
                print(l,i, '(' + str(c[0]),'wood,', c[1],'coal,' + str(c[2]),'iron)')
                time.sleep(0.05 * self.n)
        
        if self.woodbonus >= 0 or self.x == True:
            self.x = True
            for i in actions4:

                l += 1
                c = actions4.get(i)
                print(l,i, '(' + str(c[0]),'wood,', c[1],'coal,' + str(c[2]),'iron)')
                time.sleep(0.05 * self.n)
            
            
        self.c = input('What do you want to order your tribe to do?')

        if self.c == 'tree farm':
            if self.wood >= 10:
                if self.coal >= 10:
                    print('you build a tree farm.')
                    self.wood_farms += 1
                    #print(self.tr)
                    a = self.tr[0+self.mult][1]
                    b = self.tr[0+self.mult][0]
                
                    #print(self.tr)
                    self.town[b][a] = 'L'
                    self.mult += 1
                    self.wood -= 10
        if self.c == 'coal farm':
            if self.wood >= 500:
                if self.coal >= 10:
                    self.wood -= 500
                    self.coal -= 10
                    print('you build a coal farm.')
                    self.coal_farms += 1 
                    #print(self.co)
                    a = self.co[0+self.mult2][1]
                    b = self.co[0+self.mult2][0]
                
                    #print(self.tr)
                    self.town[b][a] = 'M'
                    self.mult2 += 1      
        if self.c == 'iron farm':
            if self.wood >= 1000:
                if self.coal >= 500:
                    self.wood -= 1000
                    self.coal -= 500
                    print('you build an iron farm.')
                    self.iron_farms += 1 
                    #print(self.ir)
                    a = self.ir[0+self.mult2][1]
                    b = self.ir[0+self.mult2][0]
                
                    #print(self.tr)
                    self.town[b][a] = 'B'
                    self.mult3 += 1 

        if self.c == 'armory':
            if self.wood >= 1500:
                if self.coal >= 500:
                    self.wood -= 1500
                    self.coal -= 500
                    print('you build an armory.')
                    self.armory = True
                    #print(self.ir)
                    a = int(input('what x coordinate?'))
                    b = int(input('what y coordinate?'))
                
                    #print(self.tr)
                    self.town[b-1][a-1] = 'A'
                    

        if self.c == 'upgrade wood farm':
            if self.wood >= 550:
                if self.coal >= 50:
                    self.wood -= 550
                    self.coal -= 50
                    self.woodbonus += 50
                    print('you upgrade a tree farm')
        if self.c == 'upgrade coal farm':
            if self.iron > 10:
                if self.wood >= 1500:
                    if self.coal >= 50:
                        self.wood -= 1500
                        self.coal -= 50
                        self.iron -= 10
                        self.coalbonus += 50
                        print('you upgrade a coal farm')
        if self.c == 'upgrade iron farm':
            if self.iron > 50:
                if self.wood >= 2000:
                    if self.coal >= 50:
                        self.wood -= 2000
                        self.coal -= 50
                        self.iron -= 50
                        self.ironbonus += 50
                        print('you upgrade an iron farm')
        
        if self.c == 'canal':
            if self.wood >= 1500:
                if self.coal >= 500:
                    self.wood -= 1500
                    self.coal -= 500
                    print('you build a canal. 10 water every turn.')
                    self.waterbonus += 10
            
                    #print(self.ir)
                    a = int(input('what x coordinate?'))
                    b = int(input('what y coordinate?'))
                
                    #print(self.tr)
                    self.town[b-1][a-1] = 'W'
        if self.c == '999':
            self.wood += 100000
            self.iron += 100000
            self.coal += 100000
            self.currency += 100000
            self.food += 1000
            self.water += 1000

            print('Hello fellow game developer')
        if self.c == 'farm':
            if self.wood >= 1000:
                if self.iron >= 100:
                    self.wood -= 1000
                    self.foodbonus += 10
                    self.iron -= 100
                    print('you build a farm. 10 food every turn.')
            
                    #print(self.ir)
                    a = int(input('what x coordinate?'))
                    b = int(input('what y coordinate?'))
                
                    #print(self.tr)
                    self.town[b-1][a-1] = 'F'
        
        if self.c == 'furnace':
            if self.iron >= 500:
                if self.wood >= 2000:
                    if self.coal >= 1000:
                        self.wood -= 2000
                        self.iron -= 500
                        self.coal -= 1000
                        self.blastfurnace = True
                        print('you build a blast furnace.')
                        a = int(input('what x coordinate?'))
                        b = int(input('what y coordinate?'))
                    
                        #print(self.tr)
                        self.town[b-1][a-1] = 'S'
        if self.c == 'barracks':
            if self.iron >= 50:
                if self.wood >= 1000:
                    if self.coal >= 500:
                        self.wood -= 1000
                        self.iron -= 50
                        self.coal -= 500
                        
                        print('you build a barracks .')
                        self.barracksevery += 15
                        a = int(input('what x coordinate?'))
                        b = int(input('what y coordinate?'))
                    
                        #print(self.tr)
                        self.town[b-1][a-1] = 'B'    
                            
                        

            
    def foreignpower(self):
        
        if self.eonce == True:

            print('An enemy settlement')
            self.efc = 0 
            self.eic = 0
            self.ecc = 0
            self.er = random.randint(6,10)
            self.etown = []
            self.etown.append([])
            for i in range(self.er):
                self.etown.append([])
            for i in range (self.er):
                lm = 0
                for j in range(self.er):
                    lm += 1
                    if i!= 95:
                        
                        p = random.randint(1,72)
                    
                        
                        if p > 12 and p < 15:
                            if self.efc < 3:
                                
                                if i < 10:
                                    if j < 13:
                                        self.efc += 1
                                        self.etown[i].append('T')

                            elif self.efc > 2:
                                self.etown[i].append('.')
                        
                        elif p == 17 or p == 16:
                            if self.ecc < 3:
                                
                                if i < 10:
                                    if j < 13:
                                        self.ecc += 1
                                        self.etown[i].append('C')
                            
                            elif self.ecc > 2:
                                self.etown[i].append('.')
                        
                        elif p > 17 and p < 20:
                            if self.eic < 3:
                                
                                if i < 10:
                                    if j < 13:
                                        self.eic += 1
                                        self.etown[i].append('I')
                                    
                            elif self.eic > 2:
                                self.etown[i].append('.')
                        else: 

                            self.etown[i].append('.')

                    else:

                        self.etown[i].append('.')


        
            self.eonce = False




            
            
        

        
    
    def attackenemy(self):
        self.esoldbonus = 1

        self.on = True
        self.units = []
        self.uc = []
        print('enemy town')
        for i in self.etown:
            print( ' '.join(map(str, i)))
        if self.bonce == True:
            self.battlefield = []
            for i in range(10):
                self.battlefield.append([])
            for i in self.battlefield:
                for j in range(10):
                    i.append('...')

        
        
        print('you have',round(self.soldiers/10),'units.')
        z = round(self.soldiers / 10)
        for i in range(z):
            self.units.append(str(i))
        print(self.units)
        self.ren = random.randint(3,len(self.units)-2)
        self.euc = []
        
        for i in range(self.ren):
            rx = random.randint(0,9)
            ry = random.randint(5,9)
            m = 'E'+str(i+1)
            if i < 10:
                m += '.'
            self.euc.append([ry,rx])

            self.battlefield[ry][rx] = m

        print('battlefield')
        for i in self.battlefield:
            print( ' '.join(map(str, i)))
        print('you have',self.soldiers/10,'units')
        for i in range(len(self.units)):
            print('place unit',i+1)
            xlist = [1,2,3,4,5,6,7,8,9,10]
            x = 99
            y = 99 
            ylist = [1,2,3,4,5]
            
            while x not in xlist:
                try:
                    x = int(input('what x coordinate (1-10)'))
                except ValueError:
                    print('incorrect input')
                
            while y not in ylist:
                try:
                    y = int(input('what y coordinate (1-5)'))
                except ValueError:
                    print('incorrect input')
            x -= 1
            y -= 1
            self.uc.append([y,x])
            m = 'U'+str(i+1)
            if i < 10:
                m += '.'
            
            self.battlefield[y][x] = m
            for i in self.battlefield:
                print( ' '.join(map(str, i)))
    
        print(self.uc)
        while self.on == True:
            v = 0
            vv = 0
            for i in self.battlefield:
                
                for j in range(20):
                    m1 = 'E'+str(j)+'.'
                    m1 = m1.replace(' ','')
                    mm = 'U'+str(j)+'.'
                    mm = mm.replace(' ','')
                    v += i.count(m1)
                    vv += i.count(mm)
                    m1 = 'E'+str(j)
                    m1 = m1.replace(' ','')
                    mm = 'U'+str(j)
                    mm = mm.replace(' ','')
                    v += i.count(m1)
                    vv += i.count(mm)

            print('you have',vv,'soldiers')
            print('there are', v, 'enemies')
            if v == 0:
                print('You win! the new lands are now yours. Access them by pressing the see empire option.')
                self.cities.append(self.etown)
                self.score += 1250
                self.eonce = True

                break
            if vv == 0:
                print('You and a few weary soldiers trudge back to the settlement.')
                break
            

            for i in range(10):
                for j in range(10):
                    if 'E' in self.battlefield[i][j]:
                        ppp = self.battlefield[i][j]
                        self.battlefield[i][j] = '...'
                        yplus = random.randint(-1,1)
                        xplus = 0
                        if yplus == 0:
                            xplus = random.randint(-1,1)

                        if 'U' in self.battlefield[i+yplus][j+xplus]:
                            xx = random.randint(0,(self.soldierbonus+self.esoldbonus)*100)/100
                            print(xx)
                            if xx >= self.soldierbonus:
                                self.battlefield[i+yplus][j+xplus] = ppp
                            
                            break
                        elif i+yplus < 0 or i+yplus > 9 :
                            self.battlefield[i][j] =ppp
                            break
                        elif j+xplus < 0 or j + xplus > 9:
                            self.battlefield[i][j] = ppp
                            break
                        else:
                            self.battlefield[i+yplus][j+xplus] = ppp
                            break



                            
                    
                                



            mo = int(input('1. leave \n2. move a unit forward\n3. Move a unit left\n4. Move a unit right'))
            if mo == 1:
                self.on = False
            if mo == 2:
                x = int(input('what unit number do you want to move forward?'))
                self.battlefield[self.uc[x-1][0]][self.uc[x-1][1]] = '...'
                m = 'U'+str(x)
                if x < 10:
                    m += '.'

                self.uc[x-1][0] += 1
                if 'E' in self.battlefield[self.uc[x-1][0]][self.uc[x-1][1]]:
                    xx = random.randint(0,(self.soldierbonus+self.esoldbonus)*100)/100
                    print(xx)
                    if xx <= self.soldierbonus:
                        self.battlefield[self.uc[x-1][0]][self.uc[x-1][1]] = m
                    


                else:
                    self.battlefield[self.uc[x-1][0]][self.uc[x-1][1]] = m

                for i in self.battlefield:
                    print( ' '.join(map(str, i)))
            if mo == 3:
                x = int(input('what unit number do you want to move left?'))
                self.battlefield[self.uc[x-1][0]][self.uc[x-1][1]] = '...'
                m = 'U'+str(x)
                if x < 10:
                    m += '.'

                self.uc[x-1][1] -= 1

                self.battlefield[self.uc[x-1][0]][self.uc[x-1][1]] = m
                for i in self.battlefield:
                    print( ' '.join(map(str, i)))
            if mo == 4:
                x = int(input('what unit number do you want to move right?'))
                self.battlefield[self.uc[x-1][0]][self.uc[x-1][1]] = '...'
                m = 'U'+str(x)
                if x < 10:
                    m += '.'

                self.uc[x-1][1] += 1

                self.battlefield[self.uc[x-1][0]][self.uc[x-1][1]] = m
                for i in self.battlefield:
                    print( ' '.join(map(str, i)))
                
                
            
    def enemytownuse(self):
        
        self.ec = []
        if self.etown not in self.cities:
            self.mults.append([0,0,0])

            self.cities.append(self.etown)
        
        for i in range(len(self.cities)):
            self.ec.append([])
            
            for i in self.cities[i]:
                
                print(' '.join(map(str, i)))
                
                
        w = int(input('which enemy town? 1,2,3 etc.'))
        tt=0
        ct = 0
        it = 0
        for i in self.cities[w-1]:
            tt += i.count('T')
            ct += i.count('C')
            it += i.count('I')
            


        
        self.ec[w-1].append(tt)
        self.ec[w-1].append(ct)
        self.ec[w-1].append(it)
        print(self.ec)
        self.etcc = []
        self.eicc = []
        self.eccc = []
        
        for h in range(self.er):
            for i in range(self.er):
                if self.cities[w-1][h][i] == 'T':
                    
                    self.etcc.append([i,h])
                if self.cities[w-1][h][i] == 'C':
                    
                    self.eccc.append([i,h])

                if self.cities[w-1][h][i] == 'I':
                    
                    self.eicc.append([i,h])


        
        



        print('There are',self.ec[w-1][1],'unused coal deposits')
        print('There are',self.ec[w-1][2],'unused iron deposits')
        print('There are',self.ec[w-1][0],'unused tree deposits\n')
        actions = {'establish a tree farm on one of the deposits (tree farm)':(10,10,0),'establish a coal farm on one of the deposits (coal farm)':(500,10,0),'establish an iron farm on one of the deposits (iron farm)':(1000,500,10)}
        l = 0
        for i in actions:
            l += 1
            c = actions.get(i)

            print(l,i, '(' + str(c[0]),'wood,', c[1],'coal,' + str(c[2]),'iron)')
            time.sleep(0.05 * self.n)
        self.c = input('What do you want to do?')
        
        if self.c == 'tree farm':
            if self.wood >= 10:
                if self.coal >= 10:
                    print('you build a tree farm.')
                    self.wood -= 10
                    self.wood_farms += 1
                    '''
                    a = self.etcc[0+self.mults[w-1][0]]
                    b = self.etcc[0+self.mults[w-1][0]]
                    
                    #print(self.tr)
                    self.cities[w-1][b][a] = 'L'
                    self.mults[w-1][0] += 1  
                    '''
        
        if self.c == 'coal farm':

            if self.wood >= 500:
                if self.coal >= 10:
                    self.wood -= 500
                    self.coal -= 10
                    print('you build a coal farm.')
                    self.coal_farms += 1 
                    
        if self.c == 'iron farm':
            if self.wood >= 1000:
                if self.coal >= 500:
                    self.wood -= 1000
                    self.coal -= 500
                    print('you build an iron farm.')
                    self.iron_farms += 1 
                   


    def production(self):
        

        
        self.wood += (50 * self.wood_farms)+self.woodbonus
        
        self.coal += (50 * self.coal_farms)+self.coalbonus
        
        self.iron += (50 * self.iron_farms) + (3 * self.coal_farms) + self.ironbonus
        
        #print('You have', self.wood_farms,'wood farm/s, providing',(self.wood_farms*50),'wood per turn. The extra upgrade bonus is:',self.woodbonus)
        #print('You have', self.iron_farms,'iron farm/s, providing',self.iron_farms*50,'iron per turn.The extra upgrade bonus is:',self.ironbonus)
        #print('You have', self.coal_farms,'coal farm/s, providing',self.coal_farms*50,'coal per turn.The extra upgrade bonus is:',self.coalbonus)
        self.score  = str(self.wood + self.coal*2 + self.iron*3 + self.steel*10)
        print('\nScore:',self.score)
        print('Amount of coal:',self.coal, 'with',self.coal_farms*50 + self.coalbonus,'from mines.')
        print('Amount of iron:',self.iron, 'with', self.iron_farms*50 + self.ironbonus,'from mines.')
        print('Amount of wood:',self.wood, 'with',self.wood_farms*50 + self.woodbonus,'from farms.')
        if self.steel > 0:
            print('Amount of steel:',self.steel,'')
        print('Amount of food:', self.food, 'with',self.foodbonus,'from farms')
        print('Amount of water:', self.water, "with",self.waterbonus,'from canals')
        print('Amount of energy:', self.energy,)
        print('Amount of money:', self.currency)
        print('Amount of soldiers:', self.soldiers, "with",10 + self.barracksevery,'every turn\n')
        time.sleep(self.n*0.5)
        

    def armoryuse(self):
        print('you can convert iron and steel into weapons/armor')
        print('You have',self.steel,'steel')
        print('You have',self.iron,'iron')
        print('Steel tools increase fighting success, to a higher degree than iron tools.')
        s = int(input('1 Make iron tools \n2 Make steel tools'))

        if s == 1:
            print('1 iron leads to a 0.05 increase in probablility of winning a fight')
            am = int(input('how much?'))
            self.iron -= am
            self.soldierbonus += (am * 0.05)
        if s == 2:
            print('1 steel leads to a 0.1 increase in probablility of winning a fight')
            am = int(input('How much?'))
            self.steel -= am
            self.soldierbonus += (am * 0.1)

        

            
    def blastfurnaceuse(self):
        os.system('clear')
        print('You have',self.coal,'coal')
        print('You have',self.iron,'iron')
        print('1 coal + 1 iron = 1 steel')
        m = int(input('how much?'))
        self.coal -= m
        self.iron -= m
        self.steel += m
    def Order(self):

        words = ['a difficult','an irritating','a boring', 'a hard','a stressful']

        words_but = ['successful','fun','uneventful','supreme']
        word2 = random.choice(words_but)
        word= random.choice(words)

        statement = 'Press enter to pass. What do you want to order your tribe to do?\n1.Trade currency for food.\n2.Trade currency for water.\n3.Relax for energy.\n4.Use energy to hunt for food.\n5.Use energy to search for water.\n6.Build your settlement\n7.Stop game and save scores\n8. Attack an enemy.'
        if self.armory == True:
            statement += ('\n9.Use the armory')
        if self.blastfurnace == True:
            statement += ('\n10.Use the blast furnace')
        if self.cities != []:
                statement += ('\n11.Subjugate your new lands')
            

        self.choice = int(input(statement))
        if self.choice == 1:
            self.amount = int(input('how much currency do you want to trade in?'))
            self.currency = self.currency - self.amount
            self.food_at_market =  random.randint((self.amount - 5), (self.amount + 5))
            self.food = self.food + self.food_at_market
            if self.food_at_market < self.amount:
                
                print('\nUnfortunately, you got a bad deal.\n')
                print(self.food_at_market, 'food was bought')

            elif self.food_at_market > self.amount:
                print('\nLuckily you got a good deal.\n')
                print(self.food_at_market, 'food was bought')
            else:
                print(self.food_at_market, 'food was bought')
        if self.choice == 2:
            self.amount = int(input('how much currency do you want to trade in?'))
            self.currency = self.currency - self.amount
            self.water_at_market =  random.randint((self.amount - 5), (self.amount + 5))
            self.water = self.water + self.water_at_market
            if self.water_at_market < self.amount:
                print('\nUnfortunately you got a bad deal.')
                print(self.water_at_market, 'water was bought')
            elif self.water_at_market > self.amount:
                print('Luckily you got a good deal.')
                print(self.water_at_market, 'water was bought')
            else:
                print(self.water_at_market, 'water was bought')
        if self.choice == 3:
            print('\nAfter a much needed respite, you gain energy.')
            self.energy += round(15 - (self.size/20))

        if self.choice == 4:
            
            
            e_loss = (10 + round(self.speed/15)) + random.randint(-3,3)
            f_gain = (10 + round(self.speed/10)) + random.randint(-3,3)
            self.energy -= e_loss 
            self.food += f_gain 
            print('\nAfter',word,'but',word2,'hunt,','you lose',e_loss,'energy, gaining',f_gain,'food')
            
        if self.choice == 5:
            
            e_loss = (10 + round(self.speed/15)) + random.randint(-3,3)
            w_gain = (10 + round(self.speed/10)) + random.randint(-3,3)
            self.energy -= e_loss 
            self.water += w_gain  
            print('\nAfter',word,'but',word2,'search,','you lose',e_loss,'energy, gaining',w_gain,'water')

        if self.choice == 6:

            os.system('clear')
            self.townbuild()

        if self.choice == 7:
            
            

            with open('scores','a') as f:
                pl  = str(self.wood + self.coal*2 + self.iron*3 + self.steel*10)
                total = ['the ', str(self.name), ' ', pl
                    ,'\n']
                

                f.writelines(total)
            
            with open("scores", "r") as a_file:
                word1 = 0
                word20 = 0
                letters = 'qwertyuiopasdfghjklzxcvbnm'
                numbers = [1,2,3,4,5,6,7,8,9,10]
                numbers2 = '1234567890'
                scores = []
                import re
                for line in a_file:
                    word1 = line.strip()
                    pattern = '[0-9]'
                    word1 = re.sub(pattern, '', word1)
                    if word1[-1] == ' ':
                        word1.replace(word1[-1], '')
                    
                    
                    word20 = line.strip()
                    word20 = re.sub('\D', '',word20)
                    
                    if word20[-1] == ' ':
                        word20.replace(word20[-1], '')
                    
            

                    scores.append([word1,int(word20)])

            sc = dict(scores)
            sc = sorted(sc.items(), key=lambda x: x[1])    

            sp = sc[::-1]
            l = 0
            for i in sp:
                l += 1
                print(str(l) + ')',i[0] + ':',i[1])
                time.sleep(0.15)
            sys.exit()




                
                  

                  
                  
              
            
        if self.choice == 8: 
            self.foreignpower()
            self.attackenemy()
        if self.choice == 9:
            self.armoryuse()
        if self.choice == 10:
            self.blastfurnaceuse()
        if self.choice == 11:
            self.enemytownuse()
            
        
    def mainloop(self):
        
        
        if self.food >= 200:
            self.food = 200
        if self.food <= 0:
            self.food = 0
        if self.water >= 200:
            self.water = 200
        if self.water <= 0:
            self.water = 0
        if self.energy >= 120:
            self.energy = 120
        if self.energy <= 0:
            self.energy = 0
    
        if self.food == 0:
            self.turns_without_food += 1
        
            
        if self.water == 1:
            self.turns_without_water += 1
        if self.turns_without_water == 3:
            print('Game over, the tribe of the',self.name,'die of thirst.')
                
            sys.exit()
            
        if self.turns_without_food == 5:
            print('Game over, the tribe of the',self.name,'die of hunger.')
            sys.exit()
        




player = Char()
while True:
 # player.battle()
  player.charismatrac()

  player.dangerTrack()
  player.getRobbedChance()
  player.RandomExploreLocations()
  player.RandomExploreLocations()
  player.move()
  player.startTurn()
  player.event()
  player.FoodWaterLoss()
  player.production()
  player.Warner()
  player.Order()
  
  player.mainloop()




