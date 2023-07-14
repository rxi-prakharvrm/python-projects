from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

def create_snake():
  for i in range(3):
    timmy = Turtle("square")
    timmy.color("white")
    timmy.penup()
    timmy.goto(starting_positions[i])

# def move_snake():
#   for _ in range(10):
#     timmy.forward()


create_snake()

screen.exitonclick()