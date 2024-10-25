import pygame

class Z02:
    """管理02的类"""
    
    def __init__(self,ai_game):
        """初始化02并设置其初始位置"""
        self.screen = ai_game.screen 
        self.screen_rect = ai_game.screen.get_rect()
        
        # 加载02图像并获取其外接矩形
        self.image = pygame.image.load('images/02-2.bmp')
        self.rect = self.image.get_rect()
        
        # 每个02都放在屏幕的中央
        self.rect.midbottom = self.screen_rect.center
        
    def blitme(self):
        """在指定位置绘制02"""
        self.screen.blit(self.image,self.rect)