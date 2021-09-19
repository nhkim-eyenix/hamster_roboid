# Builtin Line Tracer
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

hamster = HamsterS()

hamster.line_left()
wait(5000) # 5 seconds

hamster.line_speed(8) # speed up
wait(5000) # 5 seconds

hamster.line_right()
wait(5000) # 5 seconds

hamster.line_speed(5) # speed down
wait(5000) # 5 seconds

hamster.line_both()
wait(5000) # 5 seconds

hamster.stop() # stop