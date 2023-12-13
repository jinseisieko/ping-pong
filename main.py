"""pygame main loop"""
import sys
import time

from tqdm import tqdm

from Ball import Ball
from Consts import *
from Platform import Platform


def win_text_draw(time, win, ts):
    st = f"Player {win} win!"
    ln = int((time - ts) / 3 * len(st))
    screen.blit(pygame.font.Font(None, 90).render(st[:ln + 1], True, (255, 255, 255)), (WHIDTH / 2, 40))
    if ln == len(st):
        return win


pygame.init()

ball = Ball(WHIDTH / 2, HEIGHT / 2, 20, 5, 3 / 4)

size_x = 30
size_y = 100

x = 10
y = HEIGHT / 2

platform_left = Platform(x, y, size_x, size_y, pygame.K_w, pygame.K_s)
platform_right = Platform(WHIDTH - x - size_x, y, size_x, size_y, pygame.K_UP, pygame.K_DOWN)

screen = pygame.display.set_mode((WHIDTH, HEIGHT))
s1, s2 = 0, 0
running = True
win = 0
flag = 1
with (tqdm() as pbar):
    while running:

        current_time: int = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_DELETE]:
                running = False
                quit()
            if flag == 2:
                if event.type == pygame.KEYDOWN:
                    flag = 1

        if flag == 1:
            keys = pygame.key.get_pressed()
            platform_left.update(keys)
            platform_right.update(keys)
            ball.update(CLOCK.get_fps())

            ball.collision_pl(platform_left)
            ball.collision_pl(platform_right)

            ball.collision_box(HEIGHT)

            screen.fill(0)
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
                platform_right = Platform(WHIDTH - x - size_x, y, size_x, size_y, pygame.K_UP, pygame.K_DOWN)
                if s2 == 3:
                    ts = time.time()
                    flag = 0
                    win = 2

            if ball.x >= WHIDTH:
                s1 += 1
                ball.kill()
                platform_left.kill()
                platform_right.kill()
                ball = Ball(WHIDTH / 2, HEIGHT / 2, 20, 5, 3 - 3 / 4)
                platform_left = Platform(x, y, size_x, size_y, pygame.K_w, pygame.K_s)
                platform_right = Platform(WHIDTH - x - size_x, y, size_x, size_y, pygame.K_UP, pygame.K_DOWN)
                if s1 == 3:
                    ts = time.time()
                    flag = 0
                    win = 1


        elif flag == 0:
            screen.fill(0)
            screen.blit(pygame.font.Font(None, 90).render(str(s1), True, (255, 255, 255)), (WHIDTH / 3, 40))
            screen.blit(pygame.font.Font(None, 90).render(str(s2), True, (255, 255, 255)), (WHIDTH - WHIDTH / 3, 40))
            st = f"Player {win} won!"
            ln = int((time.time() - ts) / 3 * len(st))
            screen.blit(pygame.font.Font(None, 90).render(st[:ln + 1], True, (255, 255, 255)),
                        (0, HEIGHT - 100))
            if ln == len(st):
                flag = 2
                s1 = 0
                s2 = 0

        pygame.display.flip()
        CLOCK.tick(100)
        pbar.update(1)
pygame.quit()
sys.exit()
