from machine import Pin, PWM
from time import sleep
import time
from rotary_irq_rp2 import RotaryIRQ

Pin(14, Pin.OUT).high()

mtr1_1 = Pin(18, Pin.OUT)
mtr1_2 = Pin(19, Pin.OUT)
mtr2_1 = Pin(20, Pin.OUT)
mtr2_2 = Pin(21, Pin.OUT)

mtr1_1.low()
mtr1_2.low()
mtr2_1.low()
mtr2_2.low()

mtr1 = PWM(Pin(16))

mtr2 = PWM(Pin(17))

mtr1.freq(1000)

mtr2.freq(1000)

# 0 to 65025

mtr1.duty_u16(60000)

mtr2.duty_u16(60000)

r1 = RotaryIRQ(pin_num_clk = 2,
              pin_num_dt = 3,
              min_val = 0,
              reverse = False,
              range_mode = RotaryIRQ.RANGE_UNBOUNDED)

r2 = RotaryIRQ(pin_num_clk = 4,
              pin_num_dt = 5,
              min_val = 0,
              reverse = False,
              range_mode = RotaryIRQ.RANGE_UNBOUNDED)

val_old1 = r1.value()
val_old2 = r2.value()

while True:
    val_new1 = r1.value()
    val_new2 = r2.value()

    if val_old1 != val_new1:
        val_old1 = val_new1
         
    if val_old2 != val_new2:
            val_old2 = val_new2
    
    print(val_new1, val_new2)
    
    time.sleep_ms(5)
