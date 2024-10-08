from time import sleep

from ..joystick.joystick import Joystick
from .raspberry.servo import Servo

class BallDoor():
    servo = Servo(2, default_angle=80)
    servo.stop()
    
    button_last_state = 0
    isWorking = False
    
    def open():
        print(f'ball_door: open')
        BallDoor.servo.write(13)
    
    def close():
        print(f'ball_door: close')
        BallDoor.servo.write(85)
    
    @Joystick.when_axis_hat_change_wrapper
    def next_step(value, *args, **kwargs):
        if value[1] != -1 or value[1] == BallDoor.button_last_state:
            BallDoor.button_last_state = value[1]
            return
        
        if not BallDoor.isWorking:
            BallDoor.isWorking = True
            BallDoor.servo.start()
            BallDoor.open()
            sleep(1)
            BallDoor.close()
            sleep(0.5)
            BallDoor.servo.stop()
            BallDoor.isWorking = False
        
        BallDoor.button_last_state = value[1]
    
    @staticmethod
    def execute(data):
        if data == 'open':
            BallDoor.servo.write(70)
        
        if data == 'close':
            BallDoor.servo.write(0)