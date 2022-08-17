from blessed import Terminal
import random
import time,os,sys

positions = [[5, 10], [5, 10]]
score = 0
term = Terminal()


with term.location(0,15):
    print('p')

''''

import cv2
vidcap = cv2.VideoCapture('vid.mp4')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*200)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("shussy/image"+str(count)+".jpg", image)   
    return hasFrames
sec = 0
frameRate = 0.5 
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)

'''
from PIL import Image
import os
os.system('clear')
from numpy import asarray
def convert(bw=False,width=64, height=64,filename='zdv.jpeg'):
    im = Image.open(filename)
    if bw == True: 
        im = im.convert('1') 
    image = im.resize((30,8),Image.ANTIALIAS)
    data = asarray(image)
    #print(data[0])

    return data



def conconvert(x):
    y = []
    for i in range(len(x)):
        y.append([])
        for j in range(len(x[i])):
            qui = "\033[48;2;{};{};{}m \033[48;2;0;0;0m".format(x[i][j][0],x[i][j][1],x[i][j][2])

            y[i].append(qui)
    return y
        
import os
g = os.listdir('second')
print(len(g))
x = []
path = 'second/image'
for i in range(1,len(g)):
    c= path+str(i) + '.jpg'
    x.append(c)

for i in range(len(g) - 1):
    x[i] = conconvert(convert(filename = x[i]))


                
                
            #print(line,pixel)







for frame in range(len(x)):

    for line in range(len(x[frame])):
        for pixel in range(len(x[frame][line])):

            if frame > 0:
                with term.location(pixel,line):
                    print(x[frame][line][pixel])
                
            
            elif x[frame-1][line][pixel] == x[frame][line][pixel]:
                pass

            else:
                with term.location(pixel,line):
                    sys.stdout.write(x[frame][line][pixel])

                
