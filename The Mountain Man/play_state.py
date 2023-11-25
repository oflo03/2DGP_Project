from pico2d import *

import cursor
import game_framework
import menu_state
import option_state
import world
from back_image import BackImage
from climber import Climber
from problem import Problem

climber = None
p = None
is_clear = False
p_num = 0
bgm = None

def enter():
    global climber, p, is_clear, bgm
    BackImage('resources/background.png')
    p = Problem()
    if p_num != -1:
        p.init('problems/world'+str(p_num)+'.json')
    climber = Climber()
    is_clear = False
    if bgm == None:
        bgm = load_music('resources/bgm2.mp3')
        bgm.set_volume(option_state.volume)
        bgm.repeat_play()


def exit():
    global climber, p, bgm
    world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    global bgm, is_clear
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                bgm.stop()
                bgm = None
                menu_state.bgm.repeat_play()
                game_framework.pop_state()
            if event.key == SDLK_n:
                is_clear = True
        elif event.type == SDL_MOUSEMOTION:
            cursor.x, cursor.y = event.x, game_framework.HEIGHT - event.y
        climber.handle_events(event)


def update():
    global p_num, bgm
    world.update()
    if is_clear:
        if p_num == -1 or p_num == 10:
            bgm.stop()
            bgm = None
            menu_state.bgm.repeat_play()
            game_framework.pop_state()
            return
        exit()
        p_num += 1
        enter()


def draw():
    global p
    clear_canvas()
    world.draw()
    p.draw()
    cursor.image.draw(cursor.x, cursor.y, 64, 64)
    update_canvas()
