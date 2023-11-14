from pico2d import *
import game_framework
import world


class Climber:
    def __init__(self, pos=(game_framework.WIDTH // 2, game_framework.HEIGHT // 2)):
        self.body = load_image('resources/body.png')
        self.limbs = load_image('resources/limbs.png')
        self.pos = [pos[0], pos[1]]
        self.click_points = [[-70, 20], [70, 20], [-30, -170], [30, -170]]
        self.locked_points = []
        self.selected_index = -1
        self.dir = [0, 0]
        self.limbs_radian = [0.0, 0.0, 0.0, 0.0]
        self.limbs_preset = [(-70, 70), (70, 70), (-30, -120), (30, -120)]
        world.add_object(self, 2)

    def update(self):
        if len(self.locked_points):
            pass
        if self.selected_index == -1 and 0 == len(self.locked_points):
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
        for i in range(0, 4):
            dot_product = (self.click_points[i][1] - self.limbs_preset[i][1]) * -1
            magnitude_product = math.sqrt((self.click_points[i][0] - self.limbs_preset[i][0]) ** 2 + (
                    self.click_points[i][1] - self.limbs_preset[i][1]) ** 2)
            if magnitude_product == 0:
                break
            self.limbs_radian[i] = math.acos(dot_product / magnitude_product) * (1 if (self.click_points[i][0] - self.limbs_preset[i][0]) >= 0 else -1)

    def draw(self):
        for i in range(0, 4):
            self.limbs.composite_draw(self.limbs_radian[i], '', self.pos[0] + self.limbs_preset[i][0],
                                      self.pos[1] + self.limbs_preset[i][1])

        self.body.draw(self.pos[0], self.pos[1])
        for cp in self.click_points:
            draw_rectangle(self.pos[0] + cp[0] - 20, self.pos[1] + cp[1] - 20, self.pos[0] + cp[0] + 20,
                           self.pos[1] + cp[1] + 20)

    def handle_events(self, e):
        if e.type == SDL_MOUSEBUTTONDOWN:
            for cp in self.click_points:
                if abs(self.pos[0] + cp[0] - e.x) < 20 and abs(
                        self.pos[1] + cp[1] - (game_framework.HEIGHT - e.y)) < 20:
                    self.selected_index = self.click_points.index(cp)
                    self.click_points[self.selected_index] = [e.x - self.pos[0],
                                                              (game_framework.HEIGHT - e.y) - self.pos[1]]
                    self.locked_points.clear()
        elif e.type == SDL_MOUSEBUTTONUP:
            if self.selected_index >= 0:
                for hold in world.world[1]:
                    if abs(self.pos[0] + self.click_points[self.selected_index][0] - hold.pos[0]) < 20 and abs(
                            self.pos[1] + self.click_points[self.selected_index][1] - hold.pos[1]) < 20:
                        self.locked_points.append(self.click_points[self.selected_index])
                        self.pos = [hold.pos[0] - self.click_points[self.selected_index][0],
                                    hold.pos[1] - self.click_points[self.selected_index][1]]
                self.selected_index = -1
                self.dir = [0, 0]
        elif e.type == SDL_MOUSEMOTION:
            if self.selected_index >= 0:
                self.click_points[self.selected_index] = [e.x - self.pos[0],
                                                          (game_framework.HEIGHT - e.y) - self.pos[1]]
                if math.sqrt((e.x - self.limbs_preset[self.selected_index][0]) ** 2 + (
                        (game_framework.HEIGHT - e.y) - self.limbs_preset[self.selected_index][1]) ** 2) > 60:
                    pass
