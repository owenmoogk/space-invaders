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
enemyYInit = 70 #spawning distance from top of screen
enemySpeedX = .2 #initial speed of the enemy
bulletSpeed = 1 #speed of the bullet
bulletWidth = 16 #pixels
bulletHeight = 32 #pixels
enemySpeedXIncrement = .2 #every 50 points (5 shots) the speed of the enemy increases by this
enemyYDrop = 50 #every time the enemy reaches an edge this is they y drop
numOfEnemies = 4 #number of enemies
levelLength = 10 #number of enemies killed to move onto next level
textX = 30 #x value for showing the score
textY = 30 #y value for showing the score
levelOffset = 50 # number of pixels shifted down the level display is

#scoreboard
score = 0
level = 1
font = pygame.font.Font('freesansbold.ttf',32) #font and size
def showScore(x,y):
    scoreDisplay = font.render('Score: '+str(score),True, (255,255,255))
    screen.blit(scoreDisplay,(x,y))
    levelDisplay = font.render('Level: '+str(level),True, (255,255,255))
    screen.blit(levelDisplay,(x,y+levelOffset))
    

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
enemyX = []
enemyY = []
enemyDirection = []

for i in range(numOfEnemies):
    enemyX.append(random.randint(0,800-enemySize))
    enemyY.append(enemyYInit)
    enemyDirection.append(bool(random.randint(0,1)))

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

    #quit the game (x button)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #background
    screen.fill((0,0,0))
    screen.blit(background,(0,0))


    #draw player
    player(playerX,playerY)
    

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
    for i in range(numOfEnemies):
        if enemyDirection[i]: #right
            enemyX[i] += enemySpeedX
        else: #left
            enemyX[i] -= enemySpeedX

        if 0 > enemyX[i] or enemyX[i] > screenX-enemySize:
            enemyDirection[i] = not (enemyDirection[i])
            enemyY[i] += enemyYDrop
            if enemyDirection[i]:
                enemyX[i] +=1
            else:
                enemyX[i] -= 1
            if enemyY[i] >= playerY - enemySize:
                print ('quit cuz told')
                pygame.quit()
                sys.exit()

        enemy(enemyX[i],enemyY[i])

        #collision detection
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = playerY
            bulletState = 'ready'
            score += 10
            enemyX[i] = random.randint(0,800-enemySize)
            enemyY[i] = enemyYInit
            enemyDirection[i] = bool(random.randint(0,1))
            if score%(levelLength*10) == 0 and score > 0:
                enemySpeedX += enemySpeedXIncrement
                level += 1

    

    #bullet movement
    if bulletState == 'fire':
        fire(bulletX,bulletY)
        bulletY -= bulletSpeed
        if bulletY < 0:
            bulletState = "ready"
            bulletY = playerY
    
    showScore(textX,textY)

    #update the screen
    pygame.display.update()