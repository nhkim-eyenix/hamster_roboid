# Keyboard Controller
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# Ctrl + C to terminate

from roboid import *

turtle = Turtle()

while True:
    key = Keyboard.read()
    if key:
        if key == Keyboard.UP:
            turtle.wheels(50, 50) # move forward
        elif key == Keyboard.DOWN:
            turtle.wheels(-50, -50) # move backward
        elif key == Keyboard.LEFT:
            turtle.wheels(-50, 50) # turn left
        elif key == Keyboard.RIGHT:
            turtle.wheels(50, -50) # turn right
        elif key == " ":
            turtle.stop() # stop
    wait(10) # 10 msec