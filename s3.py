import turtle

window = turtle.Screen()
# window.register_shape("t1", ((5,-3),(0,5),(-5,-3)))
window.register_shape("strawberry.gif")
pen = turtle.Turtle()
# pen.shape("t1") # 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
pen.shape("strawberry.gif")
pen.pencolor("green")

pen.pensize(3)
COLORS = ["green", "black", "purple", "cyan"]
for j in range(4):
    pen.fillcolor(COLORS[j])
    pen.begin_fill()
    for i in range(4):
        pen.forward(100)
        pen.stamp()
        pen.left(90)
    pen.end_fill()
    pen.right(90)
turtle.done()


# کشیدن مثلت توپر با رنگ قرمز
# کشیدن مربع توپر با رنگ قهوه ای
# کشیدن مستطیل توخالی با رنگ آبی
