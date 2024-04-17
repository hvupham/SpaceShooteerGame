import pygame, sys
import os
import time
import random
from pygame import mixer
from classes import SpaceShip
from classes import Bullet
from classes import Aliens
from classes import Meteoric

pygame.init()

WIDTH = 1300
HEIGHT = 788
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mixer.pre_init(41000,-16,2,2048)
pygame.display.set_caption("SpaceShip Shotter")


#STAGE


# load background
BackGround = pygame.image.load("images/backgrounds/bg.png").convert_alpha()
BG_Move_Y = 0
Score = 0
Game_Control = 'Keyboard'
TripleBullet = 'No'
MAIN_SPACE_SHIP = SpaceShip.SpaceShip(WIDTH/2, HEIGHT-100, 'images/spaceShips/arcade.png')

# MAIN_SPACE_SHIP1 = SpaceShip.SpaceShip(700, 680, 'images/spaceShips/spaceship.png')
# MAIN_SPACE_SHIP2 = SpaceShip.SpaceShip(700, 680, 'images/spaceShips/spaceship1.png')
# MAIN_SPACE_SHIP3 = SpaceShip.SpaceShip(700, 680, 'images/spaceShips/spaceship.png')
powerup = pygame.image.load("images/power-item/lightning.png").convert_alpha()
#Create Live Tree
livetree = pygame.image.load("images/power-item/livetree.png").convert_alpha()

font=pygame.font.SysFont('Arial',32,'bold')
font_stage=pygame.font.SysFont('Arial',100,'bold')
font_gameover=pygame.font.SysFont('Arial',100,'bold')
font_sound = pygame.font.SysFont('Arial', 32, 'bold')
font_SpaceShip = pygame.font.SysFont('Arial', 32, 'bold')
font_Success = pygame.font.SysFont('Arial', 32, 'bold')

Rocket = MAIN_SPACE_SHIP
def Draw_BackGround():
    screen.blit(BackGround, (0,BG_Move_Y) )
    screen.blit(BackGround, (0, -788 + BG_Move_Y) )

    img=font.render(f'Score:{Score}',True,'red')
    screen.blit(img,(10,50))
    screen.blit(livetree,(1,1))

    # CreateUFO()
    MAIN_SPACE_SHIP.MoveRocket(Game_Control)
    MAIN_SPACE_SHIP.DisPlayRocket()
    Ufo.DisPlayAliens()
    pygame.display.update()

AILIEN ="images/ailens/alien.png"
AILIEN1 ='images/ailens/alien1.png'
ENEMY ='images/ailens/enemy.png'
METEORIC = Meteoric.Meteoric()  

Ufo = Aliens.Aliens()


ListUfo = []
ListMeteoric= []
for i in range(5):
    ailien =  Aliens.Aliens()
    ListUfo.append(ailien)
for i in range(5):
    M = Meteoric.Meteoric()
    ListMeteoric.append(M)


Bullet_Color = 'Yellow'
Bull = Bullet.Bullet()
BullL = Bullet.Bullet()
BullL.Bullet = pygame.image.load("images/bullets/yellowbullet/yellowbulletL.png").convert_alpha()
BullL.Type = 'L'
BullR = Bullet.Bullet()
BullL.Bullet = pygame.image.load("images/bullets/yellowbullet/yellowbulletR.png").convert_alpha()
BullR.Type = 'R'


if __name__ == '__main__':
    run =True
    FPS = 60
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        Draw_BackGround()
        # RocketShoot(Bull, Bullet_Color,TripleBullet)
        if Game_Control == 'Keyboard':
            Button = pygame.key.get_pressed()
            if (Button[pygame.K_SPACE]) and TripleBullet == 'No':
                if Bull.Get_Status() == 'Free':
                    Bull = Rocket.PrepareBullet(Bull, Bullet_Color)
                Rocket.Shoot(Bull, Bullet_Color)
            if (Button[pygame.K_SPACE]) and TripleBullet == 'Yes':
                if Bull.Get_Status() == 'Free':
                    Bull = Rocket.PrepareBullet(Bull, Bullet_Color)              
                if BullL.Get_Status() == 'Free':
                    BullL = Rocket.PrepareBullet(BullL, Bullet_Color)          
                if BullR.Get_Status() == 'Free':
                    BullR = Rocket.PrepareBullet(BullR, Bullet_Color)
                if Bull.Get_Status() == 'Ready' and BullL.Get_Status() == 'Ready' and BullR.Get_Status() == 'Ready':
                    Rocket.Shoot(Bull, Bullet_Color)
                    Rocket.Shoot(BullL, Bullet_Color)
                    Rocket.Shoot(BullR, Bullet_Color)
        if Game_Control == 'Mouse':            
            Mouse = pygame.mouse.get_pressed()
            if (Mouse[0]) and TripleBullet == 'No':
                if Bull.Get_Status() == 'Free':
                    Bull = Rocket.PrepareBullet(Bull, Bullet_Color)
                Rocket.Shoot(Bull, Bullet_Color)
            if (Mouse[0]) and TripleBullet == 'Yes':
                if Bull.Get_Status() == 'Free':
                    Bull = Rocket.PrepareBullet(Bull, Bullet_Color)              
                if BullL.Get_Status() == 'Free':
                    BullL = Rocket.PrepareBullet(BullL, Bullet_Color)          
                if BullR.Get_Status() == 'Free':
                    BullR = Rocket.PrepareBullet(BullR, Bullet_Color)
                if Bull.Get_Status() == 'Ready' and BullL.Get_Status() == 'Ready' and BullR.Get_Status() == 'Ready':
                    Rocket.Shoot(Bull, Bullet_Color)
                    Rocket.Shoot(BullL, Bullet_Color)
                    Rocket.Shoot(BullR, Bullet_Color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        
        for i in range(5):
            ListMeteoric[i] = ListUfo[i].PrepareMeteoric(ListMeteoric[i], Rocket, StraightI = 'meteoricS.png' ,LeftI = 'meteoricL.png', RightI = 'images/meteorics/meteoricR.png')           
            #Shoot
        # CreateUFO(AILIEN)

        for i in range(5):
            ListUfo[i].DisPlayAliens()
            METEORIC = ListUfo[i].PrepareMeteoric(METEORIC, Rocket)
            ListUfo[i].Shoot(METEORIC)

        pygame.display.update()






