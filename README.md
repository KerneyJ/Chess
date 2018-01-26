# Chess


r1 = Rectangle(Point(100,100), Point(150,150))
r1.setFill(color_rgb(255,0,0))
r1.draw(win)

otherR = Rectangle(Point(350,350), Point(500,500))
otherR.setFill(color_rgb(0,0,255))
otherR.draw(win)

time.sleep(4)

dx = otherR.getCenter().getX() - r1.getCenter().getX()
dy = otherR.getCenter().getY() - r1.getCenter().getY()

r1.move(dx,dy)
r1.undraw()
r1.draw(win)
