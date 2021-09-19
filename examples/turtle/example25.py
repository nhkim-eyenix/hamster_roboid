# Advanced Dual Theremin Sound
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

turtle1 = Turtle()
turtle2 = Turtle()
hz1 = 0
hz2 = 0

# wait until two robots are ready
wait_until_ready()

def execute():
    global hz1
    global hz2

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

# set a periodic (20 msec) callback
set_executable(execute)

wait(-1) # wait forever