import pygame
from pygame.locals import *
from Box import Box

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

boxes = ([(255, 0, 0), (0, 0)], [(0, 255, 0), (0, 60)], [(0, 0, 255), (0, 120)])
sprites = pygame.sprite.Group()
for box in boxes:
    sprites.add(Box(box[0], box[1]))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.fill((0, 0, 0))
    time_passed = clock.tick() / 1000.0
    sprites.update(time_passed)

    sprites.draw(screen)
    pygame.display.update()
