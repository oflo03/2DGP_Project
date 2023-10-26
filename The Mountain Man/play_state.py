from pico2d import *
import game_framework
import world


class BackImage:
    def __init__(self, filename, x, y):
        self.image = load_image(filename)
        self.x, self.y = x, y

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y, self.image.w * game_framework.WIDTH / 800,
                        self.image.h * game_framework.HEIGHT / 600)


def enter():
    grass = BackImage('grass.png', 400 * game_framework.WIDTH / 800, 30 * game_framework.HEIGHT / 600)
    world.add_object(grass)


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
