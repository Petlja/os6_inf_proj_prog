import math
import random
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300)
prozor = pygamebg.open_window(sirina, visina, "Месец")

xc, yc, R, w = sirina // 2, visina // 2, 100, 0
boja_tamne_strane = pg.Color(96, 96, 96, 255)
boja_svetle_strane = pg.Color(255, 255, 192, 255)
levi_polukrug_tamno = pg.Surface((R, 2*R))
pg.draw.circle(levi_polukrug_tamno, boja_tamne_strane, (0, R), R)
desni_polukrug_tamno = pg.Surface((R, 2*R))
pg.draw.circle(desni_polukrug_tamno, boja_tamne_strane, (R, R), R)

def crtaj():
    global w
    
    prozor.fill(pg.Color("black"))
    pg.draw.circle(prozor, boja_svetle_strane, (xc, yc), R)
    if w < R:
        d = R-w
        prozor.blit(levi_polukrug_tamno, (xc, yc-R))
        pg.draw.ellipse(prozor, boja_tamne_strane, (xc-d, yc-R, 2*d, 2*R))
    elif w < 2*R:
        d = w-R
        prozor.blit(levi_polukrug_tamno, (xc, yc-R))
        pg.draw.ellipse(prozor, boja_svetle_strane, (xc-d, yc-R, 2*d, 2*R))
    elif w < 3*R:
        d = 3*R-w
        prozor.blit(desni_polukrug_tamno, (xc-R, yc-R))
        pg.draw.ellipse(prozor, boja_svetle_strane, (xc-d, yc-R, 2*d, 2*R))
    else:
        d = w-3*R
        prozor.blit(desni_polukrug_tamno, (xc-R, yc-R))
        pg.draw.ellipse(prozor, boja_tamne_strane, (xc-d, yc-R, 2*d, 2*R))
    w += 2
    if w > 4*R:
        w -= 4*R

pygamebg.frame_loop(20, crtaj)
