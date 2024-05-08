import pygame, time
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
font_gameover=pygame.font.SysFont('Arial',100,'bold')
# Load hình ảnh
background = pygame.image.load("images/backgrounds/bg.png").convert_alpha()
background1 = pygame.image.load("images/backgrounds/bg1.jpg").convert_alpha()
background2 = pygame.image.load("images/backgrounds/bg3.png").convert_alpha()
background3 = pygame.image.load("images/backgrounds/bg4.png").convert_alpha()
powerup = pygame.image.load("images/power-item/lightning.png").convert_alpha()
livetree = pygame.image.load("images/power-item/livetree.png").convert_alpha()
WinBG = pygame.image.load("images/backgrounds/you-win-video-game-vector.jpg")
GameOverBG = pygame.image.load("images/backgrounds/over.jpg")
boomm = pygame.image.load("images/orther/boom.png")
home_icon = pygame.image.load("images/setting-items/home_icon.png").convert_alpha()
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
    lt = "images/power-item/livetree.png"
    pu = "images/power-item/lightning.png"
    nextleft = "images/setting-items/nextleft.png"
    nextright = "images/setting-items/nextright.png"
    home = "images/setting-items/home.png"
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
    arModeLeft = Button.Button(630,550, nextleft)
    arModeRight = Button.Button(890,550, nextright)

    HomeButton = Button.Button(WIDTH/2-130, HEIGHT- 180, home)

# Khởi tạo danh sách UFO và Meteoric
QuantityUfo =10
QuantityUfo1 =15

ListUfo = [Aliens.Aliens() for _ in range(QuantityUfo )]
ListUfo1 = [Aliens.Aliens(-100,-100,"images/ailens/enemy.png") for _ in range(QuantityUfo1 )]
ListMeteoric = [Meteoric.Meteoric() for _ in range(QuantityUfo)]
ListMeteoric1 = [Meteoric.Meteoric(-100,-100,"images/meteorics/meteoric1.png") for _ in range(QuantityUfo1)]

ExplosionMusic = mixer.Sound("sounds/explosion.wav")
ExplosionMusic.set_volume(0.8)
LaserMusic = mixer.Sound("sounds/laser.wav")
LaserMusic.set_volume(0.8)
LevelPassMusic = mixer.Sound("sounds/level.wav")

font_stage=pygame.font.SysFont('Arial',100,'bold')
font_MaxScore=pygame.font.SysFont('Arial',50,'bold')
# Hàm để vẽ các phần tử trên màn hình
def draw_elements(score, Number_livetree):
    """
    Vẽ các phần tử trên màn hình trò chơi bao gồm số cây sống và điểm số.

    Input::
        score (int): Điểm số của người chơi.
        Number_livetree (int): Số cây sống còn lại của người chơi.
    Output:
        hình ảnh các phần tử trên màn hình
    """
    for i in range(Number_livetree):
        screen.blit(livetree, (i*50+1, 1))
    img = font.render(f'Score: {score}', True, 'red')
    screen.blit(img, (10, 50))
def Display_Stage(Stage):
    """
    Hiển thị thông báo về giai đoạn trò chơi hiện tại.

    Args:
        Stage (int): Giai đoạn hiện tại của trò chơi.

    Output:
        Hiển thị thông báo về giai đoạn trò chơi trên màn hình.
    """
    img = font_stage.render(f'STAGE : {Stage}', True, 'red') 
    screen.blit(img, (450,300))
def Draw_Max_Score(MaxScore):
    """
    Args:
        MaxScore (int): Điểm số cao nhất đã đạt được trong trò chơi.

    Output:
        Hiển thị điểm số cao nhất trên màn hình.
    """
    img = font_MaxScore.render(f'MAX SCORE : {MaxScore}', True, 'green') 
    screen.blit(img, (500,600))
def Draw_Sound():
    """
    Output:
        Hiển thị biểu tượng âm thanh trên màn hình.
    """
    img = pygame.image.load("soundicon.png").convert_alpha()
    screen.blit(img, (620,140))
