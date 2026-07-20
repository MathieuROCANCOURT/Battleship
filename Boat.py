#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import dataclass


@dataclass
class Boat:
    dict_coordinate_boats: dict[tuple[int, int], bool]

    def get_ship_coord(self):
        return list(self.dict_coordinate_boats.keys())
