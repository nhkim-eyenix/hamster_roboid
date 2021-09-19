# Melody
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

turtle = Turtle()

for i in range(2):
    for j in range(2):
        turtle.note("C4", 0.5)
        turtle.note("E4", 0.5)
        turtle.note("G4", 0.5)

    for j in range(3):
        turtle.note("A4", 0.5)

    turtle.note("G4", 1)
    turtle.note("off", 0.5)

    for j in range(3):
        turtle.note("F4", 0.5)

    for j in range(3):
        turtle.note("E4", 0.5)

    for j in range(3):
        turtle.note("D4", 0.5)

    turtle.note("C4", 1)
    turtle.note("off", 0.5)

    turtle.tempo(120) # speed up