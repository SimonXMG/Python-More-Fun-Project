import turtle as t
def rainbow(width):
    radius = int(width/2)
    thickness = 2*int(width/200)
    t.penup()
    t.backward(radius)
    t.left(90)
    t.speed('fastest')
    colors = ['red','orange','yellow','green','blue','indigo','violet']
    for colorindex in range (0,7):
        t.pendown()
        t.pensize(thickness)
        t.color(colors[colorindex%7])
        t.circle(-(radius-colorindex*thickness),180)
        t.penup()
        t.right(90)
        t.forward(2*radius+thickness-2*(colorindex+1)*thickness)
        t.right(90)

rainbow(400)
t.hideturtle()
