# Basic Movement
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

hamster = HamsterS()

# pivot around left wheel 90/-90 degrees with default velocity(30%)
hamster.pivot_left_wheel(90)
hamster.pivot_left_wheel(-90)

# pivot around right wheel 90/-90 degrees with default velocity(30%)
hamster.pivot_right_wheel(90)
hamster.pivot_right_wheel(-90)

# pivot around left wheel 90/-90 degrees with 60% velocity
hamster.pivot_left_wheel(90, 60)
hamster.pivot_left_wheel(-90, 60)

# pivot around right wheel 90/-90 degrees with 60% velocity
hamster.pivot_right_wheel(90, 60)
hamster.pivot_right_wheel(-90, 60)

# pivot around left wheel 90 degrees with 60/-60% velocity
hamster.pivot_left_wheel(90, 60)
hamster.pivot_left_wheel(90, -60)

# pivot around right wheel 90 degrees with 60/-60% velocity
hamster.pivot_right_wheel(90, 60)
hamster.pivot_right_wheel(90, -60)

# pivot around left/right wheel for 2 seconds with default velocity(30%)
hamster.pivot_left_wheel_sec(2)
hamster.pivot_right_wheel_sec(2)

# pivot around left wheel for 1.5 seconds with 60/-60% velocity
hamster.pivot_left_wheel_sec(1.5, 60)
hamster.pivot_left_wheel_sec(1.5, -60)

# pivot around right wheel for 1.5 seconds with 60/-60% velocity
hamster.pivot_right_wheel_sec(1.5, 60)
hamster.pivot_right_wheel_sec(1.5, -60)

# pivot around left wheel for 1.5 seconds with 60/-60% velocity
hamster.wheels(0, 60)
wait(1500)
hamster.wheels(0, -60)
wait(1500)

# pivot around right wheel for 1.5 seconds with 60/-60% velocity
hamster.wheels(60, 0)
wait(1500)
hamster.wheels(-60, 0)
wait(1500)

# stop
hamster.stop()