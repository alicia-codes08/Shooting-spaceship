import pygame
from pygame.sprite import Sprite 

from random import randint 


class Enemy(Sprite):
    """Class for the enemies behavior."""

    def __init__(self, shooting_rocket):
        """Initialize attributes."""
        super().__init__()

        self.settings = shooting_rocket.settings # settings
        self.stats = shooting_rocket.stats
        self.screen = shooting_rocket.screen
        self.screen_rect = self.screen.get_rect() 

        self.enemy_image = pygame.image.load("enemy_ship.png").convert_alpha()
        self.enemy_scaled = pygame.transform.scale(self.enemy_image, 
                                (self.settings.enemy_w, self.settings.enemy_h))
        self.enemy = pygame.transform.rotate(self.enemy_scaled, 180) 
        self.enemy_rect = self.enemy.get_rect()

        # positioning the enemy
        self.enemy_rect.midbottom = self.screen_rect.midtop 
        left_side = int(self.settings.enemy_w*0.5)
        right_side = int(self.settings.screen_w - self.settings.enemy_w*1.5)
        self.enemy_rect.x = randint(left_side, right_side) 

        self.y = float(self.enemy_rect.y) 

    def draw_enemy(self):
        """Draw the enemy on the screen."""
        self.screen.blit(self.enemy, self.enemy_rect)

    def update(self):
        """Move the enemy along the y-axis."""
        if self.stats.active:
            self.y += self.settings.enemy_v * self.stats.speed
            self.enemy_rect.y = self.y 