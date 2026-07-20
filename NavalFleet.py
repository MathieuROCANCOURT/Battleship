#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Boat import Boat


class NavalFleet:
    def __init__(self, naval_fleet=list[Boat] | None):
        if naval_fleet is None:
            naval_fleet = [
                Boat({(2, 2): True, (2, 3): True, (2, 4): True, (2, 5): True, (2, 6): True}),
                Boat({(4, 1): True, (5, 1): True, (6, 1): True, (7, 1): True}),
                Boat({(5, 3): True, (6, 3): True, (7, 3): True}),
                Boat({(5, 8): True, (5, 9): True, (5, 10): True}),
                Boat({(9, 5): True, (9, 6): True})
            ]
        self.naval_fleet = naval_fleet
