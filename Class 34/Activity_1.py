# Draw a rectangle:

import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(50, 90, 140, 50))
    pygame.display.flip()