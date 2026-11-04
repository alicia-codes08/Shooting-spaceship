import pygame 
import sys
from pygame.sprite import Group 

from rocket import Rocket
from bullets import Bullets 
from settings import Settings 


class Shooting_Rocket():
    """Main class"""

    def __init__(self):
        """Initialize attributes."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings() # settings

        # background
        self.screen = pygame.display.set_mode((self.settings.screen_w, 
                                               self.settings.screen_h))
        self.background_image = pygame.image.load("space_bg.png").convert()
        self.background = pygame.transform.scale(self.background_image,
                            (self.settings.screen_w, self.settings.screen_h)) 
        # game elements
        self.rocket = Rocket(self) 
        self.bullets = pygame.sprite.Group()
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

    def create_enemies(self):
        """Create an enemy that moves."""     

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
        if len(self.bullets) < self.settings.capacity:
            new_bullet = Bullets(self)
            self.bullets.add(new_bullet) 


    def draw(self):
        """Draw the game based on game events.""" 
        self.screen.blit(self.background, (0, 0))
        self.rocket.draw_rocket()
        for bullet in self.bullets:
            bullet.update() 
            bullet.draw_bullet() 
        pygame.display.flip()



# running the game 
if __name__ == "__main__":
    shooting_rocket = Shooting_Rocket()
    shooting_rocket.run()  