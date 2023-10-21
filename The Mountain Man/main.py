from pico2d import *

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            #game_world.handle_event(event)
            pass

def update_world():
    #game_world.update()
    pass


def render_world():
    clear_canvas()
    #game_world.render()
    update_canvas()

open_canvas()
#create_world()
running = True
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)

close_canvas()