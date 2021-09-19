# Multiple When-Do Hand Detector
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# Ctrl + C to terminate

from roboid import *

hamsters = (HamsterS(), HamsterS(), HamsterS(), HamsterS())

# wait until four robots are ready
wait_until_ready()

# when hand found
def condition(robot):
    return robot.left_proximity() > 30 or robot.right_proximity() > 30

# move backward 5 cm with beep sound
def move(robot):
    robot.sound("beep")
    robot.move_backward()

for hamster in hamsters:
    when_do(condition, move, hamster)

wait(-1) # wait forever