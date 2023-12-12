import pygame

from Consts import *


class Platform:
    def __init__(self, x, y, size_x, size_y, key_up, key_down):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.key_up = key_up
        self.key_down = key_down
        self.dy = 1
        self.image = pygame.Surface((size_x, size_y))
        self.rect = self.image.get_rect()

    def move(self, key):
        if key == self.key_up:
            self.y += self.dy
        if key == self.key_down:
            self.y += self.dy

    def update(self):
        self.x = max(0 + self.size_x, min(WHIDTH - self.size_x, self.x))
        self.y = max(0 + self.size_y, min(HEIGHT - self.size_y, self.y))
        self.rect.x = self.x - self.size_x // 2
        self.rect.y = self.y - self.size_y // 2
