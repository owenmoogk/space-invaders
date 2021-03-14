import pygame

pygame.init()
#settings
fpsLimit = 120 #controls the max framerate

screenX = 800 #width of the screen
screenY = 600 #height of the screen

playerSize = 64 #pixels
enemySize = 64 #pixels

playerSpeed = 250/fpsLimit #player movement speed

enemyYInitMin = 50 #spawning distance from top of screen minimum
enemyYInitMax = 150 #spawning distance from top of screen minimum

enemySpeedX = 200/fpsLimit #initial speed of the enemy
bulletSpeed = 750/fpsLimit #speed of the bullet

bulletWidth = 16 #pixels
bulletHeight = 32 #pixels

enemySpeedXIncrement = .5 #every x points (5 shots) the speed of the enemy increases by this (affected by fps)
enemyYDrop = 70 #every time the enemy reaches an edge this is they y drop

numOfEnemies = 4 #number of enemies
levelLength = 10 #number of enemies killed to move onto next level

textX = 20 #x value for showing the score
textY = 10 #y value for showing the score

levelOffset = 40 # number of pixels shifted down the level display is
font = pygame.font.Font('assets/text/Starjedi.ttf',30) #font and size
gameOverFont = pygame.font.Font('assets/text/Starjedi.ttf',60)

backgroundMusic = pygame.mixer.music.load('assets/sounds/background.mp3')
pygame.mixer.music.play(-1)