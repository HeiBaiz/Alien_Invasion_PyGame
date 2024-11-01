import pygame

class Z02:
    """管理02的类"""
    
    def __init__(self,ai_game):
        """初始化02并设置其初始位置"""
        self.screen = ai_game.screen 
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # 加载02图像并获取其外接矩形
        self.image = pygame.image.load('images/02-2.bmp')
        self.rect = self.image.get_rect()
        
        # 每个02都放在屏幕的中央
        self.rect.midbottom = self.screen_rect.midbottom
        
        # 在02的属性 X 中存储一个浮点数
        self.x = float(self.rect.x)
        # 在02的属性 Y 中存储一个浮点数
        self.y = float(self.rect.y)
        
        # 移动标志（02一开始不移动）
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        """根据移动标志调整02的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.z02_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.z02_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.z02_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.z02_speed
            
        # 根据 self.x 更新 rect 对象
        self.rect.x = self.x
        self.rect.y = self.y
        
    def blitme(self):
        """在指定位置绘制02"""
        self.screen.blit(self.image,self.rect)