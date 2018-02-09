# Chess
### version Alpha 0.1 update notes
test.py:
tested the construction of a board and the draw method from the board
tested the construction of a white bishop and the draw method for that bishop

pieces.py:
Creates the board and tile classes
Board has a 2d array of tiles(self.tiles)
Tiles is a Rectangle from ugraphics
All pieces inherit from class piece
All pieces have a tile

classes.py:
Creates the player class
Players has pieces

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

### version Alpha 0.2 update notes
test.py:
Attempted to move a piece at a specific index
Draw circles where pieces could move

pieces.py:
nothing noteworthy

classes.py:
nothing noteworthy

### version Alpha 0.3 through Alpha 0.4
Nothing note worthy

### version Alpha 0.5
game.py(new test file):
Game class created
The game class has 2 players and a board
It can give players pieces
It can draw the board
Game loop is at the bottom.

board.py:
nothing noteworthy

classes.py:
nothing noteworthy

player.py:
nothing noteworthy

pieces.py:
nothing noteworthy

### version Alpha 0.6
test.py:
removed

classes.py:
removed

board.py:
nothing noteworthy

player.py:
nothing noteworthy

pieces.py:
nothing noteworthy

game.py:
nothing noteworthy

### version Alpha 0.7
player.py:
  select method:
  double for loop to find the tile that was clicked on (should become its own method)
  single for loop to find the piece that owns the tile that was clicked on
  piece is defaulted to none but it should always change value
  inside if piece equal none test the type of the piece and move accordingly

board.py:
nothing noteworthy

pieces.py:
nothing noteworthy

game.py:
nothing noteworthy

### version Alpha 0.8
pieces.py:
SetTile method created for pieces

player.py:
Able to move pieces to any spot
to move: undraw setTile(to new tile) re-draw

board.py:
nothing noteworthy

game.py:
nothing noteworthy

### version Alpha 0.9
pieces.py:
created update tiles method and can move method(specific to each type of chess piece)

player.py:
while loop that is true as long as the tile selected by a player is not a tile that the piece can move too
This while loop will keep going on until a piece that is okay with the system is selected

board.py:
nothing noteworthy

game.py:
nothing noteworthy

