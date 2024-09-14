from ..joystick.joystick import Joystick
from .raspberry.servo import Servo

class BallDoor():
    servo = Servo(2)
    state = 'close'
    
    @staticmethod
    @Joystick.when_button_a_press_wrapper
    def next_step():
        if BallDoor.state == 'close':
            BallDoor.servo.write(70)
            BallDoor.state = 'open'
        elif BallDoor.state == 'open':
            BallDoor.servo.write(0)
            BallDoor.state = 'close'
    
    @staticmethod
    def execute(data):
        print(f'ball_door: {data}')
        if data == 'open':
            BallDoor.servo.write(70)
        
        if data == 'close':
            BallDoor.servo.write(0)