from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Optional
from coordinates import uci_to_num


class PieceType(Enum):
    PAWN = "pawn"
    KNIGHT = "knight"
    BISHOP = "bishop"
    ROOK = "rook"
    QUEEN = "queen"
    KING = "king"


class PieceColour(Enum):
    BLACK = "BLACK"
    WHITE = "WHITE"


class PieceSymbol(Enum):
    PAWN_BLACK = '\u2659'
    PAWN_WHITE = '\u265F'
    ROOK_BLACK = '\u2656'
    ROOK_WHITE = '\u265C'
    KNIGHT_BLACK = '\u2658'
    KNIGHT_WHITE = '\u265E'
    BISHOP_BLACK = '\u2657'
    BISHOP_WHITE = '\u265D'
    QUEEN_BLACK = '\u2655'
    QUEEN_WHITE = '\u265B'
    KING_BLACK = '\u2654'
    KING_WHITE = '\u265A'

    
class Piece(ABC):
    def __init__(self, piece: PieceType, colour: PieceColour):
        self.piece = piece
        self.colour = colour

    @abstractmethod
    def move():
        pass


class Pawn(Piece):
    def __init__(self, colour: PieceColour):
        super().__init__(PieceType.PAWN, colour)

    def move():
        pass


class Knight(Piece):
    def __init__(self, colour: PieceColour):
        super().__init__(PieceType.KNIGHT, colour)

    def move():
        pass


class Bishop(Piece):
    def __init__(self, colour: PieceColour):
        super().__init__(PieceType.BISHOP, colour)

    def move():
        pass


class Rook(Piece):
    def __init__(self, colour: PieceColour):
        super().__init__(PieceType.ROOK, colour)

    def move():
        pass


class Queen(Piece):
    def __init__(self, colour: PieceColour):
        super().__init__(PieceType.QUEEN, colour)

    def move():
        pass


class King(Piece):
    def __init__(self, colour: PieceColour):
        super().__init__(PieceType.KING, colour)

    def move():
        pass


# let board be the single source from where we determine the position
# for simplicity, no need to make unecessary position updates everytime to the piece position attribute
# using the FirstChess approach (https://www.chessprogramming.org/8x8_Board#FirstChess)
# each explicit instantiation of a class creates a new instance in memory


symbol_map = {
    (PieceType.PAWN, PieceColour.WHITE): PieceSymbol.PAWN_WHITE.value,
    (PieceType.PAWN, PieceColour.BLACK): PieceSymbol.PAWN_BLACK.value,
    (PieceType.ROOK, PieceColour.WHITE): PieceSymbol.ROOK_WHITE.value,
    (PieceType.ROOK, PieceColour.BLACK): PieceSymbol.ROOK_BLACK.value,
    (PieceType.KNIGHT, PieceColour.WHITE): PieceSymbol.KNIGHT_WHITE.value,
    (PieceType.KNIGHT, PieceColour.BLACK): PieceSymbol.KNIGHT_BLACK.value,
    (PieceType.BISHOP, PieceColour.WHITE): PieceSymbol.BISHOP_WHITE.value,
    (PieceType.BISHOP, PieceColour.BLACK): PieceSymbol.BISHOP_BLACK.value,
    (PieceType.QUEEN, PieceColour.WHITE): PieceSymbol.QUEEN_WHITE.value,
    (PieceType.QUEEN, PieceColour.BLACK): PieceSymbol.QUEEN_BLACK.value,
    (PieceType.KING, PieceColour.WHITE): PieceSymbol.KING_WHITE.value,
    (PieceType.KING, PieceColour.BLACK): PieceSymbol.KING_BLACK.value,
    None: '.'
}


STARTING_BOARD_STATE = [ 
    
    [
        Rook(PieceColour.WHITE), Knight(PieceColour.WHITE), Bishop(PieceColour.WHITE), 
        Queen(PieceColour.WHITE), King(PieceColour.WHITE),
        Bishop(PieceColour.WHITE), Knight(PieceColour.WHITE), Rook(PieceColour.WHITE)
    ],

    [
        Pawn(PieceColour.WHITE), Pawn(PieceColour.WHITE), Pawn(PieceColour.WHITE), 
        Pawn(PieceColour.WHITE), Pawn(PieceColour.WHITE), Pawn(PieceColour.WHITE),
        Pawn(PieceColour.WHITE), Pawn(PieceColour.WHITE)
    ],
    
    [None]*8,
    [None]*8,
    [None]*8,
    [None]*8,

    [
        Pawn(PieceColour.BLACK), Pawn(PieceColour.BLACK), Pawn(PieceColour.BLACK),
        Pawn(PieceColour.BLACK), Pawn(PieceColour.BLACK), Pawn(PieceColour.BLACK),
        Pawn(PieceColour.BLACK), Pawn(PieceColour.BLACK)
    ],

    [
        Rook(PieceColour.BLACK), Knight(PieceColour.BLACK), Bishop(PieceColour.BLACK), 
        Queen(PieceColour.BLACK), King(PieceColour.BLACK),
        Bishop(PieceColour.BLACK), Knight(PieceColour.BLACK), Rook(PieceColour.BLACK)
    ]
]


class Board:
    def __init__(self, board_state: List[List[Optional[Piece]]]):
        self.board_state = board_state
        self.turn = PieceColour.WHITE

    def move(self, uci_notation: str):

        # initial_pos, target_pos are tuples to access pieces in the state
        initial_pos = uci_to_num(uci_notation[0:2])
        target_pos = uci_to_num(uci_notation[2:5])
        # promotion = uci_notation[5]

        # first square can never be None, only pieces of in-turn side must move
        first_square = self.board_state[initial_pos[0]][initial_pos[1]]
        second_square = self.board_state[target_pos[0]][target_pos[1]]

        if (first_square != None and first_square.colour == self.turn):
            
            # capturing
            if (second_square != None and second_square.colour != first_square.colour):
                
                print(f"{first_square.piece.value} MOVED BY {first_square.colour.value} from {uci_notation[0:2]} to {uci_notation[2:5]}")
                self.board_state[target_pos[0]][target_pos[1]] = None
                self.board_state[initial_pos[0]][initial_pos[1]], self.board_state[target_pos[0]][target_pos[1]] = (
                    self.board_state[target_pos[0]][target_pos[1]], self.board_state[initial_pos[0]][initial_pos[1]] 
                )

            # moving to an empty square
            elif (second_square == None):
                
                print(f"{first_square.piece.value} MOVED BY {first_square.colour.value} from {uci_notation[0:2]} to {uci_notation[2:5]}")
                self.board_state[initial_pos[0]][initial_pos[1]], self.board_state[target_pos[0]][target_pos[1]] = (
                    self.board_state[target_pos[0]][target_pos[1]], self.board_state[initial_pos[0]][initial_pos[1]] 
                )
        else:
            print("either it's not your turn or you're trying to move air")
            print(first_square, second_square)

        if self.turn == PieceColour.WHITE:
            self.turn = PieceColour.BLACK
        elif self.turn == PieceColour.BLACK:
            self.turn = PieceColour.WHITE


    def __str__(self):
        rows = []

        for i in range(7, -1, -1):
            row = [symbol_map.get((self.board_state[i][j].piece, self.board_state[i][j].colour)) if self.board_state[i][j] else '.' for j in range(8)]
            rows.append(f"{i+1} {' '.join(row)}")
        
        rows.append("  a b c d e f g h")
        return "\n".join(rows)
    