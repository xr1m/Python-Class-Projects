# Space Invader game:

import pygame
import random
import math

SCREEN_HEIGHT, SCREEN_WIDTH = 1024, 768


player_start_x = 470
player_start_y = 600

enemy_start_y_min = 50
enemy_start_y_max = 150
enemy_speed_x = 2
enemy_speed_y = 20

bullet_speed_y = 10

collision_distance = 27

pygame.init()
screen_size = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
bg = pygame.image.load("spaceinvaderbg.jpg")
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)
player_image = pygame.image.load("spaceship.png")
player_x = player_start_x
player_y = player_start_y
player_x_change = 0
player_y_change = 0

enemy_image = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
enemy_number = 6

for _i in range(enemy_number):
    enemy_image.append(pygame.image.load("alienship.jpg"))
    enemy_x.append(random.randint(0, SCREEN_WIDTH - 20))
    enemy_y.append(random.randint(enemy_start_y_min, enemy_start_y_max))
    enemy_x_change.append(enemy_speed_x)
    enemy_y_change.append(enemy_speed_y)

bullet_img = pygame.image.load("bulletimage.jpg")
bullet_x = 0
bullet_y = player_start_y
bullet_x_change = 0
bullet_y_change = bullet_speed_y
bullet_state = "Ready."

score_value = 0

font = pygame.font.Font("freesansbold.ttf", 34)
text_x = 10
text_y = 10

game_over_text = pygame.font.Font("freesansbold.ttf", 64)

def showscore(x, y):
    score = font.render("Score:" + str(score_value), True, (255, 255, 255))
    screen_size.blit(score, (x, y))

def showgameover():
    game_over = font.render("Game over!", True, (255, 255, 255))
    screen_size.blit(game_over, (200, 250))

def player(x, y):
    screen_size.blit(player_image, (x, y))

def enemy(x, y, i):
    screen_size.blit(enemy_image[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "Fire!"
    screen_size.blit(bullet_img, (x + 16, y + 10))

def collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((enemy_x - bullet_x)**2 + (enemy_y - bullet_y)**2)
    return distance < collision_distance

running = True
while running:
    screen_size.fill((0, 0, 0))
    screen_size.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
            if event.key == pygame.K_UP:
                player_y_change = 5
            if event.key == pygame.K_DOWN:
                player_y_change = -5
            if event.key == pygame.K_SPACE and bullet_state == "Ready.":
                bullet_x = player_x
                fire_bullet(bullet_x, bullet_y)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            player_x_change = 0
        if event.type == pygame.KEYUP and event.key in [pygame.K_UP, pygame.K_DOWN]:
            player_y_change = 0
    player_x += player_x_change
    player_x = max(0, min(player_x, SCREEN_WIDTH - 20))
    for i in range(enemy_number):
        if enemy_y[i] > 350:
            for j in range(enemy_number):
                enemy_y[j] == 2000
            showgameover()
            break
        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0 or enemy_x[i] >= SCREEN_WIDTH - 20:
            enemy_x_change[i] *= -1
            enemy_y[i] += enemy_y_change[i]

        if collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y):
            bullet_y = player_start_y
            bullet_state = "Ready."
            score_value += 1
            enemy_x[i] = random.randint(0, SCREEN_WIDTH-20)
            enemy_y[i] = random.randint(enemy_start_y_min, enemy_start_y_max)
        enemy(enemy_x[i], enemy_y[i], i)
    if bullet_y <= 0:
        bullet_y = player_start_y
        bullet_state = "Ready."
    elif bullet_state == "Fire!":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change
    player(player_x, player_y)
    showscore(text_x, text_y)
    pygame.display.flip()