# Mutiple Simple Movement
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# Ctrl + C to terminate

from roboid import *

turtles = (Turtle(), Turtle(), Turtle(), Turtle())

# wait until four robots are ready
wait_until_ready()

while True:
    # move forward
    for turtle in turtles:
        turtle.wheels(50, 50)

    wait(500) # 0.5 seconds

    # move backward
    for turtle in turtles:
        turtle.wheels(-50, -50)

    wait(500) # 0.5 seconds

    # turn left
    for turtle in turtles:
        turtle.wheels(-50, 50)

    wait(500) # 0.5 seconds