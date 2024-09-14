from .arduino.arduino_motor import ArduinoMotor

class FrontBoard:
    motor = ArduinoMotor(29, 28, 4)
    state = 'stop'
    
    @staticmethod
    def up():
        if FrontBoard.state == 'up':
            return
        FrontBoard.motor.forward()
        FrontBoard.state = 'up'
    
    @staticmethod
    def down():
        if FrontBoard.state == 'down':
            return
        FrontBoard.motor.backward()
        FrontBoard.state = 'down'
    
    @staticmethod
    def stop():
        if FrontBoard.state == 'stop':
            return
        FrontBoard.motor.stop()
        FrontBoard.state = 'stop'
    
    @staticmethod
    def execute(data):
        print(f'front_board: {data}')
        
        if data == 'up':
            FrontBoard.up()
        
        if data == 'down':
            FrontBoard.down()
            
        if data == 'stop':
            FrontBoard.stop()