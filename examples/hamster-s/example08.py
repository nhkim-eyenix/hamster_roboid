# Melody
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

hamster = HamsterS()

# play sound and wait until done
hamster.sound_until_done("siren")

# random beep: 3 times
hamster.sound_until_done("random beep", 3)

hamster.sound_until_done("dibidibidip")