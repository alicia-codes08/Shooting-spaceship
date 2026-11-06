class Settings():
    """Save all settings."""
    def __init__(self):
        """Save basic settings.""" 
        # screen settings
        self.screen_w = 600
        self.screen_h = 650 

        # element dimensions
        self.rocket_w = 90
        self.rocket_h = 110
        self.bullet_w = 25
        self.bullet_h = 25
        self.enemy_w = 70
        self.enemy_h = 90

        # button dimensions and colors
        self.play_w = 220
        self.play_h = 80
        self.play_text = 40
        self.play_color = (200, 30, 200)
        self.play_color_text = (255, 255, 255)

        # velocities 
        self.rocket_v = 5
        self.bullet_v = 4
        self.enemy_v = 1 

        # bullet capacity
        self.capacity = 5
        # spawn new enemy gab
        self.spawn_gab = 100 
        # points when shooting enemy
        self.points = 100 
        self.start_speed = 1 
        self.speed_up = 1.05