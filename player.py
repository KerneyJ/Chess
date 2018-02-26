from pieces import *


class Player(object):
    turn = 0

    def __init__(self):
        self.pieces = []

    def getTile(self, board, win):
        click = win.getMouse()
        tile = None
        for i in board.tiles: # Find the tile that was clicked on
            for j in i:
                if j.getP1().getX() < click.getX() < j.getP2().getX() and j.getP1().getY() < click.getY() < j.getP2().getY():
                    tile = j
                    break

        return tile

    def selectPiece(self, board, win):
        tile = self.getTile(board, win)  # get tile that was clicked on
        row = int(tile.getP1().getX() / 64)  # calculate row
        col = int(tile.getP1().getY() / 64)  # calculate column
        piece = board.b[col][row]  # Grab the piece that was clicked on
        return piece, row, col

    def select(self, win: GraphWin, board, game):

        piece, row, col = self.selectPiece(board, win)
        board.b[col][row] = "EE"  # Set the place that was clicked on to an empty tile
        print(row, col)

        row2 = 0  # Default instantiation
        col2 = 0  # Default instantiation

        if piece == "WP":  # if the piece was clicked on was a white pawn
            moveSpot = self.getTile(board, win)
            row2 = int(moveSpot.getP1().getX() / 64)
            col2 = int(moveSpot.getP1().getY() / 64)
            print(self.WPCanMove(row,col,row2,col2))
            print()

        board.b[col2][row2] = piece

    def WPCanMove(self, row, col, row2, col2):
        if col2 == col - 1:
            if row2 == row:
                return True

        if col2 == col - 2:
            if row2 == row:
                return True

        return False

    def BPCanMove(self, row, col, row2, col2):
        if col2 == col + 1:
            if row2 == row:
                return True

        if col2 == col + 2:
            if row2 == row:
                return True

        return False


