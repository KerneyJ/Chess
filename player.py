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
        row2 = 0
        col2 = 0
        canMove = False

        if piece == "WP":  # if the piece was clicked on was a white pawn
            while not canMove:
                moveSpot = self.getTile(board, win)
                row2 = int(moveSpot.getP1().getX() / 64)
                col2 = int(moveSpot.getP1().getY() / 64)
                canMove = self.WPCanMove(row, col, row2, col2)

        elif piece == "BP":
            while not canMove:
                moveSpot = self.getTile(board, win)
                row2 = int(moveSpot.getP1().getX() / 64)
                col2 = int(moveSpot.getP1().getY() / 64)
                canMove = self.BPCanMove(row, col, row2, col2)

        elif piece == "WR" or piece == "BR":
            while not canMove:
                moveSpot = self.getTile(board, win)
                row2 = int(moveSpot.getP1().getX() / 64)
                col2 = int(moveSpot.getP1().getY() / 64)
                canMove = self.RookCanMove(row, col, row2, col2, board.b)

        elif piece == "Wk" or piece == "Bk":
            while not canMove:
                moveSpot = self.getTile(board, win)
                row2 = int(moveSpot.getP1().getX() / 64)
                col2 = int(moveSpot.getP1().getY() / 64)
                canMove = self.KnightCanMove(row, col, row2, col2, board.b)

        elif piece == "WB" or piece == "BB":
            while not canMove:
                moveSpot = self.getTile(board, win)
                row2 = int(moveSpot.getP1().getX() / 64)
                col2 = int(moveSpot.getP1().getY() / 64)
                canMove = self.BishopCanMove(row, col, row2, col2, board.b)

        board.b[col][row] = "EE"  # Set the place that was clicked on to an empty tile
        board.b[col2][row2] = piece

    def WPCanMove(self, row, col, row2, col2):  # Fix the double move and attack
        if col2 == col - 1:
            if row2 == row:
                return True

        if col2 == col - 2:
            if row2 == row:
                return True

        return False

    def BPCanMove(self, row, col, row2, col2): # Fix the double move and attack
        if col2 == col + 1:
            if row2 == row:
                return True

        if col2 == col + 2:
            if row2 == row:
                return True

        return False

    def RookCanMove(self, row, col, row2, col2, board):

        pieceType = board[col][row][0]
        # print(row - row2)  If positive it goes left if negative it goes right
        # print(col - col2)  If positive it goes up if negative it goes down
        horizontalDirection = None  # 0 is left and 1 is right and 2 is not moving in this direction
        verticalDirection = None  # 0 is up and 1 is down and 2 is not moving in this direction

        if row - row2 > 0:
            horizontalDirection = "L"
        elif row - row2 < 0:
            horizontalDirection = "R"
        else:
            horizontalDirection = "N"

        if col - col2 > 0:
            verticalDirection = "U"
        elif col - col2 < 0:
            verticalDirection = "D"
        else:
            verticalDirection = "N"

        def getStop(start, stop, step, row=None, col=None):
            if not (row is None):
                for i in range(start, stop, step):
                    if not board[i][row] is "EE":
                        return i

                return stop

            elif not (col is None):
                for i in range(start, stop, step):
                    if not board[col][i] is "EE":
                        return i

                return stop

            else:
                raise AssertionError("Error row and column are none")

        stopUp = getStop(col-1, -1, -1, row=row)
        stopDown = getStop(col+1, 8, 1, row=row)
        stopRight = getStop(row+1, 8, 1, col=col)
        stopLeft = getStop(row-1, -1, -1, col=col)

        if not board[col][row][0] is board[col2][row2][0]:
            print("Different teams")
            print(verticalDirection, horizontalDirection)
            if verticalDirection is "N":
                if horizontalDirection is "L":
                    stopLeft -= 1
                else:
                    stopRight += 1
            else:
                if verticalDirection is "U":
                    stopUp -= 1
                else:
                    stopDown += 1

        # print("Up: ", stopUp, "\nRight: ", stopRight, "\nDown: ", stopDown, "\nLeft: ", stopLeft)
        if stopUp < col2 < stopDown:  # Check if it is in between stopUp and stopDown
            if stopLeft < row2 < stopRight:  # Check if it is in between stopLeft and stopRight
                if not (row == row2 and col == col2):  # Check if it is not the same spot
                    if row == row2 or col == col2:  # Make sure it is still with the same row or column
                        return True

        return False

    def KnightCanMove(self, row, col, row2, col2, board):

        # Left up
        if not board[col-1][row-2][0] is board[col][row][0]:
            if row2 == row-2 and col2 == col-1:
                return True

        # Left down
        if not board[col+1][row-2][0] is board[col][row][0]:
            if row2 == row-2 and col2 == col+1:
                return True

        # Right up
        if not board[col - 1][row + 2][0] is board[col][row][0]:
            if row2 == row + 2 and col2 == col - 1:
                return True

        # Right down
        if not board[col + 1][row + 2][0] is board[col][row][0]:
            if row2 == row + 2 and col2 == col + 1:
                return True

        # Up left
        if not board[col-2][row-1][0] is board[col][row][0]:
            if row2 == row - 1 and col2 == col - 2:
                return True
        # Up right
        if not board[col-2][row+1][0] is board[col][row][0]:
            if row2 == row + 1 and col2 == col -2:
                return True

        # Down left
        if not board[col+2][row-1][0] is board[col][row][0]:
            if row2 == row - 1 and col2 == col + 2:
                return True
        # Down right
        if not board[col+2][row+1][0] is board[col][row][0]:
            if row2 == row + 1 and col2 == col + 2:
                return True

        return False

    def BishopCanMove(self, row, col, row2, col2, board):
        pieceType = board[col][row][0]
        direction = "N/A"

        if row - row2 > 0 and col - col2 > 0: # Direction is Up Left
            direction = "UL"
            for i in range(8):
                if col-i-1 < 0 or row-i-1 < 0 or not board[col-i-1][row-i-1] is "EE":
                    if not board[col-i-1][row-i-1][0] is board[col][row][0]:
                        return True

                    break

                if row2 == row-i-1 and col2 == col-i-1:
                    return True

        elif row - row2 < 0 and col - col2 > 0: # Direction is Up Right
            direction = "UR"

            for i in range(8):
                if col+i+1 < 0 or row-i-1 < 0 or not board[col+i+1][row-i-1] is "EE":
                    if not board[col+i+1][row-i-1][0] is board[col][row][0]:
                        return True

                    break

                if row2 == row-i-1 and col2 == col+i+1:
                    return True


        elif row - row2 > 0 and col - col2 < 0: # Direction is Down Left
            for i in range(8):
                if col-i-1 < 0 or row+i+1 < 0 or not board[col-i-1][row+i+1] is "EE":
                    if not board[col-i-1][row+i+1][0] is board[col][row][0]:
                        return True

                    break

                if row2 == row+i+1 and col2 == col-i-1:
                    return True


        elif row - row2 < 0 and col - col2 < 0: # Direction is Down Right
            direction = "DR"
            for i in range(8):
                if col+i+1 > 7 or row+i+1 > 7 or not board[col+i+1][row+i+1] is "EE":
                    if not board[col+i+1][row+i+1][0] is board[col][row][0]:
                        return True
                    break

                if row2 == row-i-1 and col2 == col-i-1:
                    return True

        print(direction)

        """
        def getStop(start, stop, step, row=None, col=None):
            if not (row is None):
                for i in range(start, stop, step):
                    if not board[i][row] is "EE":
                        return i

                return stop

            elif not (col is None):
                for i in range(start, stop, step):
                    if not board[col][i] is "EE":
                        return i

                return stop

            else:
                raise AssertionError("Error row and column are none")
            
        stopUp = getStop(col - 1, -1, -1, row=row)
        stopDown = getStop(col + 1, 8, 1, row=row)
        stopRight = getStop(row + 1, 8, 1, col=col)
        stopLeft = getStop(row - 1, -1, -1, col=col)

        if not board[col][row][0] is board[col2][row2][0]:
            print("Different teams")
            print(verticalDirection, horizontalDirection)
            if verticalDirection is "N":
                if horizontalDirection is "L":
                    stopLeft -= 1
                else:
                    stopRight += 1
            else:
                if verticalDirection is "U":
                    stopUp -= 1
                else:
                    stopDown += 1

        # print("Up: ", stopUp, "\nRight: ", stopRight, "\nDown: ", stopDown, "\nLeft: ", stopLeft)
        if stopUp < col2 < stopDown:  # Check if it is in between stopUp and stopDown
            if stopLeft < row2 < stopRight:  # Check if it is in between stopLeft and stopRight
                if not (row == row2 and col == col2):  # Check if it is not the same spot
                    if row == row2 or col == col2:  # Make sure it is still with the same row or column
                        return True"""





