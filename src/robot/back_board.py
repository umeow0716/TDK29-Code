from .arduino.arduino_motor import ArduinoMotor

class BackBoard:
    motor = ArduinoMotor(40, 41, 4)
    state = 'stop'
    
    @staticmethod
    def up():
        if BackBoard.state == 'up':
            return
        BackBoard.motor.forward()
        BackBoard.state = 'up'
    
    @staticmethod
    def down():
        if BackBoard.state == 'down':
            return
        BackBoard.motor.backward()
        BackBoard.state = 'down'
    
    @staticmethod
    def stop():
        if BackBoard.state == 'stop':
            return
        BackBoard.motor.stop()
        BackBoard.state = 'stop'
    
    @staticmethod
    def execute(data):
        print(f'back_board: {data}')
        
        if data == 'up':
            BackBoard.up()
        
        if data == 'down':
            BackBoard.down()
            
        if data == 'stop':
            BackBoard.stop()