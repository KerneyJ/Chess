from board import *
from pieces import *
from player import *
win = GraphWin("Window", 512, 512)


class Game(object):

    def __init__(self, p1, p2, board):
        self.player1 = p1
        self.player2 = p2
        self.board = board

    def start(self, win: GraphWin):
        self.board.drawBoard(win)
        self.givePieces()
        for i in self.player1.pieces:
            i.drawSelf(win)

        for i in self.player2.pieces:
            i.drawSelf(win)

        Player.turn = 1

    def givePieces(self):
        for i in range(8):
            self.player1.pieces.append(WhitePawn(self.board.tiles[i][6]))

        self.player1.pieces.append(WhiteRook(self.board.tiles[0][7]))
        self.player1.pieces.append(WhiteRook(self.board.tiles[7][7]))

        self.player1.pieces.append(WhiteKnight(self.board.tiles[1][7]))
        self.player1.pieces.append(WhiteKnight(self.board.tiles[6][7]))

        self.player1.pieces.append(WhiteBishop(self.board.tiles[2][7]))
        self.player1.pieces.append(WhiteBishop(self.board.tiles[5][7]))

        self.player1.pieces.append(WhiteKing(self.board.tiles[4][7]))
        self.player1.pieces.append(WhiteQueen(self.board.tiles[3][7]))

        for i in range(8):
            self.player2.pieces.append(BlackPawn(self.board.tiles[i][1]))

        self.player2.pieces.append(BlackRook(self.board.tiles[0][0]))
        self.player2.pieces.append(BlackRook(self.board.tiles[7][0]))

        self.player2.pieces.append(BlackKnight(self.board.tiles[1][0]))
        self.player2.pieces.append(BlackKnight(self.board.tiles[6][0]))

        self.player2.pieces.append(BlackBishop(self.board.tiles[2][0]))
        self.player2.pieces.append(BlackBishop(self.board.tiles[5][0]))

        self.player2.pieces.append(BlackKing(self.board.tiles[4][0]))
        self.player2.pieces.append(BlackQueen(self.board.tiles[3][0]))


g = Game(Player(), Player(), Board())
g.start(win)

play = True
while play:
    if Player.turn % 2 != 0:
        g.player1.select()

    else:
        g.player2.select()

    k = win.getKey()
    if k == 'Escape':
        break

    Player.turn += 1
win.close()