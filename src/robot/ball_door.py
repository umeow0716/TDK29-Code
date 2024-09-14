from .raspberry.servo import Servo

class BallDoor():
    servo = Servo(2)
    state = 'close'
    
    @staticmethod
    def next_step():
        if BallDoor.state == 'close':
            BallDoor.servo.write(70)
            BallDoor.state = 'open'
        elif BallDoor.state == 'open':
            BallDoor.servo.write(0)
            BallDoor.state = 'close'
        print(BallDoor.state)
        
    
    @staticmethod
    def execute(data):
        print(f'ball_door: {data}')
        if data == 'open':
            BallDoor.servo.write(70)
        
        if data == 'close':
            BallDoor.servo.write(0)