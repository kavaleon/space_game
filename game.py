import pygame as pg
from config import *
from stars import *
from ship import *
from nlo import *
from boom import *
from meteor import *
from line import *


class Game():
    def __init__(self):
        pg.init()

    def set_text(self, mw, text='', x=10, y=10, size=40, color=(255,255,255)):
        text = pg.font.Font(None, size).render(text, True, color, None)
        mw.blit(text, (x, y))

    def play_game(self):
        def load_images(folder_name, file_name, size: tuple = (50, 50), color_key: tuple = None):
            images = []
            load = True
            n = 1
            while load:
                try:
                    if color_key:
                        #image = pg.image.load(f'{folder_name}\\{file_name}{n}.png').convert()
                        image = pg.image.load(f'{folder_name}\\{file_name}{n}.png')
                        image = pg.transform.scale(image, size)
                        image.set_colorkey(color_key)
                    else:
                        image = pg.transform.scale(pg.image.load(f'{folder_name}\\{file_name}{n}.png'), size)
                    images.append(image)
                except FileNotFoundError:
                    load = False
                n += 1
            return images

        boom_sprites = load_images('boom4', 'boom', (50, 50), color_key=(0, 0, 0))
        meteor_sprites = [
            load_images('meteor1', 'meteor', (20, 20)),
            load_images('meteor1', 'meteor', (30, 30)),
            load_images('meteor1', 'meteor', (40, 40)),
            load_images('meteor1', 'meteor', (50, 50))]

        nlo_sprites = load_images('nlo1','nlo', (50, 50))


        # pg.mixer.init()
        sound_fon = pg.mixer.Sound('sounds\\fon1.mp3')
        sound_boom = pg.mixer.Sound('sounds\\boom1.mp3')
        sound_fire = pg.mixer.Sound('sounds\\fire1.mp3')
        sound_fon.set_volume(0.01)
        sound_fire.set_volume(0.01)
        sound_boom.set_volume(0.01)
        sound_fon.play(-1)

        mw = pg.display.set_mode(WINDOW_SIZE, pg.FULLSCREEN)
        pg.display.set_caption('space')
        clock = pg.time.Clock()


        background = pg.transform.scale(pg.image.load('fon1.jpg'), WINDOW_SIZE)
        ship = Ship('ship.png', w=50, h=50, speed=4)

        ticks = 0
        score = 0
        game = True
        finish = False
        chance = list(range(1, 101))
        died_nlos = []
        meteors = pg.sprite.Group()
        stars = pg.sprite.Group()
        nlos = pg.sprite.Group()
        shoots = pg.sprite.Group()
        booms = pg.sprite.Group()
        bonuses = pg.sprite.Group()

        game_over = pg.transform.scale(pg.image.load('game_over.jpg'), WINDOW_SIZE)

        #up_line = Line(0, 0, WINDOW_SIZE[0], 30, (8, 29, 165))
        #score_line = Line(5, 5, 20, 20, (8, 29, 165))


        for _ in range(10):
            star = Star()
            star.random_y()
            stars.add(star)

        while game:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game = False

            if not finish:
                if ticks % 5 == 0:
                    star = Star()
                    stars.add(star)

                if ticks % 50 == 0:
                    nlos.add(Nlo('nlo.png', w=40, h=40))
                    nlos.add(Nlo2(sprites=nlo_sprites, sprite_group=nlos))

                if ticks % 40 == 0:
                    Meteor(meteor_sprites[randint(0, 3)], meteors)


                collide1 = pg.sprite.groupcollide(nlos, shoots, True, True)

                if pg.sprite.spritecollide(ship, meteors, False):
                    finish = True

                for nlo, shoot in collide1.items():
                    Boom(nlo.rect.center, boom_sprites, booms)
                    score += 1
                    sound_boom.play()
                    if randint(1, 100) in chance[:6]:
                        bonus = Bonus(image='bonus.png', x=nlo.rect.x, y=nlo.rect.y, h=40, w=40, speed=3)
                        bonus.add(bonuses)

                if pg.sprite.spritecollide(ship, bonuses, True):
                    ship.use_bonus()

                if pg.sprite.spritecollide(ship, nlos, True):
                    finish = ship.damage()
                mw.blit(background, (0, 0))

                self.set_text(mw, text=f"Score:{score}")


                meteors.update()
                stars.update()
                nlos.update(died_nlos=died_nlos, ship_center=ship.rect.center)
                shoots.update()
                booms.update()
                #score_line.set_text(f'Score: {score}', 24)
                bonuses.update()

                bonuses.draw(mw)
                #up_line.draw(mw)
                #score_line.draw_text(mw)
                meteors.draw(mw)
                stars.draw(mw)
                nlos.draw(mw)
                shoots.draw(mw)
                booms.draw(mw)

                if len(died_nlos) >= 3:
                    pass
                    #finish = True

                ship.update(sound_fire, shoots)
                ship.draw(mw)
            else:
                mw.blit(game_over, (0, 0))
            ticks += 1
            pg.display.update()
            clock.tick(FPS)
