from machine import Pin
import time
from rotary_irq_rp2 import RotaryIRQ
from General_N20_Driving import Robot

rbt = Robot()
rbt.stop()

r = RotaryIRQ(pin_num_clk = 6,
              pin_num_dt = 7,
              min_val = 0,
              reverse = False,
              range_mode = RotaryIRQ.RANGE_UNBOUNDED)

val_old = r.value()
while True:
    val_new = r.value()

    if val_old != val_new:
        val_old = val_new
        print('result =', val_new)

    time.sleep_ms(5)
