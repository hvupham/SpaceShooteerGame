import pygame 
import random
from classes import Meteoric
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
WIDTH = 1300
HEIGHT = 788
screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Aliens():
    def __init__ (self, x = -100, y = -100, Image = "images/ailens/alien1.png"):
        self.x = x
        self.y = y
        self.UFO = pygame.image.load(Image).convert_alpha()
        self.velocity = 5
        self.Status = 'Live'
        self.Blood = 150
    def DisPlayAliens (self):
        if self.x < 0:
            self.x = random.randint(5,WIDTH-100)
            self.y = random.randint(40,70)
        if self.x >= 0 and self.x <= WIDTH and self.y <= HEIGHT and self.y >= 0:
            if self.x <= 20:
                self.velocity = random.randint(3,8)
            elif self.x >= WIDTH-100:
                self.velocity = random.randint(-8,-3)        
            screen.blit(self.UFO, (self.x, self.y))
            self.x += self.velocity
    def PrepareMeteoric(self, METEORIC, Rocket, StraightI = 'images/meteorics/meteoricS.png' ,LeftI = 'images/meteorics/meteoricL.png', RightI = 'images/meteorics/meteoricR.png'):
        if METEORIC.Get_Status() == 'Free' and self.Status == 'Live':
            if Rocket.Get_x() <= 10 :
                METEORIC = Meteoric.Meteoric(self.x + 30, self.y + 30, LeftI,'Ready', 'Left')
            elif Rocket.Get_x() >= 1300:
                METEORIC = Meteoric.Meteoric(self.x + 30, self.y + 30, RightI,'Ready', 'Right')
            else:
                if abs(self.x - Rocket.Get_x()) <= 250:
                    METEORIC = Meteoric.Meteoric(self.x + 30, self.y + 30, StraightI ,'Ready', 'Straight')
                if self.x - Rocket.Get_x() > 250:
                    METEORIC = Meteoric.Meteoric(self.x + 30, self.y + 30, LeftI,'Ready', 'Left')
                if self.x - Rocket.Get_x() < -250:
                    METEORIC = Meteoric.Meteoric(self.x + 30, self.y + 30, RightI,'Ready', 'Right')                
        return METEORIC
    def Shoot(self, METEORIC):
        if METEORIC.Type == 'Left' and METEORIC.Status == 'Ready':          
            METEORIC.x -= METEORIC.velocityMeteoric
            METEORIC.y += METEORIC.velocityMeteoric
            METEORIC.DisPlayMeteoric()           
        if METEORIC.Type == 'Right' and METEORIC.Status == 'Ready':          
            METEORIC.x += METEORIC.velocityMeteoric
            METEORIC.y += METEORIC.velocityMeteoric
            METEORIC.DisPlayMeteoric()
        if METEORIC.Type == 'Straight' and METEORIC.Status == 'Ready':          
            METEORIC.y += METEORIC.velocityMeteoric
            METEORIC.DisPlayMeteoric()
        if METEORIC.x < 0 or METEORIC.y < 0 or METEORIC.x > 1400 or METEORIC.y > 788:
            METEORIC.Status = 'Free'
    def Get_x(self):
        return self.x
    def Get_y (self):
        return self.y
    def Boom(self):
        self.UFO = pygame.image.load("images/orther/boom.png").convert_alpha()
        self.DisPlayAliens()



