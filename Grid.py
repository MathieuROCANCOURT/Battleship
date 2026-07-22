#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Cell import Cell


class Grid:
    def __init__(self, size: int = 10):
        self.size = size
        self.grid_game = [[Cell() for _ in range(self.size)] for _ in range(self.size)]

    def __str__(self) -> str:
        separate_line = ('+' + '-' * 3) * (self.size + 1) + "+\n"
        output_grid = ' ' * 4 + separate_line[4:] + ' ' * 4 + '|'

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
