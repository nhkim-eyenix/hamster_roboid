# Staggering Walk
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# Ctrl + C to terminate

from roboid import *

turtle = Turtle()

while True:
    turtle.wheels(-100, -100) # move backward
    acc = turtle.acceleration_x()
    if acc > 2000 or acc < -2000:
        turtle.wheels(100, 100) # move forward
        wait(250) # 0.25 seconds

        turtle.wheels(-50, 50) # turn left
        wait(500) # 0.5 seconds
    wait(10) # 10 msec