from board import *
from ugraphic import *


class Piece(object):

    def __init__(self, image, t):
        self.image = Image(t.getCenter(), image)
        self.inPlay = True
        self.tile = t
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

    def __init__(self, t):
        Piece.__init__(self, "Images\WPawn.png", t)
        self.amountsMoves = 0

    def updateAvailableTiles(self, board):
        self.available_tiles = []
        if self.amountsMoves == 0:
            for i in board.tiles:
                for j in i:
                    if j.number == self.tile.number - 1 or self.tile.number - 2:
                        self.available_tiles.append(j)

        else:
            for i in board.tiles:
                for j in i:
                    if j.number == self.tile.number - 1:
                        self.available_tiles.append(j)

    def canMove(self, tile):
        can_move = False
        for i in self.available_tiles:
            if i.number == tile.number:
                can_move = True

        return can_move

    def move(self):
        self.amountsMoves += 1


class BlackPawn(Piece):

    def __init__(self, t):
        Piece.__init__(self, "Images\BPawn.png", t)

    def updateAvailableTiles(self, board):
        self.available_tiles = []
        if self.amountsMoves == 0:
            for i in board.tiles:
                for j in i:
                    if j.number == self.tile.number - 1 or self.tile.number - 2:
                        self.available_tiles.append(j)

        else:
            for i in board.tiles:
                for j in i:
                    if j.number == self.tile.number - 1:
                        self.available_tiles.append(j)

    def canMove(self, tile):
        can_move = False
        for i in self.available_tiles:
            if i.number == tile.number:
                can_move = True

        return can_move

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
    t = "Knight"

    def __init__(self, t):
        Piece.__init__(self, "Images\WKnight.png", t)

    def move(self):
        pass


class BlackKnight(Piece):
    t = "Knight"

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