from board import *
from ugraphic import *


class Piece(object):

    def __init__(self, image, t):
        self.image = Image(t.getCenter(), image)
        self.inPlay = True
        self.tile = t

    def drawSelf(self, win: GraphWin):
        self.image.draw(win)

    def undrawSelf(self):
        self.image.undraw()

    def __str__(self):
        return str(self.image) + " Inplay: " + str(self.inPlay)


# Pawns


class WhitePawn(Piece):

    def __init__(self, t):
        Piece.__init__(self, "Images\WPawn.png", t)

    def move(self):
        pass


class BlackPawn(Piece):

    def __init__(self, t):
        Piece.__init__(self, "Images\BPawn.png", t)

    def move(self):
        pass


# Rooks


class WhiteRook(Piece):

    def __init__(self, t):
        Piece.__init__(self, "Images\WRook.png", t)

    def move(self):
        pass


class BlackRook(Piece):
    def __init__(self, t):
        Piece.__init__(self, "Images\BRook.png", t)

    def move(self):
        pass


# Knight


class WhiteKnight(Piece):
    def __init__(self, t):
        Piece.__init__(self, "Images\WKnight.png", t)

    def move(self):
        pass


class BlackKnight(Piece):
    def __init__(self, t):
        Piece.__init__(self, "Images\BKnight.png", t)

    def move(self):
        pass


# Bishops


class WhiteBishop(Piece):
    def __init__(self, t):
        Piece.__init__(self, "Images\WBishop.png", t)

    def move(self):
        pass


class BlackBishop(Piece):
    def __init__(self, t):
        Piece.__init__(self, "Images\BBishop.png", t)

    def move(self):
        pass


# Kings


class WhiteKing(Piece):
    def __init__(self, t):
        Piece.__init__(self, "Images\WKing.png", t)

    def move(self):
        pass


class BlackKing(Piece):
    def __init__(self, t):
        Piece.__init__(self, "Images\BKing.png", t)

    def move(self):
        pass


# Queens


class WhiteQueen(Piece):

    def __init__(self, t):
        Piece.__init__(self, "Images\WQueen.png", t)

    def move(self):
        pass


class BlackQueen(Piece):

    def __init__(self, t):
        Piece.__init__(self, "Images\BQueen.png", t)

    def move(self):
        pass