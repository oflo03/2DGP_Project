from pico2d import *

import customize_state
import game_framework
import play_state
import world
from button import Button


class Limb:
    image = [None, None, None, None]

    def __init__(self, num, pos):
        self.num = num
        if Limb.image[self.num] == None:
            match num:
                case 0:
                    Limb.image[self.num] = load_image('resources/arm_l.png')
                case 1:
                    Limb.image[self.num] = load_image('resources/arm_r.png')
                case 2:
                    Limb.image[self.num] = load_image('resources/leg_l.png')
                case 3:
                    Limb.image[self.num] = load_image('resources/leg_r.png')
        self.pos = [pos[0], pos[1] - 60]
        self.point = [pos[0], pos[1] - 240]
        self.angle = 0.0
        self.rad_dir = [0, 0]
        self.is_lock = False

    def draw(self):
        Limb.image[self.num].composite_draw(self.angle, '', self.pos[0] - math.sin(self.angle) * 50,
                                            self.pos[1] + math.cos(self.angle) * 50)


class Climber:
    def __init__(self, pos=(game_framework.WIDTH // 2, game_framework.HEIGHT // 2)):
        self.image = load_image('resources/body.png')
        self.hp = 100
        self.pos = [pos[0], pos[1]]
        self.selected_index = -1
        self.dir = [0, 0]
        self.limbs_preset = [(-80, 80), (80, 80), (-30, -160), (30, -160)]
        self.limbs = [Limb(i, (self.pos[0] + self.limbs_preset[i][0], self.pos[1] + self.limbs_preset[i][1]))
                      for i in range(0, 4)]
        world.add_object(self, 2)

    def update(self):
        is_find = False
        finds = 0
        if self.hp < 0:
            for i in range(0, 4):
                self.limbs[i].is_lock = False
        for i in range(0, 4):
            if self.limbs[i].is_lock:
                is_find = True
                finds += 1
        if not is_find:
            self.dir[1] += -0.01
            if self.pos[1] > 1000 and self.dir[1] > 0:
                self.dir[1] = 0
            if self.pos[1] <= 300:
                if self.dir[1] < -0.1:
                    self.dir[1] *= -0.3
                elif self.dir[1] < 0.1:
                    self.dir[1] = 0
            if self.pos[1] < 280:
                self.dir[1] += 1
            self.move(self.dir)
            if self.hp < 100:
                self.hp += 0.1
        else:
            self.hp -= 0.002 * (10 - finds * finds/2)
        for i in range(0, 4):
            dis = math.sqrt((self.limbs[i].point[0] - self.limbs[i].pos[0]) ** 2
                            + (self.limbs[i].point[1] - self.limbs[i].pos[1]) ** 2)

            if not self.limbs[i].is_lock and self.selected_index != i:
                self.limbs[i].point[1] -= 2
                for j in [0, 1]:
                    self.limbs[i].point[j] = self.limbs[i].pos[j] + (
                            self.limbs[i].point[j] - self.limbs[i].pos[j]) / dis * 180
            if dis > 220:
                self.limbs[i].is_lock = False
            dot_product = (self.limbs[i].point[1] - self.limbs[i].pos[1]) * -1
            magnitude_product = math.sqrt((self.limbs[i].point[0] - self.limbs[i].pos[0]) ** 2 + (
                    self.limbs[i].point[1] - self.limbs[i].pos[1]) ** 2)
            if magnitude_product == 0:
                break
            self.limbs[i].angle = math.acos(dot_product / magnitude_product) * (
                1 if (self.limbs[i].point[0] - self.limbs[i].pos[0]) >= 0 else -1)
        customize_state.update()

    def draw(self):
        for i in range(0, 4):
            self.limbs[i].draw()

        self.image.draw(self.pos[0], self.pos[1])
        for limb in self.limbs:
            draw_rectangle(limb.point[0] - 20, limb.point[1] - 20, limb.point[0] + 20, limb.point[1] + 20)
        if customize_state.flower_image != None:
            if customize_state.flower_sel > 0 and customize_state.flower_sel < 6:
                customize_state.flower_image.clip_draw((customize_state.flower_sel - 1) * 25, 0, 25, 22, self.pos[0], self.pos[1]+180,50,44)
            if customize_state.flower_sel == 6:
                customize_state.flower_image.clip_draw((customize_state.flower_frame - 1) * 25, 0, 25, 22, self.pos[0], self.pos[1]+180,50,44)
        if self.pos[1] < 800:
            Button.font.draw(self.pos[0] - 60, self.pos[1] + 250, str(int(self.hp)), (0, 0, 0))
        else:
            Button.font.draw(self.pos[0] - 60, self.pos[1] - 500, str(int(self.hp)), (0, 0, 0))

    def handle_events(self, e):
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_a:
                self.dir[0] += -1
            elif e.key == SDLK_d:
                self.dir[0] += 1
        if e.type == SDL_KEYUP:
            if e.key == SDLK_a:
                self.dir[0] -= -1
            elif e.key == SDLK_d:
                self.dir[0] -= 1
        elif e.type == SDL_MOUSEBUTTONDOWN:
            for i in range(0, 4):
                if abs(self.limbs[i].point[0] - e.x) < 20 and abs(
                        self.limbs[i].point[1] - (game_framework.HEIGHT - e.y)) < 20:
                    self.selected_index = i
                    self.limbs[self.selected_index].point = [e.x, (game_framework.HEIGHT - e.y)]
                    self.limbs[i].is_lock = False
        elif e.type == SDL_MOUSEBUTTONUP:
            if self.selected_index >= 0:
                dis = math.sqrt((self.limbs[self.selected_index].point[0] - self.limbs[self.selected_index].pos[0]) ** 2
                                + (self.limbs[self.selected_index].point[1] - self.limbs[self.selected_index].pos[
                    1]) ** 2)
                is_find = False
                for hold in world.world[1]:
                    if abs(self.limbs[self.selected_index].point[0] - hold.pos[0]) < 20 and abs(
                            self.limbs[self.selected_index].point[1] - hold.pos[1]) < 20 and dis < 200:
                        self.limbs[self.selected_index].is_lock = True

                        self.move([hold.pos[0] - self.limbs[self.selected_index].point[0],
                                   hold.pos[1] - self.limbs[self.selected_index].point[1]])
                        is_find = True
                        if play_state.p.holds.index(hold) == len(play_state.p.holds) - 1:
                            play_state.is_clear = True
                if not is_find:
                    for i in [0, 1]:
                        self.limbs[self.selected_index].point[i] = self.limbs[self.selected_index].pos[i] + (
                                    self.limbs[self.selected_index].point[i] - self.limbs[self.selected_index].pos[
                                i]) / dis * 180
                self.selected_index = -1
                self.dir = [0, 0]
        elif e.type == SDL_MOUSEMOTION:
            if self.selected_index >= 0:
                self.limbs[self.selected_index].point = [e.x, (game_framework.HEIGHT - e.y)]
                dis = math.sqrt((self.limbs[self.selected_index].point[0] - self.limbs[self.selected_index].pos[0]) ** 2
                                + (self.limbs[self.selected_index].point[1] - self.limbs[self.selected_index].pos[
                    1]) ** 2)
                is_find = False
                for i in range(0, 4):
                    if self.limbs[i].is_lock:
                        is_find = True
                if dis >= 180 and is_find:
                    self.move([(self.limbs[self.selected_index].point[0] - self.limbs[self.selected_index].pos[0]) - (
                                self.limbs[self.selected_index].point[0] - self.limbs[self.selected_index].pos[
                            0]) / dis * 180,
                               (self.limbs[self.selected_index].point[1] - self.limbs[self.selected_index].pos[1]) - (
                                           self.limbs[self.selected_index].point[1] -
                                           self.limbs[self.selected_index].pos[1]) / dis * 180])

    def move(self, dir):
        for i in [0, 1]:
            self.pos[i] += dir[i]
        for i in range(0, 4):
            for j in [0, 1]:
                self.limbs[i].pos[j] += dir[j]
                if not self.limbs[i].is_lock:
                    self.limbs[i].point[j] += dir[j]
