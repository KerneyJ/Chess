# version: python3.6

from pieces import *





class Player(object):

    def __init__(self, c, b: Board):
        self.pieces = []
        self.__givePieces(c)
        self.board = b

    def __givePieces(self, c):
        if c == 'w':
            for i in range(8):
                self.pieces.append(WhitePawn())

            """
            self.pieces.append(WhiteRook())
            self.pieces.append(WhiteRook())

            self.pieces.append(WhiteKnight())
            self.pieces.append(WhiteKnight())

            self.pieces.append(WhiteBishop)
            self.pieces.append(WhiteBishop)

            self.pieces.append(WhiteKing)
            self.pieces.append(WhiteQueen)
            """

        else:
            for i in range(8):
                self.pieces.append(BlackPawn())

            self.pieces.append(WhiteRook())
            self.pieces.append(WhiteRook())

            self.pieces.append(WhiteKnight())
            self.pieces.append(WhiteKnight())

            self.pieces.append(WhiteBishop)
            self.pieces.append(WhiteBishop)

            self.pieces.append(WhiteKing)
            self.pieces.append(WhiteQueen)


