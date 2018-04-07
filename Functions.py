from random import randint
from collections import deque


def constrain(val, min_val, max_val):
    '''Custom constrain function'''
    if val < min_val:
        return min_val
    if val > max_val:
        return max_val
    return val


def Spawn():
    '''set random spawn locations, increased chance to
    spawn at the top of the screen than the sides'''
    side = randint(0, 5)
    X = 50*randint(0, 25)
    Y = 50*randint(0, 7)

    if side == 0:
        return 0, Y

    elif side == 1:
        return 1250, Y

    else:
        return X, 0


def bfs(g, start, barricades):

    queue, enqueued = deque([(None, start)]), set([start])
    while queue:
        parent, n = queue.popleft()
        node = [int(i) for i in n.split()]
        if node not in barricades:
            yield parent, n
            new = set(g[n]) - enqueued
            enqueued |= new
            queue.extend([(n, child) for child in new])


def shortest_path(g, start, end, barricades):
    parents = {}
    for parent, child in bfs(g, start, barricades):
        parents[child] = parent
        if child == end:
            revpath = [end]
            while True:
                parent = parents[child]
                revpath.append(parent)
                if parent == start:
                    break
                child = parent
            return list(reversed(revpath))
    return None  # or raise appropriate exception


def bfsBreacher(g, start, barricades):

    queue, enqueued = deque([(None, start)]), set([start])
    while queue:
        parent, n = queue.popleft()
        yield parent, n
        new = set(g[n]) - enqueued
        enqueued |= new
        queue.extend([(n, child) for child in new])


def shortest_pathBreacher(g, start, end, barricades):
    parents = {}
    for parent, child in bfsBreacher(g, start, barricades):
        parents[child] = parent
        if child == end:
            revpath = [end]
            while True:
                parent = parents[child]
                revpath.append(parent)
                if parent == start:
                    break
                child = parent
            return list(reversed(revpath))
    return None  # or raise appropriate exception
