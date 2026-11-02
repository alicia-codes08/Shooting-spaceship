import pygame


class Rocket():
    """class to manage the shooting rocket."""

    def __init__(self, shooting_rocket):
        """Initialize attributes."""
        self.screen = shooting_rocket.screen
        self.screen_rect = self.screen.get_rect()

        # rocket image 
        rocket_load = pygame.image.load("rocket.png").convert_alpha()
        self.rocket = pygame.transform.scale(rocket_load, (60, 80))
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
            self.rocket_rect.x += 2
        if self.moving_left and (self.rocket_rect.left>0):
            self.rocket_rect.x -= 2