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


class Tile(Rectangle):
    num = 0

    def __init__(self, p1, p2):
        self.number = Tile.num
        Rectangle.__init__(self, p1, p2)
        Tile.num += 1

    def __str__(self):
        return "Tile No.: " + str(self.number)

    """def __eq__(self, other):
        return self.num == other.num and self.getP2() == other.getP2 and self.getP1() == other.getP1()"""


class Board(object):
    def __init__(self):
        self.tiles = self.__giveTiles()

    @staticmethod
    def __giveTiles():
        tiles = []
        for i in range(8):
            temp = []
            for j in range(8):
                r = Tile(Point(i * 64, j * 64), Point((i * 64) + 64, (j * 64) + 64))
                r.setFill(color_rgb(194, 144, 60))
                if (i + 1) % 2 == 0 and (j + 1) % 2 == 0:
                    r.setFill(color_rgb(255, 255, 255))
                if (j + 1) % 2 != 0 and (i + 1) % 2 != 0:
                    r.setFill(color_rgb(255, 255, 255))

                temp.append(r)
            tiles.append(temp)

        return tiles

    def drawBoard(self, win: GraphWin):
        for i in self.tiles:
            for j in i:
                j.draw(win)

    def undrawBoard(self):
        for i in self.tiles:
            for j in i:
                j.undraw()

    def outputTileNums(self):
        for i in self.tiles:
            for j in i:
                print(j.number)
