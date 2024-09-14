from .arduino.arduino_motor import ArduinoMotor 

class Platform:
    motor = ArduinoMotor(26, 27, 5)
    state = 'stop'
    
    @staticmethod
    def up():
        if Platform.state == 'up':
            return
        Platform.motor.forward()
        Platform.state = 'up'
    
    @staticmethod
    def down():
        if Platform.state == 'down':
            return
        Platform.motor.backward()
        Platform.state = 'down'
    
    @staticmethod
    def stop():
        if Platform.state == 'stop':
            return
        Platform.motor.stop()
        Platform.state = 'stop'
    
    @staticmethod
    def execute(data):
        print(f'platform: {data}')
        
        if data == 'up':
            Platform.up()
        
        if data == 'down':
            Platform.down()
        
        if data == 'stop':
            Platform.stop()