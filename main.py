import pygame 
import sys

class Shooting_Rocket():
    """Main class"""

    def __init__(self):
        """Initialize attributes."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 600))

        # settings
        self.bg_color = (0, 0, 50)

        # give a caption 
        pygame.display.set_caption("SHOOTING ROCKET!")

    def run(self):
        """Run the game."""
        while True:
            self._activity()
            self.draw() 
            self.clock.tick(60)            

    def _activity(self):
        """Take action based on keyboard activity."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit() 


    def draw(self):
        """Draw the game based on game events.""" 
        self.screen.fill(self.bg_color)
        pygame.display.flip()


# running the game 
if __name__ == "__main__":
    shooting_rocket = Shooting_Rocket()
    shooting_rocket.run() 