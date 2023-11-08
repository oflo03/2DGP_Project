from pico2d import *

import cursor
import game_framework
import menu_state

title = None


def enter():
    global title
    title = load_image('resources/title.png')
    cursor.image = load_image('resources/cursor.png')


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
            elif event.key == SDLK_SPACE:
                game_framework.change_state(menu_state)
        elif event.type == SDL_MOUSEMOTION:
            cursor.x, cursor.y = event.x, game_framework.HEIGHT - event.y


def update():
    pass


def draw():
    global title
    clear_canvas()
    title.draw(game_framework.WIDTH // 2, game_framework.HEIGHT // 2)
    cursor.image.draw(cursor.x, cursor.y, 64, 64)
    update_canvas()
