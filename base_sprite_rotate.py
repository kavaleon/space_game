from base_sprite import BaseSprite
from config import *
import pygame as pg

class BaseSpriteRotate(BaseSprite):
    current_angle = 0
    angle = 5
    def __init__(self, image=None, x=0, y=0, w=50, h=50, speed=0, angle=5, image_pic=None):
        super().__init__(image=image, image_pic=image_pic, x=x, y=y, w=w, h=h, speed=speed, check_class=BaseSpriteRotate)
        self.angle = angle


    def rotate(self):
        self.image = pg.transform.rotate(self.image_orig, self.current_angle)
        self.current_angle = (self.current_angle + self.angle) % 360
        self.rect_r = self.image.get_rect()
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center