from classes import *
win = GraphWin("Window", 512, 512)

b = Board(1, 1)
b.drawBoard(win)
p1 = Player('w', b)

for i in p1.pieces:
    i.drawSelf(win)

while True:
    k = win.getKey()
    if k == 'Escape':
        break
win.close()