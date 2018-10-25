from pico2d import *
from ball import Ball

import game_world

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, SPACE, SHIFT_UP, SHIFT_DOWN = range(8)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYUP, SDLK_LSHIFT): SHIFT_UP,
    (SDL_KEYUP, SDLK_RSHIFT): SHIFT_UP,
    (SDL_KEYDOWN, SDLK_LSHIFT): SHIFT_DOWN,
    (SDL_KEYDOWN, SDLK_RSHIFT): SHIFT_DOWN
}


# Boy States

class IdleState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.timer = 500

    @staticmethod
    def exit(boy, event):
        # fill here
        if event == SPACE:
            boy.fire_ball()
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        # fill here
        boy.timer -= 1
        if boy.timer == 0:
            boy.add_event(SLEEP_TIMER)

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(boy.frame * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 200, 100, 100, boy.x, boy.y)


class RunState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1

        boy.dir = boy.velocity

    @staticmethod
    def exit(boy, event):
        # fill here
        if event == SPACE:
            boy.fire_ball()


    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        boy.x += boy.velocity
        boy.x = clamp(25, boy.x, 1600 - 25)

    @staticmethod
    def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)


class DashState:

    @staticmethod
    def enter(boy, event):
        print('DASH!!!!')

        boy.dir = boy.velocity
        boy.timer = 40
    @staticmethod
    def exit(boy, event):
        # fill here

        if event == SPACE:
            boy.fire_ball()

        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8

        boy.x += boy.velocity * 3
        boy.x = clamp(25, boy.x, 1600 - 25)

        boy.timer -= 1
        if boy.timer <= 0:
            boy.add_event(SLEEP_TIMER)

    @staticmethod
    def draw(boy):

        if boy.velocity >= 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)



class SleepState:
    # fill here
    @staticmethod
    def enter(boy, event):
        boy.frame = 0

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_composite_draw(boy.frame * 100, 300, 100, 100,
                                          3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)
        else:
            boy.image.clip_composite_draw(boy.frame * 100, 200, 100, 100,
                                          -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)
    pass





next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                SLEEP_TIMER: SleepState, SPACE: IdleState,SHIFT_UP: IdleState, SHIFT_DOWN: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
               SPACE: RunState, SHIFT_UP: RunState, SHIFT_DOWN: DashState},
    SleepState: {RIGHT_UP: RunState, LEFT_UP: RunState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState,
                 SPACE: IdleState, SHIFT_UP: IdleState, SHIFT_DOWN: IdleState},
    DashState: {RIGHT_UP: RunState, LEFT_UP: RunState, LEFT_DOWN: DashState, RIGHT_DOWN: DashState,
                SLEEP_TIMER: RunState, SPACE: DashState, SHIFT_UP: RunState, SHIFT_DOWN: DashState}
}

class Boy:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        self.image = load_image('animation_sheet.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)


    def fire_ball(self):
        # fill here
        ball = Ball(self.x, self.y, self.dir*3)
        game_world.add_object(ball, 1)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

