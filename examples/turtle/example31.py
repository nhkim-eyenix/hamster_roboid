# Advanced Multiple Color Pattern Detector
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

turtle1 = Turtle()
turtle2 = Turtle()

# user-defined function
def check_backward(robot):
    return robot.is_color_pattern("purple", "red")

# wait until the color pattern is (purple, red)
wait_until(check_backward, turtle1)

turtle1.sound("beep") # beep
turtle1.move_backward() # move backward

# wait until the color pattern is (purple, red)
wait_until(check_backward, turtle2)

turtle2.sound("beep") # beep
turtle2.move_backward() # move backward