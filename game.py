from board import *
from player import *
win = GraphWin("Window", 512, 512)


class Game(object):

    def __init__(self, p1, p2, board):
        self.player1 = p1
        self.player2 = p2
        self.board = board

    def start(self, win: GraphWin):
        self.board.drawBoard(win)
        self.board.updateBoard(win)
        self.draw(win)
        Player.turn = 1

    def undraw(self):
        for i in self.player1.pieces:
            i.undrawSelf()

        for i in self.player2.pieces:
            i.undrawSelf()

    def draw(self, win: GraphWin):
        for i in self.player1.pieces:
            i.drawSelf(win)

        for i in self.player2.pieces:
            i.drawSelf(win)


g = Game(Player(), Player(), Board())
g.start(win)
play = True
while play:
    if Player.turn % 2 != 0:
        g.player1.select(win, g.board, g)
        #print("p1")

    else:
        g.player2.select(win, g.board, g)
        #print("p2")

    g.board.updateBoard(win)
    k = win.checkKey()
    if k == 'Escape':
        break

    Player.turn += 1
win.close()