import pygame
from pygame.locals import *
import random
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))

welcome_page = pygame.image.load('Spaceship.png')

level_1_background = pygame.image.load('Level 1.png')
level_2_background = pygame.image.load('Level 2.png')
level_3_background = pygame.image.load('Level 3.png')
score_page = pygame.image.load('Score Page.png')
instructions = pygame.image.load('Instructions.png')
title = pygame.image.load('Space Warriors.png')
click_space = pygame.image.load('click space.png')
to_play = pygame.image.load('to play.png')
font = pygame.font.Font('Robot Monster Italic.ttf', 32)

player_one = pygame.image.load('Player 1.png')
player_one_X = 400
player_one_Y = 400
player_one_X_change = 0
player_one_Y_change = 0

player_two = pygame.image.load('Player 2.png')
player_two_X = 300
player_two_Y = 400
player_two_X_change = 0
player_two_Y_change = 0

score_value_player_one = 0
score_value_player_two = 0

starImg = []
star_X = []
star_Y = []
star_X_change = []
star_Y_change = []
num_of_stars = 6

for i in range(num_of_stars):
    starImg.append(pygame.image.load('star.png'))
    star_X.append(random.randint(0, 735))  # loads enemy in random places everytime it plays
    star_Y.append(random.randint(50, 150))
    star_X_change.append(2)
    star_Y_change.append(40)


def stars(x, y, i):
    screen.blit(starImg[i], (x, y))

def player_one_start_position(x, y):
    screen.blit(player_one, (x, y))

def player_two_start_position(x, y):
    screen.blit(player_two, (x, y))

def space_warrior_title():
    screen.blit(title, (50, 100))
    screen.blit(click_space,(200,300))
    screen.blit(to_play, (410, 300))

def show_score_one(x, y):
    score = font.render("Score: " + str(score_value_player_one), True, (255, 255, 255))
    screen.blit(score, (x, y))

text_player_one_X = 50
text_player_one_Y = 10

def show_score_two(x, y):
    score = font.render("Score: " + str(score_value_player_two), True, (255, 255, 255))
    screen.blit(score, (x, y))


text_player_two_X = 610
text_player_two_Y = 10


def Collison_Player_One(player_one_X, player_one_Y, star_X, star_Y):
    distance = math.sqrt((math.pow(player_one_X - star_X, 2)) + (math.pow(player_one_Y - star_Y, 2)))
    if distance < 27:
        return True
    else:
        return False


def Collison_Player_Two(player_two_X, player_two_Y, star_X, star_Y):
    distance = math.sqrt((math.pow(player_two_X - star_X, 2)) + (math.pow(player_two_Y - star_Y, 2)))
    if distance < 27:
        return True
    else:
        return False

screens = [level_1_background, level_2_background,level_3_background]

def level_one():
    screen.blit(level_1_background, (0,0))

def level_two():
    screen.blit(level_2_background, (0, 0))


def level_three():
    screen.blit(level_3_background, (0, 0))


def intermision():
    screen.blit(score_page, (0, 0))

running = True

while running:
    screen.fill((0, 0, 0))
    screen.blit(welcome_page, (0, 0))
    #space_warrior_title()


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_one_X_change = -5
            if event.key == pygame.K_RIGHT:
                player_one_X_change = 5
            if event.key == pygame.K_DOWN:
                player_one_Y_change = 5
            if event.key == pygame.K_UP:
                player_one_Y_change = -5
            if event.key == pygame.K_a:
                player_two_X_change = -5
            if event.key == pygame.K_d:
                player_two_X_change = 5
            if event.key == pygame.K_s:
                player_two_Y_change = 5
            if event.key == pygame.K_w:
                player_two_Y_change = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_one_X_change = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player_one_Y_change = 0
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player_two_X_change = 0
            if event.key == pygame.K_s or event.key == pygame.K_w:
                player_two_Y_change = 0

    player_one_X += player_one_X_change
    player_one_Y += player_one_Y_change
    player_two_X += player_two_X_change
    player_two_Y += player_two_Y_change
    # Player one boundary
    if player_one_X <= 0:
        player_one_X = 0
    elif player_one_X >= 736:
        player_one_X = 736
    if player_one_Y <= 0:
        player_one_Y = 0
    elif player_one_Y >= 536:
        player_one_Y = 536
        # Player two boundary
    if player_two_X <= 0:
        player_two_X = 0
    elif player_two_X >= 736:
        player_two_X = 736
    if player_two_Y <= 0:
        player_two_Y = 0
    elif player_two_Y >= 536:
        player_two_Y = 536

    #collisions
    for i in range(num_of_stars):
        if star_Y[i] > 1000:
            for j in range(num_of_stars):
                star_Y[j] = 2000

        collision_player_one = Collison_Player_One(player_one_X, player_one_Y, star_X[i], star_Y[i])
        collision_player_two = Collison_Player_Two(player_two_X, player_two_Y, star_X[i], star_Y[i])
        if collision_player_one:
            score_value_player_one += 1
            print(score_value_player_one)
            star_X[i] = random.randint(0, 735)
            star_Y[i] = random.randint(0, 535)
        if collision_player_two:
            score_value_player_two += 1
            star_X[i] = random.randint(0, 735)
            star_Y[i] = random.randint(0, 535)
        stars(star_X[i], star_Y[i], i)



    # Starting Position of Players
    player_one_start_position(player_one_X, player_one_Y)
    player_two_start_position(player_two_X, player_two_Y)
    show_score_one(text_player_one_X, text_player_one_Y)
    show_score_two(text_player_two_X, text_player_one_Y)
    pygame.display.update()

pygame.quit()

