from machine import Pin, PWM
from time import sleep
import time
from rotary_irq_rp2 import RotaryIRQ

mtr1_1 = PWM(Pin(20))
mtr1_2 = PWM(Pin(21))

mtr2_1 = PWM(Pin(18))
mtr2_2 = PWM(Pin(19))

mtr1_1.freq(1000)
mtr1_2.freq(1000)

mtr2_1.freq(1000)
mtr2_2.freq(1000)

# 0 to 65025

mtr1_1.duty_u16(60000)
mtr1_2.duty_u16(0)

mtr2_1.duty_u16(60000)
mtr2_2.duty_u16(0)

def stop():
    mtr1_1.duty_u16(0)
    mtr1_2.duty_u16(0)

    mtr2_1.duty_u16(0)
    mtr2_2.duty_u16(0)

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

count = 0

mtr1_rpm = 20000
mtr2_rpm = 20000

while True:
    val_new1 = r1.value()
    val_new2 = r2.value()

    if val_old1 != val_new1:
        val_old1 = val_new1
        
    if val_old2 != val_new2:
        val_old2 = val_new2
#         print('result =', val_new)
    
    while(abs(val_new1 - val_new2) > 10):
        print(mtr1_rpm, mtr2_rpm, val_new1, val_new2, val_new1 - val_new2)
        if(mtr1_rpm < 60000 and mtr1_rpm > 0 + abs(20*(val_new2 - val_new1))):
            mtr1_rpm += 20*(val_new2 - val_new1)
        if(mtr2_rpm < 60000 and mtr2_rpm > 0 + abs(20*(val_new1 - val_new2))):
            mtr2_rpm += 20*(val_new1 - val_new2)
        
        time.sleep_ms(50)
        
        val_new1 = r1.value()
        val_new2 = r2.value()

        if val_old1 != val_new1:
            val_old1 = val_new1
            
        if val_old2 != val_new2:
            val_old2 = val_new2
        
        mtr1_1.duty_u16(mtr1_rpm)
        mtr1_2.duty_u16(0)

        mtr2_1.duty_u16(mtr2_rpm)
        mtr2_2.duty_u16(0)
        
    
#     if(val_new1 > val_new2):
#         mtr2_rpm += 7000
#     
#     if(val_new1 < val_new2):
#         mtr1_rpm += 7000
    
    if(val_new1 == val_new2):
        mtr1_rpm = 40000
        mtr2_rpm = 40000
    
    mtr1_1.duty_u16(mtr1_rpm)
    mtr1_2.duty_u16(0)

    mtr2_1.duty_u16(mtr2_rpm)
    mtr2_2.duty_u16(0)
    
    print(mtr1_rpm, mtr2_rpm, val_new1, val_new2, val_new1 - val_new2)
    time.sleep_ms(5)
