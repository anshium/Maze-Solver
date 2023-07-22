from time import sleep
from machine import Pin
led = Pin(25, Pin.OUT)
n = 0
while n < 10:
    led.high()
    sleep(0.5)
    led.low()
    n = n+1
    
