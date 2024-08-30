import RPi.GPIO as GPIO

class Servo:
    def __init__(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        self.servo = GPIO.PWM(pin, 50)
        self.servo.start(0)
    
    def write(self, angle):
        self.servo.ChangeDutyCycle((angle/18.0) + 2.5)
        
    def stop(self):
        self.servo.stop()
        del self