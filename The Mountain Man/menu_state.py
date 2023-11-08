from pico2d import *

import cursor
import game_framework
import play_state

from button import Button

menu = None
buttons = []


def enter():
    global menu, buttons
    menu = load_image('resources/menu.png')
    buttons.append(Button('PLAY', 630))
    buttons.append(Button('MAKE', 530))
    buttons.append(Button('CUSTOMIZE', 430))
    buttons.append(Button('OPTION', 330))
    buttons.append(Button('EXIT', 230))


def exit():
    buttons.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    global font_test
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            cursor.x, cursor.y = event.x, game_framework.HEIGHT - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                for bt in buttons:
                    if bt.click():
                        match bt.name:
                            case 'PLAY':
                                game_framework.push_state(play_state)
                                pass
                            case 'MAKE':
                                pass
                            case 'CUSTOMIZE':
                                pass
                            case 'OPTION':
                                pass
                            case 'EXIT':
                                game_framework.quit()
                                pass
                        break


def update():
    pass


def draw():
    global menu
    global font_test
    clear_canvas()
    menu.draw(game_framework.WIDTH // 2, game_framework.HEIGHT // 2)
    for bt in buttons:
        bt.draw()
    cursor.image.draw(cursor.x, cursor.y, 64, 64)

    update_canvas()
