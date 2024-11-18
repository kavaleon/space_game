import pygame as pg
from random import randint
from config import *
from base_sprite_anim import *
from base_sprite_rotate import *
from base_sprite import *

where_fly = [(0, randint(0, WINDOW_SIZE[1])),
                     (WINDOW_SIZE[0], randint(0, WINDOW_SIZE[1])),
                     (randint(0, WINDOW_SIZE[0]), 0),
                     (randint(0, WINDOW_SIZE[0]), WINDOW_SIZE[1])]

class Meteor(BaseSpriteRotate, BaseSpriteAnim):
    def __init__(self, sprites: list, sprite_group, image=None):
        self.angle = randint(0, 5)
        x = where_fly[randint(0, 3)][0]
        y = where_fly[randint(0, 3)][1]
        speed = randint(1, 4)
        BaseSpriteAnim.__init__(self, image=None, x=x, y=y, sprites=sprites, sprite_group=sprite_group, speed=speed)
        #BaseSpriteRotate.__init__(self, , x=x, y=y, speed=speed, angle=5)
        self.add(sprite_group)

    def update(self):
        self.next_frame()
        self.rotate()
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.x >= WINDOW_SIZE[0] or self.rect.y >= WINDOW_SIZE[1]:
            self.kill()