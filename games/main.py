import pygame
import sys
import random
import math

from classes import SpaceShip, Bullet, Aliens, Meteoric
from classes import Button
from pygame import mixer

# Khởi tạo Pygame
pygame.init()

# Cài đặt kích thước cửa sổ
WIDTH = 1300
HEIGHT = 788
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SpaceShip Shooter")
pygame.mixer.pre_init(41000,-16,2,2048)

font_SpaceShip = pygame.font.SysFont('Arial', 32, 'bold')


# Load hình ảnh
background = pygame.image.load("images/backgrounds/bg.png").convert_alpha()
background1 = pygame.image.load("images/backgrounds/bg2.png").convert_alpha()
background2 = pygame.image.load("images/backgrounds/bg3.png").convert_alpha()
background3 = pygame.image.load("images/backgrounds/bg4.png").convert_alpha()
background4 = pygame.image.load("images/backgrounds/bg5.png").convert_alpha()
powerup = pygame.image.load("images/power-item/lightning.png").convert_alpha()
livetree = pygame.image.load("images/power-item/livetree.png").convert_alpha()
# Khởi tạo font
font = pygame.font.SysFont('Arial', 32, bold=True)

# Khởi tạo đối tượng SpaceShip
MAIN_SPACE_SHIP = SpaceShip.SpaceShip(WIDTH/2, HEIGHT-100, 'images/spaceShips/arcade.png')
SPACE_SHIP1 = SpaceShip.SpaceShip(WIDTH/2, HEIGHT-100, 'images/spaceShips/spaceship.png')
SPACE_SHIP2 = SpaceShip.SpaceShip(WIDTH/2, HEIGHT-100, 'images/spaceShips/spaceship1.png')
SPACE_SHIP3 = SpaceShip.SpaceShip(WIDTH/2, HEIGHT-100, 'images/spaceShips/spaceship2.png')


GAME_CONTROL_KEYBOARD = 'Keyboard'
GAME_CONTROL_MOUSE = 'Mouse'
TRIPLE_BULLET_NO = 'No'
TRIPLE_BULLET_YES = 'Yes'

TripleBullet = TRIPLE_BULLET_NO
Rocket = MAIN_SPACE_SHIP

# create button
if True:
    playbutton = "images/setting-items/play.png"
    optionbutton = "images/setting-items/option.png"
    quitbutton = "images/setting-items/quit.png"
    resumebutton = "images/setting-items/resume.png"
    pause = "images/setting-items/pause.png"
    musicon = "images/setting-items/musicon.png"
    musicoff = "images/setting-items/musicoff.png"
    backbutton = "images/setting-items/back.png"
    replay = "images/setting-items/replay.png"
    quitbutton1 = "images/setting-items/exit.png"
    boom = "images/orther/boom.png"
    lt = "images/setting-items/livetree.png"
    pu = "images/setting-items/lightning.png"
    nextleft = "images/setting-items/nextleft.png"
    nextright = "images/setting-items/nextright.png"

    PlayButton = Button.Button(WIDTH/2-100, HEIGHT/2 - 100, playbutton)
    OptionButton = Button.Button(WIDTH/2-100, HEIGHT/2 , optionbutton)
    QuitButton = Button.Button(WIDTH/2-100, HEIGHT/2 + 100, quitbutton)
    ResumeButton = Button.Button(WIDTH/2-100, HEIGHT/2 - 100, resumebutton)
    PauseButton = Button.Button(WIDTH-80,10,pause)

    SoundStatusOn = Button.Button(730, 130, musicon)
    SoundStatusOff = Button.Button(730, 130, musicoff)
    BackButton = Button.Button(10, 10, backbutton)
    Replay = Button.Button(380, 500, replay)
    ExitButton = Button.Button(700,500, quitbutton1)
    Boom = Button.Button(-100,-100,boom)
    NextLeft = Button.Button(630, 460, nextleft)
    NextRight = Button.Button(890, 460, nextright)
    arBulletLeft = Button.Button(630, 250, nextleft)
    arBulletRight = Button.Button(890, 250, nextright)
    arControlLeft = Button.Button(630, 350, nextleft)
    arControlRight = Button.Button(890, 350, nextright)
    arRocketLeft = Button.Button(630, 450, nextleft)
    arRocketRight = Button.Button(890, 450, nextright)



