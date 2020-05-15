import warnings
from tkinter import font
from pygame.locals import *

import pygame, sys

clock = pygame.time.Clock()

# initialization
pygame.init()

# vars (useable)
infoObject = pygame.display.Info()

display_width = infoObject.current_w
display_height = infoObject.current_h

scale_x = display_width / 1920
scale_y = display_height / 1080

screensize = display_width, display_height
screensizetxt = "screensize:" + str(display_width) + 'x' + str(display_height)

black = (0, 0, 0)
white = (255, 255, 255)
red = (225, 0, 0)
bright_red = (255, 100, 0)

lgFont = pygame.font.SysFont("Bungee, Arial", 100)
mdFont = pygame.font.SysFont("Bungee, Arial", 80)
smFont = pygame.font.SysFont("Bungee, Arial", 60)

gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)

menuImg = pygame.image.load('media/menudisplay.png')
menutextImg = pygame.image.load('media/menutext1.png')
iconImg = pygame.image.load('media/fire1.png')
mountainbg = pygame.image.load('media/mountain-bg.png')
skybg = pygame.image.load('media/background.png')
eyebg = pygame.image.load('media/settingsbg.png')
oceanbg = pygame.image.load('media/oceanbg.png')
mouthbg = pygame.image.load('media/mouthbg.gif')
gamescreen = pygame.image.load('media/gamescreen.png')
pygame.display.set_icon(iconImg)
pygame.display.set_caption('Belly Of The Beast')
font = pygame.font.SysFont(None, 20)

# vars (not-useable)
centerdisplayX = (display_width / 2)
centerdisplayY = (display_height / 2)

x = display_width / 2 - menuImg.get_rect().width / 2
y = display_height / 3.75 - menuImg.get_rect().height / 2

text = lgFont.render("Katana Rager", True, red)

fullText = lgFont.render("Press Esc to exit out of fullscreen", True, red)
x1 = display_width / 2 - text.get_rect().width / 2
y1 = (display_height / 1.280 - text.get_rect().height / 2)
y2 = (display_height / 1.15 - text.get_rect().height / 2)
y3 = (display_height / 1.045 - text.get_rect().height / 2)

menuY = display_height / 1.6 - text.get_rect().height / 2
topY = display_height / 10 - text.get_rect().height
bottomY = centerdisplayY * 2 - text.get_rect().height
middleY = display_height / 2 - text.get_rect().height
lowermiddleY = display_height / 1.70 - text.get_rect().height

screenlist = [(1920, 1080), (480, 640), (800, 600), (800, 640), (1024, 768), (1152, 864), (1280, 720), (1280, 960),
              (1280, 1024), (1440, 900)]


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
def setbgeyes():
    gameDisplay.blit(eyebg, (0, 0))


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

# sets oceanbackground in settings
def setbgocean():
    gameDisplay.blit(oceanbg, (0, 0))


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

def setbg():
    gameDisplay.blit(skybg, (0, 0))


# displays menu img and text
def menustart(x, y):
    # filters deprecation warnings

    warnings.filterwarnings("ignore", category=DeprecationWarning)
    gameDisplay.blit(skybg, (display_width, display_height))
    # gameDisplay.blit(menuImg, (x, y))
    gameDisplay.blit(menutextImg, (x, topY))


# creates all main menu buttons
def displayMenubuttons():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # Main Menu Buttons
    if x1 + 620 > mouse[0] > x1 and y1 + 100 > mouse[1] > y1:
        pygame.draw.rect(gameDisplay, bright_red, (x1, y1, 620, 80))
        gameDisplay.blit(smFont.render("START", True, white), (x1, y1))
        if click[0] == 1:
            fade(display_height, display_width)
            game()
    else:
        pygame.draw.rect(gameDisplay, red, (x1, y1, 620, 80))
        gameDisplay.blit(smFont.render("START", True, white), (x1, y1))

    if x1 + 620 > mouse[0] > x1 and y2 + 100 > mouse[1] > y2:
        pygame.draw.rect(gameDisplay, bright_red, (x1, y2, 620, 80))
        gameDisplay.blit(smFont.render("SETTINGS", True, white), (x1, y2))
        if click[0] == 1:
            fade(display_height, display_width)
            Settings()
    else:
        pygame.draw.rect(gameDisplay, red, (x1, y2, 620, 80))
        gameDisplay.blit(smFont.render("SETTINGS", True, white), (x1, y2))

    if x1 + 620 > mouse[0] > x1 and y3 + 100 > mouse[1] > y3:
        pygame.draw.rect(gameDisplay, bright_red, (x1, y3, 620, 80))
        gameDisplay.blit(smFont.render("EXIT", True, white), (x1, y3))
        if click[0] == 1:
            sys.exit()
    else:
        pygame.draw.rect(gameDisplay, red, (x1, y3, 620, 80))
        gameDisplay.blit(smFont.render("EXIT", True, white), (x1, y3))


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
        setbg()
        menustart(x, y)
        displayMenubuttons()
        pygame.display.update()


# player--------------------------------------------


player = pygame.image.load('media/gokuidle.png')
playerlocation = [display_width * .9, 50]
playerYmomentum = 0

moving_right = False
moving_left = False

game_map = [['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '2', '2', '2', '2', '2', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['2', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '2', '2'],
            ['1', '1', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']]

grass_img = pygame.image.load('tiles/floor2.png')
dirt_img = pygame.image.load('tiles/floor.png')

enterscreen = pygame.image.load('media\enterscreenbg.png')


def setbggame():
    gameDisplay.blit(enterscreen, (0, 0))


# Game
def game():
    global moving_right, moving_left, playerYmomentum, player
    running = True
    # GameLoop
    while running:

        for x in range(100):
            gameDisplay.blit(enterscreen, (0, 0))
            gameDisplay.blit(player, playerlocation)
            pygame.display.update()
            pygame.timedelay(100)

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
        # draw_text('game', font, (255, 255, 255), gameDisplay, 20, 20)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    Options()
                if event.key == K_d:
                    moving_right = True
                if event.key == K_a:
                    moving_left = True
            if event.type == KEYUP:
                if event.key == K_d:
                    moving_right = False

                if event.key == K_a:
                    moving_left = False

        pygame.display.update()
        clock.tick(60)


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

        setbgocean()
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

        setbgeyes()
        displayscreenbuttons()
        displayfullscreenbtn()
        pygame.display.update()


# Enter the mainloop----------------------------------------------------------
main_menu()

pygame.quit()
sys.exit()
