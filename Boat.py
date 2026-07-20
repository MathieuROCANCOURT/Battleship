#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import dataclass
from Grid import Grid
from StateCell import StateCell


@dataclass
class Boat:
    dict_coordinate_boats: dict[tuple[int, int], bool]

    def get_ship_coord(self) -> list[tuple[int, int]]:
        return list(self.dict_coordinate_boats.keys())

    def is_shoot(self, line, column):
        return (line, column) in self.get_ship_coord()

    def is_shoot_down(self) -> bool:
        return any(list(self.dict_coordinate_boats.values()))

    def change_state(self, line: int, column: int, grid: Grid) -> Grid:
        if self.is_shoot(line, column):
            self.dict_coordinate_boats[(line, column)] = True

            if self.is_shoot_down():
                for row, column in self.get_ship_coord():
                    grid.grid_game[line][column] = StateCell.COULER
            else:
                grid.grid_game[line][column] = StateCell.TOUCHE

        else:
            grid.grid_game[line][column] = StateCell.NON_TOUCHE

        return grid
