# Pygame Window:

import pygame

pygame.init()
screen = pygame.display.set_mode((450, 450))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()