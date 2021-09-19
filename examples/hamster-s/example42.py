# Serial
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

hamster1 = HamsterS()
hamster2 = HamsterS()

def read():
    while True:
        print(hamster2.read_serial(","))

def write():
    for _ in range(10):
        wait(500)
        hamster1.write_serial("a,")
        wait(500)
        hamster1.write_serial("b,")

wait_until_ready()
parallel(read, write)

wait(-1) # wait forever