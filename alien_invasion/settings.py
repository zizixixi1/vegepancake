class Settings():
    def __init__(self):
        #设置屏幕格式
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230,230,230)
        #设置飞船速度
        
        self.ship_limit = 3
        # 设置子弹
        
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3
        # 设置外星人
       
        self.fleet_drop_speed = 15
        

        self.speedup_scale = 1.2

        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        self.fleet_direction = 1
        
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        
