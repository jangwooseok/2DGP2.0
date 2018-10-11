import game_framework
from pico2d import *

import title_state
import main_state

name = "PauseState"
image = None
logo_time = 0.0
draw_time = 0

def enter():
    global image
    image = load_image('pause_300x100.png')
    pass


def exit():
    global image
    del(image)
    pass


def update():
    global logo_time

    #if logo_time > 1.00:
    #    logo_time = 0
        #game_framework.quit()
    #    game_framework.push_state(title_state)
    delay(0.01)
    logo_time += 0.01
    pass


def draw():
    global image
    global draw_time
    clear_canvas()
    main_state.boy.draw()
    main_state.grass.draw()
    if draw_time > 0.10:
        draw_time = 0
    elif draw_time <= 0.05:
        image.draw(400, 300)
    delay(0.05)
    draw_time += 0.01

    update_canvas()

    pass




def handle_events():
    events = get_events()
    for event in events:
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()
    pass


def pause(): pass


def resume(): pass




