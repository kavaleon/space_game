import pygame as pg

class Line():
    def __init__(self, x, y, w, h, color=None):
        self.rect = pg.Rect(x, y, w, h)
        self.color = (0, 0, 0)
        self.is_point = False
        self.rect.x = x
        self.rect.y = y

    def set_text(self, text, font_size=20):
        self.text = pg.font.Font(None, font_size).render(text, True, (255, 255, 255), None)

    def draw(self, mw):
        pg.draw.rect(mw, self.color, self.rect)

    def draw_text(self, mw, shift_x=8,  shift_y=8):
        self.draw(mw)
        mw.blit(self.text, (self.rect.x + shift_x, self.rect.y + shift_y))