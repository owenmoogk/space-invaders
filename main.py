import sys
import pygame
import random

#intalize
pygame.init()

#settings
screenX = 800
screenY = 600
playerSize = 64 #pixels
playerSpeed = 0.3

#create screen
screen = pygame.display.set_mode((screenX,screenY))

#title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("img/icon.jpg")
pygame.display.set_icon(icon)


#player
playerImg = pygame.image.load('img/player.png')
playerX = (screenX/2)-playerSize/2
playerY = screenY - (screenY/5)
def player(x,y):
    screen.blit(playerImg,(x,y))

#enemy
enemyImg = pygame.image.load('img/enemy.png')
enemySize = 64 #player size in pixels, used for aligning with walls and center
enemyX = random.randint(0,800-enemySize)
enemyY = 70
enemySpeedX = 0.3
enemyDirection = bool(random.randint(0,1))
    
def enemy(x,y):
    screen.blit(enemyImg,(x,y))


#running loop
while True:

    #playerX button work
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #fill the screen with red
    screen.fill((0,0,0))


    #draw player
    player(playerX,playerY)
    enemy(enemyX,enemyY)

    #player movement
    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_LEFT:
            playerX -= playerSpeed
        if event.key == pygame.K_RIGHT:
            playerX += playerSpeed
        if playerX < 0:
            playerX = 0
        if playerX > 800-playerSize:
            playerX = 800-playerSize

        # if event.key == pygame.K_UP:
        #     y -= speed
        # if event.key == pygame.K_DOWN:
        #     y += speed
        # if y < 0:
        #     y = 0
        # if y > 600-playerSize:
        #     y = 600-playerSize

    #enemy movement
    


    
    if enemyDirection: #right
        enemyX += enemySpeedX
    else:
        enemyX -= enemySpeedX


    if 0 > enemyX or enemyX > screenX-enemySize:
        enemyDirection = not enemyDirection
        enemyY += 60
        if enemyY > screenY-100:
            pygame.quit()
            sys.exit()
    
    

    #needed to update the screen
    pygame.display.update()