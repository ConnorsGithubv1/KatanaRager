import os
import warnings
from tkinter import font
from pygame.locals import *

import pygame, sys

# initialization
pygame.init()

#vars

infoObject = pygame.display.Info()

display_width = infoObject.current_w
display_height = infoObject.current_h
screensize = display_width, display_height

centerdisplayX = (display_width / 2)
centerdisplayY = (display_height / 2)

black = (0, 0, 0)
white = (255, 255, 255)
red = (225, 0, 0)
bright_red = (255, 100, 0)

lgFont = pygame.font.SysFont("Bungee, Arial", 100)
mdFont = pygame.font.SysFont("Bungee, Arial", 80)
smFont = pygame.font.SysFont("Bungee, Arial", 60)

settingsDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)

eyebg = pygame.image.load('media/settingsbg.png')

text = lgFont.render("Settings", True, red)
screensizetxt = "screensize:" + str(display_width) + 'x' + str(display_height)

x1 = display_width / 2 - text.get_rect().width / 2
menuY = display_height / 1.6 - text.get_rect().height / 2
topY = display_height / 10 - text.get_rect().height
bottomY = centerdisplayY * 2 - text.get_rect().height
middleY = display_height / 2 - text.get_rect().height
lowermiddleY = display_height / 1.70 - text.get_rect().height

# Settings functions---------------------------------

# sets mountainbackground in settings
def setbgeyes():
    settingsDisplay.blit(eyebg, (0, 0))


# displays buttons in settings
def displayscreenbuttons():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    counter = 0
    pygame.draw.rect(settingsDisplay, red, (x1, middleY, 620, 80))
    settingsDisplay.blit(smFont.render(screensizetxt, True, white), (x1, middleY))


def displayfullscreenbtn():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # Main Menu Buttons
    if x1 + 305 > mouse[0] > x1 and lowermiddleY + 100 > mouse[1] > lowermiddleY:
        pygame.draw.rect(settingsDisplay, bright_red, (x1, lowermiddleY, 305, 80))
        settingsDisplay.blit(smFont.render('fullscreen', True, white), (x1, lowermiddleY))
        if click[0] == 1:
            pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
    else:
        pygame.draw.rect(settingsDisplay, red, (x1, lowermiddleY, 305, 80))
        settingsDisplay.blit(smFont.render('fullscreen', True, white), (x1, lowermiddleY))

    if x1 + 620 > mouse[0] > x1 + 310 and lowermiddleY + 100 > mouse[1] > lowermiddleY:
        pygame.draw.rect(settingsDisplay, bright_red, (x1 + 310, lowermiddleY, 310, 80))
        settingsDisplay.blit(smFont.render('windowed', True, white), (x1 + 310, lowermiddleY))
        if click[0] == 1:
            pygame.display.set_mode(screensize)
    else:
        pygame.draw.rect(settingsDisplay, red, (x1 + 310, lowermiddleY, 310, 80))
        settingsDisplay.blit(smFont.render('windowed', True, white), (x1 + 310, lowermiddleY))


# Settingsloop
def Settings():
    open = True
    while open:
        settingsDisplay.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    open = False

        setbgeyes()
        displayscreenbuttons()
        displayfullscreenbtn()
        pygame.display.update()


# Enter the mainloop----------------------------------------------------------
Settings()

pygame.quit()
sys.exit()
