# TO HELP CONVERT ALGEBRAIC UCI SQUARE POSITIONS TO GRID NUMBERS


def uci_to_num(square_pos: str) -> tuple:
    
    col_to_num = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7
    }

    col = col_to_num[square_pos[0]]
    row = int(square_pos[1]) - 1

    return (row, col)