# Basic Movement
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

hamster = HamsterS()

# pivot around left pen 90/-90 degrees with default velocity(30%)
hamster.pivot_left_pen(90)
hamster.pivot_left_pen(-90)

# pivot around right pen 90/-90 degrees with default velocity(30%)
hamster.pivot_right_pen(90)
hamster.pivot_right_pen(-90)

# pivot around left pen 90/-90 degrees with 60% velocity
hamster.pivot_left_pen(90, 60)
hamster.pivot_left_pen(-90, 60)

# pivot around right pen 90/-90 degrees with 60% velocity
hamster.pivot_right_pen(90, 60)
hamster.pivot_right_pen(-90, 60)

# pivot around left pen 90 degrees with 60/-60% velocity
hamster.pivot_left_pen(90, 60)
hamster.pivot_left_pen(90, -60)

# pivot around right pen 90 degrees with 60/-60% velocity
hamster.pivot_right_pen(90, 60)
hamster.pivot_right_pen(90, -60)

# pivot around left/right pen for 2 seconds with default velocity(30%)
hamster.pivot_left_pen_sec(2)
hamster.pivot_right_pen_sec(2)

# pivot around left pen for 1.5 seconds with 60/-60% velocity
hamster.pivot_left_pen_sec(1.5, 60)
hamster.pivot_left_pen_sec(1.5, -60)

# pivot around right pen for 1.5 seconds with 60/-60% velocity
hamster.pivot_right_pen_sec(1.5, 60)
hamster.pivot_right_pen_sec(1.5, -60)