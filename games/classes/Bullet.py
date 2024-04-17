import pygame 

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
WIDTH = 1300
HEIGHT = 788
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mixer.pre_init(41000,-16,2,2048)
def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None
""" Tạo đối tượng bullet"""
class Bullet():
    def __init__ (self, x = -100, y = -100, Status = 'Free', Type = 'S'): # Khởi tạo tọa độ ban đầu, trạng thái, loại đạn
        self.x = x
        self.y = y
        self.Bullet = pygame.image.load("images/bullets/yellowbullet/yellowbulletS.png").convert_alpha()
        self.Status = Status
        self.Type = Type
    def DisPlayBullet(self):
        screen.blit(self.Bullet, (self.x, self.y))
        
    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)
    def collision(self, obj):
        return collide(self, obj)
    def Get_Status(self):
        return self.Status
    def Get_x(self):
        return self.x
    def Get_y (self):
        return self.y



