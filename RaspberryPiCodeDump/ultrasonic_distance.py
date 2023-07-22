# Ultrasonic sensor reading
from machine import Pin
import utime
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

speed_of_sound = 343
# signaloff = 0
# signalon = 0
# timepassed = 0
def ultra(location):
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    
    while echo.value() == 0:
        signaloff = utime.ticks_us()
        
    while echo.value() == 1:
        signalon = utime.ticks_us()
    
    timepassed = signalon - signaloff
    
    distance = (timepassed * speed_of_sound / 10000) / 2
    
    print("Distance: at", location, ":", distance, "cm")

