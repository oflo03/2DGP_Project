from pico2d import *
import game_framework
import world


class BackImage:
    def __init__(self, filename, pos=(game_framework.WIDTH // 2, game_framework.HEIGHT // 2), scale=(1, 1)):
        self.image = load_image(filename)
        self.pos = pos
        self.scale = scale
        world.add_object(self)

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.pos[0], self.pos[1])


def enter():
    BackImage('grass.png')


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


def update():
    world.update()
    pass


def draw():
    clear_canvas()
    world.draw()
    update_canvas()
