import random
import pygame as pg
import pygamebg

COLOR_BUTTON = (23, 187, 156)
COLOR_BACKGROUND = (7, 109,  91) 
X, Y, W, H, IMG = 0, 1, 2, 3, 4
OFFSET = 15

(w, h) = (600, 300)
surface = pygamebg.open_window(w, h, 'Решавање једначина')

def new_eq():
    global a_left, b_left, a_right, b_right
    a_left = random.randint(-10, 10)
    b_left = random.randint(-10, 10)
    a_right = random.randint(-10, 10)
    b_right = random.randint(-10, 10)

def plus_x():
    global a_left, b_left, a_right, b_right
    a_left += 1
    a_right += 1

def minus_x():
    global a_left, b_left, a_right, b_right
    a_left -= 1
    a_right -= 1

def plus_1():
    global a_left, b_left, a_right, b_right
    b_left += 1
    b_right += 1

def minus_1():
    global a_left, b_left, a_right, b_right
    b_left -= 1
    b_right -= 1

def change_sign():
    global a_left, b_left, a_right, b_right
    a_left, b_left, a_right, b_right = -a_left, -b_left, -a_right, -b_right

def change_sides():
    global a_left, b_left, a_right, b_right
    a_left, b_left, a_right, b_right = a_right, b_right, a_left, b_left

def divide():
    global a_left, b_left, a_right, b_right
    k = a_left
    a_left, b_left, a_right, b_right = a_left/k, b_left/k, a_right/k, b_right/k


def make_btn(x, y, text):
    font = pg.font.SysFont('Arial', 30)
    text_img = font.render(text, True, pg.Color('white'))
    return (x, y, text_img.get_width()+2*OFFSET, text_img.get_height(), text_img)

# define buttons
btn_new = make_btn(500, 20, 'нова')

btn_plus_x = make_btn(20, 20, '+x')
btn_minus_x = make_btn(btn_plus_x[X] + btn_plus_x[W] + 20, 20, '-x')
btn_plus_1 = make_btn(btn_minus_x[X] + btn_minus_x[W] + 20, 20, '+1')
btn_minus_1 = make_btn(btn_plus_1[X] + btn_plus_1[W] + 20, 20, '-1')

btn_change_sign = make_btn(20, btn_new[Y] + btn_new[H] + 20, '±')
btn_change_sides = make_btn(btn_change_sign[X] + btn_change_sign[W] + 20, btn_change_sign[Y], '<- ->')
btn_divide = make_btn(btn_change_sides[X] + btn_change_sides[W] + 20, btn_change_sign[Y], 'подели')

actions = [new_eq, plus_x, minus_x, plus_1, minus_1, change_sign, change_sides, divide]
buttons = [btn_new, btn_plus_x, btn_minus_x, btn_plus_1, btn_minus_1, btn_change_sign, btn_change_sides, btn_divide]

a_left, b_left, a_right, b_right = 0, 0, 0, 0
new_eq()

def point_is_inside(button, pt):
    return (button[X] <= pt[0] < button[X] + button[W] and
            button[Y] <= pt[1] < button[Y] + button[H])

def str_f(a):
    if round(a) == a:
        return str(int(a))
    return '%0.5f' % a

def str_expression(a, b):
    s = ''
    if a != 0:
        if a != 1:
            s = str_f(a) + ' X'
        else:
            s = 'X'
    if b != 0:
        if b > 0 and a != 0:
            s += ' + '
        s += str_f(b)
    if a == 0 and b == 0:
        s = '0'
    return s

def eq():
    s  = str_expression(a_left, b_left) + ' = ' + str_expression(a_right, b_right)
    solved = (a_left == 1 and b_left == 0 and a_right == 0)
    return s, solved

def draw_all():
    surface.fill(COLOR_BACKGROUND)
    for button in buttons:
        pg.draw.rect(surface, COLOR_BUTTON, (button[X], button[Y], button[W], button[H]))
        surface.blit(button[IMG], (button[X] + OFFSET, button[Y]))
        
    str_eq, solved = eq()
    font = pg.font.SysFont('Arial', 30)
    text_img = font.render(str_eq, True, pg.Color('white'))
    surface.blit(text_img, (w//2 - text_img.get_width()//2, 150))
    if solved:
        text_img = font.render('Браво!', True, pg.Color('white'))
        surface.blit(text_img, (w//2 - text_img.get_width()//2, 200))

def handle_event(event):
    if event.type == pg.MOUSEBUTTONDOWN:
        for button, action in zip(buttons, actions):
            if point_is_inside(button, event.pos):
                action()
                draw_all()
                break
    
def new_frame():
    draw_all()

pygamebg.frame_loop(25, new_frame, handle_event)
