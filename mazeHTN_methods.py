import pyhop

"""
HELPER FUNCTIONS
"""


def is_done(state, a):
    """Checks current state of domain for whether the player has reached the goal"""
    if state.x[a] == state.goal_x[a] and state.y[a] == state.goal_y[a]:
        return True
    else:
        return False


def is_dead_end(state, a):
    """Checks current state of domain for whether the player has reached a dead end"""
    paths = 0
    if state.maze.cell_at(state.x[a], state.y[a]).has_wall('N'):
        paths += 1
    elif state.maze.cell_at(state.x[a], state.y[a]).has_wall('S'):
        paths += 1
    elif state.maze.cell_at(state.x[a], state.y[a]).has_wall('E'):
        paths += 1
    elif state.maze.cell_at(state.x[a], state.y[a]).has_wall('W'):
        paths += 1

    if paths > 1 and state.x[a] != 0 and state.y[a] != 0:
        return False
    else:
        return True


def status(state, a):
    """Checks current state and returns a message if player is either done or in a dead end"""
    if is_done(state, a):
        return 'done'
    elif is_dead_end(state, a):
        return 'dead_end'


"""
METHODS
"""

# Methods for FindGoal


def walk(state, a):
    """If player has not reached goal, walk in a single direction"""
    if status(state, a) == 'done':
        return []
    else:
        return [('WalkTask', a)]


pyhop.declare_methods('FindGoal', walk)


# Methods for WalkTask


def north(state, a):
    """Walk 1 unit north, then recurse for next direction"""
    return [('up', a), ('FindGoal', a)]


def south(state, a):
    """Walk 1 unit south, then recurse for next direction"""
    return [('down', a), ('FindGoal', a)]


def west(state, a):
    """Walk 1 unit west, then recurse for next direction"""
    return [('left', a), ('FindGoal', a)]


def east(state, a):
    """Walk 1 unit east, then recurse for next direction"""
    return [('right', a), ('FindGoal', a)]


pyhop.declare_methods('WalkTask', south, north, west, east)