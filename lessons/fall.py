"""Advanced Game Topics Code and Notes [Falling Objects]."""

import pygame as pg
from pygame.locals import *
import random as rd
import sys

pg.init()

display = pg.display.set_mode([800, 500])


class falling(pg.sprite.Sprite):

    def __init__(self) -> None:
        super().__init__()
        self.rect = pg.Rect(rd.randint(0, 500), rd.randint(-1000, 0), 30, 30)

    def fall(self):
        self.rect.move_ip(0, 1)
        if self.rect.top >= 500:
            self.rect.x = rd.randint(0, 500)
            self.rect.y = rd.randint(-1000, 0)


class player(pg.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.rect = pg.Rect(400, 450, 30, 30)


x = falling()
xs = [falling() for i in range(5)]

play = player()
play2 = player()


while True:

    display.fill([255, 255, 255])

    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_LEFT:
                play.rect.move_ip(-10, 0)
            elif i.key == pg.K_RIGHT:
                play.rect.move_ip(10, 0)
            elif i.key == pg.K_a:
                play2.rect.move_ip(-10, 0)
            elif i.key == pg.K_d:
                play2.rect.move_ip(10, 0)

    for i in xs:
        pg.draw.rect(display, [10, 10, 10], i)
        i.fall()
    pg.draw.rect(display, (250, 0, 0), play)
    pg.draw.rect(display, (0, 250, 0), play2)
    
    pg.display.update()
