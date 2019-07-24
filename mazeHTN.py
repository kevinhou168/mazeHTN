from __future__ import print_function
from pyhop import *
from maze_layout import *

import mazeHTN_methods
print('')
print_methods()

import mazeHTN_operators
print('')
print_operators()

maze = Maze(10, 10, 0, 0)
maze.make_maze()
print(maze)

state1 = State('state1')
state1.x = {'me':0}
state1.y = {'me':0}
state1.xpath = {'me':[0]}  # Record of traversed paths
state1.ypath = {'me':[0]}
state1.count = {'me':1}
state1.maze = maze
state1.goal_x = {'me':state1.maze.nx-1}
state1.goal_y = {'me':state1.maze.ny-1}

results = pyhop(state1, [('FindGoal', 'me')], verbose=2)
maze.write_svg('maze.svg', maze, results)
