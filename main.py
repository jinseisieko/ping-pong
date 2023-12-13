"""pygame main loop"""
import sys

from tqdm import tqdm

from Ball import Ball
from Consts import *
from Platform import Platform

pygame.init()

ball = Ball(WHIDTH / 2, HEIGHT / 2, 20, 5, 3 / 4)

size_x = 10
size_y = 100

x = 10
y = HEIGHT / 2

platform_left = Platform(x, y, size_x, size_y, pygame.K_w, pygame.K_s)
platform_right = Platform(WHIDTH - x - size_x, y, size_x, size_y, pygame.K_UP, pygame.K_DOWN)

screen = pygame.display.set_mode((WHIDTH, HEIGHT))
s1, s2 = 0, 0
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

        screen.blit(pygame.font.Font(None, 90).render(str(s1), True, (255, 255, 255)), (WHIDTH / 3, 40))
        screen.blit(pygame.font.Font(None, 90).render(str(s2), True, (255, 255, 255)), (WHIDTH - WHIDTH / 3, 40))

        if ball.x <= 0 - ball.size:
            s2 += 1
            ball.kill()
            platform_left.kill()
            platform_right.kill()
            ball = Ball(WHIDTH / 2, HEIGHT / 2, 20, 5, 3 / 4)
            platform_left = Platform(x, y, size_x, size_y, pygame.K_w, pygame.K_s)
            platform_right = Platform(WHIDTH - 2 * x, y, size_x, size_y, pygame.K_UP, pygame.K_DOWN)

        if ball.x >= WHIDTH:
            s1 += 1
            ball.kill()
            platform_left.kill()
            platform_right.kill()
            ball = Ball(WHIDTH / 2, HEIGHT / 2, 20, 5, 3 - 3 / 4)
            platform_left = Platform(x, y, size_x, size_y, pygame.K_w, pygame.K_s)
            platform_right = Platform(WHIDTH - 2 * x, y, size_x, size_y, pygame.K_UP, pygame.K_DOWN)

        pygame.display.flip()
        CLOCK.tick(60)
        pbar.update(1)
pygame.quit()
sys.exit()
