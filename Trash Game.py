import pygame
import time
import sys
from pygame import mixer
import random
import math

#Initialize pygame
pygame.init()

#Display Size
screen = pygame.display.set_mode((1000, 700))

#Background
background = pygame.image.load('background.png')
IN_background = pygame.image.load('instruction.png')
PG_background = pygame.image.load('pregame_screen.png')
GM_background = pygame.image.load('over.png')

#Large Font (Game Over/Thank You)
L_font = pygame.font.Font('cute text.ttf', 100)

#Medium Font (Win/Pause)
M_font = pygame.font.Font('cute text.ttf', 50)

#Small Font (Restart)
S_font = pygame.font.Font('cute text.ttf', 25)

#Background Music
mixer.music.load('beach.wav')
mixer.music.play(-1)

#Caption & Icon
pygame.display.set_caption("Save the Ocean")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#Fact Displays
fact1 = pygame.image.load('Fact1.png')
fact2 = pygame.image.load('Fact2.png')
fact3 = pygame.image.load('Fact3.png')
fact4 = pygame.image.load('Fact4.png')
fact5 = pygame.image.load('Fact5.png')


#Player
playerImg = pygame.image.load('trash_bag.png')
playerX = 500
playerY = 500
playerX_change = 0

#Trash
trashImg = []
trashX = []
trashY = []
trashX_change = []
trashY_change = []
num_of_trash = 4

#Counters
score_value = 0
lost_trash = 0
fact_count = 0

#Array for Trash
for i in range (num_of_trash):
    trashImg.append(pygame.image.load('trash.png'))
    trashX.append(random.randint(0, 850))
    trashY.append(random.randint(0, 300))
    trashX_change.append(2)
    trashY_change.append(2)


def player(x, y):
    screen.blit(playerImg, (x, y))

def updateDis():
    screen.blit(background, (0,0))
    thanks_text()
    pygame.display.update()

def show_score():
    score = M_font.render("Score: " + str(score_value), True, (6, 57, 112))
    screen.blit(score, (20, 20))

def show_trash_score():
    Tscore = S_font.render("Loose Trash: " + str(lost_trash), True, (6, 57, 112))
    screen.blit(Tscore, (20, 75))

def game_over_text():
    over_text = L_font.render("GAME OVER!!!", True, (253,59,50))
    screen.blit(over_text, (235, 225))

def winning_text():
    win_text = M_font.render("YOU SAVED THE OCEAN!", True, (6,57,112))
    screen.blit(win_text, (235, 300))
    
def instruction_text():
    play_text = M_font.render('- Prevent trash from going into the ocean.', True, (6,57,112))
    how_text = M_font.render('- How to...', True, (6,57,112))
    how_text2 = M_font.render('Win: Score 5000 & don\'t loose', True, (6,57,112))
    how_text3 = M_font.render('more than 50 trash', True, (6,57,112))
    how_text4 = M_font.render('Lose: Scoring 50 loose trash.', True, (6,57,112))
    c_text = S_font.render('Press C to continue.', True, (6, 57, 112))
    screen.blit(play_text, (20, 150))
    screen.blit(how_text, (20, 250))
    screen.blit(how_text2, (300, 300))
    screen.blit(how_text3, (350, 360))
    screen.blit(how_text4, (300, 425))
    screen.blit(c_text, (750, 650))

def paused_text():
    p_text = L_font.render("Paused!", True, (6,57,112))
    p_textB = S_font.render("Press C to continue or Q to quit." , True, (6,57,112))
    screen.blit(p_text, (325, 250))
    screen.blit(p_textB, (325, 650))

def restart_text():
    r_text = M_font.render("Would you like to play again?.", True, (6,57,112))
    r_textB = S_font.render("Press Y to continue or N to exit.", True, (6,57,112))
    screen.blit(r_text, (150, 250))
    screen.blit(r_textB, (315, 650))

def thanks_text():
    ty_text = L_font.render("Thank you", True, (6,57,112))
    tyB_text = L_font.render("for playing!", True, (6,57,112))
    tyBB_text = S_font.render("~ Ashley & Charley!", True, (6,57,112))
    screen.blit(ty_text, (235, 125))
    screen.blit(tyB_text, (235, 325))
    screen.blit(tyBB_text, (635, 525))

def trash(x, y, i):
    screen.blit(trashImg[i], (x, y))

def isCollision(trashX, trashY, playerX, playerY):
    distance = (math.sqrt(math.pow((trashX - playerX), 2) + math.pow((trashY - playerY), 2)))/2
    if distance <= 85 and trashX >= playerX:
        return True
    else:
        return False

def Instruction_Screen():
    paused = True
    while paused:
        for event in pygame.event.get():
            screen.blit(IN_background, (0,0))
            instruction_text()
            pygame.display.update()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                if event.key == pygame.K_q:
                   pygame.quit()
                   sys.exit()

