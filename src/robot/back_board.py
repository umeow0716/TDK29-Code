from .arduino.arduino_motor import ArduinoMotor
from ..joystick.joystick import Joystick

class BackBoard:
    motor = ArduinoMotor(4, 32, 33)
    
    @Joystick.when_rb_change_wrapper
    def joystick_rb_update(value, *args, **kwargs):
        if value:
            BackBoard.motor.forward()
        else:
            BackBoard.motor.stop()
            
    @Joystick.when_rt_change_wrapper
    def joystick_rt_update(value, *args, **kwargs):
        if value > 250:
            BackBoard.motor.backward()
        else:
            BackBoard.motor.stop()
    
    @staticmethod
    def execute(data):
        print(f'back_board: {data}')
        
        if data == 'up':
            BackBoard.motor.forward()
        
        if data == 'down':
            BackBoard.motor.backward()
            
        if data == 'stop':
            BackBoard.motor.stop()