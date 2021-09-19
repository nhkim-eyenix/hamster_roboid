# Advanced Multiple Color Detector
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

turtle1 = Turtle()
turtle2 = Turtle()

# user-defined function
def check_red(robot):
    return robot.is_color("red")

# wait until the color is red
wait_until(check_red, turtle1)

turtle1.sound("beep") # beep
turtle1.move_backward() # move backward

# wait until the color is red
wait_until(check_red, turtle2)

turtle2.sound("beep") # beep
turtle2.move_backward() # move backward