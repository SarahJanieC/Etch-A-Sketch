from turtle import Turtle, Screen
# Application written in python that uses Turtle module that allows users to use keyboard controls to draw on GUI.
# W - forwards
# S - backwards
# A - counter-clockwise
# D - clockwise
# C - clear

t = Turtle()
screen = Screen()


def move_forwards():
    t.forward(10)

def move_backwards():
    t.backward(10)

def turn_left():
    new_heading = t.heading() + 10
    t.setheading(new_heading)

def turn_right():
    new_heading = t.heading() - 10
    t.setheading(new_heading)

def clear():
    t.reset()
    
screen.listen()
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="c", fun=clear)
screen.exitonclick()