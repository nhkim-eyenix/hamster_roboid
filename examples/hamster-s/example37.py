# Advanced Multiple Hand Detector
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

hamster1 = HamsterS()
hamster2 = HamsterS()

# user-defined function
def check(robot):
    return robot.left_proximity() > 30

# wait until the value of the left proximity is greater than 30
wait_until(check, hamster1)

# move backward 5 cm with beep sound
hamster1.sound("beep")
hamster1.move_backward()

# wait until the value of the left proximity is greater than 30
wait_until(check, hamster2)

# move backward 5 cm with beep sound
hamster2.sound("beep")
hamster2.move_backward()