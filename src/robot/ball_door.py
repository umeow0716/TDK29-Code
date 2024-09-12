from .raspberry.servo import Servo

class BallDoor():
    servo = Servo(2)
    
    @staticmethod
    def execute(data):
        print(f'ball_door: {data}')
        if data == 'open':
            BallDoor.servo.write(70)
        
        if data == 'close':
            BallDoor.servo.write(0)