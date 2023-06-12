import pygame
import math
import random
from pygame.locals import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, initial_position):
        pygame.sprite.Sprite.__init__(self)
        size = 20
        self.image = pygame.Surface((size,size),pygame.SRCALPHA,32)
        pygame.draw.circle(self.image,color,(int(size/2),int(size/2)),int(size/2))
        self.rect = self.image.get_rect()
        self.rect.topleft = initial_position
        self.speed = 500
        self.click_sound = pygame.mixer.Sound("click.wav")

    def update(self, time_passed, size):
        moved_distance = math.ceil(time_passed * self.speed)
        self.rect.left += moved_distance
        if self.rect.right >= size[0]:
            self.rect.right = size[0]
            self.speed = -self.speed
            channel = self.click_sound.play()
            channel.set_volume(0.0,1.0)
        if self.rect.left <= 0:
            self.rect.left = 0
            self.speed = -self.speed
            channel = self.click_sound.play()
            channel.set_volume(1.0,0.0)

pygame.init()

screen_width = 1000
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
ball = Ball((255,0,0),(200,100))

ballsprites = pygame.sprite.RenderUpdates()
ballsprites.add(ball)

background = pygame.Surface((screen_width,screen_height))
background.fill((255,255,255))
screen.blit(background,(0,0))
pygame.display.update()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            new_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            new_ball = Ball(new_color,event.pos)
            ballsprites.add(new_ball)
    screen.fill((0, 0, 0))
    time_passed = clock.tick(30) / 1000.0
    
    screen.blit(background,(0,0))

    ballsprites.update(time_passed, (screen_width, screen_height))
    ballsprites.draw(screen)
    pygame.display.update()
