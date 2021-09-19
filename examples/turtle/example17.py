# Color Detector
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

turtle = Turtle()

# wait while the color is not red
while not turtle.is_color("red"):
    wait(10) # 10 msec

turtle.sound("beep") # beep
turtle.wheels(-50, -50) # move backward

# wait while the color is not blue
while not turtle.is_color("blue"):
    wait(10) # 10 msec

turtle.stop() # stop