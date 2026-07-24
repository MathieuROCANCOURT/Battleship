#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Grid import Grid
from InputUser import InputUser
from NavalFleet import NavalFleet

if __name__ == "__main__":
    GRID_SIZE = 10
    grid = Grid()
    naval_fleet = NavalFleet()
    print(grid)

    # While all boats are not shoot down
    while not naval_fleet.is_end_game():
        input_user = InputUser()
        shoot = input_user.input_user()

        if shoot is not None:
            grid.change_state(shoot[0], shoot[1], naval_fleet)
            boat_target = naval_fleet.boat_shoot(shoot[0], shoot[1])

            if boat_target is not None:

                if boat_target.is_shoot(shoot[0], shoot[1]):
                    if boat_target.is_shoot_down():
                        print("Bâteau toucher et couler.")
                    else:
                        print("Bâteau toucher")
            print(grid)
        else:
            print(grid)
            print("Saisie incorrect.")

    print("Vous avez coulé tous les bateaux. La partie est terminée.")
