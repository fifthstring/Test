import time, os, random, math,sys
from PIL import Image
from numpy import asarray
def show(bw=False,width=40, height=16,filename='zdv.jpeg'):
    im = Image.open(filename)
    image = im.resize((width,height),Image.ANTIALIAS)
    x = asarray(image)
    y = ''
    for i in range(len(x)):
        for j in x[i]:
            qui = "\033[48;2;{};{};{}m \033[m".format(j[0],j[1],j[2])
            y += qui
        y += '\n'
    for i in y:
        sys.stdout.write(i)
            

