# Advanced Color Pattern Detector
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

turtle = Turtle()

# user-defined function
def check_backward():
    return turtle.is_color_pattern("purple", "red")

# wait until the color pattern is (purple, red)
wait_until(check_backward)

turtle.sound("beep") # beep
turtle.move_backward() # move backward