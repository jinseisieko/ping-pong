"""pygame main loop"""
import sys

from tqdm import tqdm

from Ball import Ball
from Consts import *
from Platform import Platform

pygame.init()

ball = Ball(WHIDTH / 2, HEIGHT / 2, 50, 5, 3 / 4)

size_x = 50
size_y = 100

x = -500
y = HEIGHT / 2

platform_left = Platform(x, y, size_x, size_y, pygame.K_w, pygame.K_s)
platform_right = Platform(WHIDTH - x - size_x, y, size_x, size_y, pygame.K_UP, pygame.K_DOWN)

screen = pygame.display.set_mode((WHIDTH, HEIGHT))

running = True
with (tqdm() as pbar):
    while running:

        current_time: int = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_DELETE]:
                running = False
                quit()

        screen.fill(0)

        keys = pygame.key.get_pressed()
        platform_left.update(keys)
        platform_right.update(keys)
        ball.update()

        ball.collision_pl(platform_left)
        ball.collision_pl(platform_right)

        ball.collision_box(HEIGHT)

        screen.blit(ball.image, ball.rect)
        screen.blit(platform_left.image, platform_left.rect)
        screen.blit(platform_right.image, platform_right.rect)

        pygame.display.flip()
        CLOCK.tick(60)
        pbar.update(1)
pygame.quit()
sys.exit()
