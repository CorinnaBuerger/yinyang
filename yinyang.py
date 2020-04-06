from turtle import circle, begin_fill, end_fill, dot, left, right, fillcolor, pencolor, pensize, shape, shapesize, speed, fd, penup, pendown, hideturtle, home

def jump(distance, angle):
    penup()
    left(angle)
    fd(distance)
    left(-angle)
    pendown()

def yin(diameter, color_1, color_2):
    radius = diameter / 2
    radius_2 = radius / 2
    dot_dia = radius_2 / 2
    fillcolor(color_1)
    pencolor("black")
    pensize(5)
    shape("turtle")
    shapesize(2)
    speed(10)

    left(90)
    begin_fill()
    circle(radius_2, 180)
    circle(radius, 180)
    left(180)
    circle(-radius_2, 180)
    end_fill()

    jump(radius_2, 90)
    dot(dot_dia, color_2)
    jump(radius_2, 270)

def yinyang(diameter, color_1, color_2):
    yin(diameter, color_1, color_2)
    home()
    left(180)
    yin(diameter, color_2, color_1)
    hideturtle()

if __name__ == "__main__":
    yinyang(400, "white", "black")    