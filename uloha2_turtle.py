import turtle as t
def kresba(size, x=10):
    t.shape("turtle")
    t.colormode(255)
    t.color(102, 153, 153)
    t.penup()
    t.goto(-size/2, size/10 * x) # kde x je celkový počet malých čar / 2
    t.pendown()
    for i in range(x):
        t.forward(size)
        t.right(90)
        t.forward(size/10)
        t.right(90)
        t.forward(size)
        t.left(90)
        t.forward(size/10)
        t.left(90)
    t.forward(size)
