from .arduino.arduino_motor import ArduinoMotor

class FrontBoard:
    motor = ArduinoMotor(27, 26, 4)
    
    @staticmethod
    def execute(data):
        print(f'front_board: {data}')
        
        if data == 'up':
            FrontBoard.motor.forward()
        
        if data == 'down':
            FrontBoard.motor.backward()
            
        if data == 'stop':
            FrontBoard.motor.stop()