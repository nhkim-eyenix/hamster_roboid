# Led
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

hamster = HamsterS()

hamster.rgbs(255, 0, 0, 0, 255, 0) # left: red and right: green
wait(500) # 0.5 seconds

hamster.rgbs(0, 0, 255) # both: blue
wait(500) # 0.5 seconds

hamster.left_rgb(255, 63, 0) # left: orange
wait(500) # 0.5 seconds

hamster.right_rgb(0, 255, 255) # right: sky blue
wait(500) # 0.5 seconds

hamster.leds("red", "green") # turn on both LEDs
wait(500) # 0.5 seconds

hamster.left_led("off") # turn off left LED
wait(500) # 0.5 seconds

hamster.left_led("blue") # turn on left LED
wait(500) # 0.5 seconds

hamster.right_led("off") # turn off right LED
wait(500) # 0.5 seconds

hamster.right_led("yellow") # turn on right LED
wait(500) # 0.5 seconds

hamster.leds("off") # turn off both LEDs