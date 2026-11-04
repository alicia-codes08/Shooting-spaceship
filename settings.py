class Settings():
    """Save all settings."""
    def __init__(self):
        """Save basic settings.""" 
        # screen settings
        self.screen_w = 700
        self.screen_h = 650 

        # element dimensions
        self.rocket_w = 90
        self.rocket_h = 110
        self.bullet_w = 25
        self.bullet_h = 25
        self.enemy_w = 70
        self.enemy_h = 90

        # velocity
        self.rocket_v = 5
        self.bullet_v = 4
        self.enemy_v = 3 

        # bullet capacity
        self.capacity = 5