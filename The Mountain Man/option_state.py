from pico2d import *

import create_state
import cursor
import game_framework
import menu_state
import play_state

from button import Button

menu = None
buttons = []
volume = 32


def enter():
    global menu, buttons
    menu = load_image('resources/option.png')
    buttons.append(Button('SOUND UP', 630))
    buttons.append(Button('SOUND DOWN', 530))
    buttons.append(Button('BACK', 230))


def exit():
    buttons.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    global volume
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.pop_state()
        elif event.type == SDL_MOUSEMOTION:
            cursor.x, cursor.y = event.x, game_framework.HEIGHT - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                for bt in buttons:
                    if bt.click():
                        match bt.name:
                            case 'SOUND UP':
                                volume += 4
                                menu_state.bgm.set_volume(volume)
                            case 'SOUND DOWN':
                                volume -= 4
                                menu_state.bgm.set_volume(volume)
                            case 'BACK':
                                game_framework.pop_state()
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
