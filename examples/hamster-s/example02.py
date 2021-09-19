# Simple Movement
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# Ctrl + C to terminate

from roboid import *

hamster = HamsterS()

while True:
    hamster.move_forward()
    hamster.move_backward()
    hamster.turn_left()