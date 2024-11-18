import pygame as pg
#from base_sprite_rotate import BaseSpriteRotate

class BaseSprite(pg.sprite.Sprite):
    def __init__(self, image=None, image_pic=None, x=0, y=0, w=0, h=0, speed=0, check_class=str):
        super().__init__()

        if image:
            self.image = pg.transform.scale(pg.image.load(image).convert_alpha(), (w, h))
        elif image_pic:
            self.image = image_pic
        else:
            raise ValueError ('пустая картинка')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #if isinstance(self, check_class):
        self.image_orig = self.image
        self.speed = speed
    def draw(self, mw):
        mw.blit(self.image, (self.rect.x, self.rect.y))