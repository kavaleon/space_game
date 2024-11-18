from base_sprite_rotate import BaseSpriteRotate
from base_sprite_anim import BaseSpriteAnim
from config import *
from random import randint

class Nlo(BaseSpriteRotate):
    def __init__(self, image, w=0, h=0):
        x = randint(0, WINDOW_SIZE[0])
        y = 0
        speed = 2
        angle = randint(1,5)
        super().__init__(image=image, x=x, y=y, w=w, h=h, speed=speed, angle=angle)

    def update(self, died_nlos, ship_center):
        self.rotate()
        self.rect.y += self.speed
        if self.rect.y >= WINDOW_SIZE[1]:
            died_nlos.append(self)
            self.kill()

class Nlo2(BaseSpriteAnim, BaseSpriteRotate):
    def __init__(self, image=None, w=0, h=0, sprites=None, sprite_group=None):
        x = randint(0, WINDOW_SIZE[0])
        y = 0
        speed = 2
        BaseSpriteAnim.__init__(self, image=image, x=x, y=y, w=w, h=h, speed=speed, sprites=sprites, sprite_group=sprite_group)
        self.frame_rate = 30
        self.angle = randint(-20, 20)

    def update(self, died_nlos, ship_center):
        self.next_frame()
        self.rotate()
        dx = ship_center[0] - self.rect.x
        dy = ship_center[1] - self.rect.y
        count = self.count(dx, dy)
        if count <= WINDOW_SIZE[0]:
            direct = self.range(dx, dy)
            self.rect.x = self.rect.x + direct[0] * self.speed
            self.rect.y = self.rect.y + direct[1] * self.speed

        if self.rect.y >= WINDOW_SIZE[1]:
            died_nlos.append(self)
            self.kill()

    def count(self, x, y):
        return (x ** 2 + y ** 2) ** .5

    def range(self, x, y):
        rang = self.count(x, y)
        return x / rang, y / rang