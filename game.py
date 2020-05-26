import os
import warnings
from tkinter import font
from typing import List, Any, Union

from pygame.locals import *

import pygame, sys

clock = pygame.time.Clock()

# initialization
pygame.init()

infoObject = pygame.display.Info()

display_width = infoObject.current_w
display_height = infoObject.current_h
screensize = display_width, display_height

# colors
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

playersizeY = 49
playersizeX = 43

moving_right = False
moving_left = False
moving = False

game_map = [['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '2', '2', '2', '2'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '2', '1', '1', '1', '1'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '2', '1', '1', '1', '1', '1'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '2', '1', '1', '1', '1', '1', '1'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1'],
            ['2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']]

grass_img = pygame.image.load('tiles/grass.png')
dirt_img = pygame.image.load('tiles/dirt.png')

mapfill = False

enterscreen = pygame.image.load('media\enterscreenbg.png')


# sets the background to a selected image
def setbg(img):
    gameDisplay.blit(pygame.transform.scale(img, (display_width, display_height)), (0, 0))

def playerrect(playersizeX,playersizeY, playerlocation):
    x = playersizeX
    y = playersizeY
    loc = playerlocation
    xpos = playerlocation[0]
    ypos = playerlocation[1]
    pygame.draw.rect(gameDisplay, red, (xpos, ypos,x,y))

# Game
def game():
    global moving_right, moving_left, playerYmomentum, player, mapfill
    running = True
    # GameLoop
    while running:

        gameDisplay.fill(blueviolet)
        gameDisplay.blit(player, playerlocation)


        if playerlocation[1] > screensize[1] - player.get_height():
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

        tilerects = []
        y = 0
        for layer in game_map:
            x = 0
            for tile in layer:
                if tile == '1':
                    gameDisplay.blit(dirt_img, (x * 96, y * 96))
                if tile == '2':
                    gameDisplay.blit(grass_img, (x * 96, y * 96))
                if tile != '0':
                    tilerects.append(pygame.Rect(x * 96, y * 96, 96, 96))
                x += 1
            y += 1


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
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

        playerrect(playersizeX,playersizeY, playerlocation)
        pygame.display.update()
        clock.tick(60)


# Enter the mainloop----------------------------------------------------------
game()

pygame.quit()
sys.exit()
