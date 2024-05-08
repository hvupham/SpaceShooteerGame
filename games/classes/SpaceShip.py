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

class SpaceShip(pygame.sprite.Sprite):
    """
    Đại diện cho tàu vũ trụ trong trò chơi.

    Attributes:
        x (int): Tọa độ x của tàu vũ trụ.
        y (int): Tọa độ y của tàu vũ trụ.
        Rocket (pygame.Surface): Hình ảnh của tàu vũ trụ.

    Methods:
        DisPlayRocket(): Hiển thị tàu vũ trụ trên màn hình.
        MoveRocket(Game_Control): Di chuyển tàu vũ trụ dựa trên bàn phím hoặc chuột.
        PrepareBullet(Bull, Bullet_Color): Chuẩn bị viên đạn để bắn.
        Shoot(Bull, Bullet_Color): Bắn viên đạn.
        Get_x(): Trả về tọa độ x của tàu vũ trụ.
        Get_y(): Trả về tọa độ y của tàu vũ trụ.
    """


    def __init__ (self, x = 700, y = 680, name = ""):
        """
        Khởi tạo một đối tượng tàu vũ trụ với các thuộc tính mặc định hoặc đã chỉ định.

        Args:
            x (int): Tọa độ x ban đầu của tàu vũ trụ.
            y (int): Tọa độ y ban đầu của tàu vũ trụ.
            name (str): Tên tệp hình ảnh của tàu vũ trụ.
        """
        self.x = x
        self.y = y
        self.Rocket = pygame.image.load(name).convert_alpha()


    def DisPlayRocket(self):
        """Hiển thị tàu vũ trụ trên màn hình."""
        screen.blit(self.Rocket, (self.x, self.y))
    def MoveRocket(self, Game_Control ):
        """
        Di chuyển tàu vũ trụ dựa trên bàn phím hoặc chuột.

        Args:
            Game_Control (str): Phương thức điều khiển ('Keyboard' hoặc 'Mouse').
        """
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
            if distance < 200:
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
        
    def PrepareBullet(self, Bull, Bullet_Color):
        if Bull.Get_Status() == 'Free':
            if Bull.Type == 'S':
                if Bullet_Color == 'Yellow':
                    Bull = Bullet.Bullet(self.x - 5, self.y - 50, 'Ready', 'S')
                    Bull.Bullet = pygame.image.load("images/bullets/bull/bullS.png").convert_alpha()           
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
                    Bull.Bullet = pygame.image.load("images/bullets/bull/bullR.png").convert_alpha()
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
                    Bull.Bullet = pygame.image.load("images/bullets/bull/bullL.png").convert_alpha()
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
    
    def Shoot(self, Bull, Bullet_Color):
        """
        Bắn viên đạn.

        Args:
            Bull: Đối tượng viên đạn.
            Bullet_Color (str): Màu của viên đạn.
        """
        if Bull.Type == 'S':
            if Bull.Get_y() < 0:
                Bull.Status = 'Free'
                if Bullet_Color == 'Yellow':
                    Bull.Bullet = pygame.image.load("images/bullets/bull/bullS.png").convert_alpha()           
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
                    Bull.Bullet = pygame.image.load("images/bullets/bull/bullL.png").convert_alpha()           
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
                    Bull.Bullet = pygame.image.load("images/bullets/bull/bullR.png").convert_alpha()           
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
        """
        Trả về tọa độ x của tàu vũ trụ.

        Returns:
            int: Tọa độ x của tàu vũ trụ.
        """
        return self.x
    def Get_y (self):
        """
        Trả về tọa độ y của tàu vũ trụ.

        Returns:
            int: Tọa độ y của tàu vũ trụ.
        """
        return self.y



