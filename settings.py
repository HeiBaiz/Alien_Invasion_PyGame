class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""
    
    def __init__(self):
        """初始化游戏设置"""
        # 屏幕素质
        self.screen_width = 1640
        self.screen_height = 960
        self.bg_color = (57, 197, 187)
        
        #飞船设置
        self.ship_speed = 10
        self.ship_limit = 3
        
        # 子弹设置
        self.bullet_speed = 5
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 11
        
        # 外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction 为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1