import pygame
from pygame.locals import *
from sys import exit
from Vector import Vector

mpos = (0.0,0.0)
destination = (500,430)
player_image = '../dragon-500px.png'
pygame.init()

screen = pygame.display.set_mode((640, 640), 0, 32)
pygame.display.set_caption("Animate X!")

mouse_cursor = pygame.image.load(player_image).convert_alpha()
clock = pygame.time.Clock()

speed = 300.0 # pixels per second
heading = Vector.vector_from_points(mpos, destination)
heading.normalize()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.fill((255, 255, 255))

    time_passed = clock.tick() / 1000.0
    moved_distance = time_passed * speed

    screen.blit(mouse_cursor, mpos)
    mpos = (mpos[0] + heading.x * moved_distance, mpos[1] + heading.y * moved_distance)
    pygame.display.update()


