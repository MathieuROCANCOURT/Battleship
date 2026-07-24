#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Cell import Cell
from NavalFleet import NavalFleet
from StateCell import StateCell


class Grid:
    def __init__(self, size: int = 10):
        self.size: int = size
        self.grid_game: list[list[Cell]] = [[Cell() for _ in range(self.size)] for _ in range(self.size)]

    def __str__(self) -> str:
        separate_line: str = ('+' + '-' * 3) * (self.size + 1) + "+\n"
        output_grid: str = ' ' * 4 + separate_line[4:] + ' ' * 4 + '|'

        for index_col in range(self.size):
            output_grid += ' ' + chr(index_col + ord('A')) + ' ' + '|'
        output_grid += '\n'

        for index_row_grid in range(1, self.size + 1):
            output_grid += separate_line + '|' + ' ' * (2 - len(str(index_row_grid))) + str(index_row_grid) + ' |'

            for index_column_grid in range(self.size):
                output_grid += ' ' + self.grid_game[index_row_grid - 1][index_column_grid].__str__() + ' |'
            output_grid += '\n'

        output_grid += separate_line
        return output_grid

    def change_state(self, line: int, column: int, naval_fleet: NavalFleet):
        boat_target = naval_fleet.boat_shoot(line, column)
        if boat_target is not None:
            naval_fleet.boat_shoot(line, column).dict_coordinate_boats[(line + 1, column + 1)] = True

            if boat_target.is_shoot_down():
                for row_ship, column_ship in boat_target.get_ship_coord():
                    self.grid_game[row_ship - 1][column_ship - 1].state_cell = StateCell.COULER
            else:
                self.grid_game[line][column].state_cell = StateCell.TOUCHE

        else:
            self.grid_game[line][column].state_cell = StateCell.NON_TOUCHE

        return naval_fleet
