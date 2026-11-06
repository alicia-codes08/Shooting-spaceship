import pygame.font

class Scoreboard():
    """Class to manage the scoreboard."""

    def __init__(self, shooting_rocket):
        """Initialize attributes."""
        self.settings = shooting_rocket.settings
        self.stats = shooting_rocket.stats 
        self.screen = shooting_rocket.screen
        self.screen_rect = self.screen.get_rect()

        # characteristics
        self.text_c = self.settings.play_color_text
        self.font = pygame.font.SysFont(None, 34)

        self.score_text()

    def score_text(self):
        """Display the score in the bottom right."""
        self.score = f"SCORE: {self.stats.score:,}"
        self.score_img = self.font.render(self.score, True,
                        self.settings.play_color_text ,self.settings.play_color)

        self.score_rect = self.score_img.get_rect() 
        self.score_rect.right = self.settings.screen_w - 30
        self.score_rect.bottom = self.settings.screen_h - 30

    def draw_scoreboard(self):
        self.screen.blit(self.score_img, self.score_rect)