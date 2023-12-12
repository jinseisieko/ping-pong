"""pygame main loop"""
import sys

import pygame
from tqdm import tqdm

pygame.init()



ball = Ball(x, y, ds, dy, angle)

size_x = 10
size_y = 100

x = 10

platform_left = Platform(x, y, size_x, size_y, pygame.K_w, pygame.K_s)
platform_right = Platform(x, y, size_x, size_y, pygame.K_UP, pygame.K_DOWN)

running = True
with (tqdm() as pbar):
    while running:

        current_time: int = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_DELETE]:
                running = False
                quit()

            if event.type == pygame.KEYDOWN:
                platform_left.move(pygame.key.get_pressed())
                platform_right.move(pygame.key.get_pressed())



        pbar.update(1)
pygame.quit()
sys.exit()
