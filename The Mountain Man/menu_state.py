from pico2d import *

import create_state
import cursor
import customize_state
import game_framework
import option_state
import play_state

from button import Button

menu = None
buttons = []
bgm = None


def enter():
    global menu, buttons, bgm
    menu = load_image('resources/menu.png')
    buttons.append(Button('PLAY', 630))
    buttons.append(Button('MAKE', 530))
    buttons.append(Button('CUSTOMIZE', 430))
    buttons.append(Button('OPTION', 330))
    buttons.append(Button('EXIT', 230))
    if bgm == None:
        bgm = load_music('resources/bgm1.mp3')
        bgm.set_volume(option_state.volume)
        bgm.repeat_play()


def exit():
    buttons.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    global font_test, bgm
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
                                play_state.p_num = 0
                                bgm.stop()
                                game_framework.push_state(play_state)
                            case 'MAKE':
                                game_framework.push_state(create_state)
                            case 'CUSTOMIZE':
                                game_framework.push_state(customize_state)
                            case 'OPTION':
                                game_framework.push_state(option_state)
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
