import random
from pico2d import *

open_canvas(800, 600)

character = load_image("animation_sheet.png")
kpu_ground = load_image("KPU_GROUND.png")

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

#open_canvas(KPU_WIDTH, KPU_HEIGHT)

direct = 0
frame = 0

def DrawCharacter(x, y):
    global frame
    global direct
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    if direct == 1:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif direct == -1:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    elif direct == 0:
        character.clip_draw(frame * 100, 100 * 3, 100, 100, x, y)
    update_canvas()

    frame = (frame + 1) % 8


def draw_line(p1, p2):

    for i in range(0, 100 + 1, 2):
        t = i / 100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]
#        draw_point((x, y))
        DrawCharacter(x, y)
        delay(0.02)
    pass





size = 20
points = [(random.randint(0, KPU_WIDTH/2), random.randint(0, KPU_HEIGHT/2)) for i in range(size)]#좌표

n = 1

while True:

    draw_line(points[n-1], points[n])
    n = (n + 1) % size

close_canvas()
