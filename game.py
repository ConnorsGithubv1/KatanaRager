import os
import warnings
from tkinter import font
from pygame.locals import *
from pygame_functions import *

import pygame, sys

from pygame_functions.pygame_functions import makeSprite

clock = pygame.time.Clock()

# initialization
pygame.init()

infoObject = pygame.display.Info()

display_width = infoObject.current_w
display_height = infoObject.current_h
screensize = display_width, display_height

#colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (170, 0, 0, 128)
bright_red = (255, 100, 0)
blueviolet = (138, 43, 226)
purple = (147, 112, 219)


gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)

optionspath = "options.py"


# player--------------------------------------------
player = pygame.image.load('media/gokuidle.png')
playerlocation = [display_width * .9, 50]
playerYmomentum = 0



moving_right = False
moving_left = False
moving = False

game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','2','2','2','2','2','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2'],
            ['1','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]

grass_img = pygame.image.load('tiles/floor2.png')
dirt_img = pygame.image.load('tiles/floor.png')

enterscreen = pygame.image.load('media\enterscreenbg.png')

# sets the background to a selected image
def setbg(img):
    gameDisplay.blit(pygame.transform.scale(img, (display_width, display_height)), (0, 0))

# Game
def game():
    global moving_right, moving_left, playerYmomentum, player
    running = True
    # GameLoop
    while running:

        gameDisplay.fill(blueviolet)
        gameDisplay.blit(player, playerlocation)


        if playerlocation[1] > screensize[1]-player.get_height():
            playerYmomentum = 0
        else:
            playerYmomentum += 0.2
        playerlocation[1] += playerYmomentum

        if moving_right == True:
            playerlocation[0] += 4
            player = pygame.image.load('media/gokuright.png')
        if moving_left == True:
            playerlocation[0] -= 4
            player = pygame.image.load('media/gokuleft.png')


        if moving == False:



        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    os.startfile(optionspath)
                if event.key == K_d:
                    moving = False
                    moving_right = True
                if event.key == K_a:
                    moving = False
                    moving_left = True
            if event.type == KEYUP:
                if event.key == K_d:
                    moving = True
                    moving_right = False
                if event.key == K_a:
                    moving = True
                    moving_left = False


        pygame.display.update()
        clock.tick(60)

# Enter the mainloop----------------------------------------------------------
game()

pygame.quit()
sys.exit()