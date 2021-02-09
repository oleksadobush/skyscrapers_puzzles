"""These modules work with puzzles game"""


def check_raw_uniqueness(board):
    """
    Check board of unique number in each row.

    Return True if each in a row have unique number, False otherwise.

    >>> check_raw_uniqueness(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ",\
" 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    >>> check_raw_uniqueness(["**** ****", "***1 ****", "**3 3****", "* 4 1****", "     9 5 ",\
" 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    """
    for numbers in board:
        new = []
        for each in numbers:
            if each != '*' and each != ' ':
                new.append(each)
        if len(new) != len(set(new)):
            return False
    return True


def reverse_board(board):
    """
    Reverses the board to vertical
    >>> reverse_board(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 "])
    ['**** ', '***  ', '** 4 ', '*1   ', '  31 ']
    """
    new_board = []
    for i in range(len(board)):
        new_num = ''
        for each in board:
            new_num = new_num + each[i]
        new_board.append(new_num)
    return new_board


def check_column_uniqueness(board):
    """
    Check column-wise compliance of the board for uniqueness

    >>> check_column_uniqueness(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ",\
" 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    """
    new_board = reverse_board(board)
    return check_raw_uniqueness(new_board)


def check_same_color(board):
    """
    Check uniqueness of numbers in blocks
    of same color

    >>> check_same_color(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     935 ",\
" 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    """
    reversed_board = reverse_board(board)
    colors_vertical = []
    for each in reversed_board[:5]:
        color = ""
        for number in each:
            if number != "*" and len(color) < 4:
                color += number
        colors_vertical.append(color)
    colors_horizontal = []
    board = board[::-1]
    for each in board[:5]:
        color = ""
        for number in each[::-1]:
            if number != "*" and len(color) < 5:
                color += number
        colors_horizontal.append(color)
    colors = []
    for i in range(len(colors_horizontal)):
        colors.append(str(colors_horizontal[i]) + str(colors_vertical[i]))
    return check_raw_uniqueness(colors)


def validate_board(board):
    """
    Returns true if board satisfies the rules, False otherwise

    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ",\
" 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    """
    return check_raw_uniqueness(board) and \
           check_column_uniqueness(board) and check_same_color(board)
