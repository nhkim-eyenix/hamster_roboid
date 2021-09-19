# Builtin Line Tracer
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

turtle = Turtle()

# follow black line
turtle.black_line()
wait(5000) # 5 seconds

turtle.line_speed(8) # speed up
wait(2000) # 5 seconds

turtle.line_speed(5) # speed down
wait(2000) # 5 seconds

# follow red line
turtle.red_line()
wait(5000) # 5 seconds

# follow green line
turtle.green_line()
wait(5000) # 5 seconds

# follow blue line
turtle.blue_line()
wait(5000) # 5 seconds

# follow any line
turtle.any_line()
wait(5000) # 5 seconds

turtle.stop() # stop