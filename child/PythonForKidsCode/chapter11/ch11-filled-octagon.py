import turtle
t = turtle.Pen()
def octagon(size, points, filled):
    if filled == True:
        t.begin_fill()
    for x in range(0, points):
        t.forward(size)
        t.right(360 / points)
    if filled == True:
        t.end_fill()
        
t.color(0, 0.85, 1)
octagon(80, 8, True)
t.color(0, 0, 0)
octagon(80, 8, False)
