import pygame
import sys

pygame.init()

# SCREEN
WIDTH = 1000
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game")

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)

# PLAYER
player_x = 100
player_y = 100
player_size = 50
player_speed = 5

# ENEMY
enemy_x = 400
enemy_y = 300
enemy_size = 50
enemy_speed = 4

clock = pygame.time.Clock()

# GAME LOOP
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # INPUT
    keys = pygame.key.get_pressed()

    # PLAYER MOVEMENT (WASD)
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed
    if keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_s]:
        player_y += player_speed

    # ENEMY MOVEMENT (ARROWS)
    if keys[pygame.K_LEFT]:
        enemy_x -= enemy_speed
    if keys[pygame.K_RIGHT]:
        enemy_x += enemy_speed
    if keys[pygame.K_UP]:
        enemy_y -= enemy_speed
    if keys[pygame.K_DOWN]:
        enemy_y += enemy_speed

    # DRAW BACKGROUND
    screen.fill(WHITE)

    # DRAW PLAYER
    pygame.draw.rect(
        screen,
        BLUE,
        (player_x, player_y, player_size, player_size)
    )

    # DRAW ENEMY
    pygame.draw.rect(
        screen,
        BLACK,
        (enemy_x, enemy_y, enemy_size, enemy_size)
    )

    # COLLISION DETECTION (GAME OVER)
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)

    if player_rect.colliderect(enemy_rect):
        print("GAME OVER 💀")
        pygame.quit()
        sys.exit()

    # UPDATE SCREEN
    pygame.display.update()
    clock.tick(60)