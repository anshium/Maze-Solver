from machine import Pin, Timer

led = Pin(25, Pin.OUT)
time = Timer()

def blink(time):
    led.toggle()

time.init(freq = 5.5, mode = Timer.PERIODIC, callback = blink)
