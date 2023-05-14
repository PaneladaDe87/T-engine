import pygame
import numpy

# resolution ignored in mobile devices
width = 1280
height = 720

# draw cube
class cube:
    def model(self):
        distance = 50
        
        # create a cube
        projected_points = []

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
