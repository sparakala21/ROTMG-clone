import pygame, sys
from settings import *
from debug import debug
from level import Level

class Game:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("The Mad God's realm")
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while not self.level.game_ended:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()
            
            self.screen.fill('black')
            debug(self.clock)            
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)
        



if __name__=="__main__":
    while True:
        game = Game()
        game.run()
    