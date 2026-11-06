import pygame.font

class Play():
    """class to manage the playbutton."""

    def __init__(self, shooting_rocket):
        """Initialize attributes."""
        self.screen = shooting_rocket.screen
        self.screen_rect = self.screen.get_rect() 
        self.settings = shooting_rocket.settings

        # characteristics
        self.play_w, self.play_h = self.settings.play_w, self.settings.play_h
        self.play_c = self.settings.play_color 
        self.text_c = self.settings.play_color_text
        self.play_font = pygame.font.SysFont(None, self.settings.play_text)

        self.play_rect = pygame.Rect(0, 0, self.play_w, self.play_h)
        self.play_rect.center = self.screen_rect.center

        self._playbutton_text("PLAY!")

    def _playbutton_text(self, text):
        """Put text on the playbutton."""
        self.text = self.play_font.render(text, True, self.text_c, self.play_c)
        self.text_rect = self.text.get_rect()

        self.text_rect.center = self.screen_rect.center

    def draw_playbutton(self):
        """Draw the playbutton on the screen."""
        self.screen.fill(self.play_c, self.play_rect)
        self.screen.blit(self.text, self.text_rect) 