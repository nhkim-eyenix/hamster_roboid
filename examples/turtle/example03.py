# Basic Movement
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

turtle = Turtle()

# turn left 90/-90 degrees with radius 6cm with default velocity(50%)
turtle.circle_left(90, 6)
turtle.circle_left(-90, 6)

# turn right 90/-90 degrees with radius 6cm with default velocity(50%)
turtle.circle_right(90, 6)
turtle.circle_right(-90, 6)

# turn left 90/-90 degrees with radius 6cm with 100% velocity
turtle.circle_left(90, 6, 100)
turtle.circle_left(-90, 6, 100)

# turn right 90/-90 degrees with radius 6cm with 100% velocity
turtle.circle_right(90, 6, 100)
turtle.circle_right(-90, 6, 100)

# turn left 90 degrees with radius 6cm with 100/-100% velocity
turtle.circle_left(90, 6, 100)
turtle.circle_left(90, 6, -100)

# turn right 90 degrees with radius 6cm with 100/-100% velocity
turtle.circle_right(90, 6, 100)
turtle.circle_right(90, 6, -100)

# turn left/right for 2 seconds with radius 6cm with default velocity(50%)
turtle.circle_left_sec(2, 6)
turtle.circle_right_sec(2, 6)

# turn left for 1.5 seconds with radius 6cm with 60/-60% velocity
turtle.circle_left_sec(1.5, 6, 60)
turtle.circle_left_sec(1.5, 6, -60)

# turn left for 1.5 seconds with radius 6cm with 60/-60% velocity
turtle.circle_right_sec(1.5, 6, 60)
turtle.circle_right_sec(1.5, 6, -60)