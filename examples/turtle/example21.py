# Advanced Sensor
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

turtle = Turtle()

def execute():
    print("Signal Strength: ", turtle.signal_strength())
    print("Floor: ", turtle.floor())
    print("Acceleration: ", turtle.acceleration_x(), turtle.acceleration_y(), turtle.acceleration_z())
    print("Temperature: ", turtle.temperature())
    print("Button: ", turtle.button())
    print("Clicked: ", turtle.clicked())
    print("Double Clicked: ", turtle.double_clicked())
    print("Long Pressed: ", turtle.long_pressed())
    print("Color Number: ", turtle.color_number())
    print("Color Pattern: ", turtle.color_pattern())
    print("Tilt: ", turtle.tilt())
    print("Battery State: ", turtle.battery_state())
    print("")

# set a periodic (20 msec) callback
set_executable(execute)

wait(-1) # wait forever