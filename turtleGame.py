import turtle

player = turtle.Turtle()

def moveForward():
    player.forward(20)
def moveLeft():
    player.left(30)
def moveRight():
    player.right(30)

screen = turtle.Screen()

screen.onkey(moveForward, "Up")
screen.onkey(moveLeft, "left")
screen.onkey(moveRight, "right")

screen.listen()

turtle.done()
