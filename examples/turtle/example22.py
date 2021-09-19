# Advanced Theremin Sound
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

turtle = Turtle()
hz = 0

def execute():
    global hz
    
    floor = turtle.floor()
    if floor < 10:
        floor = 0
    hz = (hz * 5 + floor * 50) / 10.0
    turtle.buzzer(hz)

# set a periodic (20 msec) callback
set_executable(execute)

wait(-1) # wait forever