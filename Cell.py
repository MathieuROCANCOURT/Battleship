#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import dataclass
from StateCell import StateCell


@dataclass
class Cell:
    state_cell: StateCell = StateCell.VIDE

    def __str__(self) -> str:
        match self.state_cell:
            case StateCell.VIDE:
                return ' '
            case StateCell.TOUCHE:
                return 'o'
            case StateCell.NON_TOUCHE:
                return 'x'
            case StateCell.COULER:
                return 'S'
