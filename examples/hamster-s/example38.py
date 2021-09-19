# When-Do Hand Detector
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# Ctrl + C to terminate

from roboid import *

hamster = HamsterS()

# when hand found
def condition():
    return hamster.left_proximity() > 30 or hamster.right_proximity() > 30

# move backward 5 cm with beep sound
def move():
    hamster.sound("beep")
    hamster.move_backward()

when_do(condition, move)

wait(-1) # wait forever