import pygame
from pygame.locals import *

class Box(pygame.sprite.Sprite):
    def __init__(self, initial_position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("head.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = initial_position
        #sprite should have mask attribute (else is computed every time)
        #self.mask = pygame.mask.from_surface(self.image)

    def update(self, pos):
        self.rect.center = pos

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
box1 = Box((200,200))
box2 = Box((100,10))
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == MOUSEMOTION:
            box2.update(pygame.mouse.get_pos())
            if pygame.sprite.collide_mask(box1,box2):
                print("collide")
            else:
                print("no")

    screen.fill((100, 200, 0))
    screen.blit(box1.image,box1.rect)
    screen.blit(box2.image,box2.rect)
    pygame.display.update()
