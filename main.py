import pygame 
import sys
from pygame.sprite import Group 

from rocket import Rocket
from bullets import Bullets 
from settings import Settings 
from enemies import Enemy 
from statistics import Stats
from play_button import Play


class Shooting_Rocket():
    """Class to run the game and manages the logic of the game elements."""

    def __init__(self):
        """Initialize attributes."""
        pygame.init() 
        self.clock = pygame.time.Clock()
        self.settings = Settings() # settings
        self.stats = Stats(self)
        # background
        self.screen = pygame.display.set_mode((self.settings.screen_w, 
                                               self.settings.screen_h)) 
        self.background_image = pygame.image.load("space_bg.png").convert()
        self.background = pygame.transform.scale(self.background_image,
                            (self.settings.screen_w, self.settings.screen_h)) 
        # game elements
        self.rocket = Rocket(self) 
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        # give a caption 
        pygame.display.set_caption("SHOOTING SPACESHIP!") 
        # play button
        self.play_button = Play(self) 


    def run(self):
        """Run the game."""
        while True:
            self._activity()
            if self.stats.active:
                self.create_enemies()
                self.rocket.moving_rocket() 
                self._check_enemies() 
                self._check_bullet()
                self.check_collision() 
                self.draw()     
            self.draw() 
            self.clock.tick(60)

    def check_collision(self):
        """Check if collision between bullets and enemies took place."""
        for bullet in self.bullets.copy():
            for enemy in self.enemies.copy():
                if bullet.bullet_rect.colliderect(enemy.enemy_rect):
                    self.bullets.remove(bullet)
                    self.enemies.remove(enemy)

        # Stop the game after rocket hits an enemy
        for enemy in self.enemies.copy():
            if self.rocket.rocket_rect.colliderect(enemy.enemy_rect):
                self.stats.active = False 
        # Stop the game after an enemy hits the bottom of the screen 
        for enemy in self.enemies.copy():
            if enemy.enemy_rect.bottom >= self.settings.screen_h:
                self.stats.active = False

    def create_enemies(self):
        """Create an enemy."""  
        if len(self.enemies)==0:
            new_enemy =  Enemy(self)
            self.enemies.add(new_enemy) 
        elif len(self.enemies)!=0:
            last_enemy = self.enemies.sprites()[-1]
            if last_enemy.enemy_rect.y>=self.settings.spawn_gab:
                new_enemy =  Enemy(self)
                self.enemies.add(new_enemy) 

    def _check_enemies(self):
        """Remove enemies, that are not visible anymore."""
        if self.enemies:
            for enemy in self.enemies:
                if enemy.enemy_rect.top >= self.settings.screen_h:
                    self.enemies.remove(enemy)
                
    def _check_bullet(self):
            """Remove bullets, that are not on the screen anymore."""
            if self.bullets:
                for bullet in self.bullets.copy():
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
        for enemy in self.enemies:
            enemy.update()
            enemy.draw_enemy() 
        # drawing on the screen when inactive
        if not self.stats.active:
            self.play_button.draw_playbutton()
        pygame.display.flip() 



# running the game 
if __name__ == "__main__":
    shooting_rocket = Shooting_Rocket()
    shooting_rocket.run()  