# Parallel
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

hamster = HamsterS()

# melody
def play_melody():
    for i in range(2):
        hamster.note("C4", 0.5)
        hamster.note("E4", 0.5)
        hamster.note("G4", 0.5)

    for i in range(3):
        hamster.note("A4", 0.5)

    hamster.note("G4", 1)
    hamster.note("off", 0.5)

# blink
def play_blink():
    for i in range(5):
        hamster.leds("red")
        wait(500)
        hamster.leds("off")
        wait(500)

# move
def play_move():
    hamster.move_forward()
    hamster.move_backward()
    hamster.turn_left()
    hamster.turn_right()

parallel(play_melody, play_blink, play_move)