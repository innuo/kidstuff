import RPi.GPIO as GPIO
from time import sleep
import numpy as np

Motor1A = 23
Motor1B = 24
Motor1E = 25

Motor2A = 17
Motor2B = 27
Motor2E = 22


GPIO.setmode(GPIO.BCM)
     
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

pwm1 = GPIO.PWM(Motor1E, 30)
pwm2 = GPIO.PWM(Motor2E, 30)
pwm1.start(0)
pwm2.start(0)


def command(cmd):
    #cmd = ['forwards'/'backwards', speed_1, speed_2, time]
    print(cmd)
    print()
    if cmd[0].lower() == 'f':
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.HIGH)

        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
    else:
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)

        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.HIGH)

    speed_1  = 10 * quantize(cmd[1], 0, 10, 3) 
    speed_2  = 10 * quantize(cmd[2], 0, 10, 3) 

    print (speed_1)
    print (speed_2)
    
    t = quantize(cmd[3], 0.1, 5)

    pwm1.ChangeDutyCycle(speed_1) 
    pwm2.ChangeDutyCycle(speed_2) 

    sleep(t)

    pwm1.ChangeDutyCycle(0) 
    pwm2.ChangeDutyCycle(0) 
   

def quantize(v, l, u, n = None):
    x = v
    if v < l:
        x = l
    if v > u:
        x = u
        
    if n is None: return x
    
    q = np.arange(l, u + (u-l)/n, (u-l)/n)
    x = q[np.where(q <= x)[0][-1]]
    
    return x

def motor_test():
    try:
        while True:
            direction   = input("Direction ? ")
            speed_left  = float(input("Left speed  ? "))
            speed_right = float(input("Right speed ? "))
            t           = float(input("Time ? "))       
            
            command([direction, speed_left, speed_right, t])
    except Exception as e:
        print (e)
        print("\n...DONE...")
        GPIO.cleanup()
        pwm1.stop()
        pwm2.stop()

    
    GPIO.cleanup()


def run_command_list():
    cmds = [['f', 5, 5, 2],
            ['f', 0, 5, 1],
            ['b', 5, 5, 2]]

    for c in cmds:
        command(c)

    GPIO.cleanup()
    pwm1.stop()
    pwm2.stop()
        
    
if __name__ == '__main__':
    #motor_test()
    

    GPIO.cleanup()
