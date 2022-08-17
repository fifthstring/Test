import random
import time
import os
import sys


# from PIL import Image

def cls():
    os.system('clear')


class Char():
    def __init__(self):
        a = 1
        b = 1
        # import the sprites for the player files would have to be downloaded on anyone playing game. We can't test the images on the repl

        # self.playersprite1 = Image.open(#file name of the image that we use for the sprite)
        # self.playersprite2 = Image.open(#file name of the image that we use for the sprite)
        # self.playersprite3 = Image.open(#file name of the image that we use for the sprite)
        # self.playersprite4 = Image.open(#file name of the image that we use for the sprite)


        self.name = input('What do you want to call your species?\n')
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
        #could make it a chance to buy at a random event?
        #self.buy = int('which building do you want:\n1.Mine Gives you currency over time cost: 50 \n 2.barracks gives you protection Cost:65 ECT')
        global energy
        self.energy = 100
        self.food = 0
        self.water = 0
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



        def battle(plenergy, plfood, plwater, enenergy, enxp, score, self):
            print()
            self.battleHP = (self.food + self.energy + self.water + self.size)/100
            self.enemyHP = random.randint(1,(self.turns_passed * 1.5))



        def charismatrac(self):
            self.charisma = ((self.food * 1.25) + (self.water * 1.25) + (self.energy * 0.5) + self.currency / 4)
            if self.charisma >= 100:
                self.charisma = 100
            print('your charisma is', self.charisma)
        def dangerTrack(self):
            self.danger = (self.charisma) + self.turns_passed
            if self.danger >= 100:
                self.danger = 100

        def getRobbedChance(self):
            z = random.randint(0, 300)
            c = self.currency - random.randint(int(self.currency / 3), int(self.currency / 2))

            if z < self.currency:
                self.currency = self.currency - c
                print('You have been robbed of',c)
            if self.currency >= 100:
                self.currency = 100

        # IDEAS THAT I HAVE
        # def Deathchance(self):
        #   self.deathchance = ((self.size + self.speed + ?????) / 2)/100

        # def Birthchance(self):
        #   self.birthchance = (self.charisma + WHAT OTHER FACTORS)/100

        # def popdifference(self):
        #   self.popgrowth = (self.birthchance - self.deathchance) * self.quantityofcreatures
        #	self.quantityofcreatures = self.quantityofcreatures + self.popgrowth

        # FOR A SOCIETY SYSTEM COULD BE A SECOND STAGE TO GAME. AT START YOU ARE BY YOURSELF THEN EVENTUALY YOU REACH A SOCIETY LEVEL

        # def Building(self):
        #   if self.buy == 1:
        #       if self.minebought == False:
        #           self.currency = self.currency - 50
        #           self.minebought = True
        #           self.mine = 10
        #   if self.buy == 2:
        #       if self.barracksbought == False:
        #           self.currency = self.currency - 65
        #           self.barracksbought = True
        #           self.barracks = 30

        def RandomExploreLocations(self):
            self.treasure_location = random.randint(1,4)
            self.treasure = 0
        def move(self):
            self.e = []
            for i in self.e:
                print(self.e[i])
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
                print('you found', self.treasure_bonus, 'currency!!')
                self.currency += self.treasure_bonus
            else:
                print('Unlucky No treasure this time')



        def startTurn(self):
            self.turns_passed = self.turns_passed + 1
            # self.currency = self.currency + self.mine MAYBE OTHER BUILDINGS ASWELL
            print('Food count', self.food, "\n")
            print('Water count', self.water, "\n")
            print('Amount of energy', self.energy, '\n')
            print('how much currency you have', self.currency)
            # print('Amount of Currency', self.currency, '\n')
            charismatrac(self)

        #def event(self):
        #    self.events = {'food shortage': (10), 'enemy steals your food': (10), 'injury': (30), 'water shortage': (60) }

        #    if self.energy > 50:
        #       self.events.append('injury': (30))

        #        if self.energy > 80:
        #            self.events.append('water shortage': (60))
        #            print(self.energy)
        #            self.choice = random.choice(list(self.events))
        #            self.choice = self.events.get(self.choice)
        #            self.energy -= self.choice

        #            print(self.energy)
        def FoodWaterLoss(self):
            self.food = self.food - (self.size * 0.05 + 1)
            self.water = self.water - (self.size * 0.05 + 1)
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
                print('you are running low on energy', self.energy)
            if self.food < 20:
                print('you are running low on food', self.food)
            if self.water < 20:
                print('you are running low on water', self.water)

        def Order(self):
            self.choice = int(input(
                'What do you want to order your tribe to do?\n1.trade currency for food\n2.trade currency for water\n3.Relaxe for energy\n4.Use energy to hunt for food\n5.Use energy to search for water'))
            if self.choice == 1:
                self.amount = int(input('how much currency do you want to trade in?'))
                self.currency = self.currency - self.amount
                self.food_at_market =  random.randint((self.amount - 5), (self.amount + 5))
                self.food = self.food + self.food_at_market
                if self.food_at_market < self.amount:
                    print('Unfortunatly you got a bad deal only', self.food_at_market)
                if self.food_at_market > self.amount:
                    print('Luckily you got a good deal', self.food_at_market)
                else:
                    print(self.food_at_market, 'was bought')
            if self.choice == 2:
                self.amount = int(input('how much currency do you want to trade in?'))
                self.currency = self.currency - self.amount
                self.water_at_market =  random.randint((self.amount - 5), (self.amount + 5))
                self.water = self.water + self.water_at_market
                if self.water_at_market < self.amount:
                    print('Unfortunatly you got a bad deal only', self.water_at_market)
                if self.water_at_market > self.amount:
                    print('Luckily you got a good deal', self.water_at_market)
                else:
                    print(self.water_at_market, 'was bought')
            if self.choice == 3:
                self.energy += 10
            if self.choice == 4:
                self.energy -= 10
                self.food += 10
            if self.choice == 5:
                self.energy -= 10
                self.water += 10


        def mainloop(self):
            FoodWaterLoss(self)
            startTurn(self)
            dangerTrack(self)
            getRobbedChance(self)
            RandomExploreLocations(self)
            move(self)
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
            Warner(self)
            Order(self)
            if self.food == 0:
                self.turns_without_food += 1
            if self.water == 1:
                self.turns_without_water += 1
            if self.turns_without_water == 3:
                print('Game Over')
                sys.exit()
                
            if self.turns_without_food == 3:
                print('Game Over')
                while True:
                    print()









        while True:
            mainloop(self)

Char()