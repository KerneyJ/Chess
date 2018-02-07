from pieces import *


class Player(object):
    turn = 0

    def __init__(self):
        self.pieces = []
        self.pieceTiles = []

    def select(self, win: GraphWin, board):
        click = win.getMouse()
        tile = None
        piece = None
        for i in board.tiles:
            for j in i:
                if j.getP1().getX() < click.getX() < j.getP2().getX() and j.getP1().getY() < click.getY() < j.getP2().getY():
                    tile = j
                    break

        # print(tile.number) check tile 1 number

        # Find the piece by matching tile numbers
        for i in self.pieces:
            if i.tile.number == tile.number:
                piece = i

        # Select a tile to move it to
        click = win.getMouse()

        if piece is not None:
            index = self.pieces.index(piece)
            for i in board.tiles:
                for j in i:
                    if j.getP1().getX() < click.getX() < j.getP2().getX() and j.getP1().getY() < click.getY() < j.getP2().getY():
                        tile2 = j
                        break

            # print(tile2.number) check tile2 number

            # Check what type of piece is selected
            if type(self.pieces[index].type) is type(WhitePawn):
                self.pieces[index].updateAvailableTiles(board)
                c1 = Circle(self.pieces[index].tile.getCenter(), 10)
                c1.setFill(color_rgb(0, 0, 100))
                while not self.pieces[index].canMove(tile2):
                    click = win.getMouse()
                    for i in board.tiles:
                        for j in i:
                            if j.getP1().getX() < click.getX() < j.getP2().getX() and j.getP1().getY() < click.getY() < j.getP2().getY():
                                tile2 = j

            elif type(self.pieces[index].type) is type(BlackPawn):
                pass

            elif type(self.pieces[index].type) is type(WhiteRook) or type(self.pieces[index].type) is type(BlackRook):
                pass

            elif type(self.pieces[index].type) is type(WhiteKnight) or type(self.pieces[index].type) is type(BlackKnight):
                pass

            elif type(self.pieces[index].type) is type(WhiteBishop) or type(self.pieces[index].type) is type(BlackBishop):
                pass

            elif type(self.pieces[index].type) is type(WhiteKing) or type(self.pieces[index].type) is type(BlackKing):
                pass

            elif type(self.pieces[index].type) is type(WhiteQueen) or type(self.pieces[index].type) is type(BlackQueen):
                pass

            self.pieces[index].undrawSelf()
            self.pieces[index].setTile(tile2)
            self.pieces[index].drawSelf(win)


