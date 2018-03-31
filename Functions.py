from random import randint


def constrain(val, min_val, max_val):
    if val < min_val:
        return min_val
    if val > max_val:
        return max_val
    return val


def Spawn():
    # Spawn a Grunt
    side = randint(0, 2)
    X = 50*randint(0, 25)
    Y = 50*randint(0, 12)

    if side == 0:
        return 0, Y

    elif side == 2:
        return 1250, Y

    else:
        return X, 0
