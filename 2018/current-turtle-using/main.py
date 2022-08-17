
import turtle
import random
'''
colours = ['red','orange','yellow','blue']
turle = turtle.Turtle()
turle.speed(0)
y = 300
for x in range(y):
 # turle.pencolor(random.choice(colours))
  turle.pencolor('black')
  turle.width(y/30)
  turle.left(20)

  turle.forward(y/30)
  turle.width((y-1)/30)

  turle.pencolor('white')

  turle.forward(y/30)
  turle.right(1)
  y+=4
'''
turtle.speed(0)
turtle.color('navajowhite')
turtle.width(1000)
turtle.forward(1000)
turtle.left(180)
turtle.forward(2000)

colours = ['yellowgreen','white','yellow','lightblue','red','orange','red','orange','black','navajowhite']
turle = turtle.Turtle()
turle.speed(0)
y = 200
left = 70
right = 40
for x in range(y*300):
  turle.pencolor(random.choice(colours))
  turle.width(y/2)
  turle.left(70)

  turle.forward(50)
  turle.width(y*1)

  turle.pencolor(random.choice(colours))
  turle.right(40)

  turle.forward(20)
  y -= 0.2
  left -= 25
  right -= 10