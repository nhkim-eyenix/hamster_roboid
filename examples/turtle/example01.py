# Basic Movement
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

turtle = Turtle()

# move forward/backward 6 cm, turn left/right 90 degrees with default velocity(50%)
turtle.move_forward()
turtle.move_backward()
turtle.turn_left()
turtle.turn_right()

# move forward/backward 3 cm, turn left/right 45 degrees with default velocity(50%)
turtle.move_forward(3)
turtle.move_backward(3)
turtle.turn_left(45)
turtle.turn_right(45)

# move forward/backward 3.5 cm, turn left/right 50.5 degrees with 100% velocity
turtle.move_forward(3.5, 100)
turtle.move_backward(3.5, 100)
turtle.turn_left(50.5, 100)
turtle.turn_right(50.5, 100)

# move forward/backward, turn left/right for 2 seconds with default velocity(50%)
turtle.move_forward_sec(2)
turtle.move_backward_sec(2)
turtle.turn_left_sec(2)
turtle.turn_right_sec(2)

# move forward/backward, turn left/right for 1.5 seconds with 60% velocity
turtle.move_forward_sec(1.5, 60)
turtle.move_backward_sec(1.5, 60)
turtle.turn_left_sec(1.5, 60)
turtle.turn_right_sec(1.5, 60)

# move forward/backward, turn left/right for 1.5 seconds with 60% velocity
turtle.wheels(60, 60)
wait(1500)
turtle.wheels(-60, -60)
wait(1500)
turtle.wheels(-60, 60)
wait(1500)
turtle.wheels(60, -60)
wait(1500)

# stop
turtle.stop()