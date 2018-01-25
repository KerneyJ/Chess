# version: python3.6

from pieces import *


class Player(object):

    def __init__(self, color: str):
        """Color should be white or black"""
        # Color stuff
        self.color = color.lower()
        if self.color != "white" or self.color != "black":
            raise AssertionError("Unexpected value for color", self.color)

        self.pieces = []

    def givePieces(self):
        if self.color == "white":
            for i in range(8):
                self.pieces.append(WhitePawn())

            self.pieces.append(WhiteRook())
            self.pieces.append(WhiteRook())

            self.pieces.append(WhiteKnight())
            self.pieces.append(WhiteKnight())

            self.pieces.append(WhiteBishop())
            self.pieces.append(WhiteBishop())

            self.pieces.append(WhiteKing())
            self.pieces.append(WhiteQueen())

        else:
            for i in range(8):
                self.pieces.append(BlackPawn())

            self.pieces.append(BlackRook())
            self.pieces.append(BlackRook())

            self.pieces.append(BlackKnight())
            self.pieces.append(BlackKnight())

            self.pieces.append(BlackBishop())
            self.pieces.append(BlackBishop())

            self.pieces.append(BlackKing())
            self.pieces.append(BlackQueen())