choose_successfully = pygame.USEREVENT + 1
pygame.time.set_timer(choose_successfully, 2000)
DropLiveTree = 'No'
DropPowerUp = 'No'
time_use_power_up = pygame.USEREVENT + 5
pygame.time.set_timer(time_use_power_up, 10000)
Stage_Event = pygame.USEREVENT + 6
pygame.time.set_timer(Stage_Event, 3500)

# Khởi tạo danh sách UFO và Meteoric
QuantityUfo =10
QuantityUfo1 =15




ListUfo = [Aliens.Aliens() for _ in range(QuantityUfo )]
ListUfo1 = [Aliens.Aliens(-100,-100,"images/ailens/enemy.png") for _ in range(QuantityUfo )]
ListMeteoric = [Meteoric.Meteoric() for _ in range(QuantityUfo)]
ListMeteoric1 = [Meteoric.Meteoric(-100,-100,"images/meteorics/meteoric1.png") for _ in range(QuantityUfo)]

ExplosionMusic = mixer.Sound("sounds/explosion.wav")
ExplosionMusic.set_volume(0.8)
LaserMusic = mixer.Sound("sounds/laser.wav")
LaserMusic.set_volume(0.8)
LevelPassMusic = mixer.Sound("sounds/level.wav")

# Hàm để vẽ các phần tử trên màn hình
def draw_elements(score, Number_livetree, background):
    screen.blit(background, (0, 0))
    for i in range(Number_livetree):
        screen.blit(livetree, (i*50+1, 1))
    img = font.render(f'Score: {score}', True, 'red')
    screen.blit(img, (10, 50))


font_stage=pygame.font.SysFont('Arial',100,'bold')
def Display_Stage(Stage):
    img = font_stage.render(f'STAGE : {Stage}', True, 'red')
    screen.blit(img, (550,300))
# Xử lý sự kiện
def handle_events(Choose,DropLiveTree, DropPowerUp, TripleBullet, Stage_Status):
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == choose_successfully:
            if Choose == 'Yes':
                Choose = 'No'
        
        if event.type == livetree:
            if DropLiveTree == 'No':
                DropLiveTree = 'Yes'

        if event.type == powerup:
            if DropPowerUp == 'No':
                DropPowerUp = 'Yes'

        if event.type == time_use_power_up:
            if TripleBullet == TRIPLE_BULLET_YES:
                TripleBullet = TRIPLE_BULLET_NO

        if event.type == Stage_Event:
            if Stage_Status == 'Yes':
                Stage_Status = 'No'
def Draw_Sound():
    img = pygame.image.load("soundicon.png").convert_alpha()
    screen.blit(img, (620,140))

# Hàm chính của trò chơi
#Create Play Button


def DisplayBulletColor(Bullet_Color = 'Yellow'):
    if Bullet_Color == 'Yellow':
        img = pygame.image.load("images/bullets/yellowbullet/yellowbullet.png").convert_alpha()
    if Bullet_Color == 'Red':
        img = pygame.image.load("images/bullets/redbullet/redbullet.png").convert_alpha()
    if Bullet_Color == 'Blue':
        img = pygame.image.load("images/bullets/bluebullet/bluebullet.png").convert_alpha()
    if Bullet_Color == 'Green':
        img = pygame.image.load("images/bullets/greenbullet/greenbullet.png").convert_alpha()
    screen.blit(img, (690, 220))
    img1 = font_SpaceShip.render('BULLET COLOR : ', True, (249, 244, 0))
    screen.blit(img1, (350, 260))

def Draw_GameControl(Game_Control = 'Keyboard'):
    if Game_Control == 'Mouse':
        img = pygame.image.load("images/setting-items/mouse.png").convert_alpha()
        screen.blit(img, (735, 320))
    if Game_Control == 'Keyboard':
        img = pygame.image.load("images/setting-items/keyboard.png").convert_alpha()
        screen.blit(img, (698, 300))
    img1 = font_SpaceShip.render('GAME CONTROL : ', True, (0, 178, 191))
    screen.blit(img1, (350, 360))

def distance(A, B):
    return math.sqrt( (( A.Get_x() - B.Get_x() )**2) + (( A.Get_y() - B.Get_y() )**2) )

def Draw_BossBlood(Boss):
    pygame.draw.rect( screen, (255,0,0), [Boss.x + 25,Boss.y -20, 150,10])
    pygame.draw.rect( screen, (255,255,255), [Boss.x + 25,Boss.y -20, 150-Boss.Blood ,10])

