import pygame
import numpy

# resolution ignored in mobile devices
width = 1280
height = 720

# draw cube
class cube:
    def model(self, size):
        distance = 50
        
        # create a cube
        self.size = size
        
        self.vertices = [
            numpy.array([x, y, z])
            for x in (-size, size)
            for y in (-size, size)
            for z in (-size, size)
        ]
        
    def draw(self, surface):
        for v in self.vertices:
            x, y, z = v
            x, y = x * 2 / (2 - z / self.size), y * 2 / (2 - z / self.size)

def game():
    running = True
    window = pygame.display.set_mode((width, height))
    caption = pygame.display.set_caption("T-Engine")
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    touch = True
