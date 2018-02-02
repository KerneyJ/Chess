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

        # Find the piece by matching tile numbers
        for i in self.pieces:
            if i.tile.number == tile.number:
                piece = i

        index = self.pieces.index(piece)
        moveToPoints = []
        potentialMoves = []

        if piece is not None:

            # Check what type of piece is selected 
            if type(self.pieces[index].type) is type(WhitePawn):
                c1 = Circle(Point(tile.getCenter().getX(), tile.getCenter().getY() - 64), 10)
                c2 = Circle(Point(tile.getCenter().getX(), tile.getCenter().getY() - 128), 10)

                c1.setFill(color_rgb(0, 0, 100))
                c2.setFill(color_rgb(0, 0, 100))

                c1.draw(win)
                c2.draw(win)
                moveToPoints.append(c1)
                moveToPoints.append(c2)


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

        click = win.getMouse()
        while True: # check if the tile number is a tile number that would work for the piece selected and move this
                    # into the if statement for that piece.
            for i in board.tiles:
                for j in i:
                    if j.getP1().getX() < click.getX() < j.getP2().getX() and j.getP1().getY() < click.getY() < j.getP2().getY():
                        tile2 = j
                        break

        for i in moveToPoints:
            i.undraw()

        self.pieces[index].undrawSelf()
        self.pieces[index].setTile(tile2)
        self.pieces[index].drawSelf(win)


