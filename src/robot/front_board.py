from .arduino.arduino_motor import ArduinoMotor
from ..joystick.joystick import Joystick

class FrontBoard:
    motor = ArduinoMotor(40, 41, 4)
    
    @Joystick.when_lb_change_wrapper
    def joystick_lb_update(value, *args, **kwargs):
        if value:
            FrontBoard.motor.forward()
        else:
            FrontBoard.motor.stop()
            
    @Joystick.when_lt_change_wrapper
    def joystick_lt_update(value, *args, **kwargs):
        if value > 250:
            FrontBoard.motor.backward()
        else:
            FrontBoard.motor.stop()
    
    @staticmethod
    def execute(data):
        print(f'front_board: {data}')
        
        if data == 'up':
            FrontBoard.motor.forward()
        
        if data == 'down':
            FrontBoard.motor.backward()
            
        if data == 'stop':
            FrontBoard.motor.stop()