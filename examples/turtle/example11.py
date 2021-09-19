# Sound
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

turtle = Turtle()

# play sound and wait until done
turtle.sound_until_done("siren")

# random beep: 3 times
turtle.sound_until_done("random beep", 3)

turtle.sound_until_done("dibidibidip")