def preGame_Screen():
    paused = True
    while paused:
        for event in pygame.event.get():
            screen.blit(PG_background, (0,0))
            pygame.display.update()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                if event.key == pygame.K_q:
                   pygame.quit()
                   sys.exit()

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            screen.blit(background, (0,0))
            paused_text()
            pygame.display.update()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                if event.key == pygame.K_q:
                   pygame.quit()
                   sys.exit()
def pause1():
    paused = True
    while paused:
        for event in pygame.event.get():
            screen.blit(fact1, (0,0))
            pygame.display.update()
            
            if event.type == pygame.QUIT:
                pygame.quit
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                if event.key == pygame.K_q:
                   pygame.quit()
                   sys.exit()
                   
def pause2():
    paused = True
    while paused:
        for event in pygame.event.get():
            screen.blit(fact2, (0,0))
            pygame.display.update()
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                if event.key == pygame.K_q:
                   pygame.quit()
                   sys.exit()
                   
def pause3():
    paused = True
    while paused:
        for event in pygame.event.get():
            screen.blit(fact3, (0,0))
            pygame.display.update()
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                if event.key == pygame.K_q:
                   pygame.quit()
                   sys.exit()
                   
def pause4():
    paused = True
    while paused:
        for event in pygame.event.get():
            screen.blit(fact4, (0,0))
            pygame.display.update()
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                if event.key == pygame.K_q:
                   pygame.quit()
                   sys.exit()
                   
def pause5():
    paused = True
    while paused:
        for event in pygame.event.get():
            screen.blit(fact5, (0,0))
            pygame.display.update()
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                if event.key == pygame.K_q:
                   pygame.quit()
                   sys.exit()
                   
#Key Instructions
running = True
Instruction_Screen()
time.sleep(0.5)
preGame_Screen()
time.sleep(1)

#Game Loop
while running:
    screen.fill((0,0,0))
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#Movements
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                    playerX_change = 4
            elif event.key == pygame.K_p:
                    pause()
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0
    playerX += playerX_change
    if playerX <= -200:
        playerX = -200
    elif playerX >= 750:
        playerX = 750
#Trash Movements
    for i in range(num_of_trash):
        trashY[i] += trashY_change[i]
        if trashY[i] <= 0:
            trashY_change[i] = 1
            trashX[i] += trashX_change[i]
        elif trashY[i] >= 710:
            trashY[i] = -5
            trashX[i] = random.randint(0, 850)
            lost_trash += 5
            if score_value:
                score_value -= 50
#Losing Function
        if lost_trash >= 50:
            pygame.mixer.music.stop()
            for j in range (num_of_trash):
                trashY[j] = -1000
            playerX = 350
            losing_Sound = mixer.Sound('losing.wav')
            losing_Sound.play()
#Winning Function
        if score_value >= 5000:
            pygame.mixer.music.stop()
            for j in range (num_of_trash):
                trashY[j] = -1000
            playerX = 350
            winning_Sound = mixer.Sound('winning.wav')
            winning_Sound.play()
#Restart
        option = True
        if score_value >= 5000 or lost_trash >= 50:
            if lost_trash >= 50:
                screen.blit(GM_background, (0,0))
                pygame.display.update()
                time.sleep(3)
            else:
                screen.blit(background, (0,0))
                winning_text()
                pygame.display.update()
                time.sleep(3)
            while option:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_y:
                            option = False
                            score_value = 0
                            fact_count = 0
                            lost_trash = 0
                            playerX = 500
                            playerY = 500
                            pygame.mixer.music.play()
                            for j in range(num_of_trash):
                                trashY[j] = random.randint(0, 350)
                        if event.key == pygame.K_n:
                            screen.blit(background, (0,0))
                            thanks_text()
                            pygame.display.update()
                            time.sleep(2)
                            pygame.quit()
                            sys.exit()
                            
                screen.blit(background, (0,0))
                restart_text()
                pygame.display.update()
#Fact Display
        if score_value >= 1000 and fact_count < 1:
            pause1()
            fact_count += 1
        if score_value >= 2000 and fact_count < 2:
            pause2()
            fact_count += 1
        if score_value >= 3000 and fact_count < 3:
            pause3()
            fact_count += 1
        if score_value >= 4000 and fact_count < 4:
            pause4()
            fact_count += 1
#Catching Trash
        collision = isCollision(trashX[i], trashY[i], playerX, playerY)
        if collision:
            trashX[i] = random.randint(0, 850)
            trashY[i] = 0
            score_value += 50
            trash_Sound = mixer.Sound('trash.wav')
            trash_Sound.play()
        trash(trashX[i], trashY[i], i)

    player(playerX, playerY)
    show_score()
    show_trash_score()
    pygame.display.update()
#Quit Game
pygame.quit()
