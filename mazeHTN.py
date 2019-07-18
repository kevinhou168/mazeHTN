import maze_layout
from __future__ import print_function
from pyhop import *

import mazeHTN_methods
print('')
print_methods()

import mazeHTN_operators
print('')
print_operators()

state1 = State('state1')
state1.x = {'me':0}
state1.y = {'me':0}
state1.xpath = {'me':[0]}  # Record of traversed paths
state1.ypath = {'me':[0]}
state1.count = {'me':1}
state1.goal_x = {'me':state1.maze.nx}
state1.goal_y = {'me':state1.maze.ny}
state1.maze = maze_layout.maze.make_maze()

pyhop(state1, [('FindGoal', 'me')], verbose=3)