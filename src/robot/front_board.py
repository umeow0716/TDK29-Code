from .arduino.arduino_motor import ArduinoMotor
from ..joystick.joystick import Joystick

class FrontBoard:
    motor = ArduinoMotor(4, 46, 47)
    
    @Joystick.when_lb_change_wrapper
    def joystick_lb_update(value, *args, **kwargs):
        if value:
            print("frontboard forward")
            FrontBoard.motor.forward()
        else:
            print("frontboard stop")
            FrontBoard.motor.stop()
            
    @Joystick.when_lt_change_wrapper
    def joystick_lt_update(value, *args, **kwargs):
        if value > 250:
            print("frontboard backward")
            FrontBoard.motor.backward()
        else:
            print("frontboard stop")
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