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
from player import *


class Board(object):
    def __init__(self):
        """ Create methods for the board. Has a list of tiles, a list of pieces,
            and a b which is a representation of the board. """
        self.tiles = self.__giveTiles()
        self.pieces = []
        self.b = [["BR","Bk","BB","BQ","BK","BB","Bk","BR"],
                  ["BP","BP","BP","BP","BP","BP","BP","BP"],
                  ["EE","EE","EE","EE","EE","EE","EE","EE"],
                  ["EE","EE","EE","EE","EE","EE","EE","EE"],
                  ["EE","EE","EE","EE","EE","EE","EE","EE"],
                  ["EE","EE","EE","EE","EE","EE","EE","EE"],
                  ["WP","WP","WP","WP","WP","WP","WP","WP"],
                  ["WR","Wk","WB","WQ","WK","WB","Wk","WR"]]

    @staticmethod
    def __giveTiles():
        tiles = []
        for i in range(8):
            temp = []
            for j in range(8):
                r = Rectangle(Point(i * 64, j * 64), Point((i * 64) + 64, (j * 64) + 64))
                r.setFill(color_rgb(194, 144, 60))
                if (i + 1) % 2 == 0 and (j + 1) % 2 == 0:
                    r.setFill(color_rgb(255, 255, 255))
                if (j + 1) % 2 != 0 and (i + 1) % 2 != 0:
                    r.setFill(color_rgb(255, 255, 255))

                temp.append(r)
            tiles.append(temp)

        return tiles

    def drawBoard(self, win):
        for i in self.tiles:
            for j in i:
                j.draw(win)

    def undrawBoard(self):
        for i in self.tiles:
            for j in i:
                j.undraw()

    def updateBoard(self, win):

        for i in self.pieces:
            i.undraw()

        self.pieces = []

        for i in range(len(self.b)):
            for j in range(len(self.b[i])):

                # Draw black pieces
                if self.b[i][j] is "BR":
                    img = Image(Point((j*64) + 32, (i*64) + 32), "Images\BRook.png")
                    img.draw(win)
                    self.pieces.append(img)

                elif self.b[i][j] is "Bk":
                    img = Image(Point((j * 64) + 32, (i*64) + 32), "Images\BKnight.png")
                    img.draw(win)
                    self.pieces.append(img)

                elif self.b[i][j] is "BB":
                    img = Image(Point((j * 64) + 32, (i*64) + 32), "Images\BBishop.png")
                    img.draw(win)
                    self.pieces.append(img)

                elif self.b[i][j] is "BK":
                    img = Image(Point((j * 64) + 32, (i*64) + 32), "Images\BKing.png")
                    img.draw(win)
                    self.pieces.append(img)

                elif self.b[i][j] is "BQ":
                    img = Image(Point((j * 64) + 32, (i*64) + 32), "Images\BQueen.png")
                    img.draw(win)
                    self.pieces.append(img)

                elif self.b[i][j] is "BP":
                    img = Image(Point((j * 64) + 32, (i*64) + 32), "Images\BPawn.png")
                    img.draw(win)
                    self.pieces.append(img)

                # Draw white team
                if self.b[i][j] is "WR":
                    img = Image(Point((j*64) + 32, (i*64) + 32), "Images\WRook.png")
                    img.draw(win)
                    self.pieces.append(img)

                elif self.b[i][j] is "Wk":
                    img = Image(Point((j * 64) + 32, (i*64) + 32), "Images\WKnight.png")
                    img.draw(win)
                    self.pieces.append(img)

                elif self.b[i][j] is "WB":
                    img = Image(Point((j * 64) + 32, (i*64) + 32), "Images\WBishop.png")
                    img.draw(win)
                    self.pieces.append(img)

                elif self.b[i][j] is "WK":
                    img = Image(Point((j * 64) + 32, (i*64) + 32), "Images\WKing.png")
                    img.draw(win)
                    self.pieces.append(img)

                elif self.b[i][j] is "WQ":
                    img = Image(Point((j * 64) + 32, (i*64) + 32), "Images\WQueen.png")
                    img.draw(win)
                    self.pieces.append(img)

                elif self.b[i][j] is "WP":
                    img = Image(Point((j * 64) + 32, (i*64) + 32), "Images\WPawn.png")
                    img.draw(win)
                    self.pieces.append(img)

                elif self.b[i][j] is "TP":
                    img = Image(Point((j * 64) + 32, (i*64) + 32), "Images\TestPawn.png")
                    img.draw(win)
                    self.pieces.append(img)