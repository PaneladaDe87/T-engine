import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
CAPTION = pygame.display.set_caption("T-Engine")

class RUN:
    def START(self):
        self.RUNNING = True
        while self.RUNNING == True:
            for EVENT in pygame.event.get():
                if EVENT.type == pygame.QUIT:
                    self.RUNNING = False
                    pygame.quit()
                    
if __name__ == '__main__':
    GAME = RUN()
    GAME.START()
