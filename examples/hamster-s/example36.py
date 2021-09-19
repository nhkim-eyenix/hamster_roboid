# Gripper
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

hamster = HamsterS()

hamster.open_gripper()
hamster.close_gripper()

# turn off the power of a gripper
hamster.release_gripper()