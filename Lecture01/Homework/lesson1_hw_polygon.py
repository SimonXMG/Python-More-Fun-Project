import turtle as t
def DrawPolygon(sn):
    t.fillcolor('yellow')
    t.begin_fill()
    for a in range (sn):
        t.forward(500/sn)
        t.right(360/sn)
    t.end_fill()
sn = input('What is the number of sides that your polygon has?')
DrawPolygon(eval(sn))

