import random
import numpy as np
import os
import time
dim = [30,30]
import sys
sys.setrecursionlimit(9999)


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


class Cell:
    def __init__(self,value):
        self.value = value


class world:



    def __init__(self):
        self.walks = 0
        self.world = [
            [Cell(1) for i in range(dim[0]) ]
            for i in range(dim[1])
        ]

        #self.world[1][1] = Cell(1)

        self.coords = [15,15]

        self.changed = 0

        self.visited = []
        self.vcont = -1

        self.steps =0

    
    def recursiveDivision(self,rangex = [0,dim[0]],rangey = [0,dim[1]]):

        if rangex[1]-rangex[0] ==1 or rangey[1] - rangey[0]==1 or rangex[1]-rangex[0] ==0 or rangey[1] - rangey[0]==0 :return
        try:
            xcor = random.randint(rangex[0]+1, rangex[1]-2)
            ycor = random.randint(rangey[0]+1, rangey[1]-2)
        except:
            return
        #box1 = [rangex[0] : xcor; ycor :rangey[1]]

        for i in range(rangey[0],rangey[1]):
            for j in range(rangex[0],rangex[1]):
                if i == ycor or j == xcor:
                    setattr(self.world[i][j], 'value', 0)
        
            
        o = [1,2,3,4]
        random.shuffle(o)
        for i in range(3):
            c = o[i]
            if c == 1:
                x = xcor
                y = random.randint(ycor+1, rangey[1] - 1)
                setattr(self.world[x][y], 'value', 1)
            if c == 2:
                x = xcor
                y = random.randint(rangey[0], ycor-1)
                setattr(self.world[x][y], 'value', 1)
            if c == 3:
                x = random.randint(xcor+1,rangex[1] - 1)
                y = random.randint(ycor, rangey[1] - 2)
                setattr(self.world[x][y], 'value', 1)
            if c == 3:
                x = random.randint(xcor+1,rangex[1] - 1)
                y = random.randint(rangey[0], ycor)
                setattr(self.world[x][y], 'value', 1)
            




        
        self.recursiveDivision(rangex = [rangex[0],xcor] , rangey = [ycor+1,rangey[1]])
        self.recursiveDivision(rangex = [xcor+1,rangex[1]] , rangey = [ycor+1,rangey[1]])
        self.recursiveDivision(rangex = [rangex[0],xcor] , rangey = [rangey[0],ycor])
        self.recursiveDivision(rangex = [xcor+1,rangex[1]] , rangey = [rangey[0],ycor])


    

    
    def filter(self,i):
        if i == 0:
            return('\033[48;2;1;1;1m  \033[m')
        if i == 2:
            return('\033[48;2;254;1;1m  \033[m')
        else:
            return('\033[48;2;255;255;255m  \033[m')
    def displayPartial(self,w,h):
        xview = []
        yview = []
        if self.coords[0] <= round(w/2): xview = [0,w]
        elif self.coords[0] >= dim[0] - w/2: xview = [dim[0]-w,dim[0]]
        elif 2==2:
            xview = [self.coords[0] - round(w/2),self.coords[0] + round(w/2)]

        
        if self.coords[1] < round(h/2): yview = [0,h]
        elif self.coords[1] >= dim[1] - h/2: yview = [dim[1]-h,dim[1]]
        elif 2==2:
            yview = [self.coords[1] - round(h/2),self.coords[1] + round(h/2)]

        world = np.array(self.world)

        print(xview,yview)
        view = world[yview[0]:yview[1],xview[0]:xview[1]]

        for i in range(len(view)): 
            for j in range(len(view[i])):
                    if i == self.coords[1] and j == self.coords[0]:
                    
                        print(self.filter(2),end='')
                    else:
                        print(self.filter(view[i][j].value),end='')

            print('')
        

        


w = world()
w.recursiveDivision([0,dim[0]], [0,dim[1]])

while True:
    x = getch.__call__()
    if x == 'w':
        print('w')
        #time.sleep(0.1)
        w.coords[1] -= 1
    if x == 'a':
        w.coords[0] -= 1
        #time.sleep(0.1)
    if x == 's':
        w.coords[1] += 1
        #time.sleep(0.1)
    if x == 'd':
        w.coords[0] += 1
        #time.sleep(0.1)
    
    os.system('clear')

    
    w.displayPartial(30,30)
    print(w.coords)


