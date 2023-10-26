import time

WIDTH, HEIGHT = 1920, 1080
frame_time = 0.0
running = None
stack = None


def change_state(state):
    global stack
    if (len(stack) > 0):
        stack[-1].exit()
        stack.pop()
    stack.append(state)
    state.enter()


def push_state(state):
    global stack
    if (len(stack) > 0):
        stack[-1].pause()
    stack.append(state)
    state.enter()


def pop_state():
    global stack
    if (len(stack) > 0):
        stack[-1].exit()
        stack.pop()

    if (len(stack) > 0):
        stack[-1].resume()


def quit():
    global running
    running = False


def run(start_state):
    global running, stack
    running = True
    stack = [start_state]
    start_state.enter()

    current_time = time.time()
    while (running):
        stack[-1].handle_events()
        stack[-1].update()
        stack[-1].draw()
        global frame_time
        frame_time = time.time() - current_time
        current_time = time.time()

    while (len(stack) > 0):
        stack[-1].exit()
        stack.pop()
