# Hand Detector
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

hamster = HamsterS()

# wait while the value of the left proximity is less than 30
while hamster.left_proximity() < 30:
    wait(10) # 10 msec

# move backward 5 cm with beep sound
hamster.sound("beep")
hamster.move_backward() 