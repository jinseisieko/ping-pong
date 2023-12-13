import math

import pygame.sprite

from Consts import *


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, size, startv, an) -> None:
        super().__init__()

        self.size = size
        self.image = pygame.Surface((size, size))
        pygame.draw.circle(self.image, (255, 255, 255), (size / 2, size / 2), size / 2)
        self.rect = self.image.get_rect()

        self.x, self.y = x, y

        self.v = startv
        self.an = an

        self.vx = 0.
        self.vy = 0.

    def collision_pl(self, pl):
        if pl.rect.colliderect(self.rect):
            self.an = -(self.an + math.pi)
            self.v += 1
            self.update()

    def collision_box(self, h):
        if self.y <= 0:
            self.an = 2 * math.pi - self.an
            self.update()
        if self.y >= h - self.size:
            self.an = 2 * math.pi - self.an
            self.update()

    def update(self):
        self.vx = self.v * math.cos(self.an)
        self.vy = self.v * math.sin(self.an)
        if CLOCK.get_fps() != 0:
            self.x += self.vx * TICKS / (CLOCK.get_fps() + 1e-10)
            self.y += self.vy * TICKS / (CLOCK.get_fps() + 1e-10)

        self.rect.x = round(self.x)
        self.rect.y = round(self.y)
