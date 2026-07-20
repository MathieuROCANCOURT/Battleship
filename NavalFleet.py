#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Boat import Boat


class NavalFleet:
    def __init__(self, naval_fleet: list[Boat] | None = None):
        if naval_fleet is None:
            naval_fleet = [
                Boat({(2, 2): False, (2, 3): False, (2, 4): False, (2, 5): False, (2, 6): False}),
                Boat({(4, 1): False, (5, 1): False, (6, 1): False, (7, 1): False}),
                Boat({(5, 3): False, (6, 3): False, (7, 3): False}),
                Boat({(5, 8): False, (5, 9): False, (5, 10): False}),
                Boat({(9, 5): False, (9, 6): False})
            ]
        self.naval_fleet = naval_fleet

    def is_end_game(self):
        return any(ship.is_shoot_down() for ship in self.naval_fleet)
