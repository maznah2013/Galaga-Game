import pgzrun
import random

WIDTH=1200
HEIGHT=600
TITLE="THE GALAGA GAME"

score=0
lives=3
is_game_over=False
speed=5
bullets=[]
enemies=[]

#SHIP
ship=Actor("ship")
ship.pos=(600, HEIGHT-60)

#ENEMIES
for i in range(8):
    enemy=Actor("bug")
    enemy.x=random.randint(0, WIDTH-80)
    enemy.y=random.randint(-100, 0)
    enemies.append(enemy)
