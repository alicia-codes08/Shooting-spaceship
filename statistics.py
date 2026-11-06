from pathlib import Path

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
        self.getting_highscore() 

    def reset_stats(self):
        """Let the statistics change during the game and reset it afterwards."""
        self.score = 0 
        self.speed = self.settings.start_speed

    def saving_highscore(self):
        """Saving the highscore after leaving the game."""
        saving_file = Path("saved_highscore.txt")
        highscore_str = str(self.highscore)
        saving_file.write_text(highscore_str)  

    def getting_highscore(self):
        """Getting the saved highscore from a file if there if it exists."""
        saved_file = Path("saved_highscore.txt") 
        if saved_file.exists():
            str_highscore = saved_file.read_text(encoding="utf-8")
            self.highscore = int(str_highscore) 
            