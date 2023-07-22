from machine import Pin

Pin(25, Pin.OUT).high()

C2 = Pin(18, Pin.IN) # Yellow
C1 = Pin(19, Pin.IN) # Green
M1 = Pin(18, Pin.OUT) # White
M2 = Pin(21, Pin.OUT) # Red

M1.value(1)
M2.value(0)
