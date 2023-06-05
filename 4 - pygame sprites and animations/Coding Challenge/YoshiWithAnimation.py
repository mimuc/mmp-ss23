import os, pygame
from pygame.locals import *

def load_sliced_sprites(w, h, filename, padding_y = 0):
    images = []
    master_image = pygame.image.load(filename).convert_alpha()

    master_image.set_colorkey((255, 0, 255))
    master_width, master_height = master_image.get_size()

    for i in range(int(master_width/w)):
        images.append(master_image.subsurface((i * w, padding_y, w, h)))

    return images


class YoshiWithAnimation(pygame.sprite.Sprite):
    def __init__(self, initial_position, fps):
        pygame.sprite.Sprite.__init__(self)
        self.act_frame = 0
       # create the images for the animation
        self.frames = load_sliced_sprites(25, 35, "yoshi_spritesheet_by_yoshi888_d2jjcax_cropped_1to3.png", 0)
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = initial_position
        self.fps = fps
        self.change_time = 1.0/self.fps
        self.time = 0

    def update(self, time_passed):
        self.time += time_passed
        if self.time >= self.change_time:
            self.act_frame = (self.act_frame + 1) % len(self.frames)
            self.image = self.frames[self.act_frame]
            self.time = 0

