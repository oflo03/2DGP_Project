from pico2d import *

import cursor
import game_framework
import world
from back_image import BackImage
from climber import Climber
from problem import Problem

climber = None


def enter():
    global climber
    BackImage('resources/background.png')
    Problem('problems/test.pr')
    climber = Climber()


def exit():
    global climber
    world.clear()
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
                game_framework.pop_state()
        elif event.type == SDL_MOUSEMOTION:
            cursor.x, cursor.y = event.x, game_framework.HEIGHT - event.y
        climber.handle_events(event)


def update():
    world.update()
    pass


def draw():
    clear_canvas()
    world.draw()
    cursor.image.draw(cursor.x, cursor.y, 64, 64)
    update_canvas()
