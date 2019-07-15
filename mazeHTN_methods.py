import pyhop

"""
HELPER FUNCTIONS
"""


def is_done(state, a):
    if state.x[a] == 6 and state.y[a] == 1:
        return True
    else:
        return False


def is_dead_end(state, a):
    paths = 0
    if state.maze[state.y[a] + 1][state.x[a]] == 0:
        paths += 1
    elif state.maze[state.y[a] - 1][state.x[a]] == 0:
        paths += 1
    elif state.maze[state.y[a]][state.x[a] - 1] == 0:
        paths += 1
    elif state.maze[state.y[a]][state.x[a] + 1] == 0:
        paths += 1

    if paths > 1 and state.x[a] != 5 and state.y[a] != 7:
        return False
    else:
        return True


def status(state, a):
    if is_done(state, a):
        return 'done'
    elif is_dead_end(state, a):
        return 'dead_end'


"""
METHODS
"""

# Methods for FindGoal


def walk(state, a):
    if status(state, a) == 'done':
        return []
    else:
        return [('WalkTask', a)]


pyhop.declare_methods('FindGoal', walk)


# Methods for WalkTask


def north(state, a):
    return [('up', a), ('FindGoal', a)]


def south(state, a):
    return [('down', a), ('FindGoal', a)]


def west(state, a):
    return [('left', a), ('FindGoal', a)]


def east(state, a):
    return [('right', a), ('FindGoal', a)]


pyhop.declare_methods('WalkTask', south, north, west, east)