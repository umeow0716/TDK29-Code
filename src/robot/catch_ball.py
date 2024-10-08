from .arduino.arduino_motor import ArduinoMotor
from ..joystick.joystick import Joystick

class CatchBall:
    motor = ArduinoMotor(27, 26, 7)
    
    @Joystick.when_button_y_change_wrapper
    def joystick_button_y_update(value, *args, **kwargs):
        if value:
            CatchBall.motor.forward()
        else:
            CatchBall.motor.stop()
            
    @Joystick.when_button_b_change_wrapper
    def joystick_button_b_update(value, *args, **kwargs):
        if value:
            CatchBall.motor.backward()
        else:
            CatchBall.motor.stop()
    
    @staticmethod
    def execute(data):
        print(f'catch_ball: {data}')
        
        if data == 'up':
            CatchBall.motor.forward()
        
        if data == 'down':
            CatchBall.motor.backward()
            
        if data == 'stop':
            CatchBall.motor.stop()