from classes import *
win = GraphWin("Window", 512, 512)


p1 = Player("white")
p2 = Player("black")
b = Board(p1, p2)
b.drawBoard(win)

# Demo of adding a piece and drawing it
# p = WhiteBishop()
# b.tiles[0][0].addPiece(p)
# b.tiles[0][0].drawPiece(win)


while True:
    k = win.getKey()
    if k == 'Escape':
        break
win.close()