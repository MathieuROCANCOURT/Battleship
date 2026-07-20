#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum


class StateCell(Enum):
    VIDE = 1
    TOUCHE = 2
    NON_TOUCHE = 3
    COULER = 4
