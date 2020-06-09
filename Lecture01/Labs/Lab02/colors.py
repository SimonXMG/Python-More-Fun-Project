import turtle

turtle.bgcolor("black")
tony = turtle.Pen()
tony.width(3)
for i in range(100):
    tony.pencolor("yellow")
    tony.forward(i * 4)
    tony.right(96)
    tony.pencolor("blue")
    tony.forward(i * 4)
    tony.right(96)