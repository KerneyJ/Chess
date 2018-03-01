from ugraphic import *


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
        row2 = -2
        col2 = -2

        if piece == "WP":  # if the piece was clicked on was a white pawn
            while not self.WPCanMove(row, col, row2, col2):
                moveSpot = self.getTile(board, win)
                row2 = int(moveSpot.getP1().getX() / 64)
                col2 = int(moveSpot.getP1().getY() / 64)

            print(self.WPCanMove(row,col,row2,col2))
            print()

        elif piece == "BP":
            while not self.BPCanMove(row, col, row2, col2):
                moveSpot = self.getTile(board, win)
                row2 = int(moveSpot.getP1().getX() / 64)
                col2 = int(moveSpot.getP1().getY() / 64)

        if piece == "WR" or piece == "BR":
            while not self.RookCanMove(row, col, row2, col2, board.b):
                moveSpot = self.getTile(board, win)
                row2 = int(moveSpot.getP1().getX() / 64)
                col2 = int(moveSpot.getP1().getY() / 64)

            """
            while not self.RookCanMove(row, col, row2, col2, board.b):
                moveSpot = self.getTile(board, win)
                row2 = int(moveSpot.getP1().getX() / 64)
                col2 = int(moveSpot.getP1().getY() / 64)"""

        board.b[col][row] = "EE"  # Set the place that was clicked on to an empty tile
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

    def RookCanMove(self, row, col, row2, col2, board):

        stopUp = 0
        stopRight = 0
        stopLeft = 0
        stopDown = 0

        # print(row, col)
        for i in range(col-1, -1, -1):  # going up
            # print(board[i][row])
            if board[i][row] is not "EE":
                stopUp = i
                break

        for i in range(col+1, 8, 1):  # going down
            # print(board[i][row])
            if board[i][row] is not "EE":
                stopDown = i
                break

        for i in range(row+1, 8, 1):  # going right
            if board[col][i] is not "EE":
                stopRight = i
                break

        for i in range(row-1, -1, -1):
            #  print(board[col][i])
            if board[col][i] is not "EE":
                stopLeft = i
                break

        # print("Up: ", stopUp, "\nRight: ", stopRight, "\nDown: ", stopDown, "\nLeft: ", stopLeft)
        if stopUp < col2 < stopDown:  # Check if it is in between stopUp and stopDown
            if stopLeft < row2 < stopRight:  # Check if it is in between stopLeft and stopRight
                if not (row == row2 and col == col2):  # Check if it is not the same spot
                    if row == row2 or col == col2:  # Make sure it is still with the same row or column
                        return True

        return False




