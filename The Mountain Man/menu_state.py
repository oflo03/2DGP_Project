from pico2d import *
import game_framework
import play_state

menu = None
font_test = None


def enter():
    global menu, font_test
    menu = load_image('resources/menu.png')
    font_test = load_font('NanumGaRamYeonGgoc.ttf', 50)


def exit():
    pass


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
            elif event.key == SDLK_SPACE:
                game_framework.change_state(play_state)
        elif event.type == SDL_MOUSEBUTTONDOWN:
            print(str(event.x) + ', ' + str(event.y))


def update():
    pass


def draw():
    global menu
    global font_test
    clear_canvas()
    menu.draw(game_framework.WIDTH // 2, game_framework.HEIGHT // 2)
    font_test.draw(100, 100, 'test')
    update_canvas()
