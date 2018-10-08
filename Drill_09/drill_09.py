from pico2d import *
import random

# Game object class here
class Boy:
    def __init__(self):
        #self.x, self.y = 0, 90
        #self.frame = 0
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        #self.frame = (self.frame + 1) % 8
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
    pass

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)
    pass

class Ball:
    def __init__(self):
        #self.x, self.y = 0, 90
        #self.frame = 0
        self.x, self.y = random.randint(100, 700), 600
        self.speed = random.randint(5, 10)

        self.image1 = load_image('ball21x21.png')
        self.image2 = load_image('ball41x41.png')

        self.is_big_ball = random.randint(0, 1)

    def update(self):
        self.y -= self.speed
        if self.y <= 70 and self.is_big_ball == 1:
            self.y = 70
        elif self.y <= 60 and self.is_big_ball == 0:
            self.y = 60

    def draw(self):
        if self.is_big_ball == 0:
            self.image1.draw(self.x, self.y)
        if self.is_big_ball == 1:
            self.image2.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

#boy = Boy()
team = [Boy() for i in range(11)]
balls = [Ball() for j in range(20)]
grass = Grass()

running = True

# game main loop code
for boy in team:
    boy.__init__()
for ball in balls:
    ball.__init__()
grass.__init__()

while running:
    handle_events()

    for boy in team:
        boy.update()
    for ball in balls:
        ball.update()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in balls:
        ball.draw()

    update_canvas()

    delay(0.05)


# finalization code
close_canvas()