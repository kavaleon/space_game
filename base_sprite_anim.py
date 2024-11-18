from base_sprite import BaseSprite
from random import randint
from config import *

class BaseSpriteAnim(BaseSprite):
    def __init__(self, image='', x=0, y=0, w=0, h=0, speed=0, sprites=[], sprite_group=[]):
        BaseSprite.__init__(self, image=image, x=x, y=y, w=w, h=h, image_pic=sprites[0], speed=speed)
        self.frames = sprites
        self.frame_rate = randint(1, 10)
        self.frame_num = 0
        self.image = self.frames[self.frame_num]
        self.rect = self.image.get_rect()
        self.speed = speed
        self.speed_x = randint(-4, 4)
        self.speed_y = randint(-4,4)
        self.rect.x = x
        self.rect.y = y
        self.add(sprite_group)
        self.ticks = 1


    def next_frame(self):
        if self.ticks % self.frame_rate == 0:
            self.image = self.frames[self.frame_num]
            self.image_orig = self.image
            self.frame_num += 1

        if self.frame_num == len(self.frames):
            self.frame_num = 1

        self.ticks += 1