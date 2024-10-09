from .arduino.arduino_motor import ArduinoMotor 
from ..joystick.joystick import Joystick

class Platform:
    motor = ArduinoMotor(5, 29, 28)
    
    @Joystick.when_button_x_change_wrapper
    def joystick_button_x_update(value, *args, **kwatgs):
        if value:
            Platform.motor.forward()
        else:
            Platform.motor.stop()
            
    @Joystick.when_button_a_change_wrapper
    def joystick_button_a_update(value, *args, **kwargs):
        if value:
            Platform.motor.backward()
        else:
            Platform.motor.stop()
    
    @staticmethod
    def execute(data):
        print(f'platform: {data}')
        
        if data == 'up':
            Platform.motor.forward()
        
        if data == 'down':
            Platform.motor.backward()
        
        if data == 'stop':
            Platform.motor.stop()