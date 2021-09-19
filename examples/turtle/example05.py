# Acceleration
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

turtle = Turtle()

# acceleration
for i in range(100):
    turtle.wheels(i, i)
    wait(20) # 20 msec

# 0.5 seconds
wait(500)

# deceleration
for i in range(100, 0, -1):
    turtle.wheels(i, i)
    wait(20) # 20 msec

turtle.stop()