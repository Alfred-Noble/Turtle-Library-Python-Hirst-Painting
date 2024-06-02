#  Drawing 10*10 dots
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
color_list = [(240, 240, 245), (223, 223, 228), (236, 236, 216), (140, 140, 207), (25, 25, 48), (26, 26, 159),
              (237, 237, 235), (209, 209, 111), (144, 144, 63), (230, 230, 93), (4, 4, 197)]


def random_color():
    random_color_need = random.choice(color_list)
    return random_color_need


a = 30
count_dot = 0


def draw_dot(size_gap):
    tim.hideturtle()
    global a,  count_dot
    for i in range(1, 11):
        for _ in range(10):
            tim.penup()
            tim.fd(size_gap)
            tim.pendown()
            tim.color(random_color())
            tim.dot(20)
            count_dot += 1
        tim.penup()
        tim.home()
        tim.left(90)
        tim.forward(a)
        tim.right(90)
        tim.pendown()
        a += 30
    tim.shape("turtle")
    print(count_dot)
    print(a)


draw_dot(50)

t.Screen()
t.exitonclick()
