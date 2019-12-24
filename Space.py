#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Space:

    def __init__(self, id, coordinates, neighbors):
        self.id = id
        self.coordinates = coordinates
        self.neighbors = neighbors
        self.card_id = None

    def assign(self, card_id):
        self.card_id = card_id

    def unassign(self):
        self.card_id = None

    def current_card_id(self):
        return self.card_id
