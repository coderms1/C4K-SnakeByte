import turtle

screen = turtle.Screen()
screen.register_shape("funkyT.gif")

funkyT = turtle.Turtle()
funkyT.shape("funkyT.gif")

def moveForward():
    funkyT.forward(20)

def turnLeft():
    funkyT.left(30)

def turnRight():
    funkyT.right(30)

screen.onkey(moveForward, "Up")
screen.onkey(turnLeft, "Left")
screen.onkey(turnRight, "Right")

screen.listen()
turtle.done()
