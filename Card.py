#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Constants import *
import pprint
import collections


class Card:

    def __init__(self, id, sides):
        """ Sides of the card look like
                0
            3       1
                2
        """
        self.id = id
        self.sides = collections.deque(sides)
        self.rotation = 0
        self.space_id = None

    def rotate(self):
        self.sides.rotate(1)
        self.rotation = (self.rotation - 1) % 4

    def assign(self, space_id):
        self.space_id = space_id

    def unassign(self):
        self.space_id = None

    def current_space_id(self):
        return self.space_id

    def get_picture_on_side(self, side):
        return self.sides[side]

    def get_picture_on_side_short(self, side):
        return '{}{}'.format(self.sides[side][0][0:1], self.sides[side][1][0:1])

    def get_card_view(self):
        return '{0:4}\n {1:4}{2:4} \n{3:4}'.format(
            self.get_picture_on_side_short(0),
            self.get_picture_on_side_short(3),
            self.get_picture_on_side_short(1),
            self.get_picture_on_side_short(2),
        )

        # "{:6d} {:6d} {:6d}".format(i, i*i, i*i*i))


cards_alaska = {
    0: Card(
        id=0,
        sides=[
            [MOOSE, TOP],
            [BEAR, TOP],
            [WOLF, TOP],
            [ELK, TOP],
        ]
    ),
    1: Card(
        id=1,
        sides=[
            [ELK, TOP],
            [WOLF, BOTTOM],
            [MOOSE, TOP],
            [MOOSE, BOTTOM],
        ]),
    2: Card(
        id=2,
        sides=[
            [BEAR, TOP],
            [WOLF, BOTTOM],
            [MOOSE, TOP],
            [WOLF, TOP],
        ]),
    3: Card(
        id=3,
        sides=[
            [WOLF, BOTTOM],
            [ELK, BOTTOM],
            [ELK, TOP],
            [MOOSE, TOP],
        ]),
    4: Card(
        id=4,
        sides=[
            [MOOSE, BOTTOM],
            [BEAR, TOP],
            [ELK, TOP],
            [WOLF, TOP],
        ]),
    5: Card(
        id=5,
        sides=[
            [WOLF, BOTTOM],
            [ELK, TOP],
            [BEAR, BOTTOM],
            [WOLF, TOP],
        ]),

    6: Card(
        id=6,
        sides=[
            [WOLF, BOTTOM],
            [ELK, BOTTOM],
            [WOLF, BOTTOM],
            [MOOSE, TOP],
        ]),

    7: Card(
        id=7,
        sides=[
            [ELK, BOTTOM],
            [ELK, TOP],
            [BEAR, TOP],
            [BEAR, TOP],
        ]),

    8: Card(
        id=8,
        sides=[
            [BEAR, TOP],
            [MOOSE, BOTTOM],
            [ELK, TOP],
            [MOOSE, TOP],
        ]),
}


cards_sample = {
    0: Card(
        id=0,
        sides=[
            [HAWK, BOTTOM],
            [EAGLE, BOTTOM],
            [VULTURE, TOP],
            [EAGLE, TOP],
        ]
    ),
    1: Card(
        id=1,
        sides=[
            [VULTURE, TOP],
            [HAWK, BOTTOM],
            [OWL, BOTTOM],
            [EAGLE, TOP],
        ]),
    # 2: Card(
    #     id=2,
    #     sides=[
    #         [VULTURE, TOP],
    #         [EAGLE, BOTTOM],
    #         [OWL, TOP],
    #         [HAWK, TOP],
    #     ]),
    # 3: Card(
    #     id=3,
    #     sides=[
    #         [VULTURE, BOTTOM],
    #         [HAWK, BOTTOM],
    #         [OWL, TOP],
    #         [VULTURE, TOP],
    #     ]),
    # 4: Card(
    #     id=4,
    #     sides=[
    #         [OWL, TOP],
    #         [EAGLE, BOTTOM],
    #         [VULTURE, BOTTOM],
    #         [HAWK, TOP],
    #     ]),
    # 5: Card(
    #     id=5,
    #     sides=[
    #         [OWL, BOTTOM],
    #         [HAWK, BOTTOM],
    #         [VULTURE, TOP],
    #         [EAGLE, TOP],
    #     ]),

    # 6: Card(
    #     id=6,
    #     sides=[
    #         [OWL, BOTTOM],
    #         [HAWK, TOP],
    #         [EAGLE, TOP],
    #         [OWL, TOP],
    #     ]),

    # 7: Card(
    #     id=7,
    #     sides=[
    #         [VULTURE, TOP],
    #         [EAGLE, TOP],
    #         [OWL, TOP],
    #         [HAWK, BOTTOM],
    #     ]),

    # 8: Card(
    #     id=8,
    #     sides=[
    #         [VULTURE, BOTTOM],
    #         [OWL, BOTTOM],
    #         [HAWK, BOTTOM],
    #         [EAGLE, BOTTOM],
    #     ]),
}

