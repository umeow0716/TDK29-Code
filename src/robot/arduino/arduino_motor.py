from .arduino import Arduino

class ArduinoMotor:
    def __init__(self, forward_pin, backward_pin, pwm_pin, default_speed=255):
        self.forward_pin = forward_pin
        self.backward_pin = backward_pin
        self.pwm_pin = pwm_pin
        self.speed = default_speed
        
        Arduino.analogWrite(self.pwm_pin, default_speed)
        self.stop()
    
    def forward(self, inverse=False):
        Arduino.digitalWrite(self.forward_pin, 1 if not inverse else 0)
        Arduino.digitalWrite(self.backward_pin, 0 if not inverse else 1)
    
    def backward(self, inverse=False):
        Arduino.digitalWrite(self.forward_pin, 0 if not inverse else 1)
        Arduino.digitalWrite(self.backward_pin, 1 if not inverse else 0)
        
    def stop(self):
        Arduino.digitalWrite(self.forward_pin, 0)
        Arduino.digitalWrite(self.backward_pin, 0)
    
    def setSpeed(self, speed):
        if speed == self.speed:
            return
        Arduino.analogWrite(self.pwm_pin, speed)
        self.speed = speed