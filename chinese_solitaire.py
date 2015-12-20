import pygame, sys
from time import sleep
from pygame.locals import *
from pygame.sprite import *

# Setup tpygame
pygame.init()

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 153, 0)
RED = (193, 0, 0)
GRAY = (112, 138, 144)
SAND = (240, 240, 230) 

# Font
my_font = pygame.font.Font(None, 18)
my_font.set_bold(True)

# set up the window
xAxis = 294
yAxis = 324

gameWindow = pygame.display.set_mode((xAxis, yAxis))
pygame.display.set_caption('Chinese Solitaire')
gameWindow.fill(SAND)

# Create the buttons
newLabel = my_font.render("New Game", 1, BLACK)
resignLabel = my_font.render("Resign", 1, BLACK)
pygame.draw.line(gameWindow, BLACK, (147,1), (147,30), 4)
gameWindow.blit(newLabel, (25,5))
gameWindow.blit(resignLabel, (190,5))

# Create the Borders
# Horizontal Borders
pygame.draw.line(gameWindow, BLACK, (0,1), (yAxis-1,1), 4)
pygame.draw.line(gameWindow, BLACK, (0,yAxis-3), (xAxis,yAxis-3), 4)
pygame.draw.line(gameWindow, BLACK, (0,30), (yAxis-1,30), 4)
# Vertical Borders
pygame.draw.line(gameWindow, BLACK, (xAxis-3,1), (xAxis-3,yAxis), 4)
pygame.draw.line(gameWindow, BLACK, (1,0), (1,yAxis-1), 4)

# Block size is 30x30px; line size is 2px
# Draw the lines (every 32px starting from 34)
for x in range(34, xAxis, 32):
    pygame.draw.line(gameWindow, BLACK, (x,30), (x,yAxis), 2)
for y in range(64, yAxis, 32):
    pygame.draw.line(gameWindow, BLACK, (0,y), (xAxis,y), 2)





pygame.display.update()

for i in range(1,10):
    sleep(2)

pygame.quit()

class Tile(Sprite):
    # __full = None
    # __avaliable = None
    # __selected = None

    # def __init__(self, full, aval, sel):
    #     Sprite.__init__(self)
    #     self.__full = full
    #     self.__avaliable = aval
    #     self.__selected = sel

    # def setFull(self, full):
    #     self.__full = full

    # def getFull(self):
    #     return self.__full

    # def setAvaliable(self, aval):
    #     self.__avaliable = aval

    # def getAvaliable(self):
    #     return self.__avaliable

    # def setSelected(self, sel):
    #     self.__selected = sel

    # def getSelected(self):
    #     return self.__selected
    
    def __init__(self, full, aval, sel):
        Sprite.__init__(self)
        self.full = full
        self.avaliable = aval
        self.selected = sel
        self.image = None

    #TODO continue the class Tile and ChineseSolitaire  


# this one will inherit Board
class ChineseSolitaire():
    __playable = None
    



    __init__(self,)











# Resolution

# horiz = 270
# vert = 270

# my_screen = pygame.display.set_mode((horiz, vert), 0 , 32)
# pygame.display.set_caption('Chinese Solitaire')

# WHITE =(255, 255, 255)
# BLACK =(0, 0, 0)
# color = WHITE
# my_screen.fill(color)

# pygame.display.update()

# x = True
# while x:

#     for ev in pygame.event.get():
#         if ev.type == QUIT:
#             pygame.quit()           
#             sys.exit()
#         if ev.type == KEYDOWN:
#             x = True
#         if ev.type == MOUSEBUTTONDOWN:
#             x = False
#     my_font = pygame.font.SysFont(None, 32)
#     my_text = my_font.render("Remove all the bilies",\
#                              True, BLACK, WHITE)
#     my_screen.blit(my_text, (20,20))

#     my_text = my_font.render("(...continue)",\
#                              True, BLACK, WHITE)
#     my_screen.blit(my_text, (20,100))
#     pygame.display.update()


# class Tile(Sprite):
#     def __init__(self, createX, createY, dimX, dimY):
#         Sprite.__init__(self)
#         self.rect = pygame.Rect(createX, createY, dimX, dimY)
#         self.isEmpty = True
#         self.image = None

#     def empty(self):
#         self.isEmpty = True
#         self.image = None

#     def load(self, item, surf):
#         self.isEmpty = False
#         surf.blit(self.transimage, self.rect)

# class Board(Group):
    
#     def __init__(self):
#         Group.__init__(self)

