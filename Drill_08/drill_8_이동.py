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

def draw_curve_4_points(p1, p2, p3, p4):

    # draw p1-p2
    for i in range(0, 50, 2):
        t = i / 100
        x = (2*t**2-3*t+1)*p1[0]+(-4*t**2+4*t)*p2[0]+(2*t**2-t)*p3[0]
        y = (2*t**2-3*t+1)*p1[1]+(-4*t**2+4*t)*p2[1]+(2*t**2-t)*p3[1]
        DrawCharacter(x, y)
        delay(0.02)

    # draw p2-p3
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2
        DrawCharacter(x, y)
        delay(0.02)

    # draw p3-p4
    for i in range(50, 100, 2):
        t = i / 100
        x = (2*t**2-3*t+1)*p2[0]+(-4*t**2+4*t)*p3[0]+(2*t**2-t)*p4[0]
        y = (2*t**2-3*t+1)*p2[1]+(-4*t**2+4*t)*p3[1]+(2*t**2-t)*p4[1]
        DrawCharacter(x, y)
        delay(0.02)


    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p3[0] + (3*t**3 - 5*t**2 + 2)*p4[0] + (-3*t**3 + 4*t**2 + t)*p1[0] + (t**3 - t**2)*p2[0])/2
        y = ((-t**3 + 2*t**2 - t)*p3[1] + (3*t**3 - 5*t**2 + 2)*p4[1] + (-3*t**3 + 4*t**2 + t)*p1[1] + (t**3 - t**2)*p2[1])/2


        DrawCharacter(x, y)
        delay(0.02)




size = 20
points = [(random.randint(0, KPU_WIDTH/2), random.randint(0, KPU_HEIGHT/2)) for i in range(size)]#좌표
#points = [(-400,-400), (-300,400), (-200,-400), (-150,400), (-100,-400), (0,400), (10,-400), (-100,400), (-200,400), (-300,400)]#좌표

n = 1

while True:
    draw_curve_4_points(points[n], points[n+1],points[n+2], points[n+3])


    n = (n + 1) % size

close_canvas()
