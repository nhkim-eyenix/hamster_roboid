# Advanced Hand Detector
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

hamster = HamsterS()

# user-defined function
def check():
    return hamster.left_proximity() > 30

# wait until the value of the left proximity is greater than 30
wait_until(check)

# move backward 5 cm with beep sound
hamster.sound("beep")
hamster.move_backward()