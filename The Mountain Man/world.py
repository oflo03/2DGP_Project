world = [[], [], [], []]


# 0: background
# 1: hold
# 2: climber
# 3: UI


def add_object(o, depth=0):
    if depth < len(world):
        world[depth].append(o)
        return
    raise ValueError('the depth request is out of layer index')


def update():
    for layer in world:
        for o in layer:
            o.update()


def draw():
    for layer in world:
        for o in layer:
            o.draw()


# 객체 삭제
def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
    raise ValueError('object is not in world')


def clear():
    for layer in world:
        layer.clear()
