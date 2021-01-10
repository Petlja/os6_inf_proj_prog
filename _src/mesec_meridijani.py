import math
import random
import pygame as pg
import pygamebg

(sirina, visina) = (800, 200)
prozor = pygamebg.open_window(sirina, visina, "Месец")

R = 80
boja_tamne_strane = pg.Color(96, 96, 96, 255)
boja_svetle_strane = pg.Color(255, 255, 192, 255)
levi_polukrug_tamno = pg.Surface((R, 2*R))
pg.draw.circle(levi_polukrug_tamno, boja_tamne_strane, (0, R), R)
desni_polukrug_tamno = pg.Surface((R, 2*R))
pg.draw.circle(desni_polukrug_tamno, boja_tamne_strane, (R, R), R)

def polozaj(xc, yc, d):
    pg.draw.circle(prozor, boja_svetle_strane, (xc, yc), R)
    pg.draw.ellipse(prozor, boja_tamne_strane, (xc-d, yc-R, 2*d, 2*R), 2)

prozor.fill(pg.Color("black"))
polozaj(100, 100, 60)
polozaj(300, 100, 40)
polozaj(500, 100, 20)
polozaj(700, 100, 0)

pg.display.update()
pg.image.save(prozor, 'mesec_konture.png')

pygamebg.wait_loop()

