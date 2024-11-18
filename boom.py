import pygame as pg

class Boom(pg.sprite.Sprite):
    def __init__(self, center, sprites:list, sprite_group):
        super().__init__()
        self.frames = sprites
        self.frame_rate = 1
        self.frame_num = 0
        self.image = self.frames[self.frame_num]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.add(sprite_group)

    def update(self):
        self.image = self.frames[self.frame_num]
        self.frame_num += 1
        if self.frame_num == len(self.frames):
            self.kill()



