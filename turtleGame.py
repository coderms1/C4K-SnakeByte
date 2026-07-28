import turtle

player = turtle.Turtle()

def moveForward():
    player.forward(20)

def turnLeft():
    player.left(30)

def turnRight():
    player.right(30)

screen = turtle.Screen()

screen.onkey(moveForward, "Up")
screen.onkey(turnLeft, "Left")
screen.onkey(turnRight, "Right")

screen.listen()

turtle.done()
