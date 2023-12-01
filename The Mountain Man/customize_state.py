from pico2d import *

import create_state
import cursor
import game_framework
import play_state

from button import Button

menu = None
buttons = []

flower_image = None
flower_sel = 0
flower_frame = 0


def enter():
    global menu, buttons, flower_image
    menu = load_image('resources/customize.png')
    flower_image = load_image('resources/flower.png')
    buttons.append(Button('NEXT', 630))
    buttons.append(Button('BACK', 230))


def exit():
    buttons.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    global flower_sel
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
                            case 'NEXT':
                                flower_sel = (flower_sel + 1) % 7
                            case 'BACK':
                                game_framework.pop_state()
                        break


def update():
    global flower_frame
    flower_frame = (flower_frame + 1) %5+1


def draw():
    global menu
    global flower_image, flower_sel, flower_frame
    clear_canvas()
    menu.draw(game_framework.WIDTH // 2, game_framework.HEIGHT // 2)
    for bt in buttons:
        bt.draw()
    if flower_sel > 0 and flower_sel < 6:
        flower_image.clip_draw((flower_sel-1)*25,0,25,22,game_framework.WIDTH // 2, game_framework.HEIGHT // 2-100,200,176)
    if flower_sel == 6:
        flower_image.clip_draw((flower_frame-1)*25,0,25,22,game_framework.WIDTH // 2, game_framework.HEIGHT // 2-100,200,176)
    cursor.image.draw(cursor.x, cursor.y, 64, 64)

    update_canvas()
