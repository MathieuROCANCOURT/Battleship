#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Cell import Cell


class Grid():
    def __init__(self, size: int = 10):
        self.size = size

    def init_grid(self):
        """
        Generate start grid

        :return: grid with size x size
        """
        return [[Cell() for _ in range(self.size)] for _ in range(self.size)]
