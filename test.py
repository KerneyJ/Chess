from classes import *
from pieces import *
win = GraphWin("Window", 512, 512)

b = Board(1, 1)
b.drawBoard(win)
p = WhiteBishop()
p.drawSelf(win)
while True:
    k = win.getKey()
    if k == 'Escape':
        break
win.close()