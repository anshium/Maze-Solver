# (C) Ansh Chablani
# All Rights Reserved

# This is the thing I will use to conveniently control the robot using the functions.
from machine import Pin, PWM
from time import sleep
import time
from rotary_irq_rp2 import RotaryIRQ

class Micromouse:
    def __init__(self):
        self.mtr1en = PWM(Pin(17))
        self.mtr2en = PWM(Pin(16))
        self.mtr1en.freq(1000)
        self.mtr2en.freq(1000)
        self.mtr1en.duty_u16(0) # Initially set speed of motor 1 (left motor) to be 0
        self.mtr2en.duty_u16(0) # Initially set speed of motor 2 (right motor) to be 0
        
        self.mtr1_1 = Pin(20, Pin.OUT)
        self.mtr1_2 = Pin(21, Pin.OUT)
        self.mtr2_1 = Pin(18, Pin.OUT)
        self.mtr2_2 = Pin(19, Pin.OUT)
        
        self.r1 = RotaryIRQ(pin_num_clk = 2,
              pin_num_dt = 3,
              min_val = 0,
              reverse = False,
              range_mode = RotaryIRQ.RANGE_UNBOUNDED)

        self.r2 = RotaryIRQ(pin_num_clk = 4,
                      pin_num_dt = 5,
                      min_val = 0,
                      reverse = False,
                      range_mode = RotaryIRQ.RANGE_UNBOUNDED)
        
        # Stopping the motors initially
        self.mtr1_1.low()
        self.mtr1_2.low()
        self.mtr2_1.low()
        self.mtr2_2.low()
        self.mtr1en.duty_u16(0)
        self.mtr2en.duty_u16(0)
        
        # Sensors
        self.leftIR = Pin(6, Pin.IN)
        self.leftFrontIR = Pin(7, Pin.IN)
        self.frontLeftIR = Pin(8, Pin.IN)
        self.frontRightIR = Pin(9, Pin.IN)
        self.rightFrontIR = Pin(10, Pin.IN)
        self.rightIR = Pin(11, Pin.IN)
    # The enableFWD, enableBWD, enableLEFT and enableRIGHT functions can be used in creative ways
    # in addition to what their name suggets.
    
    # In addition to this function enabling the motor to go forwars, it can also go left or right based on the rmp provided
    # to each motor
    def enableFWD(self):
        self.mtr1_1.high()
        self.mtr1_2.low()
        self.mtr2_1.high()
        self.mtr2_2.low()
    
    # Same header comment as in case of forward
    def enableBWD(self):
        self.mtr1_1.low()
        self.mtr1_2.high()
        self.mtr2_1.low()
        self.mtr2_2.high()
    
    # This function can be using in both cases, on central axis and any other axis based on rpm
    def enableLEFT(self):
        self.mtr1_1.high()
        self.mtr1_2.low()
        self.mtr2_1.low()
        self.mtr2_2.high()
    
    def enableRIGHT(self):
        self.mtr1_1.low()
        self.mtr1_2.high()
        self.mtr2_1.high()
        self.mtr2_2.low()

    # Set left motor to operate in forward sense
    def enableLeftMTRFWD(self):
        self.mtr1_1.high()
        self.mtr1_2.low()
    
    # Set right motor to operate in forward sense
    def enableRightMTRFWD(self):
        self.mtr2_1.high()
        self.mtr2_2.low()
    
    # Set left motor to operate in backward sense
    def enableLeftMTRBWD(self):
        self.mtr1_1.low()
        self.mtr1_2.high()
        
    # Set right motor to operate in backward sense
    def enableRightMTRBWD(self):
        self.mtr2_1.low()
        self.mtr2_2.high()
    
    # Self destruct the robot
    def selfDestruct(self, password):
        if(password == "destroy"):
            print("Password Correct")
            time_remaining = 60 * 1000
            while True:
                print("In self-destruct mode")
                print("Time remaining:", time_remaining, "ms")
                self.enableLeftMTRFWD()
                self.mtr1en.duty_u16(70000)
                time.sleep_ms(1)
                self.enableLeftMTRBWD()
                self.mtr1en.duty_u16(70000)
                time.sleep_ms(1)
                self.enableRightMTRFWD()
                self.mtr1en.duty_u16(70000)
                time.sleep_ms(1)
                self.enableRightMTRBWD()
                self.mtr1en.duty_u16(70000)
                time.sleep_ms(1)
                time += 60*1000 - 1 * 4
        print("Sorry wrong password!")
    
    # Set the PWM value of the left motor
    def setLeftMTR_PWM(self, pwm):
        self.mtr1en.duty_u16(pwm)
    
    def setRightMTR_PWM(self, pwm):
        self.mtr2en.duty_u16(pwm)
    
    def setMotorsPWM(self, pwm1, pwm2):
        self.mtr1en.duty_u16(pwm1)
        self.mtr2en.duty_u16(pwm2)
        
    # Stop the left motor
    def leftMTRStop(self):
        self.setLeftMTR_PWM(0)
        self.mtr1_1.low()
        self.mtr1_2.low()
    
    # Stop the right motor
    def rightMTRStop(self):
        self.setRightMTR_PWM(0)
        self.mtr2_1.low()
        self.mtr2_2.low()
    
    # Stop both motors
    def bothMotorsStop(self):
        self.setMotorsPWM(0, 0)
        self.leftMTRStop()
        self.rightMTRStop()
    
    def getLeftEncoderValue(self):
        return self.r1.value()
    
    def getRightEncoderValue(self):
        return self.r2.value()
    
    # enc1_val and enc2_val can both be positive and negative
    # Please suggest improvements if any
    def moveEncoderSteps(self, enc1_val, enc2_val, pwm1=60000, pwm2=60000):
        if(pwm1 < 0 or pwm2 < 0):
            print("Invalid input, exiting.")
            return
        # Taking note of the initial value of the encoders
        initial_value1 = self.r1.value()
        initial_value2 = self.r2.value()
        
        # Setting motors to a desired speed
        self.setMotorsPWM(pwm1, pwm2)
        
        # Setting directions of motors based on what the encoder values were specified
        if(enc1_val > 0):
            self.enableLeftMTRFWD()
        if(enc2_val > 0):
            self.enableRightMTRFWD()
        if(enc1_val < 0):
            self.enableLeftMTRBWD()
        if(enc2_val < 0):
            self.enableRightMTRBWD()
            
        # Flags to exit a particular loop
        flag1 = 0
        flag2 = 0
        
        # A while true loop, not the best way to do it perhaps but works considerably well.
        while True:
            print(self.r1.value() - initial_value1)
            print(enc2_val)
            if(self.r1.value() - initial_value1 >= enc1_val):
                self.leftMTRStop()
                flag1 = 1
            if(self.r1.value() - initial_value2 >= enc2_val):
                self.rightMTRStop()
                flag2 = 1
            if(flag1 and flag2):
                break
            time.sleep_ms(5)
        return
    def getIRSensorData(self):
        return [self.leftIR.value(),
                self.leftFrontIR.value(),
                self.frontLeftIR.value(),
                self.frontRightIR.value(),
                self.rightFrontIR.value(),
                self.rightIR.value()]
