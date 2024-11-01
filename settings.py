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
        
        # 子弹设置
        self.bullet_speed = 5
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 11
        