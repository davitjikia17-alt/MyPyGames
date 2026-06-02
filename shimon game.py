import pygame
import sys

pygame.init()

# SCREEN
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("shimon gay")

clock = pygame.time.Clock()

# COLORS
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)

# BALL
ball_x = 300
ball_y = 200
ball_radius = 20

ball_speed_x = 5
ball_speed_y = 4

# GAME LOOP
while True:

    # EXIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # MOVE BALL
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # BOUNCE ON WALLS
    if ball_x <= ball_radius or ball_x >= WIDTH - ball_radius:
        ball_speed_x *= -1

    if ball_y <= ball_radius or ball_y >= HEIGHT - ball_radius:
        ball_speed_y *= -1

    # DRAW
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (int(ball_x), int(ball_y)), ball_radius)

    pygame.display.update()
    clock.tick(60)