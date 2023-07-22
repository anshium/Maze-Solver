import utime
from servo import Servo
import ultrasonic_distance as ud

s1 = Servo(18)       # Servo pin is connected to GP0
 
def servo_Map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
 
def servo_Angle(angle):
    if angle < 0:
        angle = 0
    if angle > 180:
        angle = 180
    s1.goto(round(servo_Map(angle,0,180,0,1024))) # Convert range value to angle value
    
dist_record_sleep = 0.4

if __name__ == '__main__':
    servo_Angle(0)
    while not False:
        for i in range(0,55,10):
            servo_Angle(i)
            utime.sleep(0.01)
        ud.ultra(1)
        utime.sleep(dist_record_sleep)
        
        for i in range(55,110,10):
            servo_Angle(i)
            utime.sleep(0.01)
        ud.ultra(2)
        utime.sleep(dist_record_sleep) 
         
#         for i in range(90,135,10):
#             servo_Angle(i)
#             utime.sleep(0.01)
#         ud.ultra()
#         utime.sleep(dist_record_sleep)
#         
#         for i in range(135,180,10):
#             servo_Angle(i)
#             utime.sleep(0.01)
#         ud.ultra()
#         utime.sleep(dist_record_sleep)
        
#         for i in range(180,135,-10):
#             servo_Angle(i)
#             utime.sleep(0.01)
#         ud.ultra()
#         utime.sleep(dist_record_sleep)
#         
#         for i in range(135,90,-10):
#             servo_Angle(i)
#             utime.sleep(0.01)
#         ud.ultra()
#         utime.sleep(dist_record_sleep)
#         
        for i in range(110,55,-10):
            servo_Angle(i)
            utime.sleep(0.01)
        ud.ultra(3)
        utime.sleep(dist_record_sleep)
        
        for i in range(55,0,-10):
            servo_Angle(i)
            utime.sleep(0.01)
        ud.ultra(2)
        utime.sleep(dist_record_sleep)
