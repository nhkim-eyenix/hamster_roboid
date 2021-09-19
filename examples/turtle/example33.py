# Multiple When-Do Color Pattern Detector
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# Ctrl + C to terminate

from roboid import *

turtles = (Turtle(), Turtle(), Turtle(), Turtle())

# when the color pattern is (purple, red)
def check_backward(robot):
    return robot.is_color_pattern("purple", "red")

# move backward 6 cm
def move_backward(robot):
    robot.sound("beep")
    robot.move_backward()

for turtle in turtles:
    when_do(check_backward, move_backward, turtle)

wait(-1) # wait forever