def DisplayBulletColor(Bullet_Color = 'Yellow'):
    """
    Args:
        Bullet_Color (str): Màu của viên đạn ('Yellow', 'Red', 'Blue', 'Green').

    Output:
        Hiển thị hình ảnh đạn tương ứng với màu được chọn trên màn hình.
    """
    if Bullet_Color == 'Yellow':
        img = pygame.image.load("images/bullets/bull/bull.png").convert_alpha()
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
    """
    Args:
        Game_Control (str): Phương thức điều khiển trò chơi ('Keyboard' hoặc 'Mouse').

    Output:
        Hiển thị biểu tượng điều khiển trò chơi tương ứng trên màn hình.
    """
    if Game_Control == 'Mouse':
        img = pygame.image.load("images/setting-items/mouse.png").convert_alpha()
        screen.blit(img, (735, 320))
    if Game_Control == 'Keyboard':
        img = pygame.image.load("images/setting-items/keyboard.png").convert_alpha()
        screen.blit(img, (698, 300))
    img1 = font_SpaceShip.render('GAME CONTROL : ', True, (0, 178, 191))
    screen.blit(img1, (350, 360))
def distance(A, B): 
    """
    Tính khoảng cách giữa hai đối tượng.

    Args:
        A (object): Đối tượng A.
        B (object): Đối tượng B.

    Returns:
        float: Khoảng cách giữa hai đối tượng.
    """
    return math.sqrt( (( A.Get_x() - B.Get_x() )**2) + (( A.Get_y() - B.Get_y() )**2) )
def Draw_BossBlood(Boss):
    """
    Args:
        Boss (object): Đối tượng Boss.

    Output:
        Hiển thị thanh máu của Boss trên màn hình.
    """
    pygame.draw.rect( screen, (255,0,0), [Boss.x + 25,Boss.y -20, 150,10])
    pygame.draw.rect( screen, (255,255,255), [Boss.x + 25,Boss.y -20, 150-Boss.Blood ,10])
def GameOver(Score):
    """
    Args:
        Score (int): Điểm số của người chơi khi kết thúc trò chơi.

    Output:
        Hiển thị thông báo kết thúc trò chơi và điểm số của người chơi trên màn hình.
    """
    img_gameover = font_gameover.render('GAME OVER . . .', True, 'white')
    screen.blit(img_gameover, (500, 100))
    img_s=font_gameover.render(f'Score: {Score}',True,'red')
    screen.blit(img_s,(400,250))
def Draw_Sound():
    """
    Output:
        Hiển thị biểu tượng âm thanh trên màn hình.
    """
    img = pygame.image.load("images/setting-items/soundicon.png").convert_alpha()
    screen.blit(img, (620,140))


def Draw_GameMode(Game_Mode = 'Easy'):
    """
    Args:
        Game_Mode (str): Chế độ chơi ('Easy', 'Medium', 'Hard').

    Output:
        Hiển thị biểu tượng chế độ chơi tương ứng trên màn hình.
    """
    if Game_Mode == 'Easy':
        img = pygame.image.load("images/setting-items/easy.png").convert_alpha()
    if Game_Mode == 'Medium':
        img = pygame.image.load("images/setting-items/medium.png").convert_alpha()
    if Game_Mode == 'Hard':
        img = pygame.image.load("images/setting-items/Hard.png").convert_alpha()
    screen.blit(img, (730, 550))
    img1 = font_SpaceShip.render('GAME MODE : ', True, (91, 189, 43))
    screen.blit(img1, (350, 565))


LiveTree = Button.Button(100, -100, lt)
LiveTreeMusic = mixer.Sound("sounds/livetree.wav")
PowerUp = Button.Button(700, -900, pu)
PowerUpMusic = mixer.Sound("sounds/livetree.wav")

