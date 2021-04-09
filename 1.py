import pgzrun
from random import randint
WIDTH = 800
HEIGHT = 600
alien = Actor('grisha')
alien.pos = 400, 300

def draw():
    screen.clear()
    alien.draw()

def update():
    alien.left += randint(-10,10)
    alien.top +=randint(-10,10)
    if alien.left > WIDTH:
        alien.right = WIDTH
    if alien.right < 0:
        alien.right = 0
    if alien.top<0:
        alien.top=0
    if alien.top>HEIGHT :
        alien.top=HEIGHT 
    

pgzrun.go()
