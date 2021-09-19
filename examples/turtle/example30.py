# Multiple When-Do Color Detector
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# Ctrl + C to terminate

from roboid import *

turtles = (Turtle(), Turtle(), Turtle(), Turtle())

# wait until four robots are ready
wait_until_ready()

# when the color is red
def check_red(robot):
    return robot.is_color("red")

# move backward 6 cm
def move_backward(robot):
    robot.sound("beep")
    robot.move_backward()

for turtle in turtles:
    when_do(check_red, move_backward, turtle)

wait(-1) # wait forever