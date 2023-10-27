from pico2d import *
import game_framework
import play_state

menu = None


def enter():
    global menu
    menu = load_image('menu.png')


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
                game_framework.change_state(play_state)


def update():
    pass


def draw():
    global menu
    clear_canvas()
    menu.draw(game_framework.WIDTH // 2, game_framework.HEIGHT // 2)
    update_canvas()
