#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
from Constants import DIRECTIONS


class Board:
    def __init__(self, n):
        self.size = n
        self.spaces_range = range(0, n)
        self.rows = int(math.ceil(math.sqrt(n)))
        self.board = self.board()
        self.positions = self.positions()
        self.spaces = {}
        # self.generate_neighbors()

    def board(self):
        return [
            self.spaces_range[i:i + self.rows] for i in range(0, self.size, self.rows)
        ]

    def positions(self):
        return [
            [x, y] for x in range(0, len(self.board)) for y in range(0, len(self.board[x]))
        ]

    def show(self):
        print('\n'.join(' '.join(map(str, x)) for x in self.board))

    def assign_card(self, space, card):
        self.spaces[space] = card

    # def generate_neighbors(self):
    #     for space in self.spaces_range:
    #         cell = self.positions[space]

    #         potential_nodes = map(
    #             lambda d: [d[0] + cell[0], d[1] + cell[1]], DIRECTIONS
    #         )
    #         print(potential_nodes)

    #         nodes = {}
    #         for i, n in enumerate(potential_nodes):
    #             if n in self.positions:
    #                 nodes[i] = n

    #         print(nodes)

        # self.nodes = nodes

    # def generate_neighbors(self, cell, positions):
    #     potential_nodes = map(
    #         lambda d: [d[0] + cell[0], d[1] + cell[1]], DIRECTIONS
    #     )

    #     nodes = {}
    #     for i, n in enumerate(potential_nodes):
    #         if n in positions:
    #             nodes[i] = n

    #     self.nodes = nodes
