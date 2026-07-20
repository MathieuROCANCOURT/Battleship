#!/usr/bin/env python
# -*- coding: utf-8 -*-

def init_coordinate_boats():
    """
    Init all coordinates to each boats

    :return: dictionary with coordinates each boats
    """
    return {
        "torpedo boat": {"E9", "F9"},
        "submarine": {"H5", "I5", "J5"},
        "destroyer": {"C5", "C6", "C7"},
        "cruiser": {"A4", "A5", "A6", "A7"},
        "aircraft carrier": {"B2", "C2", "D2", "E2", "F2"}
    }


def convert_letter_column_to_index(letter):
    """
    Convert letter to index to affect the now data in grid in battleship

    :param letter: A column letter on Battleship
    :return: A number corresponding to the index
    """
    return int(ord(letter) - ord('A'))


def input_user():
    """
    Input user to write the coordinate shot

    :return: Coordinates shot, None if input incorrect.
    """
    coordinate_user = input("Saisir les coordonnées d'une case:")
    if 2 <= len(coordinate_user) <= 3 and 'A' <= coordinate_user[0] <= 'J' and coordinate_user[
        1:].isdigit() and 0 <= int(coordinate_user[1:]) <= 10:
        return coordinate_user[0], int(coordinate_user[1:])
    return None, None


def show_grid(grid_battleship):
    """
    Show grid in console with lines and columns

    :param grid_battleship: grid battleship of user
    """
    seperate_line = ('+' + '-' * 3) * 11 + "+\n"
    output_grid = ' ' * 4 + seperate_line[4:] + ' ' * 4 + '|'

    for index_col in range(10):
        output_grid += ' ' + chr(index_col + ord('A')) + ' ' + '|'
    output_grid += '\n'

    for index_row_grid in range(1, 11):
        output_grid += seperate_line + '|' + ' ' * (2 - len(str(index_row_grid))) + str(index_row_grid) + ' |'

        for index_column_grid in range(10):
            output_grid += ' ' + grid_battleship[index_row_grid - 1][index_column_grid] + ' |'
        output_grid += '\n'

    output_grid += seperate_line
    print(output_grid)


if __name__ == "__main__":
    grid = init_grid()
    dict_coordinate_boats = init_coordinate_boats()
    dict_coordinate_boats_copy = init_coordinate_boats()
    show_grid(grid)

    # While all boats are not shoot down
    while dict_coordinate_boats:
        letter_column, number_line = input_user()
        boat_shoot, boat_shoot_down = False, False

        if number_line is not None:
            index_column = convert_letter_column_to_index(letter_column)
            # If this case wasn't target
            if grid[number_line - 1][index_column] == ' ':

                for key, values in dict_coordinate_boats.items():
                    for coordinates in values:
                        if letter_column + str(number_line) == coordinates:
                            boat_shoot = True
                            grid[number_line - 1][index_column] = 'o'  # Boat was hit
                            dict_coordinate_boats[key].remove(coordinates)

                            # If all of a ship's squares are hit
                            if not dict_coordinate_boats[key]:
                                boat_shoot_down = True
                                # Indicate on the grid that the boat was sunk
                                for value in dict_coordinate_boats_copy[key]:
                                    grid[int(value[1:]) - 1][convert_letter_column_to_index(value[0])] = 'S'
                                dict_coordinate_boats.pop(key)
                            break
                    if boat_shoot:
                        break
                if not boat_shoot:
                    grid[number_line - 1][index_column] = 'x'  # Boat wasn't hit
            else:
                print("Vous avez déjà tiré à ces coordonnées.")
        else:
            print("Saisie incorrect.")

        show_grid(grid)
        if boat_shoot_down:
            print("Bâteau toucher et couler.")
        elif boat_shoot:
            print("Bâteau toucher")

    print("Vous avez coulé tous les bateaux. La partie est terminée.")
