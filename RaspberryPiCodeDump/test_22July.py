# (C) Ansh Chablani
# All Rights Reserved
# 
# PD controller for the robot to turn precisely that many angles
# Here I am basing the input to be received from the shell.
#
# For an angle controller
#
# Use: To turn and drive straight (in case of 0 degrees)
# Goal: Difference in encoder counts corresponding to a certain angle.
# Error: Goal - (Left Counts - Right Counts)
# Output: Add to one motor, subtract from the other.
#
# I am taking the convention of acw rotation to be positive and cw rotation to be negative.

from RobotAPI import Micromouse
from machine import Pin, PWM
from time import sleep
import time
from rotary_irq_rp2 import RotaryIRQ
import math

mm = Micromouse()

kona = float(input("Enter angle to rotate: "))
# kona = kona * (950/90)
move = 1
errorLeft = 0
errorRight = 0
print("1")
Kp = 35000 # To be detemined accurately
Kd = 5000

# In cm
radius = 16 // 2
print("2")
# kona * r
distanceToMove = kona * radius * (math.pi / 180)
print("3")
leftOneRotationEncValue = 343
print("4")
rightOneRotationEncValue = 347

circumference = 10.053 # In cm
print("5")
leftEncValuePerCM = leftOneRotationEncValue / circumference
rightEncValuePerCM = rightOneRotationEncValue / circumference
print("6")

toMoveLeft = (leftEncValuePerCM * distanceToMove + rightEncValuePerCM * distanceToMove) / 2
toMoveRight = (leftEncValuePerCM * distanceToMove + rightEncValuePerCM * distanceToMove) / 2

# So what I want is that we should be able to make the left and the right motor until both of them move the same amount
# That is decided by the average of the encoder steps they are required to move individually.

# First take count of the initial encoder steps.
print("7")
oldPosLeft = mm.getLeftEncoderValue()
oldPosRight = mm.getRightEncoderValue()
print("8")

# Then let us have counts for the moves that have happened in the left and the right motor.
movedLeft = 0
movedRight = 0

print(toMoveLeft, toMoveRight)

flag1 = 0
flag2 = 0

# Initial PWM supplied
PWMLeft = 60000
PWMRight = 60000

print(toMoveLeft, toMoveRight)
mm.enableLeftMTRFWD()
mm.enableRightMTRBWD()

mm.setMotorsPWM(PWMLeft, PWMRight)

while True:
    # First set the positions of the motors
    if flag1 == 0:
        pass
        #print("Here before enableLeftMTRFWD")
        #mm.enableLeftMTRFWD()
    else:
        print("Here before mm.leftMTRStop()")
        mm.leftMTRStop()
        #break # this is for testing
        PWMLeft = 0
    
    if flag2 == 0:
        pass
        #print("Here before mm.enableRightMTRBWD()")
        #mm.enableRightMTRBWD()
    else:
        print("Here before mm.rightMTRStop().......................................")
        mm.rightMTRStop()
        #break # this is for testing 
        PWMRight = 0
    
    # Relaxation time to stop
    time.sleep_ms(5)
    
    # Then give them some speed
    if not (flag1 and flag2):
        pass
        #print("mm.setMotorsPWM")
        #mm.setMotorsPWM(PWMLeft, PWMRight)
    
    currentPosLeft = mm.getLeftEncoderValue()
    currentPosRight = mm.getRightEncoderValue()
    
    if oldPosLeft != currentPosLeft:
        oldPosLeft = currentPosLeft
         
    if oldPosRight != currentPosRight:
        oldPosRight = currentPosRight
    
    # Change speed based if the destination is close
    if abs(oldPosLeft) >= toMoveLeft - 100:
        PWMLeft -= 20000
        
    if abs(oldPosRight) >= toMoveRight - 100:
        PWMRight -= 20000
    
#     if abs(oldPosLeft) >= toMoveLeft - 50:
#         PWMLeft -= 20000
#         
#     if abs(oldPosRight) >= toMoveRight - 50:
#         PWMRight -= 20000
#     
#     if abs(oldPosLeft) >= toMoveLeft - 10:
#         PWMLeft -= 15000
#         
#     if abs(oldPosRight) >= toMoveRight - 10:
#         PWMRight -= 15000
    
    # Stop if the destination is reached.
    if abs(oldPosLeft) >= toMoveLeft:
        print("Reached Left")
        
        mm.leftMTRStop()
        PWMLeft = 0
        # Relaxation time to stop
        time.sleep_ms(5)
        flag1 = 1
        
    if abs(oldPosRight) >= toMoveRight:
        print("Reached Right")
        
        PWMRight = 0
        print("rightMTRStop.................., flag 2 is set")
        mm.rightMTRStop()
        #mm.bothMotorsStop()
        # Relaxation time to stop
        time.sleep_ms(5)
        flag2 = 1
    
    print("flag1 =", flag1, "flag2 =", flag2)
    if(flag1 and flag2):
        print("-----------break---------------------")
        break
    
    print(oldPosLeft, oldPosRight)
    time.sleep_ms(5)

#mm.bothMotorsStop()
print("10")


