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


class Board(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # Give tiles to the board
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

    def drawBoard(self, win: GraphWin):
        for i in self.tiles:
            for j in i:
                j.draw(win)

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

class Piece(object):

    def __init__(self, point = Tile(1,1), image= ""):
        self.image = Image(point, image)
        self.inPlay = True
        self.position = '1a'

    def drawSelf(self, win: GraphWin):
        self.image.draw(win)

    def undrawSelf(self):
        self.image.undraw()

# Pawns


class WhitePawn(Piece):

    def __init__(self, point = Tile(1,1)):
        Piece.__init__(self, point, "Images\WPawn.png")

    def move(self):
        pass


class BlackPawn(Piece):

    def __init__(self, point = Tile(1,1)):
        Piece.__init__(self, point, "Images\BPawn.png")

    def move(self):
        pass

# Rooks


class WhiteRook(Piece):

    def __init__(self, point = Tile(1,1)):
        Piece.__init__(self, point, "Images\WRook.png")

    def move(self):
        pass


class BlackRook(Piece):
    def __init__(self, point = Tile(1,1)):
        Piece.__init__(self, point, "Images\BRook.png")

    def move(self):
        pass

# Knight


class WhiteKnight(Piece):
    def __init__(self, point = Tile(1,1)):
        Piece.__init__(self, point, "Images\WKnight.png")

    def move(self):
        pass


class BlackKnight(Piece):
    def __init__(self, point = Tile(1,1)):
        Piece.__init__(self, point, "Images\BKnight.png")

    def move(self):
        pass


# Bishops


class WhiteBishop(Piece):
    def __init__(self, point = Tile(1,1)):
        Piece.__init__(self, point, "Images\WBishop.png")

    def move(self):
        pass


class BlackBishop(Piece):
    def __init__(self, point=Tile(1, 1)):
        Piece.__init__(self, point, "Images\BBishop.png")

    def move(self):
        pass
# Kings


class WhiteKing(Piece):
    def __init__(self, point = Tile(1,1)):
        Piece.__init__(self, point, "Images\WKing.png")

    def move(self):
        pass


class BlackKing(Piece):
    def __init__(self, point = Tile(1,1)):
        Piece.__init__(self, point, "Images\BKing.png")

    def move(self):
        pass

# Queens


class WhiteQueen(Piece):

    def __init__(self, point = Tile(1,1)):
        Piece.__init__(self, point, "Images\WQueen.png")

    def move(self):
        pass


class BlackQueen(Piece):

    def __init__(self, point = Tile(1,1)):
        Piece.__init__(self, point, "Images\BQueen.png")

    def move(self):
        pass