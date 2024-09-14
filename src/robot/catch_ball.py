from .arduino.arduino_motor import ArduinoMotor

class CatchBall:
    motor = ArduinoMotor(33, 32, 7)
    state = 'stop'
    
    @staticmethod
    def up():
        if CatchBall.state == 'up':
            return
        CatchBall.motor.forward()
        CatchBall.state = 'up'
    
    @staticmethod
    def down():
        if CatchBall.state == 'down':
            return
        CatchBall.motor.backward()
        CatchBall.state = 'down'
    
    @staticmethod
    def stop():
        if CatchBall.state == 'stop':
            return
        CatchBall.motor.stop()
        CatchBall.state = 'stop'
    
    @staticmethod
    def execute(data):
        print(f'catch_ball: {data}')
        
        if data == 'up':
            CatchBall.up()
        
        if data == 'down':
            CatchBall.down()
            
        if data == 'stop':
            CatchBall.stop()