from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def f():
    tim.forward(20)


def b():
    tim.backward(20)


def left():
    tim.left(20)


def right():
    tim.right(20)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(f, 'w')
screen.onkey(b, 's')
screen.onkey(left, 'a')
screen.onkey(right, 'd')
screen.onkey(clear, 'c')

screen.exitonclick()
