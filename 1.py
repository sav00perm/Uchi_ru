import pgzrun
from random import randint
WIDTH = 800
HEIGHT = 600
alien = Actor('grisha')
alien.pos = 400, 300

a1=Actor('grisha')
a2=Actor('alien')
a1.pos = 50, 100
a2.pos = 140, 100

def on_mouse_down(pos):
    if a1.collidepoint(pos):
        alien.image = 'grisha'
    elif a2.collidepoint(pos):
        alien.image = 'alien'
    else:
        print("Выбери героя!")

def draw():
    screen.clear()
    alien.draw()
    a1.draw()
    a2.draw()

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

