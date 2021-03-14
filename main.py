import sys, pygame, random
from settings import *

clock = pygame.time.Clock()
screen = pygame.display.set_mode((screenX,screenY))

#title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("assets/img/icon.jpg")
pygame.display.set_icon(icon)

#background
background = pygame.image.load('assets/img/background.jpg')

#scoreboard
score = 0
level = 1
def showScore(x,y):
    scoreDisplay = font.render('Score: '+str(score),True, (255,255,255))
    screen.blit(scoreDisplay,(x,y))
    levelDisplay = font.render('Level: '+str(level),True, (255,255,255))
    screen.blit(levelDisplay,(x,y+levelOffset))
    
#seconds init
start_ticks=pygame.time.get_ticks() #starter tick

#player
playerImg = pygame.image.load('assets/img/player.png')
playerX = (screenX/2)-playerSize/2
playerY = screenY - (screenY/5)
def player(x,y):
    screen.blit(playerImg,(x,y))

#enemy
enemyImg = pygame.image.load('assets/img/enemy.png')
enemyX = []
enemyY = []
enemyDirection = []

for i in range(numOfEnemies):
    enemyX.append(random.randint(0,screenX-enemySize))
    enemyY.append(random.randint(enemyYInitMin,enemyYInitMax))
    enemyDirection.append(bool(random.randint(0,1)))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

#bullet
bulletImg = pygame.image.load('assets/img/bullet.png')
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

#game over
def gameOverText(x,y):
    textGameOver = gameOverFont.render('Game 0ver!',True,(255,255,255))
    screen.blit(textGameOver, (x,y))

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
                bulletSound = pygame.mixer.Sound('assets/sounds/shoot.wav')
                bulletSound.play()
            
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

        #game over
        if enemyY[i] >= playerY - enemySize:
            for p in range (numOfEnemies):
                enemyY[p] = screenY
            gameOverText(200,200)
            break

        enemy(enemyX[i],enemyY[i])

        #collision detection
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = playerY
            bulletState = 'ready'
            score += 10
            enemyX[i] = random.randint(0,screenX-enemySize)
            enemyY[i] = random.randint(enemyYInitMin,enemyYInitMax)
            enemyDirection[i] = bool(random.randint(0,1))
            #sound
            bulletSound = pygame.mixer.Sound('assets/sounds/explosion.wav')
            bulletSound.play()
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

    clock.tick(fpsLimit)
    pygame.display.update()