cards_ben = {
    0: Card(
        id=0,
        sides=[
            [HAWK, BOTTOM],
            [EAGLE, BOTTOM],
            [VULTURE, TOP],
            [EAGLE, TOP],
        ]
    ),
    1: Card(
        id=1,
        sides=[
            [VULTURE, TOP],
            [HAWK, BOTTOM],
            [OWL, BOTTOM],
            [EAGLE, TOP],
        ]),
    2: Card(
        id=2,
        sides=[
            [VULTURE, TOP],
            [EAGLE, BOTTOM],
            [OWL, TOP],
            [HAWK, TOP],
        ]),
    3: Card(
        id=3,
        sides=[
            [VULTURE, BOTTOM],
            [HAWK, BOTTOM],
            [OWL, TOP],
            [VULTURE, TOP],
        ]),
    4: Card(
        id=4,
        sides=[
            [OWL, TOP],
            [EAGLE, BOTTOM],
            [VULTURE, BOTTOM],
            [HAWK, TOP],
        ]),
    5: Card(
        id=5,
        sides=[
            [OWL, BOTTOM],
            [HAWK, BOTTOM],
            [VULTURE, TOP],
            [EAGLE, TOP],
        ]),

    6: Card(
        id=6,
        sides=[
            [OWL, BOTTOM],
            [HAWK, TOP],
            [EAGLE, TOP],
            [OWL, TOP],
        ]),

    7: Card(
        id=7,
        sides=[
            [VULTURE, TOP],
            [EAGLE, TOP],
            [OWL, TOP],
            [HAWK, BOTTOM],
        ]),

    8: Card(
        id=8,
        sides=[
            [VULTURE, BOTTOM],
            [OWL, BOTTOM],
            [HAWK, BOTTOM],
            [EAGLE, BOTTOM],
        ]),
}

cards_amazon = {
    0: Card(
        id=0,
        sides=[
            [EAGLE, BOTTOM],
            [OWL, TOP],
            [HAWK, TOP],
            [VULTURE, TOP],
        ]
    ),
    1: Card(
        id=1,
        sides=[
            [HAWK, BOTTOM],
            [VULTURE, TOP],
            [EAGLE, TOP],
            [OWL, BOTTOM],
        ]),
    2: Card(
        id=2,
        sides=[
            [EAGLE, BOTTOM],
            [OWL, TOP],
            [HAWK, TOP],
            [VULTURE, TOP],
        ]),
    3: Card(
        id=3,
        sides=[
            [HAWK, BOTTOM],
            [OWL, BOTTOM],
            [EAGLE, TOP],
            [VULTURE, TOP],
        ]),
    4: Card(
        id=4,
        sides=[
            [EAGLE, BOTTOM],
            [VULTURE, BOTTOM],
            [HAWK, TOP],
            [OWL, TOP],
        ]),
    5: Card(
        id=5,
        sides=[
            [HAWK, BOTTOM],
            [OWL, BOTTOM],
            [EAGLE, TOP],
            [VULTURE, TOP],
        ]),

    6: Card(
        id=6,
        sides=[
            [EAGLE, BOTTOM],
            [VULTURE, TOP],
            [EAGLE, TOP],
            [HAWK, BOTTOM],
        ]),

    7: Card(
        id=7,
        sides=[
            [HAWK, BOTTOM],
            [OWL, TOP],
            [VULTURE, TOP],
            [VULTURE, BOTTOM],
        ]),

    8: Card(
        id=8,
        sides=[
            [EAGLE, BOTTOM],
            [VULTURE, TOP],
            [EAGLE, TOP],
            [HAWK, BOTTOM],
        ]),
}


def main():
    pprint.pprint(cards[0].__dict__)
    # cards[0].rotate()
    print(cards[0].get_picture_on_side(1))
    print(cards[0].get_card_view())


if __name__ == '__main__':
    main()
