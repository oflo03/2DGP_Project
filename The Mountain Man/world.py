world = [[], [], [], []]


# 0: background
# 1: hold
# 2: player
# 3: UI

def create_world():
    pass


def add_object(o, depth=0):
    if depth < len(world):
        world[depth].append(o)
        return
    raise ValueError('the depth request is out of layer index')


def update():
    for layer in world:
        for o in layer:
            o.update()


def render():
    for layer in world:
        for o in layer:
            o.draw()


def handle_event(e):
    for layer in world:
        for o in layer:
            o.handle_event(e)


# 객체 삭제
def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
    raise ValueError('object is not in world')
