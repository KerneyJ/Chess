from pieces import *


class Player(object):

    turn = 0

    def __init__(self):
        self.pieces = []

    def select(self, win: GraphWin):
        click = win.getMouse()
        # figure out what tile has been clicked