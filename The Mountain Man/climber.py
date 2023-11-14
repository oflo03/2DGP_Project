from pico2d import *
import game_framework
import world


class Climber:
    def __init__(self, pos=(game_framework.WIDTH // 2, game_framework.HEIGHT // 2)):
        self.body = load_image('resources/body.png')
        self.limbs = load_image('resources/limbs.png')
        self.pos = [pos[0], pos[1]]
        self.click_points = [(-40, 90), (40, 90)]
        self.locked_points = [None, None]
        self.selected_point = None
        self.dir = [0, 0]
        world.add_object(self, 2)

    def update(self):
        if not self.selected_point:
            self.dir[1] += -0.01
            if self.pos[1] <= 100:
                if self.dir[1] < -0.1:
                    self.dir[1] *= -0.3
                elif self.dir[1] < 0.1:
                    self.dir[1] = 0
            if self.pos[1] < 90:
                self.dir[1] = 1
            for i in [0, 1]:
                self.pos[i] += self.dir[i]

    def draw(self):
        self.limbs.composite_draw(-0.3, '', self.pos[0] - 60, self.pos[1] + 70)
        self.limbs.composite_draw(0.3, '', self.pos[0] + 60, self.pos[1] + 70)
        self.body.draw(self.pos[0], self.pos[1])
        for cp in self.click_points:
            draw_rectangle(self.pos[0] + cp[0] - 20, self.pos[1] + cp[1] - 20, self.pos[0] + cp[0] + 20,
                           self.pos[1] + cp[1] + 20)

    def handle_events(self, e):
        if e.type == SDL_MOUSEBUTTONDOWN:
            for cp in self.click_points:
                if abs(self.pos[0] + cp[0] - e.x) < 20 and abs(
                        self.pos[1] + cp[1] - (game_framework.HEIGHT - e.y)) < 20:
                    self.selected_point = cp
        elif e.type == SDL_MOUSEBUTTONUP:
            self.selected_point = None
            self.dir = [0, 0]
        elif e.type == SDL_MOUSEMOTION:
            if self.selected_point:
                self.pos = [e.x - self.selected_point[0], (game_framework.HEIGHT - e.y) - self.selected_point[1]]
