# When-Do Color Pattern Detector
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# Ctrl + C to terminate

from roboid import *

turtle = Turtle()

# when the color pattern is (purple, red)
def check_backward():
    return turtle.is_color_pattern("purple", "red")

# when the color pattern is (purple, blue)
def check_forward():
    return turtle.is_color_pattern("purple", "blue")

# move backward 6 cm
def move_backward():
    turtle.sound("beep")
    turtle.move_backward()

# move forward 6 cm
def move_forward():
    turtle.sound("beep")
    turtle.move_forward()

when_do(check_backward, move_backward)
when_do(check_forward, move_forward)

wait(-1) # wait forever