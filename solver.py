#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Constants import *
from Board import Board
from Space import Space
from Card import *
import collections
import itertools
import math
import pprint


def get_neighbor_direction(a, b):
    for i, d in DIRECTIONS:
        if a[0] + d[0] == b[0] and a[1] + d[1] == b[1]:
            return i


def generate_neighbors(cell, positions):
    potential_nodes = map(
        lambda d: [d[0] + cell[0], d[1] + cell[1]], DIRECTIONS
    )

    nodes = {}
    for i, n in enumerate(potential_nodes):
        if n in positions:
            nodes[i] = n

    return nodes


def print_objects(d):
    for v in d.values():
        pprint.pprint(v.__dict__)


def assign_card_to_space(card, space):
    card.assign(space.id)
    space.assign(card.id)


def unassign_card_to_space(card, space):
    card.unassign()
    space.unassign()


def get_current_card_from_space(space, cards):
    card_id = space.current_card_id()
    if card_id != None:
        return cards[card_id]
    else:
        return None


def check_card_fit(board, space, spaces, cards):

    card = get_current_card_from_space(space, cards)

    fit = True
    for direction, coordinates in space.neighbors.iteritems():

        # get neighbor card
        neighbor_space_id = board.positions.index(coordinates)
        neighbor_card = get_current_card_from_space(
            spaces[neighbor_space_id], cards)
        if neighbor_card == None:
            continue

        # check fit
        fit = is_match(
            card.get_picture_on_side(direction),
            neighbor_card.get_picture_on_side(EDGE_MAP[direction])
        )
        if not fit:
            break

    return fit


def print_solution(board, spaces, cards):
    outer_spacing = '{: >8}'
    inner_spacing = '{: >0}{: >5} '

    strings = []
    data = []

    for i, row in enumerate(board.board):
        strings += [
            '{0}\n   {1}\n{0}'.format(
                len(row) * outer_spacing, len(row) * inner_spacing
            )
        ]

        card = None
        top = []
        middle = []
        bottom = []
        for space in row:
            card_id = spaces[space].current_card_id()
            if card_id != None:
                card = cards[card_id]
                top += [card.get_picture_on_side_short(0)]
                middle += [
                    card.get_picture_on_side_short(3),
                    card.get_picture_on_side_short(1)
                ]
                bottom += [card.get_picture_on_side_short(2)]
            else:
                top += ['__']
                middle += ['__', '__']
                bottom += ['__']
        data += [top + middle + bottom]

    for i, string in enumerate(strings):
        print(string.format(*data[i]))


def is_match(a, b):
    """
        is_match([EAGLE, BOTTOM], [EAGLE, TOP]) == True
        is_match([EAGLE, BOTTOM], [EAGLE, BOTTOM]) == False
        is_match([VULTURE, BOTTOM], [EAGLE, TOP]) == False
    """

    return a[0] == b[0] and a[1] != b[1]


def print_iteration(space_id, card_id, rotation):
    print('space_id: {}\ncard_id: {}\nrotation: {}\n'.format(
        space_id, card_id, rotation
    ))


# def print_iteration(space_id, card_id, rotation, trials):
#     print('space_id: {}\ncard_id: {}\nrotation: {}\ntrials: {}\n'.format(
#         space_id, card_id, rotation, trials
#     ))


def recursive_solver(board, cards, spaces, available_card_ids, current_space):
    # print('current_space: \nID: {}\nDICT: {}\n'.format(
    #     current_space.id, current_space.__dict__)
    # )

    while len(available_card_ids) > 0:
        card_in_hand = cards[available_card_ids.pop()]
        # print('card_in_hand: \nID: {}\nDICT: {}\n'.format(
        #     card_in_hand.id, card_in_hand.__dict__)
        # )

        assign_card_to_space(card_in_hand, current_space)

        card_match = False
        rotations = 0
        while rotations < 4:
            card_in_hand.rotate()
            rotations += 1
            # print_iteration(current_space.id, card_in_hand.id,
            #                 rotations)
            card_match = check_card_fit(board, current_space, spaces, cards)
            # print('card_match: {}\n'.format(card_match))
            # print_solution(board, spaces, cards)

            if card_match:
                next_space = None
                for space_id, space in spaces.iteritems():
                    # print(space_id, space, space.current_card_id())
                    if space.current_card_id() is None:
                        next_space = space

                if next_space is None:
                    print('SOLVED')
                    print_solution(board, spaces, cards)

                # print('next_space: \nID: {}\nDICT: {}\n'.format(
                #     next_space.id, next_space.__dict__)
                # )

                # print('cards: {}\n'.format(cards))
                # print_objects(cards)
                next_available_card_ids = [
                    card_id for card_id, card in cards.iteritems() if card.current_space_id() is None
                ]
                # print('next_available_card_ids: {}\n'.format(
                #     next_available_card_ids))

                recursive_solver(board, cards, spaces,
                                 next_available_card_ids, next_space)

        unassign_card_to_space(card_in_hand, current_space)


def main():
    # Create all the cards
    # print
    # print_objects(cards)
    # cards = cards_sample
    # cards = cards_ben
    # cards = cards_amazon
    cards = cards_alaska

    # Create the board
    board = Board(len(cards))
    # board = Board(2)
    # print
    # print(board.__dict__)

    # Create the spaces
    spaces = {}
    for space in board.spaces_range:
        spaces[space] = Space(
            id=space,
            coordinates=board.positions[space],
            neighbors=generate_neighbors(
                board.positions[space], board.positions)
        )
    # print
    # print_objects(spaces)

    available_card_ids = [card_id for card_id in cards.keys()]
    recursive_solver(board, cards, spaces, available_card_ids, spaces[0])

    # solved = False
    # for space_id, space in spaces.iteritems():

    #     card_in_hand = cards[available_cards.pop()]
    #     assign_card_to_space(card_in_hand, space)

    #     card_match = False
    #     rotations = 0
    #     while not card_match and rotations < 4:
    #         card_in_hand.rotate()
    #         rotations += 1
    #         card_match = check_card_fit(board, space, spaces, cards)
    #         print(card_match)
    #         print(card_in_hand.__dict__)
    #         print_solution(board, spaces, cards)

    #     if not card_match:
    #         unassign_card_to_space(card_in_hand, space)

    #     # cards_to_try = [card_id for card_id in cards.keys()]
    #     # list(set(list_2)-set(list_1))
    #     # print(cards_to_try)
    #     # print(id, space.__dict__)

    # print
    # # print_solution(board, spaces, cards)

    # # # for the next space, assign it a card
    # # # rotate until the card works
    # # # if the card doesnt work, pick a new card


if __name__ == '__main__':
    main()
