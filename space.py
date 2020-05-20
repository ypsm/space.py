import math
import pygame
from pygame import mixer
import random

pygame.init()
fps = pygame.time.Clock()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Space invader')

mixer.music.load('background.wav')
mixer.music.play(-1)

bg = pygame.image.load('background.jpg')
player = pygame.image.load('invaders.png')
bullet = pygame.image.load('bullet.png')
enemy = pygame.image.load('enemylaser.png')

playerX = 400 
playerY = 500
score = 0
bulletX = playerX
bulletY = playerY
status = 'ready'
status_1= 'ready'
color=(255,255,255 )
text_X = 16
text_y = 16
bullet_xchange = []
bullet_ychange = []

enemyImg = []
enemyX = []
enemyY = []
enemyDirection = []
enemyX_change = []
enemyY_change = []
new =0
enemyCount = 1                 
font_1=pygame.font.SysFont(None, 40,bold=True,italic=True)
def create_enemie():
    global new
    new =enemyCount
    for _ in range(enemyCount):
        enemyImg.append(pygame.image.load('transportation.png'))
        enemyX.append(random.randint(0, 736))
        enemyY.append(random.randint(50, 150))   
        enemyX_change.append(2)
        enemyY_change.append(40)
def bullet_fire():
    global status, playerX, playerY, bulletX, bulletY
    if status == 'fire':
        return
    bulletX = playerX + 13
    bulletY = playerY
    status = 'fire'
    bullet_sound = mixer.Sound('laser.wav')
    bullet_sound.play()

def check_and_fire():
    global bulletX, bulletY, status
    if status == 'ready':
        return
    window.blit(bullet, (bulletX, bulletY))
    bulletY-=10
    if bulletY <= 50:
        status = 'ready'

def show_enemies():
    for i in range(enemyCount):
        window.blit(enemyImg[i], (enemyX[i], enemyY[i]))
def game_over_text():
    over_text = font_1.render("GAMEOVER!!! YOU ARE DESTROYED", True, (144,166,188))
    window.blit(over_text,(20,250))
  
def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = math_sort(math.pow(enemyX - bulletX, 2), (math.pow(enemyY - bulletY,2)))
    if distance <27:
        return True
    else:
        return False            

def check_collision():
   global bulletX, bulletY, enemyX, enemyY, enemyCount, score, status
   for i in range(enemyCount):
       xHit = False
       yHit = False
       if bulletX >= enemyX[i] and bulletX <= enemyX[i]+45:
           xHit = True
       if bulletY >= enemyY[i] and bulletY <= enemyY[i]+30:
           yHit = True
       if xHit and yHit:
           enemyImg.pop(i)
           enemyX.pop(i)
           enemyY.pop(i)
           enemyCount -= 1
           status = 'ready'                  
           explosion_music = mixer.Sound('explosion.wav')
           explosion_music.play()         
           score +=1
           return    
    
            
def show_score():
    screen_text_3 =font_1.render("score :"+str(score),True, color)
    window.blit(screen_text_3,(600,0))

def check_enemie_detroyed():
    global enemyCount
    if enemyCount==0:
        enemyCount =new +1  
        create_enemie() 

create_enemie()

run = True
while run:
    window.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX += 10
                if playerX>=700:
                    playerX = 700
            elif event.key == pygame.K_LEFT:
                playerX -= 10
                if playerX<=10:
                   playerX = 10
            elif event.key == pygame.K_SPACE:
                bullet_fire()
#Enemy movement
    for i in range (enemyCount):
         enemyX[i] += enemyX_change[i]
        #game over
         if enemyY[i] > 490:
            for i in range(enemyCount):
                enemyY[i] = 200
            game_over_text()
            pygame.display.update()
                
         if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
         elif enemyX[i] >= 736:
            enemyX_change[i]  = -2
            enemyY[i] += enemyY_change[i]
   
    window.blit(player, (playerX, playerY))
    show_enemies()
    check_and_fire()
    check_collision()
    show_score()
    check_enemie_detroyed()
    pygame.display.update()