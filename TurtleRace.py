from turtle import Turtle, Screen

width = 500
height = 400
xpoint = -230
ypoint = -100
colors =  ["red","orange", "yellow","green", "blue","purple"]
increase = 0


screen = Screen()
screen.setup(width = width, height = height)
user_bet = screen.textinput( title = "Make your bet", prompt= "Which Turtle will in the race? Enter a color: ")

for color in colors:
    _ = Turtle(shape = "turtle")
    _.color(color)
    _.penup()
    _.goto(x = xpoint, y = ypoint+increase)
    increase += 50
screen.exitonclick()