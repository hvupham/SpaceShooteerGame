import pygame 
import time
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
WIDTH = 1300 
HEIGHT = 788
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mixer.pre_init(41000,-16,2,2048)

class Meteoric():
    def __init__ (self, x = -100, y = -100, Meteoric = 'images/meteorics/meteoricS.png', Status = 'Free', Type = 'Straight'):
        self.x = x 
        self.y = y
        self.Meteoric = pygame.image.load(Meteoric).convert_alpha()
        self.Status = Status
        self.Type = Type
        self.velocityMeteoric = 3
    def DisPlayMeteoric(self):
        screen.blit( self.Meteoric, (self.x, self.y) )
    def Get_Status(self):
        return self.Status
    def Get_x(self):
        return self.x
    def Get_y (self):
        return self.y
    def Get_Type(self):
        return self.Type




