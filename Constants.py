#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BIRDS OF PREY
EAGLE = 'EAGLE'
OWL = 'OWL'
VULTURE = 'VULTURE'
HAWK = 'HAWK'

# ALASKA
WOLF = 'WOLF'
BEAR = 'BEAR'
ELK = 'ELK'
MOOSE = 'MOOSE'

# PARTS
TOP = 'TOP'
BOTTOM = 'BOTTOM'

# LOGIC
DIRECTIONS = [
    [-1, 0],  # up
    [0, 1],  # right
    [1, 0],  # down
    [0, -1],  # left
]
EDGE_MAP = {
    0: 2,  # top: bottom
    1: 3,  # right: left
    2: 0,  # bottom: top
    3: 1,  # left: right
}
