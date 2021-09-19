# Parallel
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

turtle = Turtle()

# melody
def play_melody():
    for i in range(2):
        turtle.note("C4", 0.5)
        turtle.note("E4", 0.5)
        turtle.note("G4", 0.5)

    for i in range(3):
        turtle.note("A4", 0.5)

    turtle.note("G4", 1)
    turtle.note("off", 0.5)

# blink
def play_blink():
    for i in range(5):
        turtle.led("red")
        wait(500)
        turtle.led("off")
        wait(500)

# move
def play_move():
    turtle.move_forward()
    turtle.move_backward()
    turtle.turn_left()
    turtle.turn_right()

parallel(play_melody, play_blink, play_move)