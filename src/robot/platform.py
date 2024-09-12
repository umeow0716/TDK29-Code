from .arduino.arduino_motor import ArduinoMotor 

class Platform:
    motor = ArduinoMotor(28, 29, 5)
    
    @staticmethod
    def execute(data):
        print(f'platform: {data}')
        
        if data == 'up':
            Platform.motor.forward()
        
        if data == 'down':
            Platform.motor.backward()
        
        if data == 'stop':
            Platform.motor.stop()