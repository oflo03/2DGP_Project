from pico2d import load_font, draw_rectangle

import game_framework
import cursor


class Button:
    font = None

    def __init__(self, name, h):
        if Button.font == None:
            Button.font = load_font('NanumGaRamYeonGgoc.ttf', 70)
        self.name = name
        self.h = h

    def click(self):
        if abs(cursor.x - game_framework.WIDTH // 2) < len(self.name) * 20 and abs(cursor.y - self.h) < 35:
            return True
        return False

    def draw(self):
        Button.font.draw(game_framework.WIDTH // 2 - len(self.name) * 20, self.h, self.name,
                         (0, 0, 0) if self.click() else (100, 100, 100))
        draw_rectangle(game_framework.WIDTH // 2 - len(self.name) * 20, self.h - 35,
                       game_framework.WIDTH // 2 + len(self.name) * 20, self.h + 35)
