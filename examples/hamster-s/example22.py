# Extension - Voltage
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# This example requires a Hamster's extension kit
# Ctrl + C to terminate

from roboid import *

hamster = HamsterS()

# set a port A to the servo output mode
hamster.io_mode_a("voltage input")

while True:
    print(hamster.input_a(), hamster.voltage_a())