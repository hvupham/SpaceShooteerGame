import pygame , time, sys
import random
import math
from pygame import mixer
from classes import Bullet
import time
WIDTH = 1300
HEIGHT = 788
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mixer.pre_init(41000,-16,2,2048)
""" Tạo đối tượng SpaceShip"""
class SpaceShip(pygame.sprite.Sprite):
    # Khởi tạo tọa độ ban đầu và load hình ảnh của tàu vũ trụ
    def __init__ (self, x = 700, y = 680, name = ""):
        self.x = x
        self.y = y
        self.Rocket = pygame.image.load(name).convert_alpha()
    
    # Tạo phương thức để xử lý việc di chuyển của tàu vũ trụ (điều khiển bằng bàn phím hoặc chuột)
    def MoveRocket(self, Game_Control ):
        if Game_Control == 'Keyboard':
            Button = pygame.key.get_pressed()
            # Trong phương thức MoveRocket()
            if (Button[pygame.K_w] or Button[pygame.K_UP]) and self.y >= 0:
                self.y -= 10
            if (Button[pygame.K_s] or Button[pygame.K_DOWN]) and self.y <= HEIGHT-30:
                self.y += 10
            if (Button[pygame.K_a] or Button[pygame.K_LEFT]) and self.x >= 10:
                self.x -= 10
            if (Button[pygame.K_d] or Button[pygame.K_RIGHT]) and self.x <= WIDTH-40:
                self.x += 10
        if Game_Control == 'Mouse':
            pos = pygame.mouse.get_pos() # trả về tọa độ con trỏ chuột
            distance = math.sqrt( (( pos[0] - self.x )**2) + (( pos[1] - self.y )**2) )
            if pos[0] >= 0 and pos[0] <= WIDTH and pos[1] >= 0 and pos[1] <= HEIGHT: 
                if distance > 1:
                    if self.x < pos[0] and self.y > pos[1]:
                        self.x += 10
                        self.y -= 10
                    if self.x < pos[0] and self.y < pos[1]:
                        self.x += 10
                        self.y += 10
                    if self.x > pos[0] and self.y > pos[1]:
                        self.x -= 10
                        self.y -= 10
                    if self.x > pos[0] and self.y < pos[1]:
                        self.x -= 10
                        self.y += 10
        
    # hiển thị tàu vũ trụ lên màn hình

    def DisPlayRocket(self):
        screen.blit(self.Rocket, (self.x, self.y))

    # Xử lý việc bắn đạn từ tàu vũ trụ
    def PrepareBullet(self, Bull, Bullet_Color):
        if Bull.Get_Status() == 'Free':
            if Bull.Type == 'S':
                if Bullet_Color == 'Yellow':
                    Bull = Bullet.Bullet(self.x - 5, self.y - 50, 'Ready', 'S')
                    Bull.Bullet = pygame.image.load("images/bullets/yellowbullet/yellowbulletS.png").convert_alpha()           
                if Bullet_Color == 'Red':
                    Bull = Bullet.Bullet(self.x - 22 , self.y - 90, 'Ready', 'S')
                    Bull.Bullet = pygame.image.load("images/bullets/redbullet/redbulletS.png").convert_alpha()          
                if Bullet_Color == 'Blue':
                    Bull = Bullet.Bullet(self.x - 3, self.y - 90, 'Ready', 'S')
                    Bull.Bullet = pygame.image.load("images/bullets/bluebullet/bluebulletS.png").convert_alpha()          
                if Bullet_Color == 'Green':
                    Bull = Bullet.Bullet(self.x - 5, self.y - 90, 'Ready', 'S')
                    Bull.Bullet = pygame.image.load("images/bullets/greenbullet/greenbulletS.png").convert_alpha()
           
            if Bull.Type == 'R':
                if Bullet_Color == 'Yellow':
                    Bull = Bullet.Bullet(self.x - 10, self.y - 60, 'Ready', 'R')
                    Bull.Bullet = pygame.image.load("images/bullets/yellowbullet/yellowbulletR.png").convert_alpha()
                if Bullet_Color == 'Red':
                    Bull = Bullet.Bullet(self.x - 30, self.y - 90, 'Ready', 'R')
                    Bull.Bullet = pygame.image.load("images/bullets/redbullet/redbulletR.png").convert_alpha()
                if Bullet_Color == 'Blue':
                    Bull = Bullet.Bullet(self.x - 20, self.y - 80, 'Ready', 'R')
                    Bull.Bullet = pygame.image.load("images/bullets/bluebullet/bluebulletR.png").convert_alpha()
                if Bullet_Color == 'Green':
                    Bull = Bullet.Bullet(self.x - 20, self.y - 80, 'Ready', 'R')
                    Bull.Bullet = pygame.image.load("images/bullets/greenbullet/greenbulletR.png").convert_alpha()

            if Bull.Type == 'L':
                if Bullet_Color == 'Yellow':
                    Bull = Bullet.Bullet(self.x - 40, self.y - 60, 'Ready', 'L')
                    Bull.Bullet = pygame.image.load("images/bullets/yellowbullet/yellowbulletL.png").convert_alpha()
                if Bullet_Color == 'Red':
                    Bull = Bullet.Bullet(self.x - 70, self.y - 90, 'Ready', 'L')
                    Bull.Bullet = pygame.image.load("images/bullets/redbullet/redbulletL.png").convert_alpha()
                if Bullet_Color == 'Blue':
                    Bull = Bullet.Bullet(self.x - 70, self.y - 90, 'Ready', 'L')
                    Bull.Bullet = pygame.image.load("images/bullets/bluebullet/bluebulletL.png").convert_alpha()
                if Bullet_Color == 'Green':
                    Bull = Bullet.Bullet(self.x - 70, self.y - 90, 'Ready', 'L')
                    Bull.Bullet = pygame.image.load("images/bullets/greenbullet/greenbulletL.png").convert_alpha()

        return Bull
    
    # Xử lý việc bắn đạn từ tàu vũ trụ
    def Shoot(self, Bull, Bullet_Color):
        if Bull.Type == 'S':
            if Bull.Get_y() < 0:
                Bull.Status = 'Free'
                if Bullet_Color == 'Yellow':
                    Bull.Bullet = pygame.image.load("images/bullets/yellowbullet/yellowbulletS.png").convert_alpha()           
                if Bullet_Color == 'Red':
                    Bull.Bullet = pygame.image.load("images/bullets/redbullet/redbulletS.png").convert_alpha()         
                if Bullet_Color == 'Blue':
                    Bull.Bullet = pygame.image.load("images/bullets/bluebullet/bluebulletS.png").convert_alpha()         
                if Bullet_Color == 'Green':
                    Bull.Bullet = pygame.image.load("images/bullets/greenbullet/greenbulletS.png").convert_alpha()     
                Bull.Type = 'S'
                Bull.x = -100
                Bull.y = -100

            if Bull.Get_Status() == 'Ready':
                Bull.y -= 30
                Bull.DisPlayBullet()
               
        elif Bull.Type == 'L':
            if Bull.Get_y() < 0:
                Bull.Status = 'Free'
                if Bullet_Color == 'Yellow':
                    Bull.Bullet = pygame.image.load("images/bullets/yellowbullet/yellowbulletL.png").convert_alpha()           
                if Bullet_Color == 'Red':
                    Bull.Bullet = pygame.image.load("images/bullets/redbullet/redbulletL.png").convert_alpha()         
                if Bullet_Color == 'Blue':
                    Bull.Bullet = pygame.image.load("images/bullets/bluebullet/bluebulletL.png").convert_alpha()         
                if Bullet_Color == 'Green':
                    Bull.Bullet = pygame.image.load("images/bullets/greenbullet/greenbulletL.png").convert_alpha()
                Bull.Type = 'L'
                Bull.x = -100
                Bull.y = -100
            if Bull.Get_Status() == 'Ready':
                Bull.y -= 20
                Bull.x -= 15
                Bull.DisPlayBullet()
                

        elif Bull.Type == 'R':
            if Bull.Get_y() < 0:
                Bull.Status = 'Free'
                if Bullet_Color == 'Yellow':
                    Bull.Bullet = pygame.image.load("images/bullets/yellowbullet/yellowbulletR.png").convert_alpha()           
                if Bullet_Color == 'Red':
                    Bull.Bullet = pygame.image.load("images/bullets/redbullet/redbulletR.png").convert_alpha()         
                if Bullet_Color == 'Blue':
                    Bull.Bullet = pygame.image.load("images/bullets/bluebullet/bluebulletR.png").convert_alpha()         
                if Bullet_Color == 'Green':
                    Bull.Bullet = pygame.image.load("images/bullets/greenbullet/greenbulletR.png").convert_alpha()
                Bull.Type = 'R'
                Bull.x = -100
                Bull.y = -100
            if Bull.Get_Status() == 'Ready':
                Bull.y -= 20
                Bull.x += 15
                Bull.DisPlayBullet()
                
        

    
    def Get_x(self):
        return self.x
    def Get_y (self):
        return self.y



