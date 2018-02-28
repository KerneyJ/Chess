# Chess
### version Alpha 1.0.0 update notes
Images:

![alt text](https://github.com/KerneyJ/Chess/blob/v.-Alpha-0.3/Images/BPawn.png "Logo Title Text 1")
![alt text](https://github.com/KerneyJ/Chess/blob/v.-Alpha-0.3/Images/BRook.png "Logo Title Text 1")
![alt text](https://github.com/KerneyJ/Chess/blob/v.-Alpha-0.3/Images/BKnight.png "Logo Title Text 1")
![alt text](https://github.com/KerneyJ/Chess/blob/v.-Alpha-0.3/Images/BBishop.png "Logo Title Text 1")
![alt text](https://github.com/KerneyJ/Chess/blob/v.-Alpha-0.3/Images/BQueen.png "Logo Title Text 1")
![alt text](https://github.com/KerneyJ/Chess/blob/v.-Alpha-0.3/Images/BKing.png "Logo Title Text 1")

![alt text](https://github.com/KerneyJ/Chess/blob/v.-Alpha-0.3/Images/WPawn.png "Logo Title Text 1")
![alt text](https://github.com/KerneyJ/Chess/blob/v.-Alpha-0.3/Images/WRook.png "Logo Title Text 1")
![alt text](https://github.com/KerneyJ/Chess/blob/v.-Alpha-0.3/Images/WKnight.png "Logo Title Text 1")
![alt text](https://github.com/KerneyJ/Chess/blob/v.-Alpha-0.3/Images/WBishop.png "Logo Title Text 1")
![alt text](https://github.com/KerneyJ/Chess/blob/v.-Alpha-0.3/Images/WQueen.png "Logo Title Text 1")
![alt text](https://github.com/KerneyJ/Chess/blob/v.-Alpha-0.3/Images/WKing.png "Logo Title Text 1")


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
