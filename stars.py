from random import randint
import pygame as pg
from config import *


class Star(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        size = randint(1, 3)
        self.image = pg.Surface((5, 5), pg.SRCALPHA)
        pg.draw.circle(self.image, (255, 255, 255), (2, 2), size)
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, WINDOW_SIZE[0])
        self.rect.y = -5
        self.speed = randint(1, 10)

    def random_y(self):
        self.rect.y = randint(10, WINDOW_SIZE[1])

    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= WINDOW_SIZE[1]:
            self.kill()

    def draw(self, mw):
        mw.blit(self.image, (self.rect.x, self.rect.y))

    def __str__(self):
        return f'x = {self.rect.x}, y = {self.rect.y}'
