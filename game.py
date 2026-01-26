import pgzrun
import random

WIDTH=1200
HEIGHT=600
TITLE="THE GALAGA GAME"

CENTER_X=WIDTH//2
CENTER_Y=HEIGHT//2

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

#BULLETS
def on_key_down(key):
    if key==keys.SPACE:
        #CREATE A NEW BULLET
        bullet=Actor("bullet")
        bullet.x=ship.x
        bullet.y=ship.y-50
        bullets.append(bullet)

#SCORE DISPLAY
def draw_score():    
    screen.draw.text(f"SCORE: {score}",(50,30),color="white")
    screen.draw.text(f"LIVES: {lives}", (50,60), color="white")

#FUNCTION TO DRAW GAME STATE
def draw():
    if lives>0:
        screen.clear()
        screen.fill("#2F6690")
        ship.draw()
        for enemy in enemies:
            enemy.draw()
        for bullet in bullets:
            bullet.draw()    
        draw_score()
    else:
        game_over_screen()

#FUNCTION TO UPDATE GAME STATE
def update():
    global lives, score

    #MOVE THE SHIP LEFT AND RIGHT
    if keyboard.left:
        ship.x -=speed
        if ship.x<=0:
            ship.x=0

    elif keyboard.right:
        ship.x +=speed
        if ship.x>=WIDTH:
            ship.x=WIDTH
    
    #MOVE THE BULLETS
    for bullet in bullets:
        if bullet.y<=0:
            bullets.remove(bullet)
        else:
            bullet.y -=10
    
    #MOVE THE ENEMIES
    for enemy in enemies:
        enemy.y +=5
        if enemy.y>HEIGHT:
            enemy.x=random.randint(0,WIDTH-80)
            enemy.y=random.randint(-100, 0) 
        
        #COLLISION WITH BULLETS
        for bullet in bullets:
            if enemy.colliderect(bullet): 
                score +=100
                sounds.eep.play()
                bullets.remove(bullet)
                enemies.remove(enemy)
    
        #COLLISION WITH SHIP
        if enemy.colliderect(ship):
            lives-=1
            enemies.remove(enemy)

            if lives==0:
                game_over()
    
    #CONTINUE CREATING ENEMIES
    if len(enemies)<8:
        enemy=Actor("bug")
        enemy.x=random.randint(0, WIDTH-80)
        enemy.y=random.randint(-100, 0)
        enemies.append(enemy)


def game_over():
    global is_game_over
    is_game_over=True
                

def game_over_screen():
    screen.clear()
    screen.fill("#140D4F")
    screen.draw.text("GAME OVER!", (CENTER_X-200, CENTER_Y), fontsize=60, color="white")
    screen.draw.text(f"score:{score}", (CENTER_X-200,CENTER_Y+50), fontsize=40, color="white")
    screen.draw.text("Press the space bar to play again!", (CENTER_X-200, CENTER_Y+100), fontsize=40, color="white")
    
    if keyboard.SPACE:
        restart_game()


#FUNCTION TO RESTART THE GAME
def restart_game():
    global lives, score, enemies, bullets
    lives=3
    score=0
    enemies=[]
    bullets=[]
    for i in range(8):
        enemy=Actor("bug")
        enemy.x=random.randint(0, WIDTH-80)
        enemy.y=random.randint(-100, 0)
        enemies.append(enemy)


pgzrun.go()