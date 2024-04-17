import pygame
import sys
import random
import math

from classes import SpaceShip, Bullet, Aliens, Meteoric
from pygame import mixer

# Khởi tạo Pygame
pygame.init()

# Cài đặt kích thước cửa sổ
WIDTH = 1300
HEIGHT = 788
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SpaceShip Shooter")
pygame.mixer.pre_init(41000,-16,2,2048)


# Load hình ảnh và âm thanh
background = pygame.image.load("images/backgrounds/bg.png").convert_alpha()
powerup = pygame.image.load("images/power-item/lightning.png").convert_alpha()
livetree = pygame.image.load("images/power-item/livetree.png").convert_alpha()
# Khởi tạo font
font = pygame.font.SysFont('Arial', 32, bold=True)

# Khởi tạo đối tượng SpaceShip
MAIN_SPACE_SHIP = SpaceShip.SpaceShip(WIDTH/2, HEIGHT-100, 'images/spaceShips/arcade.png')
GAME_CONTROL_KEYBOARD = 'Keyboard'
GAME_CONTROL_MOUSE = 'Mouse'
TRIPLE_BULLET_NO = 'No'
TRIPLE_BULLET_YES = 'Yes'

Game_Control = GAME_CONTROL_KEYBOARD
TripleBullet = TRIPLE_BULLET_NO
Rocket = MAIN_SPACE_SHIP
# Khởi tạo danh sách UFO và Meteoric
QuantityUfo =10
ListUfo = [Aliens.Aliens() for _ in range(QuantityUfo )]
ListMeteoric = [Meteoric.Meteoric() for _ in range(QuantityUfo)]
# Hàm để vẽ các phần tử trên màn hình
def draw_elements(score, Number_livetree):
    screen.blit(background, (0, 0))
    for i in range(Number_livetree):
        screen.blit(livetree, (i*50+1, 1))
    img = font.render(f'Score: {score}', True, 'red')
    screen.blit(img, (10, 50))

# Xử lý sự kiện
def handle_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

# Hàm chính của trò chơi

def main():
    Score = 0
    Number_livetree =3

    NumberUfo = 0
    # QuantityUfo =2

    Bullet_Color = 'Yellow'
    Bull = Bullet.Bullet()
    BullL = Bullet.Bullet()
    BullL.Bullet = pygame.image.load("images/bullets/yellowbullet/yellowbulletL.png").convert_alpha()
    BullL.Type = 'L'
    BullR = Bullet.Bullet()
    BullL.Bullet = pygame.image.load("images/bullets/yellowbullet/yellowbulletR.png").convert_alpha()
    BullR.Type = 'R'

    global running
    running = True
    FPS = 60
    clock = pygame.time.Clock()
    while running:
        clock.tick(FPS)
        handle_events()
        draw_elements(Score, Number_livetree)
        Rocket.MoveRocket(GAME_CONTROL_KEYBOARD)
        Rocket.DisPlayRocket()
        if Game_Control == GAME_CONTROL_KEYBOARD:
            Button = pygame.key.get_pressed()
            if (Button[pygame.K_SPACE]) and TripleBullet == TRIPLE_BULLET_NO:
                if Bull.Get_Status() == 'Free':
                    Bull = Rocket.PrepareBullet(Bull, Bullet_Color)
                Rocket.Shoot(Bull, Bullet_Color)
            if (Button[pygame.K_SPACE]) and TripleBullet == TRIPLE_BULLET_YES:
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
        
        if Game_Control == GAME_CONTROL_MOUSE:            
            Mouse = pygame.mouse.get_pressed()
            if (Mouse[0]) and TripleBullet == TRIPLE_BULLET_NO:
                if Bull.Get_Status() == 'Free':
                    Bull = Rocket.PrepareBullet(Bull, Bullet_Color)
                Rocket.Shoot(Bull, Bullet_Color)
            if (Mouse[0]) and TripleBullet == TRIPLE_BULLET_YES:
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

        for i in range(QuantityUfo-NumberUfo):
            ListUfo[i].DisPlayAliens()
        for i in range(QuantityUfo):
            ListMeteoric[i]= ListUfo[i].PrepareMeteoric(ListMeteoric[i], Rocket)
            ListUfo[i].Shoot(ListMeteoric[i])

            if ListUfo[i].Status == 'Live':
                distanceUFO = math.sqrt( (( Bull.Get_x() - ListUfo[i].Get_x() )**2) + (( Bull.Get_y() - ListUfo[i].Get_y() )**2) )
                if distanceUFO < 40 and Bull.Get_y() >= 0 and Bull.Get_y() <= HEIGHT and ListUfo[i].x >= 0 and ListUfo[i].x <= WIDTH  :
                    Bull.x, Bull.y = -100, -100
                    Score += 1
                    ListUfo[i].Status = 'Die'
                    ListUfo[i].x = -100
                    ListUfo[i].y = -100

                    NumberUfo += 1
                    # QuantityUfo-=1
                    print("Stage", 'UFO: ', NumberUfo)
                    print(distanceUFO)

            distaceRocket = math.sqrt( (( ListMeteoric[i].Get_x() - Rocket.Get_x() )**2) + (( ListMeteoric[i].Get_y() - Rocket.Get_y() )**2) )
            if distaceRocket < 30 and ListUfo[i].Status == 'Live':
                    Number_livetree -= 1
                    ListMeteoric[i].x = -100
                    ListMeteoric[i].y = -100
       

            
            
                    
        pygame.display.update()
    


# Chạy trò chơi
if __name__ == '__main__':
    main()
