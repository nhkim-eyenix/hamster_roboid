# Color Pattern Detector
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

turtle = Turtle()

# wait while the color pattern is not (purple, red)
while not turtle.is_color_pattern("purple", "red"):
    wait(10) # 10 msec

turtle.sound("beep") # beep
turtle.move_backward() # move backward