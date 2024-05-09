"""
Module: aliens.py

Module này chứa định nghĩa của lớp Aliens, đảm nhận việc quản lý các thực thể người ngoài hành tinh trong trò chơi.

Các lớp:
    - Aliens: Đại diện cho một thực thể người ngoài hành tinh với các thuộc tính và phương thức cho việc di chuyển, bắn và hiển thị.

Hàm:
    Không có

Hằng số:
    - WIDTH (int): Chiều rộng của màn hình trò chơi.
    - HEIGHT (int): Chiều cao của màn hình trò chơi.
"""

import pygame 
import random
from classes import Meteoric
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
WIDTH = 1300
HEIGHT = 788
screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Aliens():
    """
    Đại diện cho một thực thể người ngoài hành tinh với các thuộc tính và phương thức cho việc di chuyển, bắn và hiển thị.

    Các thuộc tính:
        - x (int): Tọa độ x của vị trí của người ngoài hành tinh.
        - y (int): Tọa độ y của vị trí của người ngoài hành tinh.
        - UFO (pygame.Surface): Hình ảnh đại diện cho người ngoài hành tinh.
        - velocity (int): Vận tốc của người ngoài hành tinh.
        - Status (str): Trạng thái của người ngoài hành tinh ('Live' hoặc 'Dead').
        - Blood (int): Điểm máu của người ngoài hành tinh.

    Các phương thức:
        - DisplayAliens(): Hiển thị người ngoài hành tinh trên màn hình.
        - PrepareMeteoric(): Chuẩn bị một đám thiên thạch để bắn.
        - Shoot(METEORIC): Bắn đám thiên thạch.
        - Get_x(): Trả về tọa độ x của người ngoài hành tinh.
        - Get_y(): Trả về tọa độ y của người ngoài hành tinh.
        - Boom(): Thay đổi hình ảnh của người ngoài hành tinh để biểu thị vụ nổ.
    """
    def __init__ (self, x = -100, y = -100, Image = "images/ailens/alien1.png"):
        """
        Khởi tạo một đối tượng người ngoài hành tinh với các thuộc tính mặc định hoặc đã chỉ định.

        Args:
            x (int): Tọa độ x ban đầu của người ngoài hành tinh.
            y (int): Tọa độ y ban đầu của người ngoài hành tinh.
            Image (str): Đường dẫn đến tệp hình ảnh đại diện cho người ngoài hành tinh.
        """
        self.x = x
        self.y = y
        self.UFO = pygame.image.load(Image).convert_alpha()
        self.velocity = 5
        self.Status = 'Live'
        self.Blood = 150
    def DisPlayAliens (self):
        """
        Hiển thị người ngoài hành tinh trên màn hình với di chuyển ngẫu nhiên trong ranh giới của màn hình.
        """
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
        """
        Chuẩn bị một đám thiên thạch để bắn dựa trên vị trí của người ngoài hành tinh và tên lửa.

        Args:
            METEORIC (Meteoric): Đối tượng thiên thạch được chuẩn bị để bắn.
            Rocket (Rocket): Đối tượng tên lửa được sử dụng để xác định hướng bắn.
            StraightI (str): Đường dẫn đến tệp hình ảnh cho việc bắn thẳng.
            LeftI (str): Đường dẫn đến tệp hình ảnh cho việc bắn sang trái.
            RightI (str): Đường dẫn đến tệp hình ảnh cho việc bắn sang phải.

        Returns:
            METEORIC (Meteoric): Đối tượng thiên thạch đã chuẩn bị.
        """
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
        """
        Bắn đám thiên thạch đã chuẩn bị.

        Args:
            METEORIC (Meteoric): Đối tượng thiên thạch đã chuẩn bị để bắn.
        """
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
        """
        Trả về tọa độ x của người ngoài hành tinh.

        Returns:
            int: Tọa độ x của người ngoài hành tinh.
        """
        return self.x
    def Get_y (self):
        """
        Trả về tọa độ y của người ngoài hành tinh.

        Returns:
            int: Tọa độ y của người ngoài hành tinh.
        """
        return self.y
    def Boom(self):
        """
        Thay đổi hình ảnh của người ngoài hành tinh để biểu thị vụ nổ.
        """
        self.UFO = pygame.image.load("images/orther/boom.png").convert_alpha()
        self.DisPlayAliens()



