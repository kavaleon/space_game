import pygame as pg
from base_sprite import BaseSprite
from config import *

class Ship(BaseSprite):
    shoot_reload = 10
    def __init__(self, image, w, h, speed):
        super().__init__(image=image, x=0, y=0, w=w, h=h, speed=speed)
        self.rect.x = WINDOW_SIZE[0]/2 - self.rect.width/2
        self.rect.y = WINDOW_SIZE[1] - 100
        self.health = 100
        self.r = 0
        self.g = 255

    def draw(self, mw):
        BaseSprite.draw(self, mw)
        width = self.health * self.rect.width / 100
        self.health_rect = pg.rect.Rect(self.rect.x, self.rect.y + self.rect.height, width, 10)
        pg.draw.rect(mw, (self.r, self.g, 0), self.health_rect)
        pg.draw.rect(mw, (255, 255, 255), pg.rect.Rect(self.rect.x, self.rect.y + self.rect.height,
                                                       self.rect.height, 10), width=1)

    def shoot(self, sound, shoots):
        if self.shoot_reload <= 0:
            shoot = Fire(image='m_shoot.png', x=self.rect.x, y=self.rect.y, w=10, h=20, speed=6)
            shoot.add(shoots)
            self.shoot_reload = 10
            sound.play()

    def update(self, sound, shoots):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.x -= self.speed
        elif keys[pg.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pg.K_UP]:
            self.rect.y -= self.speed
        elif keys[pg.K_DOWN]:
            self.rect.y += self.speed
        if keys[pg.K_SPACE]:
            self.shoot(sound, shoots)
        self.shoot_reload -= 1

    def damage(self):
        self.health -= 20
        self.r += 60
        self.g -= 60
        if self.health > 0:
            return False
        else:
            return True

    def use_bonus(self):
        if self.health < 100:
            self.health += 10
            self.r -= 30
            self.g += 30
class Fire(BaseSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()

class Bonus(BaseSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= WINDOW_SIZE[1]:
            self.kill()

