#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import LiteralString
from StateCell import StateCell


@dataclass
class Cell:
    state_init_cell: StateCell

    def __init__(self):
        self.state_init_cell = StateCell.VIDE

    def __str__(self) -> LiteralString:
        match self.state_init_cell:
            case StateCell.VIDE:
                return ' '
            case StateCell.TOUCHE:
                return 'o'
            case StateCell.NON_TOUCHE:
                return 'x'
            case StateCell.COULER:
                return 'S'
