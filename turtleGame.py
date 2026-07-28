import turtle

funkyT = turtle.Turtle()
screen = turtle.Screen()

def moveForward():
    funkyT.forward(50)
def turnLeft():
    funkyT.left(90)
def turnRight():
    funkyT.right(90)
def makeCircle():
    funkyT.circle(100)

screen.onkey(moveForward, "Up")
screen.onkey(turnLeft, "Left")
screen.onkey(turnRight, "Right")
screen.onkey(makeCircle, "Down")
screen.listen()
turtle.done()
