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


# v.-Alpha-0.1 to v.-Alpha-1.6
### All pieces work in isolation

## Bugs:
''' javascript
Black knight first move:
Traceback (most recent call last):
  File "I:/Desktop/Chess-v.-Alpha-1.5/game.py", line 43, in <module>
    g.player2.select(win, g.board, g)
  File "I:\Desktop\Chess-v.-Alpha-1.5\player.py", line 59, in select
    canMove = self.KnightCanMove(row, col, row2, col2, board.b)
  File "I:\Desktop\Chess-v.-Alpha-1.5\player.py", line 203, in KnightCanMove
    if not board[col + 1][row + 2][0] is board[col][row][0]:
IndexError: list index out of range
'''
