import pyhop

"""
HELPER FUNCTIONS
"""


def already_through(state, a, y, x):
    """Checks if a certain tile has already been traversed through"""
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
    """Check tile above player, walk if criteria met"""
    if not state.maze.cell_at(state.x[a], state.y[a]).has_wall('N') and \
            (not already_through(state, a, state.y[a] - 1, state.x[a])):
        state.y[a] -= 1
        state.count[a] += 1
        state.xpath[a].append(state.x[a])
        state.ypath[a].append(state.y[a])
        return state
    else:
        return False


def down(state, a):
    """Check tile below player, walk if criteria met"""
    if not state.maze.cell_at(state.x[a], state.y[a]).has_wall('S') and \
            (not already_through(state, a, state.y[a] + 1, state.x[a])):
        state.y[a] += 1
        state.count[a] += 1
        state.xpath[a].append(state.x[a])
        state.ypath[a].append(state.y[a])
        return state
    else:
        return False


def left(state, a):
    """Check tile left of player, walk if criteria met"""
    if not state.maze.cell_at(state.x[a], state.y[a]).has_wall('W') and \
            (not already_through(state, a, state.y[a], state.x[a] - 1)):
        state.x[a] -= 1
        state.count[a] += 1
        state.xpath[a].append(state.x[a])
        state.ypath[a].append(state.y[a])
        return state
    else:
        return False


def right(state, a):
    """Check tile right of player, walk if criteria met"""
    if not state.maze.cell_at(state.x[a], state.y[a]).has_wall('E') and \
            (not already_through(state, a, state.y[a], state.x[a] + 1)):
        state.x[a] += 1
        state.count[a] += 1
        state.xpath[a].append(state.x[a])
        state.ypath[a].append(state.y[a])
        return state
    else:
        return False


pyhop.declare_operators(up, down, left, right)