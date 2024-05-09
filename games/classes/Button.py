import pygame 
pygame.init()
screen = pygame.display.set_mode((1400, 788))

NewCursor = pygame.image.load("images/setting-items/newcursor.png")
def Draw_MouseCursor():
    """
    Vẽ con trỏ chuột mới.

    Output:
        Hiển thị con trỏ chuột mới trên màn hình tại vị trí hiện tại của chuột.
    """
    pos = pygame.mouse.get_pos()
    screen.blit( NewCursor, (pos[0] - 12, pos[1] - 3) )
class Button():
    """
    Đại diện cho một nút trong trò chơi hoặc ứng dụng.

    Attributes:
        x (int): Vị trí x của nút trên màn hình.
        y (int): Vị trí y của nút trên màn hình.
        image (Surface): Hình ảnh của nút.
        rect (Rect): Hình chữ nhật bao quanh nút, được sử dụng để xác định vùng nhấp chuột.
        clicked (bool): Trạng thái của nút sau khi được nhấp.
    """

    def __init__(self, x, y, image):
        """
        Khởi tạo một đối tượng nút với vị trí (x, y) và hình ảnh được chỉ định.

        Parameters:
            x (int): Vị trí x của nút trên màn hình.
            y (int): Vị trí y của nút trên màn hình.
            image (str): Đường dẫn đến hình ảnh của nút.
        """
        self.x = x
        self.y = y
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False        
    def Draw(self):
        """
        Vẽ nút trên màn hình tại vị trí (x, y).
        """
        screen.blit(self.image, (self.x, self.y))
    def Click(self):
        """
        Xử lý sự kiện nhấp chuột vào nút.

        Returns:
            bool: True nếu nút được nhấp, False nếu không.
        """
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
        """
        Lấy vị trí x của nút.
        """
        return self.x
    def Get_y (self):
        """
        Lấy vị trí y của nút.

        Returns:
            int: Vị trí y của nút.
        """
        return self.y
print(Button.__doc__)