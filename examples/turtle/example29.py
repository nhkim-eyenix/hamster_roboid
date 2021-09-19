# When-Do Color Detector
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# Ctrl + C to terminate

from roboid import *

turtle = Turtle()

# when the color is red
def check_red():
    return turtle.is_color("red")

# when the color is blue
def check_blue():
    return turtle.is_color("blue")

# move backward 6 cm
def move_backward():
    turtle.sound("beep")
    turtle.move_backward()

# move forward 6 cm
def move_forward():
    turtle.sound("beep")
    turtle.move_forward()

when_do(check_red, move_backward)
when_do(check_blue, move_forward)

wait(-1) # wait forever