# Advanced Multiple Hand Follower
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

hamsters = (Hamster(), Hamster(), Hamster(), Hamster())

# wait until four robots are ready
wait_until_ready()

def execute():
    for hamster in hamsters:
        # left wheel
        proximity = hamster.left_proximity()
        if proximity > 15:
            hamster.left_wheel((40 - proximity) * 4)
        else:
            hamster.left_wheel(0)

        # right wheel
        proximity = hamster.right_proximity()
        if proximity > 15:
            hamster.right_wheel((40 - proximity) * 4)
        else:
            hamster.right_wheel(0)

# set a periodic (20 msec) callback
set_executable(execute)

wait(-1) # wait forever