from machine import Pin

mtr1_1 = Pin(18, Pin.OUT)
mtr1_2 = Pin(19, Pin.OUT)
mtr2_1 = Pin(20, Pin.OUT)
mtr2_2 = Pin(21, Pin.OUT)

class Robot:
    def __init__(self):
        mtr1_1.low()
        mtr1_2.low()
        mtr2_1.low()
        mtr2_2.low()

    def fwd(self):
        mtr1_1.high()
        mtr1_2.low()
        mtr2_1.high()
        mtr2_2.low()

    def bwd(self):
        mtr1_2.high()
        mtr1_1.low()
        mtr2_2.high()
        mtr2_1.low()
        
    def left(self):
        mtr1_1.high()
        mtr1_2.low()
        mtr2_2.high()
        mtr2_1.low()

    def right(self):
        mtr1_2.high()
        mtr1_1.low()
        mtr2_1.high()
        mtr2_2.low()
        
    def stop(self):
        mtr1_2.low()
        mtr1_1.low()
        mtr2_1.low()
        mtr2_2.low()

r = Robot()
r.fwd()
