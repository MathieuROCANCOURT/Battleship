#!/usr/bin/env python
# -*- coding: utf-8 -*-

class InputUser:
    def __init__(self):
        self.coordinate = None

    def input_user(self, size_board: int = 10) -> tuple[str, int] | None:
        """
            Input user to write the coordinate shot

            :return: Coordinates shot, None if input incorrect.
        """
        self.coordinate = input("Saisir les coordonnées d'une case:")

        if self.is_correct_input(size_board):
            return self.coordinate[0], int(self.coordinate[1:])

        return None

    def is_correct_input(self, size_board: int):
        return (2 <= len(self.coordinate) <= 3
                and 'A' <= self.coordinate[0] <= chr(ord('A') + size_board)
                and self.coordinate[1:].isdigit()
                and 0 <= int(self.coordinate[1:]) <= size_board)
