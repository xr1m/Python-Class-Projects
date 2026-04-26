# Colourful bounce:

import pygame
import random

pygame.init()

SPRITE_COLOUR_CHANGE = pygame.USEREVENT + 1
BACKGROUND_COLOUR_CHANGE = pygame.USEREVENT + 2

# For background colours:

Red = pygame.Color("red")
Blue = pygame.Color("blue")
Green = pygame.Color("green")
White = pygame.Color("white")

# Sprite Colour:

Yellow = pygame.Color("yellow")
Orange = pygame.Color("orange")
Sky_Blue = pygame.Color("skyblue")
Dark_Blue = pygame.Color("darkblue")

class sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] =- self.velocity[0]
            boundary_hit = True
        if self.rect.top <= 0 or self.rect.bottom >= 500:
            self.velocity[1] =- self.velocity[1]
            boundary_hit = True
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOUR_CHANGE))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOUR_CHANGE))
    def changecolor(self):
        self.image.fill(random.choice([Yellow, Orange, Sky_Blue, Dark_Blue]))
def change_background_color():
    global bg_color
    bg_color = random.choice([Red, Blue, Green, White])

sprite_list = pygame.sprite.Group()
sp1 = sprite(Yellow, 20, 30)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)
sprite_list.add(sp1)

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My Pygame.")
bg_color = White
screen.fill(bg_color)
exit = False
clock = pygame.time.Clock()
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == SPRITE_COLOUR_CHANGE:
            sp1.changecolor()
        elif event.type == BACKGROUND_COLOUR_CHANGE:
            change_background_color()

    sprite_list.update()
    screen.fill(bg_color)
    sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()