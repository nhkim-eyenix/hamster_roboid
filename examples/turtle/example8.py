# Siren
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# Ctrl + C to terminate

from roboid import *

turtle = Turtle()

while True:
    for hz in range(500, 700, 10):
        turtle.buzzer(hz)
        wait(20) # 20 msec