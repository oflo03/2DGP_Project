from pico2d import *
import game_framework

class Player:
    def __init__(self, pos=(game_framework.WIDTH // 2, game_framework.HEIGHT // 2)):
        self.image = load_image('player.png')
        self.pos = pos

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.pos[0], self.pos[1])