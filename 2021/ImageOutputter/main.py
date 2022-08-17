
from PIL import Image
import sys 
from numpy import asarray


def show(bw=False,width=64, height=64,filename='zdv.jpeg'):
    im = Image.open(filename)
    image = im.resize((40,16),Image.ANTIALIAS)
    x = asarray(image)
    y = ''
    for i in range(len(x)):
        for j in x[i]:
            qui = "\033[48;2;{};{};{}m \033[48;2;0;0;0m".format(j[0],j[1],j[2])
            y += qui
        y += '\n'
    for i in y:
        sys.stdout.write(i)
            
        

show(filename = 'chest.jpg')



