from pico2d import load_image, draw_rectangle

import game_framework
import world

hold_image = [None, None, None, None]


class Hold:
    def __init__(self, hold_num, pos=(game_framework.WIDTH // 2, game_framework.HEIGHT // 2), scale=(1, 1)):
        self.num = hold_num
        if hold_image[self.num] == None:
            hold_image[self.num] = load_image('resources/hold ' + str(hold_num) + '.png')
        self.pos = pos
        self.scale = scale
        world.add_object(self, 1)

    def update(self):
        pass

    def draw(self):
        hold_image[self.num].draw(self.pos[0], self.pos[1])
        draw_rectangle(self.pos[0] - 20, self.pos[1] - 20, self.pos[0] + 20, self.pos[1] + 20)
