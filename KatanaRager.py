import warnings
from tkinter import font
from pygame.locals import *

import pygame, sys

# initialization
pygame.init()

# vars (useable)
infoObject = pygame.display.Info()

display_width = infoObject.current_w
display_height = infoObject.current_h

screensize = display_width, display_height
screensizetxt = "screensize:"+ str(display_width) + 'x' + str(display_height)

black = (0, 0, 0)
white = (255, 255, 255)
red = (225, 0, 0)
bright_red = (255, 100, 0)

lgFont = pygame.font.SysFont("Bungee, Arial", 100)
mdFont = pygame.font.SysFont("Bungee, Arial", 80)
smFont = pygame.font.SysFont("Bungee, Arial", 60)

gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)

menuImg = pygame.image.load('media/temple-export.png')
iconImg = pygame.image.load('media/fire1.png')
mountainbg = pygame.image.load('media/mountain-bg.png')
player = pygame.image.load('media/gokustanding.png')
pygame.display.set_icon(iconImg)
pygame.display.set_caption('Katana_Rager')
font = pygame.font.SysFont(None, 20)

# vars (not-useable)
centerdisplayX = (display_width / 2)
centerdisplayY = (display_height / 2)
x = display_width / 2 - 320
y = display_height / 2 - 320 - 200
text = lgFont.render("Katana Rager", True, red)
fullText = lgFont.render("Press Esc to exit out of fullscreen", True, red)
x1 = display_width / 2 - text.get_rect().width / 2
y1 = display_height / 2 - text.get_rect().height / 2 + 310
y2 = (display_height / 2 - text.get_rect().height / 2 + 400)
y3 = (display_height / 2 - text.get_rect().height / 2 + 490)
bottomY = centerdisplayY * 2 - text.get_rect().height
middleY = display_height / 2 - text.get_rect().height
lowermiddleY = display_height / 1.70 - text.get_rect().height

screenlist = [(1920,1080),(480, 640),(800, 600),(800, 640),(1024, 768),(1152, 864),(1280, 720),(1280, 960),(1280, 1024),(1440, 900)]


# Multipurpose functions-------------------------------------------

