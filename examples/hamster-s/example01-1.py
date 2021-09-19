# Basic Movement
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

hamster = HamsterS()

# move forward/backward 5 cm, turn left/right 90 degrees with default velocity(30%)
hamster.move_forward()
hamster.move_backward()
hamster.turn_left()
hamster.turn_right()

# move forward/backward 3 cm, turn left/right 45 degrees with default velocity(30%)
hamster.move_forward(3)
hamster.move_backward(3)
hamster.turn_left(45)
hamster.turn_right(45)

# move forward/backward 3.5 cm, # turn left/right 50.5 degrees with 60% velocity
hamster.move_forward(3.5, 60)
hamster.move_backward(3.5, 60)
hamster.turn_left(50.5, 60)
hamster.turn_right(50.5, 60)

# move forward/backward, turn left/right for 2 seconds with default velocity(30%)
hamster.move_forward_sec(2)
hamster.move_backward_sec(2)
hamster.turn_left_sec(2)
hamster.turn_right_sec(2)

# move forward/backward, turn left/right for 1.5 seconds with 60% velocity
hamster.move_forward_sec(1.5, 60)
hamster.move_backward_sec(1.5, 60)
hamster.turn_left_sec(1.5, 60)
hamster.turn_right_sec(1.5, 60)

# move forward/backward, turn left/right for 1.5 seconds with 60% velocity
hamster.wheels(60, 60)
wait(1500)
hamster.wheels(-60, -60)
wait(1500)
hamster.wheels(-60, 60)
wait(1500)
hamster.wheels(60, -60)
wait(1500)

# stop
hamster.stop()