def main():
    # Khai báo các đối tượng 
    Game_Menu = True
    InGame = False
    OptionStatus = False
    Sound = True
    Game_Over = False
    Game_Win = False
    Stage_Status = True
    Game_Mode = 'Easy'
    Bullet_Color = 'Yellow'
    Rocket = MAIN_SPACE_SHIP
    TripleBullet = TRIPLE_BULLET_NO


    Stage = 1
    Score = 0
    Number_livetree =3
    NumberUfo = 0
    NumberUfo1 = 0
    Max_score = 0

    Game_Control = GAME_CONTROL_MOUSE
    meteoric1 ="images/meteorics/meteoric1.png"
    meteoric1L ="images/meteorics/meteoric1L.png"
    meteoric1R ="images/meteorics/meteoricR.png"
    # LiveTree
    live_tree = pygame.USEREVENT + 1
    time_live_tree = random.randint(15000, 25000)
    pygame.time.set_timer(live_tree, time_live_tree)
    DropLiveTree = False
    #Power Up
    power_up = pygame.USEREVENT + 2
    time_power_up = random.randint(15000, 25000)
    pygame.time.set_timer(power_up, time_power_up)
    DropPowerUp = False
    time_use_power_up = pygame.USEREVENT + 3
    pygame.time.set_timer(time_use_power_up, 10000)
    Stage_Event = pygame.USEREVENT + 4
    pygame.time.set_timer(Stage_Event, 3500)



    
    Bullet_Color = 'Yellow'
    Bull = Bullet.Bullet()
    BullL = Bullet.Bullet()
    BullL.Bullet = pygame.image.load("images/bullets/bull/bullL.png").convert_alpha()
    BullL.Type = 'L'
    BullR = Bullet.Bullet()
    BullL.Bullet = pygame.image.load("images/bullets/bull/bullR.png").convert_alpha()
    BullR.Type = 'R'

    Boss = Aliens.Aliens(x = -100, y = -100, Image = "images/ailens/boss.png") 
    BossBullet = Meteoric.Meteoric(x = -100, y = -100, Meteoric = 'images/bullets/bossbullet/bossbulletS1.png', Status = 'Free', Type = 'Straight')


    global running
    running = True
    FPS = 100
    clock = pygame.time.Clock()
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == live_tree:
                if DropLiveTree == False:
                    DropLiveTree = True
            if event.type == power_up:
                if DropPowerUp == False:
                    DropPowerUp = True
            if event.type == time_use_power_up:
                if TripleBullet == TRIPLE_BULLET_YES:
                    TripleBullet = TRIPLE_BULLET_NO
            if event.type == Stage_Event:
                if Stage_Status == True:
                    Stage_Status = False
            
        # Màn hình chính
        if Game_Menu == True and InGame == False :   
            screen.blit(background,(0,0))
            screen.blit(home_icon,(WIDTH/2 -50, HEIGHT/2-250))
            PlayButton.Draw()
            OptionButton.Draw()
            QuitButton.Draw()
            Draw_Max_Score(Max_score)
            if PlayButton.Click() :
                Game_Menu = False
                InGame = True
        

            
        # Play     
        elif  InGame == True and Game_Menu == False and Stage_Status == False and OptionStatus == False :  
            draw_elements(Score, Number_livetree)
            screen.blit(background, (0, 0))  
            if  Stage_Status == True:
                Display_Stage(Stage)
            Rocket.MoveRocket(Game_Control)
            Rocket.DisPlayRocket()
            LiveTree.Draw()
            if Stage ==1:
                for i in range(QuantityUfo):
                    if ListUfo[i].Status == 'Live':
                        ListUfo[i].DisPlayAliens()              
                    ListMeteoric[i]= ListUfo[i].PrepareMeteoric(ListMeteoric[i], Rocket)
                    ListUfo[i].Shoot(ListMeteoric[i])
                    if ListUfo[i].Status == 'Live':
                        if TripleBullet == TRIPLE_BULLET_NO:
                            distanceUFO = distance(Bull, ListUfo[i])
                            if distanceUFO < 40  :
                                ListUfo[i].Boom()
                                ExplosionMusic.play()
                                Bull.x, Bull.y = -100, -100
                                Score += 1
                                ListUfo[i].Status = 'Die'
                                ListUfo[i].x = -100
                                NumberUfo += 1
                        if TripleBullet == TRIPLE_BULLET_YES:
                            distanceUFO = distance(Bull, ListUfo[i])
                            distanceUFOL = distance(BullL, ListUfo[i])
                            distanceUFOR = distance(BullR, ListUfo[i])
                            if distanceUFO < 40 or distanceUFOL < 40 or distanceUFOR < 40 :
                                ExplosionMusic.play()
                                Bull.x, Bull.y = -100, -100
                                Score += 1
                                ListUfo[i].Status = 'Die'
                                ListUfo[i].x = -100
                                ListUfo[i].y = -100
                                NumberUfo += 1
                                print("Stage", 'UFO: ', NumberUfo)
                                print(distanceUFO)
                    distaceRocket = distance(Rocket, ListMeteoric[i])
                    if distaceRocket < 30 and ListUfo[i].Status == 'Live':
                            Number_livetree -= 1
                            ListMeteoric[i].x = -100
                            ListMeteoric[i].y = -100
                if NumberUfo == QuantityUfo:
                    Stage=2
                    Stage_Status =True
            if Stage == 2:
                screen.blit(background1, (0, 0))
                Rocket.MoveRocket(Game_Control)
                Rocket.DisPlayRocket()
                LiveTree.Draw()
                for i in range(QuantityUfo1):
                    if ListUfo1[i].Status == 'Live':
                        ListUfo1[i].DisPlayAliens()      
                    ListMeteoric1[i]= ListUfo1[i].PrepareMeteoric(ListMeteoric1[i], Rocket,meteoric1,meteoric1L,meteoric1R)
                    ListUfo1[i].Shoot(ListMeteoric1[i]) 
                    if ListUfo1[i].Status == 'Live':   
                        if TripleBullet == TRIPLE_BULLET_NO:
                            distanceUFO = distance(Bull, ListUfo1[i])
                            if distanceUFO < 40 :
                                ExplosionMusic.play()
                                Bull.x, Bull.y = -100, -100
                                Score += 2
                                ListUfo1[i].Status = 'Die'
                                ListUfo1[i].x = -100
                                NumberUfo1 += 1
                        if TripleBullet == TRIPLE_BULLET_YES:
                            distanceUFO = distance(Bull, ListUfo1[i])
                            distanceUFOL = distance(BullL, ListUfo1[i])
                            distanceUFOR = distance(BullR, ListUfo1[i])
                            if distanceUFO < 40 or distanceUFOL < 40 or distanceUFOR < 40    :
                                ExplosionMusic.play()
                                Bull.x, Bull.y = -100, -100
                                Score += 2
                                ListUfo1[i].Status = 'Die'
                                ListUfo1[i].x = -100
                                NumberUfo1 += 1
                    distaceRocket = distance(ListMeteoric1[i], Rocket)
                    if distaceRocket < 30 and ListUfo1[i].Status == 'Live':
                            Number_livetree -= 1
                            ListMeteoric1[i].x = -100
                if NumberUfo1 == QuantityUfo1:
                    Stage=3
                    Stage_Status =True
                    NumberUfo1 =0
                    for i in range(QuantityUfo1):
                        if ListUfo1[i].Status == 'Die':
                            ListUfo1[i].Status = 'Live'
            if Stage == 3:
                screen.blit(background2, (0, 0))
                Rocket.MoveRocket(Game_Control)
                Rocket.DisPlayRocket()
                Boss.DisPlayAliens()
                Draw_BossBlood(Boss)
                BossBullet = Boss.PrepareMeteoric(BossBullet, Rocket, StraightI = 'images/bullets/bossbullet/bossbulletS1.png' ,LeftI = 'images/bullets/bossbullet/bossbulletL1.png', RightI = 'images/bullets/bossbullet/bossbulletR1.png' )
                Boss.Shoot(BossBullet)
                distanceRK = distance(BossBullet, Rocket)
                if distanceRK < 50 and Boss.Status == 'Live':
                            Number_livetree -= 1
                            BossBullet.x = -100

                for i in range(QuantityUfo1):
                    if ListUfo1[i].Status == 'Live':
                        ListUfo1[i].DisPlayAliens()      
                    ListMeteoric1[i]= ListUfo1[i].PrepareMeteoric(ListMeteoric1[i], Rocket,meteoric1,meteoric1L,meteoric1R)
                    ListUfo1[i].Shoot(ListMeteoric1[i]) 
                    if ListUfo1[i].Status == 'Live':      
                            if TripleBullet == TRIPLE_BULLET_NO:
                                distanceUFO = distance(Bull, ListUfo1[i])
                                if distanceUFO < 40 :
                                    ExplosionMusic.play()
                                    Bull.x, Bull.y = -100, -100
                                    Score += 2
                                    ListUfo1[i].Status = 'Die'
                                    ListUfo1[i].x = -100
                                    NumberUfo1 += 1
                            if TripleBullet == TRIPLE_BULLET_YES:
                                distanceUFO = distance(Bull, ListUfo1[i])
                                distanceUFOL = distance(BullL, ListUfo1[i])
                                distanceUFOR = distance(BullR, ListUfo1[i])
                                if distanceUFO < 40 or distanceUFOL < 40 or distanceUFOR < 40  :
                                    ExplosionMusic.play()
                                    Bull.x, Bull.y = -100, -100
                                    Score += 2
                                    ListUfo1[i].Status = 'Die'
                                    ListUfo1[i].x = -100
                                    NumberUfo1 += 1
                    distaceRocket = distance(ListMeteoric1[i], Rocket)

                    if distaceRocket < 30 and ListUfo1[i].Status == 'Live':
                            ExplosionMusic.play()
                            Number_livetree -= 1
                            ListMeteoric1[i].x = -100
                distanceBoss = distance(Boss, Bull)
                if distanceBoss < 100:
                    Boss.Blood -= 5
                    Bull.x = -100
                    print(Boss.Blood)
                if Boss.Blood <=0 and NumberUfo1 == QuantityUfo1:
                    ExplosionMusic.play()
                    Game_Win = True
                    InGame = False
                    Boss.x =-1000

            PauseButton.Draw()

            LiveTree.Draw()
            if DropLiveTree == True:
                LiveTree.x = random.randint(10,WIDTH-100)
                LiveTree.y = 0
                DropLiveTree = False
            LiveTree.y += 3

            PowerUp.Draw()
            if DropPowerUp == True:
                PowerUp.x = random.randint(10,WIDTH-100)
                PowerUp.y = -2000
                DropPowerUp = False
            PowerUp.y += 3
            if Number_livetree < 3:
                distanceLiveTree = distance(LiveTree, Rocket)
                if distanceLiveTree < 30:
                    LiveTree.x = -100
                    Number_livetree += 1

            distancePower = distance(PowerUp, Rocket)
            if distancePower < 50:
                TripleBullet = TRIPLE_BULLET_YES
                DropPowerUp = True
        
            draw_elements(Score, Number_livetree)
            if Number_livetree == 0:
                Game_Over = True
                InGame = False

            Button = pygame.key.get_pressed() 
            if (Button[pygame.K_SPACE]) and TripleBullet == TRIPLE_BULLET_NO:
                if Bull.Get_Status() == 'Free':
                    Bull = Rocket.PrepareBullet(Bull, Bullet_Color)
                Rocket.Shoot(Bull, Bullet_Color)
                LaserMusic.play()

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
                    LaserMusic.play()
     




        elif Game_Win == True :
            screen.blit(WinBG,(0,0))   
            HomeButton.Draw()
            if HomeButton.Click() :
                Game_Win = False
                Game_Menu = True 
                Game_Over = False
                InGame = False
                Score = 0
                NumberUfo=0
                NumberUfo1 =0
                Stage =1
                Boss.Blood = 150
                Number_livetree =3
                for i in range(QuantityUfo):
                    if ListUfo[i].Status == 'Die':
                        ListUfo[i].Status = 'Live'
                for i in range(QuantityUfo1):
                    if ListUfo1[i].Status == 'Die':
                        ListUfo1[i].Status = 'Live'


        elif Game_Over == True and InGame == False :
            screen.blit(background,(0,0))
            GameOver(Score)
            Stage = 1
            Number_livetree = 3                          
            Replay.Draw()
            if Replay.Click() :
                Score = 0
                Game_Menu = True 
                Game_Over = False
                InGame = False
                NumberUfo=0
                NumberUfo1 =0
                Boss.Blood = 150
                for i in range(QuantityUfo):
                    if ListUfo[i].Status == 'Die':
                        ListUfo[i].Status = 'Live'
                for i in range(QuantityUfo1):
                    if ListUfo1[i].Status == 'Die':
                        ListUfo1[i].Status = 'Live'

        elif InGame == True and Stage_Status == True:
            if Stage == 1:
                screen.blit(background,(0,0))
            if Stage == 2:
                screen.blit(background1,(0,0))
            if Stage == 3:
                screen.blit(background2,(0,0))
            Display_Stage(Stage)


        elif OptionStatus == True:
            screen.blit(background,(0,0))
            BackButton.Draw()
            Draw_Sound()
            if Sound == True:
                SoundStatusOn.Draw()        
                if SoundStatusOn.Click():
                    Sound = False
                    ExplosionMusic.set_volume(0.0)  
                    LaserMusic.set_volume(0.0)  
                    LiveTreeMusic.set_volume(0.0) 
                    PowerUpMusic.set_volume(0.0)
                    LevelPassMusic.set_volume(0.0)

            elif Sound == False:
                SoundStatusOff.Draw()
                if SoundStatusOff.Click():
                    Sound = True
                    ExplosionMusic.set_volume(0.8)
                    LaserMusic.set_volume(0.8)
                    LiveTreeMusic.set_volume(1.0)
                    PowerUpMusic.set_volume(1.0)
                    LevelPassMusic.set_volume(1.0)
            # Set Game Mode
            arModeRight.Draw()
            arModeLeft.Draw()
            Draw_GameMode(Game_Mode)
            if Game_Mode == 'Easy' and arModeRight.Click():
                Game_Mode = 'Medium'
            if Game_Mode == 'Easy' and arModeRight.Click():
                Game_Mode = 'Hard'
            if Game_Mode == 'Medium' and arModeRight.Click():
                Game_Mode = 'Hard'
            if Game_Mode == 'Medium' and arModeRight.Click():
                Game_Mode = 'Easy'
            if Game_Mode == 'Hard' and arModeRight.Click():
                Game_Mode = 'Easy'
            if Game_Mode == 'Hard' and arModeRight.Click():
                Game_Mode = 'Medium'
            if Game_Mode == 'Easy':
                for i in range(QuantityUfo):
                    ListMeteoric[i].velocityMeteoric = 3
                for i in range(QuantityUfo1):
                    ListMeteoric1[i].velocityMeteoric = 3
                BossBullet.velocityMeteoric = 3
                
            elif Game_Mode == 'Medium':
                for i in range(QuantityUfo):
                    ListMeteoric[i].velocityMeteoric = 4
                for i in range(QuantityUfo1):
                    ListMeteoric1[i].velocityMeteoric = 4
                BossBullet.velocityMeteoric = 4
                
            else:
                for i in range(QuantityUfo):
                    ListMeteoric[i].velocityMeteoric = 5
                for i in range(QuantityUfo1):
                    ListMeteoric1[i].velocityMeteoric = 5
                BossBullet.velocityMeteoric = 5
                
        
            # Set back button
            if BackButton.Click() :
                Game_Menu = True
                OptionStatus = False
            if True:
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
            # Game_Control= choose_Gamecotrol(Game_Control)
            arRocketRight.Draw()
            screen.blit(Rocket.Rocket, (750,450))
            if True:
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
        if ResumeButton.Click():
            InGame = True
            Game_Menu = False
        if Game_Menu == True and InGame == True:
            screen.blit(background,(0,0))
            ResumeButton.Draw()
            OptionButton.Draw()
            QuitButton.Draw()
        if QuitButton.Click() == True and InGame == True:
            Game_Menu = True
            InGame = False
        if QuitButton.Click() == True and Game_Menu == True:
            running = False
            sys.exit()
        if OptionButton.Click():
            OptionStatus = True
            Game_Menu = False
        if Score > Max_score:
            Max_score = Score
        pygame.display.update()
if __name__ == '__main__':
    main()
    print (Aliens.__doc__)
