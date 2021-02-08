"""These modules deals with game of skyscrapers"""


def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    >>> read_input("check.txt")
    ['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']
    """
    new_data = []
    with open(path) as data:
        data = data.readlines()
        for each in data:
            each = each.rstrip()
            new_data.append(each)
    return new_data


def left_to_right_check(input_line: str, pivot: int) -> bool:
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    check = False
    buildings = input_line[1:-1]
    count = 0
    current_floor = 0
    for floor in buildings:
        try:
            floor = int(floor)
        finally:
            if floor > current_floor:
                current_floor = floor
                count += 1
    if pivot == count:
        check = True
    return check


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', \
    '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', \
    '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', \
    '*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    check = True
    for buildings in board:
        if '?' in buildings:
            check = False
            break

    return check


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', \
    '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', \
    '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', \
    '*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    check = True
    for buildings in board[1:-1]:
        houses = []
        raw_buildings = buildings[1:-1]
        for each in raw_buildings:
            try:
                each = int(each)
            finally:
                houses.append(each)
        if len(houses) != len(set(houses)):
            check = False
            break

    return check


def check_horizontal_visibility(board: list) -> bool:
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', \
    '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', \
    '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', \
    '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    check = False
    if check_uniqueness_in_rows(board) and check_not_finished_board(board):
        for buildings in board[1:-1]:
            hint_left = buildings[0]
            hint_right = buildings[-1]
            reversed_buildings = buildings[::-1]
            if hint_left != '*':
                hint_left = int(hint_left)
                if not left_to_right_check(buildings, hint_left):
                    return check
            if hint_right != '*':
                hint_right = int(hint_right)
                if left_to_right_check(reversed_buildings, hint_right):
                    check = True
                else:
                    return check
            else:
                check = True

    return check


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness
    (buildings of unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', \
    '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', \
    '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', \
    '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    check = False
    new_board = []
    for i in range(len(board)):
        new_num = ''
        for each in board:
            new_num = new_num + each[i]
        new_board.append(new_num)
    if check_horizontal_visibility(new_board):
        check = True
    return check


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    >>> check_skyscrapers("check.txt")
    True
    """
    check = False
    board = read_input(input_path)

    if check_horizontal_visibility(board) and check_columns(board):
        check = True

    return check
