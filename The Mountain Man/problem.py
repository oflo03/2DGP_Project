import world
from hold import Hold
import json
from button import Button


class Problem:
    def __init__(self):
        self.holds = []

    def init(self, filename):
        with open(filename, 'r') as f:
            problem_data_list = json.load(f)
            for data in problem_data_list:
                h = Hold()
                h.__dict__.update(data)
                self.holds.append(h)

    def save(self, filename):
        with open(filename, 'w') as f:
            problem_data_list = [{"num": h.num, "pos": h.pos} for h in self.holds]
            json.dump(problem_data_list,f)

    def delete(self):
        self.holds.clear()
        world.world[1].clear()

    def draw(self):
        if len(self.holds) > 0:
            Button.font.draw(self.holds[len(self.holds)-1].pos[0] - 60, self.holds[-1].pos[1] + 50, "TOP", (0, 0, 0))
