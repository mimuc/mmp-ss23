#!/usr/bin/env python
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.

import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

screen=pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("Pong Pong!")

#Creating 2 bars, a ball and background.
back = pygame.Surface((640,480))
background = back.convert()
background.fill((0,0,0))
bar = pygame.Surface((10,50))
bar1 = bar.convert()
bar1.fill((0,0,255))
wall = pygame.Surface((11,471))
wall = wall.convert()
wall.fill((0,0,255))


circ_sur = pygame.Surface((15,15))
circ = pygame.draw.circle(circ_sur,(0,255,0),(7,7),7)
circle = circ_sur.convert()
circle.set_colorkey((0,0,0))

# some dimsions and start positions
bar1_x, bar1_y = 10., 215.
circle_x, circle_y = 307.5, 232.5
bar1_move = 0.
speed_x, speed_y, speed_circ = 250., 250., 250.

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                bar1_move = -ai_speed
            elif event.key == K_DOWN:
                bar1_move = ai_speed
        elif event.type == KEYUP:
            if event.key == K_UP:
                bar1_move = 0.
            elif event.key == K_DOWN:
                bar1_move = 0.


    screen.blit(background,(0,0))
    frame = pygame.draw.rect(screen,(255,255,255),Rect((5,5),(630,470)),2)
    screen.blit(bar1,(bar1_x,bar1_y))
    screen.blit(wall,(625,5))
    screen.blit(circle,(circle_x,circle_y))
    bar1_y += bar1_move
    if bar1_y < 10:
        bar1_y = 10
    if bar1_y > 420:
        bar1_y = 420

# movement of ball
    time_passed = clock.tick(30)
    time_sec = time_passed / 1000.0
    circle_x += speed_x * time_sec
    circle_y += speed_y * time_sec
    ai_speed = speed_circ * time_sec


#since we don't know anything about collision, ball hitting bars goes like this.
    if circle_x <= bar1_x + 10.:
        if circle_y >= bar1_y - 7.5 and circle_y <= bar1_y + 42.5:
            circle_x = 20.
            speed_x = -speed_x
    if circle_x < 5.:
        circle_x, circle_y = 320., 232.5
        speed_x = -speed_x
        bar1_y= 215.
        # the user failed
        rand_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        circ = pygame.draw.circle(circ_sur,rand_color,(7,7),7)
        circle = circ_sur.convert()
        circle.set_colorkey((0, 0, 0))

    elif circle_x > 608.:
        speed_x = -speed_x
        circle_x = 608.
    if circle_y <= 10.:
        speed_y = -speed_y
        circle_y = 10.
    elif circle_y >= 457.5:
        speed_y = -speed_y
        circle_y = 457.5

    pygame.display.update()
