import pygame
import numpy

pygame.init()

BLACK = (0, 0, 0)

WIDTH = 1280
HEIGHT = 720

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
CAPTION = pygame.display.set_caption("T-Engine")

class LOAD_ICON:
    def __init__(self):
        self.ICON = pygame.image.load_image("./icon.png")

class RUN:
    def START(self):
        self.RUNNING = True
        while self.RUNNING == True:
            for EVENT in pygame.event.get():
                if EVENT.type == pygame.QUIT:
                    self.RUNNING = False
                    
            WINDOW.fill(BLACK)
            pygame.display.flip()
                    
        LOAD_ICON()
        pygame.quit()
                    
if __name__ == '__main__':
    GAME = RUN()
    GAME.START()
