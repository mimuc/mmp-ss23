import pygame
from pygame.locals import *
from YoshiWithAnimation import YoshiWithAnimation

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
bomb1 = YoshiWithAnimation((0,0),4)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.fill((255, 255, 255))
    time_passed = clock.tick() / 1000.0
    bomb1.update(time_passed)
    screen.blit(bomb1.image,bomb1.rect)
    pygame.display.update()
