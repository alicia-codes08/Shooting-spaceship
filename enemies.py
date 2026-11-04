import pygame
from pygame.sprite import Sprite 

from random import randint 


class Enemies(Sprite):
    """Class for the enemies behavior."""

    def __init__(self, shooting_rocket):
        """Initialize attributes."""
        self.settings = shooting_rocket.settings # settings
        self.screen = shooting_rocket.screen
        self.screen_rect = self.screen.get_rect() 

        self.enemy_image = pygame.image.load("enemy_ship.png").convert_alpha()
        self.enemy_scaled = pygame.transform.scale(self.enemy_image, 
                                (self.settings.enemy_w, self.settings.enemy_h))
        self.enemy = pygame.transform.rotate(self.enemy_scaled, 180) 
        self.enemy_rect = self.enemy.get_rect()

        # positioning the enemy
        self.enemy_rect.midbottom = self.screen_rect.midtop 
        self.enemy.x = randint(self.settings.screen_w) 

        self.y = float(self.enemy.y)

    def move_enemy(self):
        """Move the enemy along the y-axis."""
        self.y += self.settings.enemy_v 
        self.enemy.y = self.y 