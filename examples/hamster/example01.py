# Basic Movement
# author: Kwang-Hyun Park (akaii@kw.ac.kr)
import sys
sys.path.append("/home/kyle/다운로드/hamster_driver/roboid-python3.7-v1.5.2/dist/roboid-1.5.2")
from roboid import *

hamster = Hamster()

# move forward/backward, turn left/right for 1 second with default velocity(30%)
hamster.move_forward()
hamster.move_backward()
hamster.turn_left()
hamster.turn_right()

# move forward/backward, turn left/right for 2 seconds with default velocity(30%)
hamster.move_forward(2) # 앞으로 움직이다
hamster.move_backward(2) # 뒤
hamster.turn_left(2) # 왼쪽
hamster.turn_right(2) # 오른쪽

# move forward/backward, turn left/right for 1.5 seconds with 60% velocity
hamster.move_forward(1.5, 60)
hamster.move_backward(1.5, 60)
hamster.turn_left(1.5, 60)
hamster.turn_right(1.5, 60)

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