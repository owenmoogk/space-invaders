import sys
import pygame
import random

#intalize
pygame.init()

#settings
screenX = 800 #width of the screen
screenY = 600 #height of the screen
playerSize = 64 #pixels
enemySize = 64 #pixels
playerSpeed = 0.3 #player movement speed
enemyYInit = 70 #drop when reaches edge of screen
enemySpeedX = .3 #initial speed of the enemy
bulletSpeed = 1 #speed of the bullet
bulletWidth = 16 #pixels
bulletHeight = 32 #pixels
enemySpeedXIncrement = 0.1 #every 50 points (5 shots) the speed of the enemy increases by this
enemyYDrop = 50 #every time the enemy reaches an edge this is they y drop

#score
score = 0

#create screen
screen = pygame.display.set_mode((screenX,screenY))

#title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("img/icon.jpg")
pygame.display.set_icon(icon)

#background
background = pygame.image.load('img/background.jpg')

#player
playerImg = pygame.image.load('img/player.png')
playerX = (screenX/2)-playerSize/2
playerY = screenY - (screenY/5)
def player(x,y):
    screen.blit(playerImg,(x,y))

#enemy
enemyImg = pygame.image.load('img/enemy.png') 
enemyX = random.randint(0,800-enemySize)
enemyY = enemyYInit
enemyDirection = bool(random.randint(0,1))
def enemy(x,y):
    screen.blit(enemyImg,(x,y))

#bullet
bulletImg = pygame.image.load('img/bullet.png')
bulletX = playerX
bulletY = playerY
bulletState = 'ready' #ready = cant see bullet ---- fire = bullet is currently moving
def fire(x,y):
    screen.blit(bulletImg,(x + bulletWidth,y))

#collision detection
def isCollision(enemyX,enemyY,bulletX,bulletY):
    if bulletY > enemyY and bulletY < enemyY + enemySize:
        if bulletX + bulletWidth > enemyX and bulletX < enemyX + enemySize:
            return True
        else:
            return False
    else:
        return False



#running loop
while True:

    #playerX button work
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #background
    screen.fill((0,0,0))
    screen.blit(background,(0,0))


    #draw player
    player(playerX,playerY)
    enemy(enemyX,enemyY)

    #inputs
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX -= playerSpeed
        if event.key == pygame.K_RIGHT:
            playerX += playerSpeed
        if playerX < 0:
            playerX = 0
        if playerX > screenX-playerSize:
            playerX = screenX-playerSize
        if event.key == pygame.K_DOWN:
            if bulletState != 'fire':
                bulletState = 'fire'
                fire(playerX,bulletY)
                bulletX = playerX + bulletWidth/2
            

    #enemy movement
    if enemyDirection: #right
        enemyX += enemySpeedX
    else:
        enemyX -= enemySpeedX

    if 0 > enemyX or enemyX > screenX-enemySize:
        enemyDirection = not enemyDirection
        enemyY += enemyYDrop
        print ('enemy y',enemyY,'playery+enemysize',playerY,enemySize)
        if enemyY >= playerY - enemySize:
            pygame.quit()
            sys.exit()

    #bullet movement
    if bulletState == 'fire':
        fire(bulletX,bulletY)
        bulletY -= bulletSpeed
        if bulletY < 0:
            bulletState = "ready"
            bulletY = playerY
    
    #collision detection
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = playerY
        bulletState = 'ready'
        score += 10
        print (score)
        if score%50 == 0:
            enemySpeedX += enemySpeedXIncrement
        enemyX = random.randint(0,800-enemySize)
        enemyY = enemyYInit
        enemyDirection = bool(random.randint(0,1))
    

    #update the screen
    pygame.display.update()