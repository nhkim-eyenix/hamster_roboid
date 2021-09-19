# Dual Theremin Sound
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# Ctrl + C to terminate

from roboid import *

turtle1 = Turtle()
turtle2 = Turtle()

# wait until two robots are ready
wait_until_ready()

hz1 = 0
hz2 = 0
while True:
    floor = turtle1.floor()
    if floor < 10:
        floor = 0
    hz1 = (hz1 * 5 + floor * 50) / 10.0
    turtle1.buzzer(hz1)

    floor = turtle2.floor()
    if floor < 10:
        floor = 0
    hz2 = (hz2 * 5 + floor * 50) / 10.0
    turtle2.buzzer(hz2)

    wait(20) # 20 msec