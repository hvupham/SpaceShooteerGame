import pygame , time, sys
import random
import math
from pygame import mixer
import time
from classes import Bullet
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
screen = pygame.display.set_mode((1400, 788))

# Load hình ảnh con chuột
NewCursor = pygame.image.load("images/setting-items/newcursor.png")
def Draw_MouseCursor():
    # if Game_Control == 'Mouse' and Game_Menu == False and InGame == True and OptionStatus == False and Game_Over == False and Game_Win == False:
    #     screen.blit( NewCursor, (-100, -100) )
    # else:
    pos = pygame.mouse.get_pos()
    screen.blit( NewCursor, (pos[0] - 12, pos[1] - 3) )

class Button():
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False        
    def Draw(self):
        screen.blit(self.image, (self.x, self.y))
    def Click(self):
        Draw_MouseCursor()
        pygame.mouse.set_visible(False)
        IsClick = False
        Mouse = pygame.mouse.get_pressed()        
        pos = pygame.mouse.get_pos()            
        if self.rect.collidepoint(pos):            
            if self.clicked == False and Mouse[0]:
                self.clicked = True
                IsClick = True
        if Mouse[0] == 0:
            self.clicked = False       
        return IsClick
pygame.init()