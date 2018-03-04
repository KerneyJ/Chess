### Method should be local to RookCanMove
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