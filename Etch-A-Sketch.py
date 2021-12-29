from turtle import Screen, Turtle, backward
from turtle import Screen, Turtle

def forward():
    tim.forward(10)
def backward():
    tim.backward(10)
def Counter_Clockwise():
    tim.left(10)
def Clockwise():
    tim.right(10)
def Clear_Drawing():    
    tim.clear()    
def home():
    tim.hideturtle()
    tim.penup()
    tim.home() 
    tim.pendown()   
    tim.showturtle()

tim = Turtle()
screen = Screen()

    
screen.listen()
screen.onkey(key = "w", fun = forward)
screen.onkey(key = "s", fun = backward)
screen.onkey(key = "a", fun = Counter_Clockwise)
screen.onkey(key = "d", fun = Clockwise)
screen.onkey(key = "c", fun = Clear_Drawing)
screen.onkey(key = "h", fun = home)
screen.exitonclick()


