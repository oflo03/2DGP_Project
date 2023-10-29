from pico2d import *
import game_framework
import world
from back_image import BackImage


def enter():
    BackImage('grass.png')


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
