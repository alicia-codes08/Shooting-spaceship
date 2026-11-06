class Stats():
    """class to manage the status of the game"""
    def __init__(self, shooting_rocket):
        """Initialize attributes."""
        # settings
        self.settings = shooting_rocket.settings
        # game status
        self.active = False
        # highscore 
        self.highscore = 0 

        self.reset_stats() 

    def reset_stats(self):
        """Let the statistics change during the game and reset it afterwards."""
        self.score = 0