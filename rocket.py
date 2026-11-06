import pygame


class Rocket():
    """class to manage the shooting rocket."""

    def __init__(self, shooting_rocket):
        """Initialize attributes."""
        self.screen = shooting_rocket.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = shooting_rocket.settings # settings
        self.stats = shooting_rocket.stats

        # rocket image 
        rocket_load = pygame.image.load("purple_rocket.png").convert_alpha()
        self.rocket = pygame.transform.scale(rocket_load, 
                            (self.settings.rocket_w, self.settings.rocket_h))
        self.rocket_rect = self.rocket.get_rect() 

        # start rocket in the middle on the bottom of the screen
        self.rocket_rect.midbottom = self.screen_rect.midbottom
        self.rocket_rect.y -= 30 

        self.moving_right = False
        self.moving_left = False

    def draw_rocket(self):
        """Drawing the rocket on the screen."""
        self.screen.blit(self.rocket, self.rocket_rect) 

    def moving_rocket(self):
        """Moving rocket horizontal."""
        if self.moving_right and (self.rocket_rect.right<self.screen_rect.right):
            self.rocket_rect.x += self.settings.rocket_v * self.stats.speed
        if self.moving_left and (self.rocket_rect.left>0):
            self.rocket_rect.x -= self.settings.rocket_v * self.stats.speed

    def center_rocket(self):
        """Center the rocket when starting a new game."""
        self.rocket_rect.midbottom = self.screen_rect.midbottom
        self.rocket_rect.y -= 30 
