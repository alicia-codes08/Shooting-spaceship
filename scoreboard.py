import pygame.font

class Scoreboard():
    """Class to manage the scoreboard."""

    def __init__(self, shooting_rocket):
        """Initialize attributes."""
        self.settings = shooting_rocket.settings
        self.stats = shooting_rocket.stats 
        self.screen = shooting_rocket.screen
        self.screen_rect = self.screen.get_rect()
        self.play_button = shooting_rocket.play_button

        # characteristics
        self.text_c = self.settings.play_color_text
        self.font = pygame.font.Font("press_start_2p/PressStart2P.ttf", 20)
        self.font_high = pygame.font.Font("press_start_2p/PressStart2P.ttf", 25)

        self.score_text()
        self.highscore_text() 

    def score_text(self):
        """Display the score in the bottom right."""
        self.score = f"SCORE: {self.stats.score:,}"
        self.score_img = self.font.render(self.score, True,
                        self.settings.play_color_text, None)

        self.score_rect = self.score_img.get_rect() 
        self.score_rect.right = self.settings.screen_w - 20
        self.score_rect.bottom = self.settings.screen_h - 20

    def highscore_text(self):
        """Display the highscore above the playbutton."""
        self.highscore = f"HIGHSCORE: {self.stats.highscore:,}"
        self.highscore_img = self.font_high.render(self.highscore, True, 
                            self.settings.play_color_text, None)

        self.highscore_rect = self.highscore_img.get_rect()
        self.highscore_rect.center = self.screen_rect.center
        self.highscore_rect.bottom = self.play_button.play_rect.top - 30 
        

    def draw_scoreboard(self):
        """Drawing the scoreboard on the screen."""
        if self.stats.active:
            self.screen.blit(self.score_img, self.score_rect) 
        else:
            self.screen.blit(self.highscore_img, self.highscore_rect)