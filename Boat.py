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

    def is_shoot(self, line: int, column: int) -> bool:
        return (line, column) in self.get_ship_coord()

    def is_shoot_down(self) -> bool:
        return any(list(self.dict_coordinate_boats.values()))

    def change_state(self, line: int, column: int, grid: Grid) -> Grid:
        if self.is_shoot(line, column):
            self.dict_coordinate_boats[(line, column)] = True

            if self.is_shoot_down():
                for row_ship, column_ship in self.get_ship_coord():
                    grid.grid_game[row_ship][column_ship].state_cell = StateCell.COULER
            else:
                grid.grid_game[line][column].state_cell = StateCell.TOUCHE

        else:
            grid.grid_game[line][column].state_cell = StateCell.NON_TOUCHE

        return grid
