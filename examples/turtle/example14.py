# Theremin Sound
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# Ctrl + C to terminate

from roboid import *

turtle = Turtle()

hz = 0
while True:
    floor = turtle.floor()
    if floor < 10:
        floor = 0
    hz = (hz * 5 + floor * 50) / 10.0
    turtle.buzzer(hz)

    wait(20) # 20 msec