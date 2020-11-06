import sys
import pygame

#intalize
pygame.init()

#create screen
screen = pygame.display.set_mode((800,600))

#title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("img/icon.jpg")
pygame.display.set_icon(icon)


#player
playerImg = pygame.image.load('img/player.png')
playerSize = 64 #player size in pixels, used for aligning with walls and center
playerX = 400-playerSize/2
playerY = 480

def player(x,y):
    screen.blit(playerImg,(x,y))

#enemy
enemyImg = pygame.image.load('img/enemy.png')
enemySize = 64 #player size in pixels, used for aligning with walls and center
enemyX = 400-enemySize/2
enemyY = 70

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

    speed = 0.3 #movement speed

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_LEFT:
            playerX -= speed
        if event.key == pygame.K_RIGHT:
            playerX += speed
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



    #needed to update the screen
    pygame.display.update()