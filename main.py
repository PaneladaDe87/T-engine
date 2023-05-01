import pygame

pygame.init()

BLACK = (0, 0, 0)

SCREEN_SIZE = ((1280, 720))

WINDOW = pygame.display.set_mode(SCREEN_SIZE)
CAPTION = pygame.display.set_caption("T-Engine")

class RUN:
    def START(self):
        self.RUNNING = True
        while self.RUNNING == True:
            for EVENT in pygame.event.get():
                if EVENT.type == pygame.QUIT:
                    self.RUNNING = False
                    
            WINDOW.fill(BLACK)
            pygame.display.flip()
                    
        pygame.quit()
                    
if __name__ == '__main__':
    GAME = RUN()
    GAME.START()
