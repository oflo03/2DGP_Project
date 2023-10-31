from pico2d import *
import game_framework
import world
from back_image import BackImage
from hold import Hold


def enter():
    BackImage('grass.png')
    for i in range(0, 10):
        Hold(0, (500 + i * 50, 500 + i * 50))


def exit():
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()


def update():
    world.update()
    pass


def draw():
    clear_canvas()
    world.draw()
    update_canvas()
