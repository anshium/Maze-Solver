from machine import Pin, PWM
from time import sleep

mtr1_1 = PWM(Pin(18))
mtr1_2 = PWM(Pin(19))

mtr1_1.freq(1000)
mtr1_2.freq(1000)

# 0 to 65025

mtr1_1.duty_u16(0)
mtr1_2.duty_u16(0)

import time
from rotary_irq_rp2 import RotaryIRQ

r = RotaryIRQ(pin_num_clk = 6,
              pin_num_dt = 7,
              min_val = 0,
              reverse = False,
              range_mode = RotaryIRQ.RANGE_UNBOUNDED)

val_old = r.value()
count = 0
while True:
    val_new = r.value()

    if val_old != val_new:
        val_old = val_new
#         print('result =', val_new)
    if(val_new > 5000):
        print(count)
    else:
        count += 5
    time.sleep_ms(5)
