#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
import itertools
import sys
import pdb
import pprint


class Card:
    def __init__(self, sides):
        """ Sides of the card look like
                0
            3       1
                2
        """
        self.sides = collections.deque(sides)
        self.name == '_'.join(self.sides)
        self.rotations = [0, 1, 2, 3]

    def rotate(self):
        self.rotations.rotate(1)
        self.sides = self.sides.rotate(self.rotations[0])
        self.name == '_'.join(self.sides)


class Board:
    def __init__(self, n, cards):

        self.board = {}
        self.positions = generate_positions(n)
        self.neighbors = generate_neighbors()
        self.sequence = [i + 1 for i in xrange(n)]
        for i in xrange(n):
            board[i + 1] = {
                'position': positions[i],
                'neighbors': neighbors[i],
                'card': None
            }
        self.cards = cards
        self.side_map = {
            (-1, 0): 0, (0, 1): 1, (1, 0): 2, (0, -1): 3
        }

    def generate_positions(self, n):
        return sorted(
            list(itertools.product(xrange(n), xrange(n))),
            key=lambda i: max(i) + abs(i[0] - i[1])
        )

    def generate_neighbors(self):
        neighbors = []
        for pos in self.positions:
            plus_minus = [1, -1]
            possible = [
                (pos[0] + i, pos[1]) for i in plus_minus
            ] + [
                (pos[0], pos[1] + i) for i in plus_minus
            ]
            neighbors.append([x for x in possible if x in self.positions])

        return neighbors

    def is_match(self, sides):
        """ Takes in two sides as a list and determines whether they're a match
        """
        prefix = [x[0] for x in sides]
        suffix = [x[1] for x in sides]
        if (prefix[0] == prefix[1] and suffix.sum(3) and len(sides) == 2):
            return True

        return False

    def add_card_to_board(self, seq, card):
        self.board[seq]['card'] = card

    def remove_card_from_board(self, seq, card):
        self.board[seq]['card'] = None

    def find_side(self, neighbor, pos):
        idx = (neighbor[0] - pos[0], neighbor[1] - pos[1])
        return self.side_map[idx]

    def solver(self):
        # place a card to position 1
        for card in self.cards:
            for seq in self.sequence:
                add_card_to_board(seq, card)
                for neighbor in self.board[seq]['neighbors']:
                    side = find_side(self.board[seq]['position'], neighbor)
                    board_side = self.board[seq]['card'].sides[side]
                    potential_cards = [
                        card for card in self.cards
                        if card != self.board[seq]['card']
                        and 
                    ]

        # find all possible cards for next position

        # place a card to position 2
            # if match
                # log board state
                # place new card
            # else
                # rotate
                # check for match

        # find all possible cards for next position

        # place a card to position 3
            # if match
                # log board state
                # place new card
            # else
                # rotate
                # check for match

        # find all possible cards for next position

        # place a card to position 4
            # if match
                # log board state
                # done
            # else
                # rotate
                # check for match


def main():
    print 'hello'
    sides = ['H1', 'E1', 'V1', 'O2']
    t = collections.deque(sides)
    print t
    t.rotate(0)
    print t
    left, right, up, down = sides
    print left


if __name__ == '__main__'
    main()
