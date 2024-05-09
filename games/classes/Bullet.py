import pygame 

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
WIDTH = 1300
HEIGHT = 788
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mixer.pre_init(41000,-16,2,2048)

class Bullet():
    """
    Class Bullet:
    Đại diện cho viên đạn trong trò chơi.

    Attributes:
        x (int): Tọa độ x của viên đạn.
        y (int): Tọa độ y của viên đạn.
        Bullet (pygame.Surface): Hình ảnh của viên đạn.
        Status (str): Trạng thái của viên đạn ('Free' hoặc 'Used').
        Type (str): Loại của viên đạn ('S' cho pháp sư, 'B' cho bảo vệ, 'E' cho quái vật).

    Methods:
        DisPlayBullet(): Hiển thị viên đạn trên màn hình.
        off_screen(height): Kiểm tra xem viên đạn có ra khỏi màn hình không.
        collision(obj): Kiểm tra va chạm của viên đạn với một đối tượng khác.
        Get_Status(): Trả về trạng thái của viên đạn.
        Get_x(): Trả về tọa độ x của viên đạn.
        Get_y(): Trả về tọa độ y của viên đạn.
    """
    def __init__ (self, x = -100, y = -100, Status = 'Free', Type = 'S'): 
        """
        Hàm khởi tạo: 
        Khởi tạo một đối tượng viên đạn với các thuộc tính mặc định hoặc đã chỉ định.

        Args:
            x (int): Tọa độ x ban đầu của viên đạn.
            y (int): Tọa độ y ban đầu của viên đạn.
            Status (str): Trạng thái ban đầu của viên đạn ('Free' hoặc 'Used').
            Type (str): Loại của viên đạn ('S' cho pháp sư, 'B' cho bảo vệ, 'E' cho quái vật).
        """
        self.x = x
        self.y = y
        self.Bullet = pygame.image.load("images/bullets/bull/bullS.png").convert_alpha()
        self.Status = Status
        self.Type = Type
    def DisPlayBullet(self):
        """
        Phương thức DisPlayBullet():
            Hiển thị viên đạn trên màn hình.
        """
        screen.blit(self.Bullet, (self.x, self.y))
    def Get_Status(self):
        """
        Phương thức Get_Status():
            Trả về trạng thái của viên đạn.
        """
        return self.Status
    def Get_x(self):
        """
        Trả về tọa độ x của viên đạn.

        Returns:
            int: Tọa độ x của viên đạn.
        """
        return self.x
    def Get_y (self):
        """
        Trả về tọa độ y của viên đạn.

        Returns:
            int: Tọa độ y của viên đạn.
        """
        return self.y



