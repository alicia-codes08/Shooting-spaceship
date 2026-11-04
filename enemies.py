import pygame
from pygame.sprite import Sprite 

class Enemies(Sprite):
    """Class for the enemies behavior."""

    def __init__(self, shooting_rocket):
        """Initialize attributes."""
        self.screen = shooting_rocket.screen