import pygame 
pygame.init()
WIDTH = 1300 
HEIGHT = 788
screen = pygame.display.set_mode((WIDTH, HEIGHT))
class Meteoric():
    """
    Đại diện cho thiên thạch trong trò chơi.

    Attributes:
        x (int): Tọa độ x của thiên thạch.
        y (int): Tọa độ y của thiên thạch.
        Meteoric (pygame.Surface): Hình ảnh của thiên thạch.
        Status (str): Trạng thái của thiên thạch ('Free' hoặc 'Used').
        Type (str): Loại của thiên thạch ('Straight', 'Left', 'Right').

    Methods:
        DisPlayMeteoric(): Hiển thị thiên thạch trên màn hình.
        Get_Status(): Trả về trạng thái của thiên thạch.
        Get_x(): Trả về tọa độ x của thiên thạch.
        Get_y(): Trả về tọa độ y của thiên thạch.
        Get_Type(): Trả về loại của thiên thạch.
    """

    def __init__ (self, x = -100, y = -100, Meteoric = 'images/meteorics/meteoricS.png', Status = 'Free', Type = 'Straight'):
        """
        Khởi tạo một đối tượng thiên thạch với các thuộc tính mặc định hoặc đã chỉ định.

        Args:
            x (int): Tọa độ x ban đầu của thiên thạch.
            y (int): Tọa độ y ban đầu của thiên thạch.
            Meteoric (str): Đường dẫn đến hình ảnh của thiên thạch.
            Status (str): Trạng thái ban đầu của thiên thạch ('Free' hoặc 'Used').
            Type (str): Loại của thiên thạch ('Straight', 'Left', 'Right').
        """
        self.x = x 
        self.y = y
        self.Meteoric = pygame.image.load(Meteoric).convert_alpha()
        self.Status = Status
        self.Type = Type
        self.velocityMeteoric = 3
    def DisPlayMeteoric(self):
        """Hiển thị thiên thạch trên màn hình."""
        screen.blit( self.Meteoric, (self.x, self.y) )
    def Get_Status(self):
        """
        Trả về trạng thái của thiên thạch.

        Returns:
            str: Trạng thái của thiên thạch ('Free' hoặc 'Used').
        """
        return self.Status
    def Get_x(self):
        """
        Trả về tọa độ x của thiên thạch.

        Returns:
            int: Tọa độ x của thiên thạch.
        """
        return self.x
    def Get_y (self):
        """
        Trả về tọa độ y của thiên thạch.

        Returns:
            int: Tọa độ y của thiên thạch.
        """
        return self.y
    def Get_Type(self):
        """
        Trả về loại của thiên thạch.

        Returns:
            str: Loại của thiên thạch ('Straight', 'Left', 'Right').
        """
        return self.Type


