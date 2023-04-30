import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
CAPTION = pygame.display.set_caption("T-Engine")

class LOAD_ICON:
    def __init__():
        ICON = pygame.image.load_image("./icon.png")

class RUN:
    def START(self):
        self.RUNNING = True
        while self.RUNNING == True:
            for EVENT in pygame.event.get():
                if EVENT.type == pygame.QUIT:
                    self.RUNNING = False
                    pygame.quit()
                    
            LOAD_ICON()
                    
if __name__ == '__main__':
    GAME = RUN()
    GAME.START()
