# Dual Theremin Sound
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# Ctrl + C to terminate

from roboid import *

hamster1 = Hamster()
hamster2 = Hamster()

# wait until two robots are ready
wait_until_ready()

hz1 = 0
hz2 = 0
while True:
    proximity = hamster1.left_proximity()
    if proximity < 10:
        proximity = 0
    hz1 = (hz1 * 5 + proximity * 50) / 10.0
    hamster1.buzzer(hz1)

    proximity = hamster2.left_proximity()
    if proximity < 10:
        proximity = 0
    hz2 = (hz2 * 5 + proximity * 50) / 10.0
    hamster2.buzzer(hz2)

    wait(20) # 20 msec