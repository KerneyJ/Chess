# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 20:37:59 2018

@author: Jamie

layout
8
7
6
5
4
3
2
1
 a  b  c  d  e  f  g  h
"""

from ugraphic import *
from classes import *


class Tile(Rectangle):
    def __init__(self, x, y):
        Rectangle.__init__(self, Point(x, y), Point(x + 64, y + 64))
        self.__pieces = []

    def addPiece(self, p: Piece):
        self.__pieces.append(p)

    def checkCapture(self):
        if len(self.__pieces) == 2:
            self.__pieces.pop(0)

    def drawPiece(self):
        self.__pieces[0].move() # STOPPING POINT 9:34 1/24/2018


class Board(object):
    def __init__(self, p1: Player, p2: Player):
        self.player1 = p1
        self.player2 = p2
        self.tiles = self.__giveTiles()

    @staticmethod
    def __giveTiles():
        tiles = []
        for i in range(8):
            temp = []
            for j in range(8):
                r = Rectangle(Point(i * 64, j * 64), Point((i * 64) + 64, (j * 64) + 64))
                if (i + 1) % 2 == 0 and (j + 1) % 2 == 0:
                    r.setFill(color_rgb(194, 144, 60))
                if (j + 1) % 2 != 0 and (i + 1) % 2 != 0:
                    r.setFill(color_rgb(194, 144, 60))

                temp.append(r)
            tiles.append(temp)

        return tiles

    def placePieces(self):
        # Place player1
        for i in range(8):
            self.tiles[5][i].addPiece(self.player1.pieces[i]) # Place pawns

    def drawBoard(self, win: GraphWin):
        for i in self.tiles:
            for j in i:
                j.draw(win)


class Piece(object):

    def __init__(self, image= ""):
        self.image = Image(Point(1,1), image)
        self.inPlay = True

    def drawSelf(self, win: GraphWin):
        self.image.draw(win)

    def undrawSelf(self):
        self.image.undraw()


# Pawns


class WhitePawn(Piece):

    def __init__(self):
        Piece.__init__(self, "Images\WPawn.png")

    def move(self):
        pass


class BlackPawn(Piece):

    def __init__(self):
        Piece.__init__(self, "Images\BPawn.png")

    def move(self):
        pass


# Rooks


class WhiteRook(Piece):

    def __init__(self):
        Piece.__init__(self, "Images\WRook.png")

    def move(self):
        pass


class BlackRook(Piece):
    def __init__(self):
        Piece.__init__(self, "Images\BRook.png")

    def move(self):
        pass

# Knight


class WhiteKnight(Piece):
    def __init__(self):
        Piece.__init__(self, "Images\WKnight.png")

    def move(self):
        pass


class BlackKnight(Piece):
    def __init__(self):
        Piece.__init__(self, "Images\BKnight.png")

    def move(self):
        pass


# Bishops


class WhiteBishop(Piece):
    def __init__(self):
        Piece.__init__(self, "Images\WBishop.png")

    def move(self):
        pass


class BlackBishop(Piece):
    def __init__(self):
        Piece.__init__(self, "Images\BBishop.png")

    def move(self):
        pass
# Kings


class WhiteKing(Piece):
    def __init__(self):
        Piece.__init__(self, "Images\WKing.png")

    def move(self):
        pass


class BlackKing(Piece):
    def __init__(self):
        Piece.__init__(self, "Images\BKing.png")

    def move(self):
        pass

# Queens


class WhiteQueen(Piece):

    def __init__(self):
        Piece.__init__(self, "Images\WQueen.png")

    def move(self):
        pass


class BlackQueen(Piece):

    def __init__(self):
        Piece.__init__(self, "Images\BQueen.png")

    def move(self):
        pass