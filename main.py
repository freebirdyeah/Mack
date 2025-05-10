from board import Board, STARTING_BOARD_STATE


if __name__ == '__main__':
    board = Board(STARTING_BOARD_STATE)
    board.move("e2e4")
    print(board)