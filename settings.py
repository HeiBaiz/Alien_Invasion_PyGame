class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""
    
    def __init__(self):
        """初始化游戏设置"""
        # 屏幕素质
        self.screen_width = 1640
        self.screen_height = 960
        self.bg_color = (57, 197, 187)
        
        #飞船的设置
        self.ship_speed = 10