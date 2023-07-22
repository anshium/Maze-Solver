from RobotAPI import Micromouse
from machine import Pin, PWM
from time import sleep
import time
from rotary_irq_rp2 import RotaryIRQ

mm = Micromouse()

# mm.setMotorsPWM(60000, 60000)
# mm.enableRightMTRFWD()
# mm.enableLeftMTRFWD()
# 
# mm.bothMotorsStop()

mm.moveEncoderSteps(300, 300)
