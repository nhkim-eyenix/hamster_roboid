# Basic Movement
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

hamster = HamsterS()

# left pen draws 90/-90 degrees of circle on the left with radius 5cm with default velocity(30%)
hamster.left_pen_circle_left(90, 5)
hamster.left_pen_circle_left(-90, 5)

# left pen draws 90/-90 degrees of circle on the right with radius 5cm with default velocity(30%)
hamster.left_pen_circle_right(90, 5)
hamster.left_pen_circle_right(-90, 5)

# right pen draws 90/-90 degrees of circle on the left with radius 5cm with default velocity(30%)
hamster.right_pen_circle_left(90, 5)
hamster.right_pen_circle_left(-90, 5)

# right pen draws 90/-90 degrees of circle on the right with radius 5cm with default velocity(30%)
hamster.right_pen_circle_right(90, 5)
hamster.right_pen_circle_right(-90, 5)

# body turns left 90/-90 degrees with radius 5cm with default velocity(30%)
hamster.circle_left(90, 5)
hamster.circle_left(-90, 5)

# body turns right 90/-90 degrees with radius 5cm with default velocity(30%)
hamster.circle_right(90, 5)
hamster.circle_right(-90, 5)

# left pen draws 90/-90 degrees of circle on the left with radius 5cm with 60% velocity
hamster.left_pen_circle_left(90, 5, 60)
hamster.left_pen_circle_left(-90, 5, 60)

# left pen draws 90/-90 degrees of circle on the right with radius 5cm with 60% velocity
hamster.left_pen_circle_right(90, 5, 60)
hamster.left_pen_circle_right(-90, 5, 60)

# right pen draws 90/-90 degrees of circle on the left with radius 5cm with 60% velocity
hamster.right_pen_circle_left(90, 5, 60)
hamster.right_pen_circle_left(-90, 5, 60)

# right pen draws 90/-90 degrees of circle on the right with radius 5cm with 60% velocity
hamster.right_pen_circle_right(90, 5, 60)
hamster.right_pen_circle_right(-90, 5, 60)

# body turns left 90/-90 degrees with radius 5cm with 60% velocity
hamster.circle_left(90, 5, 60)
hamster.circle_left(-90, 5, 60)

# body turns right 90/-90 degrees with radius 5cm with 60% velocity
hamster.circle_right(90, 5, 60)
hamster.circle_right(-90, 5, 60)

# left pen draws circle on the left/right for 2 seconds with radius 5cm with default velocity(30%)
hamster.left_pen_circle_left_sec(2, 5)
hamster.left_pen_circle_right_sec(2, 5)

# left pen draws circle on the left/right for 2 seconds with radius 5cm with default velocity(30%)
hamster.right_pen_circle_left_sec(2, 5)
hamster.right_pen_circle_right_sec(2, 5)

# body turns left/right for 2 seconds with radius 5cm with default velocity(30%)
hamster.circle_left_sec(2, 5)
hamster.circle_right_sec(2, 5)

# left pen draws circle on the left/right for 2 seconds with radius 5cm with 60% velocity
hamster.left_pen_circle_left_sec(2, 5, 60)
hamster.left_pen_circle_right_sec(2, 5, 60)

# left pen draws circle on the left/right for 2 seconds with radius 5cm with 60% velocity
hamster.right_pen_circle_left_sec(2, 5, 60)
hamster.right_pen_circle_right_sec(2, 5, 60)

# body turns left/right for 2 seconds with radius 5cm with 60% velocity
hamster.circle_left_sec(2, 5, 60)
hamster.circle_right_sec(2, 5, 60)