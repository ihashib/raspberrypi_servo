import RPi.GPIO as GPIO
from time import sleep

def SetAngle(angle):
    duty = angle / 18 + 2
    pwm.ChangeDutyCycle(duty)
    sleep(1)   
    
servo = 22
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo, GPIO.OUT)
pwm=GPIO.PWM(servo, 50)
pwm.start(0)

SetAngle(0)

pwm.stop()
GPIO.cleanup()



