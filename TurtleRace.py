from turtle import Turtle, Screen
import random

width = 500
height = 400
xpoint = -230
ypoint = -100
colors =  ["red","orange", "yellow","green", "blue","purple"]
turtles = []
increase = 0


screen = Screen()
screen.setup(width = width, height = height)

for color in colors:
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x = xpoint, y = ypoint+increase)
    increase += 50
    turtles.append(new_turtle)
    
user_bet = screen.textinput( title = "Make your bet", prompt= "Which Turtle will in the race? Enter a color: ")

while user_bet:
    if user_bet.lower() in colors:
        is_race_on = True
        break
    else:
        user_bet = screen.textinput( title = "Wrong input", prompt= "Which Turtle will in the race? Enter a color: ")

while is_race_on:
    for turtle in turtles:
        steps = random.randint(0,10)
        turtle.forward(steps)
        if turtle.xcor() > 230:
            is_race_on = False
            result = turtle.pencolor()
            
print("The race is over!")
if result == user_bet:
    print(f"You won! The {result} turtle won!")
else:
    print(f"You lose! The {result} turtle Won!")    


screen.exitonclick()