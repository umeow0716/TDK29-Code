from .arduino import Arduino

class ArduinoMotor:
    def __init__(self, forward_pin, backward_pin, pwm_pin):
        self.forward_pin = forward_pin
        self.backward_pin = backward_pin
        self.pwm_pin = pwm_pin
        self.speed = 255
        
        Arduino.analogWrite(self.pwm_pin, 255)
        self.stop()
    
    def forward(self):
        Arduino.digitalWrite(self.forward_pin, 1)
        Arduino.digitalWrite(self.backward_pin, 0)
    
    def backward(self):
        Arduino.digitalWrite(self.forward_pin, 0)
        Arduino.digitalWrite(self.backward_pin, 1)
        
    def stop(self):
        Arduino.digitalWrite(self.forward_pin, 0)
        Arduino.digitalWrite(self.backward_pin, 0)
    
    def setSpeed(self, speed):
        if speed == self.speed:
            return
        Arduino.analogWrite(self.pwm_pin, speed)
        self.speed = speed