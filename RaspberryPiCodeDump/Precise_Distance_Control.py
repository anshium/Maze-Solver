# Precise Distance Control
# Purpose: To move a fixed number of encoder counts in both the motor wheels so as to move a particular number of steps.

from RobotAPI import Micromouse
from machine import Pin, PWM
from time import sleep
import time
from rotary_irq_rp2 import RotaryIRQ
import math

mm = Micromouse()

distance = float(input("Enter the distance to travel: "))

leftOneRotationEncValue = 343

rightOneRotationEncValue = 347

circumference = 10.053 # In cm

leftEncValuePerCM = leftOneRotationEncValue / circumference
rightEncValuePerCM = rightOneRotationEncValue / circumference

toMoveLeft = ((distance * leftEncValuePerCM) + (distance * rightEncValuePerCM)) / 2
toMoveRight = ((distance * leftEncValuePerCM) + (distance * rightEncValuePerCM)) / 2

flag1 = 0
flag2 = 0

PWMLeft = 40000
PWMRight = 40000

oldPosLeft = mm.getLeftEncoderValue()
oldPosRight = mm.getRightEncoderValue()

print(toMoveLeft, toMoveRight)
while True:
    if(input()):
        break

while True:
    if flag1 == 0:
        mm.enableLeftMTRFWD()
    else:
        mm.leftMTRStop()
        PWMLeft = 0
    
    if flag2 == 0:
        mm.enableRightMTRFWD()
    else:
        mm.rightMTRStop()
        PWMRight = 0
    
    # Relaxation time to stop
    time.sleep_ms(5)
    
    # Then give them some speed
    if not (flag1 and flag2):
        mm.setLeftMTR_PWM(PWMLeft)
        mm.setRightMTR_PWM(PWMRight)
    
    currentPosLeft = mm.getLeftEncoderValue()
    currentPosRight = mm.getRightEncoderValue()
    
    if oldPosLeft != currentPosLeft:
        oldPosLeft = currentPosLeft
         
    if oldPosRight != currentPosRight:
        oldPosRight = currentPosRight
        
    # Change speed based if the destination is close
    if abs(currentPosLeft) >= toMoveLeft - 100:
        PWMLeft -= 20000
        
    if abs(currentPosRight) >= toMoveRight - 100:
        PWMRight -= 20000
    
    # Stop if the destination is reached.
    if abs(currentPosLeft) >= toMoveLeft:
        print("Reached Left")
        
        mm.leftMTRStop()
        PWMLeft = 0
        # Relaxation time to stop
        time.sleep_ms(5)
        flag1 = 1
        
    if abs(currentPosRight) >= toMoveRight:
        print("Reached Right")
        
        PWMRight = 0
        print("rightMTRStop.................., flag 2 is set")
        mm.rightMTRStop()
        # mm.bothMotorsStop()
        # Relaxation time to stop
        time.sleep_ms(5)
        flag2 = 1
    
    print("flag1 =", flag1, "flag2 =", flag2)
    if(flag1 and flag2):
        print("-----------break---------------------")
        break
    
    print(currentPosLeft, currentPosRight)
    time.sleep_ms(5)

print(currentPosLeft, currentPosRight)

#mm.bothMotorsStop()
print("10")
