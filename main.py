import pygame 
import sys
from pygame.sprite import Group 

from rocket import Rocket
from bullets import Bullets 


class Shooting_Rocket():
    """Main class"""

    def __init__(self):
        """Initialize attributes."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 600)) 
        # game elements
        self.rocket = Rocket(self) 
        self.bullets = pygame.sprite.Group()
        # settings
        self.bg_color = (0, 0, 10)
        # give a caption 
        pygame.display.set_caption("SHOOTING ROCKET!")


    def run(self):
        """Run the game."""
        while True:
            self._activity()
            self.rocket.moving_rocket() 
            self._check_bullet()
            self.draw() 
            self.clock.tick(60)         

    def _check_bullet(self):
            """Remove bullets, that are not on the screen anymore."""
            if self.bullets:
                for bullet in self.bullets:
                    if bullet.bullet_rect.bottom <= 0:
                        self.bullets.remove(bullet)    

    def _activity(self):
        """Take action based on keyboard activity."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit() 
                elif event.key == pygame.K_RIGHT:
                    self.rocket.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.rocket.moving_left = True
                elif event.key == pygame.K_SPACE:
                    self._make_bullet()

            elif event.type == pygame.KEYUP:
                if event.key==pygame.K_RIGHT:
                    self.rocket.moving_right = False
                elif event.key==pygame.K_LEFT:
                    self.rocket.moving_left = False 

    def _make_bullet(self):
        """Make a dart"""
        new_bullet = Bullets(self)
        self.bullets.add(new_bullet) 


    def draw(self):
        """Draw the game based on game events.""" 
        self.screen.fill(self.bg_color)
        self.rocket.draw_rocket()
        for bullet in self.bullets:
            bullet.update() 
            bullet.draw_bullet() 
        pygame.display.flip()


# running the game 
if __name__ == "__main__":
    shooting_rocket = Shooting_Rocket()
    shooting_rocket.run()  