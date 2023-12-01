from pico2d import *

import cursor
import game_framework
import play_state
import world
from back_image import BackImage
from hold import Hold
from problem import Problem

p = None
hold_num = -1


def enter():
    global p
    BackImage('resources/background.png')
    p = Problem()
    p.init('problems/save.json')


def exit():
    world.clear()


def pause():
    exit()
    pass


def resume():
    enter()
    pass


def handle_events():
    global p, hold_num
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.pop_state()
            elif event.key == SDLK_s:
                p.save('problems/save.json')
            elif event.key == SDLK_1:
                hold_num = 0
            elif event.key == SDLK_2:
                hold_num = 1
            elif event.key == SDLK_3:
                hold_num = 2
            elif event.key == SDLK_4:
                hold_num = 3
            elif event.key == SDLK_5:
                hold_num = 4
            elif event.key == SDLK_d:
                hold_num = -1
            elif event.key == SDLK_r:
                p.delete()
            elif event.key == SDLK_p:
                p.save('problems/save.json')
                game_framework.push_state(play_state)
                play_state.p.delete()
                play_state.p.init('problems/save.json')
                play_state.p_num = -1

        elif event.type == SDL_MOUSEMOTION:
            cursor.x, cursor.y = event.x, game_framework.HEIGHT - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if hold_num == -1:
                for h in p.holds:
                    if abs(event.x - h.pos[0]) < 20 and abs(game_framework.HEIGHT - event.y - h.pos[1]) < 20:
                        p.holds.remove(h)
                        world.world[1].remove(h)
            else:
                p.holds.append(Hold(hold_num, [event.x, game_framework.HEIGHT - event.y]))


def update():
    world.update()
    pass


def draw():
    global p
    clear_canvas()
    world.draw()
    p.draw()
    cursor.image.draw(cursor.x, cursor.y, 64, 64)
    update_canvas()
