import pyhop

"""
HELPER FUNCTIONS
"""


def already_through(state, a, y, x):
    for i in range(state.count[a]):
        x1 = state.xpath[a][i]
        y1 = state.ypath[a][i]
        if x == x1 and y == y1:
                return True
    return False


"""
OPERATORS
"""


def up(state, a):
    if state.maze[state.y[a] - 1][state.x[a]] == 0 and (not already_through(state, a, state.y[a] - 1, state.x[a])):
        state.y[a] -= 1
        state.count[a] += 1
        state.xpath[a].append(state.x[a])
        state.ypath[a].append(state.y[a])
        return state
    else:
        return False


def down(state, a):
    if state.maze[state.y[a] + 1][state.x[a]] == 0 and (not already_through(state, a, state.y[a] + 1, state.x[a])):
        state.y[a] += 1
        state.count[a] += 1
        state.xpath[a].append(state.x[a])
        state.ypath[a].append(state.y[a])
        return state
    else:
        return False


def left(state, a):
    if state.maze[state.y[a]][state.x[a] - 1] == 0 and (not already_through(state, a, state.y[a], state.x[a] - 1)):
        state.x[a] -= 1
        state.count[a] += 1
        state.xpath[a].append(state.x[a])
        state.ypath[a].append(state.y[a])
        return state
    else:
        return False


def right(state, a):
    if state.maze[state.y[a]][state.x[a] + 1] == 0 and (not already_through(state, a, state.y[a], state.x[a] + 1)):
        state.x[a] += 1
        state.count[a] += 1
        state.xpath[a].append(state.x[a])
        state.ypath[a].append(state.y[a])
        return state
    else:
        return False


pyhop.declare_operators(up, down, left, right)