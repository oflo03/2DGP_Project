from pico2d import load_image

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
