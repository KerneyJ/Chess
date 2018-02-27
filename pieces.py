from board import *
from ugraphic import *


class Piece(object):

    def __init__(self, image):
        self.number = 0
        self.image = Image(Point(0,0),image)
        self.inPlay = True

        self.type = type(self)
        self.available_tiles = []

    def drawSelf(self, win: GraphWin):
        self.image.draw(win)

    def undrawSelf(self):
        self.image.undraw()

    def setTile(self, t):
        self.tile = t
        center = self.tile.getCenter()
        self.image.move(-1 * (self.image.getAnchor().getX() - center.getX()), -1 *(self.image.getAnchor().getY() - center.getY()))

    def __str__(self):
        return str(self.image) + " Inplay: " + str(self.inPlay) + " Type: " + str(self.type)


# Pawns


class WhitePawn(Piece):

    def __init__(self):
        Piece.__init__(self, "Images\WPawn.png")
        self.amountsMoves = 0
        self.amountsMoves += 1


    def canMove(self, tile):
        can_move = False
        for i in self.available_tiles:
            if i.number == tile.number:
                can_move = True

        return can_move


class BlackPawn(Piece):

    def __init__(self):
        Piece.__init__(self, "Images\BPawn.png")
        self.amountMoves = 0
        self.amountMoves += 1

    def canMove(self, tile):
        can_move = False
        for i in self.available_tiles:
            if i.number == tile.number:
                can_move = True

        return can_move


# Rooks


class WhiteRook(Piece):
    num = 0

    def __init__(self):
        Piece.__init__(self, "Images\WRook.png")

    def canMove(self, tile):
        can_move = False
        for i in self.available_tiles:
            if i.number == tile.number:
                can_move = True

        return can_move


class BlackRook(Piece):
    num = 0

    def __init__(self):
        Piece.__init__(self, "Images\BRook.png")
        self.number = BlackRook.num
        BlackRook.num += 1

    def canMove(self, tile):
        can_move = False
        for i in self.available_tiles:
            if i.number == tile.number:
                can_move = True

        return can_move


# Knight


class WhiteKnight(Piece):

    def __init__(self):
        Piece.__init__(self, "Images\WKnight.png")
        self.number = BlackRook.num
        BlackRook.num += 1

    def move(self):
        pass


class BlackKnight(Piece):

    def __init__(self):
        Piece.__init__(self, "Images\BKnight.png")
        self.number = BlackRook.num
        BlackRook.num += 1

    def move(self):
        pass


# Bishops


class WhiteBishop(Piece):

    def __init__(self):
        Piece.__init__(self, "Images\WBishop.png")
        self.number = BlackRook.num
        BlackRook.num += 1

    def move(self):
        pass


class BlackBishop(Piece):
    def __init__(self):
        Piece.__init__(self, "Images\BBishop.png")
        self.number = BlackRook.num
        BlackRook.num += 1

    def move(self):
        pass


# Kings


class WhiteKing(Piece):
    def __init__(self):
        Piece.__init__(self, "Images\WKing.png")
        self.number = BlackRook.num
        BlackRook.num += 1

    def move(self):
        pass


class BlackKing(Piece):
    def __init__(self):
        Piece.__init__(self, "Images\BKing.png")
        self.number = BlackRook.num
        BlackRook.num += 1

    def move(self):
        pass


# Queens


class WhiteQueen(Piece):

    def __init__(self):
        Piece.__init__(self, "Images\WQueen.png")
        self.number = BlackRook.num
        BlackRook.num += 1

    def move(self):
        pass


class BlackQueen(Piece):

    def __init__(self):
        Piece.__init__(self, "Images\BQueen.png")
        self.number = BlackRook.num
        BlackRook.num += 1

    def move(self):
        pass