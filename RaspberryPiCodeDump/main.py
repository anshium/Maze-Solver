from machine import Pin, PWM

en = PWM(Pin(18))

en.freq(1000)

en.duty_u16(19300)

led = Pin(14, Pin.OUT)
led.high()
