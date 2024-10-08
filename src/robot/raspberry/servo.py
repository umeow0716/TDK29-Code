from threading import Thread
from time import sleep
import RPi.GPIO as GPIO

class Servo:
    def __init__(self, pin, default_angle=0, mode=180):
        GPIO.setup(pin, GPIO.OUT)
        self.mode = mode if (mode == 180 or mode == 360) else 180
        self.servo = GPIO.PWM(pin, 50)
        self.servo.start(0)
        
        self.write(default_angle)
        self.angle = default_angle
        
        if self.mode == 360:
            self.write(7.5)
            sleep(0.1)
            self.write(default_angle)
        
        if self.mode == 180:
            self.servo.ChangeFrequency(5000)
        
    def _start_thread(self):
        Thread(target=self.keep_alive, daemon=True).start()
    
    def keep_alive(self):
        while True:
            self.write(self.angle)
            sleep(5)
    
    def write(self, angle):
        if self.mode == 180:
            self.servo.ChangeFrequency(50)
            self.servo.ChangeDutyCycle((angle/18.0) + 2.5)
        else:
            self.servo.ChangeDutyCycle(angle)
        self.angle = angle
        
    def stop(self):
        self.servo.stop()
    
    def start(self, dutycycle=0):
        self.servo.start(dutycycle)