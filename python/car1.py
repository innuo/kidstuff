import RPi.GPIO as GPIO
from time import sleep

Motor1A = 23
Motor1B = 24
Motor1E = 25

Motor2A = 17
Motor2B = 27
Motor2E = 22

def setup():
    GPIO.setmode(GPIO.BCM)
     
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)

    GPIO.setup(Motor2A,GPIO.OUT)
    GPIO.setup(Motor2B,GPIO.OUT)
    GPIO.setup(Motor2E,GPIO.OUT)
    pass


def motor1(seconds, forward=True):
    print("Starting motor 1 for %d seconds"%seconds)
    if forward:
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.HIGH)
    else:
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        
    GPIO.output(Motor1E,GPIO.HIGH)
    sleep(seconds)
    GPIO.output(Motor1E,GPIO.LOW) 
    print("Stopping motor 1")

def motor2(seconds, forward=True):
    print("Starting motor 2 for %d seconds"%seconds)
    if forward:
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
    else:
        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.HIGH)
        
    GPIO.output(Motor2E,GPIO.HIGH)
    sleep(seconds)
    GPIO.output(Motor2E,GPIO.LOW) 
    print("Stopping motor 2")


def user_input():
    while True:
        motor = int(input("Which motor? "))
        seconds = int(input("How long? "))
        mode = input("Foward? ")
        
        if seconds < 0:
            seconds = 1
        if seconds > 5:
            seconds = 5

        motor_func = motor1 if motor == 1 else motor2

        
        if mode.lower()[0] == 'y':
            motor_func(seconds, True)
        else:
            motor_func(seconds, False)

    GPIO.cleanup()
        
        
        
    
if __name__ == "__main__":
    setup()

    try:
        user_input()
    except:
        print("Wrong input! Done...")
        
    #motor1(5)
    #motor2(15)
    
    GPIO.cleanup()
