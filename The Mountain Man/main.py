from pico2d import *
import game_framework
import title_state


open_canvas(game_framework.WIDTH, game_framework.HEIGHT)
game_framework.run(title_state)
close_canvas()
