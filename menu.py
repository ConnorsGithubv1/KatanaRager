import os
import warnings
from pygame.locals import *
from time import sleep

import pygame, sys

# initialization
pygame.init()


#background music
pygame.mixer.init()
pygame.mixer.music.load('sounds\menumusic.mp3')
pygame.mixer.music.set_volume(0.35)
pygame.mixer.music.play()

# vars-----------------------
# screen info
infoObject = pygame.display.Info()
display_width = infoObject.current_w
display_height = infoObject.current_h
screensize = display_width, display_height

# file paths
settingspath = "settings.py"
gamepath = "game.py"

# screen created
menuDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)

# images
menuImg = pygame.image.load('media/menudisplay.png')
menutextImg = pygame.image.load('media/menutext1.png')

bg1 = 'media/menu/01background1.png'
bg2 = 'media/menu/01background2.png'
bg3 = 'media/menu/01background3.png'
bg4 = 'media/menu/01background4.png'
bg5 = 'media/menu/01background5.png'
bg6 = 'media/menu/01background6.png'
bg7 = 'media/menu/01background7.png'


luffybg = pygame.image.load('media/luffybg.png')

imglist = [bg1, bg2, bg3, bg4, bg5, bg6, bg7]


#colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (170, 0, 0, 128)
bright_red = (255, 100, 0)
blueviolet = (138, 43, 226)
purple = (147, 112, 219)

# fonts
lgFont = pygame.font.SysFont("Bungee, Arial", 100)
mdFont = pygame.font.SysFont("Bungee, Arial", 80)
smFont = pygame.font.SysFont("Bungee, Arial", 60)

# dont know what this is used for
text = lgFont.render("belly of the beast", True, red)

# all X coordinates
centerdisplayX = (display_width / 2)
x = display_width / 2 - menuImg.get_rect().width / 2
x1 = display_width - text.get_rect().width / 2

# all Y coordinates
centerdisplayY = (display_height / 2)
y = display_height / 3.75 - menuImg.get_rect().height / 2
y1 = (display_height / 2 - (text.get_rect().height / 2))
y2 = y1 + 75
y3 = y2 + 75
menuY = display_height / 1.6 - text.get_rect().height / 2
topY = display_height / 10 - text.get_rect().height

# button lengths (used for start, settings, and exit button)
btnXlen = 300
btnYlen = 70

#functions--------------------------------------------------
# used to fade out of screens
def fade(width, height):

    fade = pygame.Surface((screensize))
    fade.fill((0, 0, 0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        menuDisplay.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(1)

# sets the background to a selected image
def setbg(imglist):

    x = 0
    z = 0
    while z < 100:
        while x < 7:
            img = imglist[x]
            print(img)
            a = pygame.image.load(img)
            menuDisplay.blit(pygame.transform.scale(a, (display_width, display_height)), (0, 0))
            x = x + 1
            if x == 6:
                x = 0
            z = z + 1

    """
    img = " "
    x = 0
    while x > 7:
        img = list[0]
        menuDisplay.blit(pygame.transform.scale(img, (display_width, display_height)), (0, 0))
        x + 1
        if x == 6:
            x = 0
    """

#finds position of mouse
def mousePos():
    return pygame.mouse.get_pos()


# work in progress
def menustart():
    # filters deprecation warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)


# finds the postion of a given button
def buttonposition(button):
    pos = 0
    return pos

# creates a useable button
def createbtn(xpos, ypos, name, color, xlen, ylen):
    pygame.draw.rect(menuDisplay, color, (xpos, ypos, xlen, ylen))
    menuDisplay.blit(smFont.render(name, True, white), (xpos, ypos))

# Start button // starts game
def startbtn():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    #checks if mouse is hovering over button / checks if button is clicked
    if x1 + btnXlen > mouse[0] > x1 and y1 + btnYlen > mouse[1] > y1:
        createbtn(x1, y1, 'START', purple, btnXlen, btnYlen)
        if click[0] == 1:
            fade(display_height, display_width)
            os.startfile(gamepath)
            sys.exit()
    else:
        createbtn(x1, y1, 'START', blueviolet, btnXlen, btnYlen)

# settings button // used to access redirect user to settings screenF
def settingsbtn():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    #checks if mouse is hovering over button / checks if button is clicked
    if x1 + btnXlen > mouse[0] > x1 and y2 + btnYlen > mouse[1] > y2:
        createbtn(x1, y2, "SETTINGS", purple, btnXlen, btnYlen)
        if click[0] == 1:
            fade(display_height, display_width)
            os.startfile(settingspath)
    else:
        createbtn(x1, y2, "SETTINGS", blueviolet, btnXlen, btnYlen)

# exit Button // ends menu screen and closes game
def exitbtn():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # checks if mouse is hovering over button / checks if button is clicked
    if x1 + btnXlen > mouse[0] > x1 and y3 + btnYlen > mouse[1] > y3:
        createbtn(x1, y3, "EXIT", purple, btnXlen, btnYlen)
        if click[0] == 1:
            sys.exit()
    else:
        createbtn(x1, y3, "EXIT", blueviolet, btnXlen, btnYlen)


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



        menuDisplay.fill(black)
        setbg(imglist)
        menustart()
        startbtn()
        settingsbtn()
        exitbtn()
        mousePos()

        pygame.display.update()



# Enter the mainloop----------------------------------------------------------
main_menu()

pygame.quit()
sys.exit()