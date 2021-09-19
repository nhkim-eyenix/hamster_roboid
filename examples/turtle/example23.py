# Advanced Color Detector
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

turtle = Turtle()

# user-defined function
def check_red():
    return turtle.is_color("red")

# user-defined function
def check_blue():
    return turtle.is_color("blue")

# wait until the color is red
wait_until(check_red)

turtle.sound("beep") # beep
turtle.wheels(-50, -50) # move backward

# wait until the color is blue
wait_until(check_blue)

turtle.stop() # stop