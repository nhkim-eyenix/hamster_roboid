# Melody
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

hamster = HamsterS()

# play sound 2 times
hamster.sound("beep", 2)
wait(500)

hamster.sound("random beep")
wait(500)

hamster.sound("siren")
wait(500)

hamster.sound("engine")
wait(500)

hamster.sound("robot")
wait(500)