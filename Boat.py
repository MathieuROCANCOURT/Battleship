#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import dataclass


@dataclass
class Boat:
    dict_coordinate_boats: dict[tuple[int, int], bool]

    def get_ship_coord(self) -> list[tuple[int, int]]:
        return list(self.dict_coordinate_boats.keys())

    def is_shoot(self, line: int, column: int) -> bool:
        return (line, column) in self.get_ship_coord()

    def is_shoot_down(self) -> bool:
        return all(list(self.dict_coordinate_boats.values()))
