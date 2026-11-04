class Settings():
    """Save all settings."""
    def __init__(self):
        """Save basic settings.""" 
        # screen settings
        self.screen_w = 800
        self.screen_h = 600 

        # element dimensions
        self.rocket_w = 70
        self.rocket_h = 90
        self.bullet_w = 30
        self.bullet_h = 30 

        # velocity
        self.rocket_v = 2
        self.bullet_v = 4

        # bullet capacity
        self.capacity = 5