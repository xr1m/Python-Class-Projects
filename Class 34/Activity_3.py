# Color Changing Sprite:

import pygame

def main():
    pygame.init()
    WIDTH, HEIGHT = 500, 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Color Changing Sprite.")
    colors = {"Red": pygame.Color("red"), "Blue": pygame.Color("blue"), "Yellow": pygame.Color("yellow"), "Green": pygame.Color("green"), "Purple": pygame.Color("purple")}
    current_color = colors["Blue"]
    x, y = 30, 30
    sprite_width, sprite_height = 60, 60
    clock = pygame.time.Clock()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            x = x-2
        if pressed[pygame.K_RIGHT]:
            x = x+2
        if pressed[pygame.K_UP]:
            y = y+2
        if pressed[pygame.K_DOWN]:
            y = y-2
        x = min(max(0, x), WIDTH-sprite_width)
        y = min(max(0, y), HEIGHT-sprite_height)
        
        if x == 0:
            current_color = colors["Red"]
        elif x == WIDTH-sprite_width:
            current_color = colors["Yellow"]
        elif y == 0:
            current_color = colors["Green"]
        elif y == HEIGHT-sprite_height:
            current_color = colors["Purple"]
        else:
            current_color = colors["Blue"]
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_color, (x, y, sprite_height, sprite_width))
        pygame.display.flip()
        clock.tick(90)
    pygame.quit()

if __name__ == "__main__":
    main()
