import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
    """class to manage the behavior of bullets."""

    def __init__(self, shooting_rocket):
        """Initialize attributes"""
        super().__init__()

        self.screen = shooting_rocket.screen
        self.screen_rect = self.screen.get_rect() 

        self.settings = shooting_rocket.settings # settings

        self.rocket = shooting_rocket.rocket
        self.rocket_rect = self.rocket.rocket_rect

        # image of an individual bullet
        bullet_image = pygame.image.load("bullet.png").convert_alpha()
        self.bullet = pygame.transform.scale(bullet_image, 
                            (self.settings.bullet_w, self.settings.bullet_h))
        self.bullet_rect = self.bullet.get_rect() 

        # fire bullets form the middle top of the rocket
        self.bullet_rect.midtop = self.rocket_rect.midtop 

        self.y = float(self.bullet_rect.y)


    def draw_bullet(self):
        """Draw the bullet on the screen."""
        self.screen.blit(self.bullet, self.bullet_rect) 

    def update(self):
        """Move the bullets verticaly."""
        self.y -= self.settings.bullet_v 
        self.bullet_rect.y = self.y 