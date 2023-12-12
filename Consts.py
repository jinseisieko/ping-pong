from ctypes import windll

import pygame

WHIDTH, HEIGHT = windll.user32.GetSystemMetrics(0), windll.user32.GetSystemMetrics(1)
CLOCK = pygame.time.Clock()
TICKS = 60

