from Consts import *


class Platform:
    def __init__(self, x, y, size_x, size_y, key_up, key_down):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.key_up = key_up
        self.key_down = key_down
        self.dy = 10
        self.image = pygame.Surface((size_x, size_y))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

    def move(self, keys):
        if keys[self.key_up]:
            if CLOCK.get_fps() != 0:
                self.y -= self.dy * TICKS / (CLOCK.get_fps() + 1e-10)
        if keys[self.key_down]:
            if CLOCK.get_fps() != 0:
                self.y += self.dy * TICKS / (CLOCK.get_fps() + 1e-10)

    def update(self, keys):
        self.move(keys)
        self.x = max(0, min(WHIDTH - self.size_x, self.x))
        self.y = max(0, min(HEIGHT - self.size_y, self.y))
        self.rect.x = self.x
        self.rect.y = self.y
