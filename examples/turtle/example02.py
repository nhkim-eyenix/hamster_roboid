# Basic Movement
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

turtle = Turtle()

# pivot around left wheel 90/-90 degrees with default velocity(50%)
turtle.pivot_left(90)
turtle.pivot_left(-90)

# pivot around right wheel 90/-90 degrees with default velocity(50%)
turtle.pivot_right(90)
turtle.pivot_right(-90)

# pivot around left wheel 90/-90 degrees with 100% velocity
turtle.pivot_left(90, 100)
turtle.pivot_left(-90, 100)

# pivot around right wheel 90/-90 degrees with 100% velocity
turtle.pivot_right(90, 100)
turtle.pivot_right(-90, 100)

# pivot around left wheel 90 degrees with 100/-100% velocity
turtle.pivot_left(90, 100)
turtle.pivot_left(90, -100)

# pivot around right wheel 90 degrees with 100/-100% velocity
turtle.pivot_right(90, 100)
turtle.pivot_right(90, -100)

# pivot around left/right wheel for 2 seconds with default velocity(50%)
turtle.pivot_left_sec(2)
turtle.pivot_right_sec(2)

# pivot around left wheel for 1.5 seconds with 60/-60% velocity
turtle.pivot_left_sec(1.5, 60)
turtle.pivot_left_sec(1.5, -60)

# pivot around right wheel for 1.5 seconds with 60/-60% velocity
turtle.pivot_right_sec(1.5, 60)
turtle.pivot_right_sec(1.5, -60)

# pivot around left wheel for 1.5 seconds with 60/-60% velocity
turtle.wheels(0, 60)
wait(1500)
turtle.wheels(0, -60)
wait(1500)

# pivot around right wheel for 1.5 seconds with 60/-60% velocity
turtle.wheels(60, 0)
wait(1500)
turtle.wheels(-60, 0)
wait(1500)

# stop
turtle.stop()