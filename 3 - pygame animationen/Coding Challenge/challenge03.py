import pygame, time
from pygame.locals import *
from sys import exit
from Vector import Vector

player_image = 'dragon-500px.png'
pygame.init()

screen = pygame.display.set_mode((1200, 900), 0, 32)
pygame.display.set_caption("Animate X!")
dragon = pygame.image.load(player_image).convert_alpha()

clock = pygame.time.Clock()

speed = 300.0

pos = (100, 100)
destination = pos

while True:
    time_passed = clock.tick(60) / 1000.0
    moved_distance = time_passed * speed
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            destination = pygame.mouse.get_pos()
            print(destination)

    screen.fill((255,255,255))

    heading = Vector.vector_from_points(pos, destination)

    # only move when pos is not yet too close to destination
    if heading.get_magnitude() > 2.5:
        heading.normalize()
        pos = (pos[0] + heading.x * moved_distance, pos[1] + heading.y * moved_distance)

    screen.blit(dragon, (pos[0]-dragon.get_width()/2, pos[1]-dragon.get_height()/2))

    pygame.display.update()