# used to fade out of screens
def fade(width, height):
    fade = pygame.Surface((screensize))
    fade.fill((0, 0, 0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        gameDisplay.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(1)


# used to create screens (not contributial to actual game code)
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# Settings functions---------------------------------

# sets mountainbackground in settings
def setbgmountain(x, y):
    x4 = x - (1568 / 2)
    y4 = y - (864 / 2)
    gameDisplay.blit(mountainbg, (round(x4), round(y4)))


# displays buttons in settings
def displayscreenbuttons():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    counter = 0
    pygame.draw.rect(gameDisplay, red, (x1, middleY, 620, 80))
    gameDisplay.blit(smFont.render(screensizetxt, True, white), (x1, middleY))


def displayfullscreenbtn():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # Main Menu Buttons
    if x1 + 305 > mouse[0] > x1 and lowermiddleY + 100 > mouse[1] > lowermiddleY:
        pygame.draw.rect(gameDisplay, bright_red, (x1, lowermiddleY, 305, 80))
        gameDisplay.blit(smFont.render('fullscreen', True, white), (x1, lowermiddleY))
        if click[0] == 1:
            pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
    else:
        pygame.draw.rect(gameDisplay, red, (x1, lowermiddleY, 305, 80))
        gameDisplay.blit(smFont.render('fullscreen', True, white), (x1, lowermiddleY))

    if x1 + 620 > mouse[0] > x1 + 310 and lowermiddleY + 100 > mouse[1] > lowermiddleY:
        pygame.draw.rect(gameDisplay, bright_red, (x1 + 310, lowermiddleY, 310, 80))
        gameDisplay.blit(smFont.render('windowed', True, white), (x1 + 310, lowermiddleY))
        if click[0] == 1:
            pygame.display.set_mode(screensize)
    else:
        pygame.draw.rect(gameDisplay, red, (x1 + 310, lowermiddleY, 310, 80))
        gameDisplay.blit(smFont.render('windowed', True, white), (x1 + 310, lowermiddleY))


# Options functions------------------------------------

# exit button used in options screen
def displayUniversalExitbutton():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x1 + 620 > mouse[0] > x1 and y3 + 100 > mouse[1] > y3:
        pygame.draw.rect(gameDisplay, bright_red, (x1, y3, 620, 80))
        gameDisplay.blit(smFont.render("EXIT", True, white), (x1, y3 + 10))
        if click[0] == 1:
            sys.exit()
    else:
        pygame.draw.rect(gameDisplay, red, (x1, y3, 620, 80))
        gameDisplay.blit(smFont.render("EXIT", True, white), (x1, y3 + 10))


# creates button that can be used to access main menu
def displayUniversalMainMenubutton():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x1 + 620 > mouse[0] > x1 and (centerdisplayY + 40) + 100 > mouse[1] > (centerdisplayY + 40):
        pygame.draw.rect(gameDisplay, bright_red, (x1, (centerdisplayY + 40), 620, 80))
        gameDisplay.blit(smFont.render("MAIN MENU", True, white), (x1, (centerdisplayY + 40)))
        if click[0] == 1:
            main_menu()
    else:
        pygame.draw.rect(gameDisplay, red, (x1, (centerdisplayY + 40), 620, 80))
        gameDisplay.blit(smFont.render("MAIN MENU", True, white), (x1, (centerdisplayY + 40)))


# Menu Functions-----------------------------------------------------

# displays menu img and text
def menustart(x, y):
    # filters deprecation warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    gameDisplay.blit(menuImg, (x, y))
    gameDisplay.blit(text, (x1, y1 - 140))


# creates all main menu buttons
def displayMenubuttons():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # Main Menu Buttons
    if x1 + 620 > mouse[0] > x1 and y1 + 100 > mouse[1] > y1:
        pygame.draw.rect(gameDisplay, bright_red, (x1, y1, 620, 80))
        gameDisplay.blit(smFont.render("START", True, white), (x1, y1 + 10))
        if click[0] == 1:
            fade(display_height, display_width)
            game()
    else:
        pygame.draw.rect(gameDisplay, red, (x1, y1, 620, 80))
        gameDisplay.blit(smFont.render("START", True, white), (x1, y1 + 10))

    if x1 + 620 > mouse[0] > x1 and y2 + 100 > mouse[1] > y2:
        pygame.draw.rect(gameDisplay, bright_red, (x1, y2, 620, 80))
        gameDisplay.blit(smFont.render("SETTINGS", True, white), (x1, y2 + 10))
        if click[0] == 1:
            fade(display_height, display_width)
            Settings()
    else:
        pygame.draw.rect(gameDisplay, red, (x1, y2, 620, 80))
        gameDisplay.blit(smFont.render("SETTINGS", True, white), (x1, y2 + 10))

    if x1 + 620 > mouse[0] > x1 and y3 + 100 > mouse[1] > y3:
        pygame.draw.rect(gameDisplay, bright_red, (x1, y3, 620, 80))
        gameDisplay.blit(smFont.render("EXIT", True, white), (x1, y3 + 10))
        if click[0] == 1:
            sys.exit()
    else:
        pygame.draw.rect(gameDisplay, red, (x1, y3, 620, 80))
        gameDisplay.blit(smFont.render("EXIT", True, white), (x1, y3 + 10))


# Screens--------------------------------------------------------------------

# Main Menu
def main_menu():
    # MenuLoop
    gameExit = False
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()

        gameDisplay.fill(black)
        menustart(x, y)
        displayMenubuttons()
        pygame.display.update()


# Game
def game():
    running = True
    # GameLoop
    while running:
        gameDisplay.fill((0, 26, 0))

        draw_text('game', font, (255, 255, 255), gameDisplay, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    Options()

        pygame.display.update()


# optionsloop
def Options():
    running = True
    while running:
        gameDisplay.fill((0, 0, 0))

        draw_text('options', font, (255, 255, 255), gameDisplay, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        displayUniversalExitbutton()
        displayUniversalMainMenubutton()
        pygame.display.update()


# Settingsloop
def Settings():
    open = True
    while open:
        gameDisplay.fill((0, 0, 0))

        draw_text('Settings', font, (255, 255, 255), gameDisplay, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    open = False

        setbgmountain(display_width / 2, display_height / 2)
        displayscreenbuttons()
        displayfullscreenbtn()
        pygame.display.update()


# Enter the mainloop----------------------------------------------------------
main_menu()

pygame.quit()
sys.exit()
