import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理飞船发射子弹的类"""
    
    def __init__(self, ai_game):
        """在飞船当前位置创建一个子弹对象"""
        super().__init__()
        self.screen = ai_game.screen 
        self.settings = ai_game.settings 
        self.color = self.settings.bullet_color
        
        # 在（0，0）处创建子弹的矩阵，再设置正确位置
        #self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        
        # 加载子弹图像并获取其外接矩形
        self.image = pygame.image.load('images/bullet.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.midtop = ai_game.ship.rect.midtop 
        
        # 存储浮点数表示子弹位置
        self.y = float(self.rect.y)
        
    def update(self):
        """向上移动子弹"""
        # 更新子弹的准确位置
        self.y -= self.settings.bullet_speed
        # 更新表示子弹的 rect 的位置
        self.rect.y = self.y
        
    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        #pygame.draw.rect(self.screen, self.color, self.rect)
        # 发射图片
        self.screen.blit(self.image,self.rect)