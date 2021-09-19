# Builtin Line Tracer Intersection
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

turtle = Turtle()

# follow black line until red
turtle.black_line_until_red()

# cross at intersection
turtle.cross_forward()

# follow black line until red
turtle.black_line_until_red()

# turn left at intersection
turtle.cross_left()

# follow black line until red
turtle.black_line_until_red()