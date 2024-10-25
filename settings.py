class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""
    
    def __init__(self):    
        """初始化游戏设置"""
        # 屏幕素质
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 255, 255)
        # 飞船的设置
        self.ship_speed = 1.5
        