def main():
    Game_Menu = True
    InGame = False
    OptionStatus = False
    SoundOnOff = True
    Game_Control = GAME_CONTROL_KEYBOARD  
    Rocket = MAIN_SPACE_SHIP
    Game_Over = False
    Game_Win = False
    Game_Mode = 'Easy'
    Bullet_Color = 'Yellow'

    meteoric1 ="images/meteorics/meteoric1.png"
    meteoric1L ="images/meteorics/meteoric1L.png"
    meteoric1R ="images/meteorics/meteoricR.png"



    Score = 0
    Number_livetree =3

    NumberUfo = 0
    NumberUfo1 = 0

    # QuantityUfo =2
    Stage =3
    Bullet_Color = 'Yellow'
    Bull = Bullet.Bullet()
    BullL = Bullet.Bullet()
    BullL.Bullet = pygame.image.load("images/bullets/yellowbullet/yellowbulletL.png").convert_alpha()
    BullL.Type = 'L'
    BullR = Bullet.Bullet()
    BullL.Bullet = pygame.image.load("images/bullets/yellowbullet/yellowbulletR.png").convert_alpha()
    BullR.Type = 'R'

    Boss = Aliens.Aliens(x = -100, y = -100, Image = "images/ailens/boss.png") 
    BossBullet = Meteoric.Meteoric(x = -100, y = -100, Meteoric = 'images/bullets/bossbullet/bossbulletS1.png', Status = 'Free', Type = 'Straight')


    global running
    running = True
    FPS = 60
    clock = pygame.time.Clock()
    while running:
        clock.tick(FPS)
        handle_events(choose_successfully, livetree, powerup, time_use_power_up, Stage_Event )
        if Game_Menu == True and InGame == False :   
            screen.blit(background,(0,0))
            PlayButton.Draw()
            OptionButton.Draw()
            QuitButton.Draw()
            if PlayButton.Click() :
                Game_Menu = False
                InGame = True
            
                
        elif  InGame == True:  
            draw_elements(Score, Number_livetree,background)
            PauseButton.Draw()

            Rocket.MoveRocket(Game_Control)
            Rocket.DisPlayRocket()
            if Stage ==1:
                for i in range(QuantityUfo):
                    if ListUfo[i].Status == 'Live':
                        ListUfo[i].DisPlayAliens()
                for i in range(QuantityUfo):
                    ListMeteoric[i]= ListUfo[i].PrepareMeteoric(ListMeteoric[i], Rocket)
                    ListUfo[i].Shoot(ListMeteoric[i])
                    if ListUfo[i].Status == 'Live':
                        distanceUFO = distance(Bull, ListUfo[i])
                        if distanceUFO < 40 and Bull.Get_y() >= 0 and Bull.Get_y() <= HEIGHT and ListUfo[i].x >= 0 and ListUfo[i].x <= WIDTH  :
                            ExplosionMusic.play()
                            Bull.x, Bull.y = -100, -100
                            Score += 1
                            ListUfo[i].Status = 'Die'
                            ListUfo[i].x = -100
                            ListUfo[i].y = -100
                            NumberUfo += 1
                            print("Stage", 'UFO: ', NumberUfo)
                            print(distanceUFO)
                    distaceRocket = math.sqrt( (( ListMeteoric[i].Get_x() - Rocket.Get_x() )**2) + (( ListMeteoric[i].Get_y() - Rocket.Get_y() )**2) )
                    if distaceRocket < 30 and ListUfo[i].Status == 'Live':
                            Number_livetree -= 1
                            ListMeteoric[i].x = -100
                            ListMeteoric[i].y = -100
                if NumberUfo == QuantityUfo:
                    Stage=2
            if Stage == 2:
                Display_Stage(Stage)
                draw_elements(Score, Number_livetree,background1 )
                Rocket.MoveRocket(GAME_CONTROL_KEYBOARD)
                Rocket.DisPlayRocket()
                for i in range(QuantityUfo):
                    if ListUfo1[i].Status == 'Live':
                        ListUfo1[i].DisPlayAliens()      
                    ListMeteoric1[i]= ListUfo1[i].PrepareMeteoric(ListMeteoric1[i], Rocket,meteoric1,meteoric1L,meteoric1R)
                    ListUfo1[i].Shoot(ListMeteoric1[i]) 
                    if ListUfo1[i].Status == 'Live':      
                        distanceUFO = distance(Bull, ListUfo1)
                        if distanceUFO < 40 and Bull.Get_y() >= 0 and Bull.Get_y() <= HEIGHT and ListUfo1[i].x >= 0 and ListUfo1[i].x <= WIDTH  :
                            ExplosionMusic.play()

                            Bull.x, Bull.y = -100, -100
                            Score += 2
                            ListUfo1[i].Status = 'Die'
                            ListUfo1[i].x = -100
                            NumberUfo1 += 1
                            print("Stage", 'UFO: ', NumberUfo)
                            print(distanceUFO)
                    # distaceRocket = math.sqrt( (( ListMeteoric1[i].Get_x() - Rocket.Get_x() )**2) + (( ListMeteoric1[i].Get_y() - Rocket.Get_y() )**2) )
                    distaceRocket = distance(ListMeteoric1[i], Rocket)

                    if distaceRocket < 30 and ListUfo1[i].Status == 'Live':
                            Number_livetree -= 1
                            ListMeteoric1[i].x = -100
                            ListMeteoric1[i].y = -100 
                if NumberUfo1 == QuantityUfo1:
                    Stage=3
            if Stage == 3:
                Display_Stage(Stage)
                draw_elements(Score, Number_livetree,background1 )
                Rocket.MoveRocket(GAME_CONTROL_KEYBOARD)
                Rocket.DisPlayRocket()
                Boss.DisPlayAliens()
                Draw_BossBlood(Boss)
                BossBullet = Boss.PrepareMeteoric(BossBullet, Rocket, StraightI = 'images/bullets/bossbullet/bossbulletS1.png' ,LeftI = 'images/bullets/bossbullet/bossbulletL1.png', RightI = 'images/bullets/bossbullet/bossbulletR1.png' )
            #Shoot
                Boss.Shoot(BossBullet)
                distanceRK = distance(BossBullet, Rocket)
                if distanceRK < 50 and Boss.Status == 'Live':
                            Number_livetree -= 1
                            BossBullet.x = -100
                for i in range(QuantityUfo):
                    if ListUfo1[i].Status == 'Live':
                        ListUfo1[i].DisPlayAliens()      
                    ListMeteoric1[i]= ListUfo1[i].PrepareMeteoric(ListMeteoric1[i], Rocket,meteoric1,meteoric1L,meteoric1R)
                    ListUfo1[i].Shoot(ListMeteoric1[i]) 
                    if ListUfo1[i].Status == 'Live':      
                            distanceUFO = math.sqrt( (( Bull.Get_x() - ListUfo1[i].Get_x() )**2) + (( Bull.Get_y() - ListUfo1[i].Get_y() )**2) )
                            if distanceUFO < 40 and Bull.Get_y() >= 0 and Bull.Get_y() <= HEIGHT and ListUfo1[i].x >= 0 and ListUfo1[i].x <= WIDTH  :
                                ExplosionMusic.play()

                                Bull.x, Bull.y = -100, -100
                                Score += 2
                                ListUfo1[i].Status = 'Die'
                                ListUfo1[i].x = -100
                                NumberUfo1 += 1
                                print("Stage", 'UFO: ', NumberUfo)
                                print(distanceUFO)
                        # distaceRocket = math.sqrt( (( ListMeteoric1[i].Get_x() - Rocket.Get_x() )**2) + (( ListMeteoric1[i].Get_y() - Rocket.Get_y() )**2) )
                    distaceRocket = distance(ListMeteoric1[i], Rocket)

                    if distaceRocket < 30 and ListUfo1[i].Status == 'Live':
                            ExplosionMusic.play()
                            
                            Number_livetree -= 1
                            ListMeteoric1[i].x = -100
                            ListMeteoric1[i].y = -100 
                distanceBoss = distance(Boss, Bull)
                if distanceBoss < 100:
                    Boss.Blood -= 5
                    Bull.x = -100
                    Bull.y = -100
                    if Boss.Blood <=0 and NumberUfo1 == QuantityUfo1:
                        ExplosionMusic.play()
                        Game_Win == True



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
        
            
        elif OptionStatus == True:
            screen.blit(background,(0,0))
            BackButton.Draw()
            if SoundOnOff == 'On':
                SoundStatusOn.Draw()
            if BackButton.Click() :
                Game_Menu = True
                OptionStatus = False
            
            DisplayBulletColor(Bullet_Color)
            arBulletLeft.Draw()
            arBulletRight.Draw()
            if Bullet_Color == 'Yellow' and arBulletLeft.Click() :
                Bullet_Color = 'Green'
            if Bullet_Color == 'Yellow' and arBulletRight.Click() :
                Bullet_Color = 'Red'
            if Bullet_Color == 'Red' and arBulletLeft.Click() :
                Bullet_Color = 'Yellow'
            if Bullet_Color == 'Red' and arBulletRight.Click() :
                Bullet_Color = 'Blue'
            if Bullet_Color == 'Blue' and arBulletLeft.Click() :
                Bullet_Color = 'Red'        
            if Bullet_Color == 'Blue' and arBulletRight.Click() :
                Bullet_Color = 'Green'
            if Bullet_Color == 'Green' and arBulletLeft.Click() :
                Bullet_Color = 'Blue'
            if Bullet_Color == 'Green' and arBulletRight.Click() :
                Bullet_Color = 'Yellow'
            arControlRight.Draw()
            arControlLeft.Draw()
            Draw_GameControl(Game_Control)
            if Game_Control == GAME_CONTROL_MOUSE and arControlRight.Click():
                Game_Control = GAME_CONTROL_KEYBOARD
            if Game_Control == GAME_CONTROL_MOUSE and arControlLeft.Click():
                Game_Control = GAME_CONTROL_KEYBOARD
            if Game_Control == GAME_CONTROL_KEYBOARD and arControlRight.Click():
                Game_Control = GAME_CONTROL_MOUSE
            if Game_Control == GAME_CONTROL_KEYBOARD and arControlLeft.Click():
                Game_Control = GAME_CONTROL_MOUSE
            arRocketLeft.Draw()
            arRocketRight.Draw()
            screen.blit(Rocket.Rocket, (750,450))

            if Rocket == MAIN_SPACE_SHIP and arRocketRight.Click():
                Rocket = SPACE_SHIP1
            if Rocket == SPACE_SHIP1 and arRocketRight.Click():
                Rocket = SPACE_SHIP2
            if Rocket == SPACE_SHIP2 and arRocketRight.Click():
                Rocket = SPACE_SHIP3
            if Rocket == SPACE_SHIP3 and arRocketRight.Click():
                Rocket = MAIN_SPACE_SHIP

            if Rocket == MAIN_SPACE_SHIP and arRocketLeft.Click():
                Rocket = SPACE_SHIP3
            if Rocket == SPACE_SHIP3 and arRocketLeft.Click():
                Rocket = SPACE_SHIP2
            if Rocket == SPACE_SHIP2 and arRocketLeft.Click():
                Rocket = SPACE_SHIP1
            if Rocket == SPACE_SHIP1 and arRocketLeft.Click():
                Rocket = MAIN_SPACE_SHIP
            if Rocket == MAIN_SPACE_SHIP and arRocketRight.Click():
                Rocket = SPACE_SHIP1
            if Rocket == SPACE_SHIP1 and arRocketRight.Click():
                Rocket = SPACE_SHIP2
            if Rocket == SPACE_SHIP2 and arRocketRight.Click():
                Rocket = SPACE_SHIP3
            if Rocket == SPACE_SHIP3 and arRocketRight.Click():
                Rocket = MAIN_SPACE_SHIP

            if Rocket == MAIN_SPACE_SHIP and arRocketLeft.Click():
                Rocket = SPACE_SHIP3
            if Rocket == SPACE_SHIP3 and arRocketLeft.Click():
                Rocket = SPACE_SHIP2
            if Rocket == SPACE_SHIP2 and arRocketLeft.Click():
                Rocket = SPACE_SHIP1
            if Rocket == SPACE_SHIP1 and arRocketLeft.Click():
                Rocket = MAIN_SPACE_SHIP
            
            
        if PauseButton.Click() :
            Game_Menu = True
            InGame = True
        if Game_Menu == True and InGame == True:
            screen.blit(background,(0,0))
            ResumeButton.Draw()
            OptionButton.Draw()
            QuitButton.Draw()
        if QuitButton.Click() == True:
            running = False
            sys.exit()
        if OptionButton.Click():
                OptionStatus = True
                Game_Menu = False

            
 
        
                
            
                    
        pygame.display.update()
    


# Chạy trò chơi
if __name__ == '__main__':
    main()
