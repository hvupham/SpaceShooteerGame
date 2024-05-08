import pygame 
pygame.init()
screen = pygame.display.set_mode((1400, 788))

NewCursor = pygame.image.load("images/setting-items/newcursor.png")
def Draw_MouseCursor():
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
    def Get_x(self):
        return self.x
    def Get_y (self):
        return self.y

pygame.init()