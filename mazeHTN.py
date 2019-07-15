from __future__ import print_function
from pyhop import *

import mazeHTN_methods
print('')
print_methods()

import mazeHTN_operators
print('')
print_operators()

state1 = State('state1')
state1.x = {'me':5}
state1.y = {'me':7}
state1.xpath = {'me':[5]}
state1.ypath = {'me':[7]}
state1.count = {'me':1}

state1.maze =  [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
                [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
                [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
                [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


pyhop(state1, [('FindGoal', 'me')], verbose=3)