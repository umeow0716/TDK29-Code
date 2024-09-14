from time import sleep
from .arduino.arduino_motor import ArduinoMotor

class Movement:
    left_wheel = ArduinoMotor(24, 25, 2)
    right_wheel = ArduinoMotor(22, 23, 3)
    
    state = 'stop'
    
    @staticmethod
    def forward():
        if Movement.state == 'forward':
            return
        print('forward')
        Movement.left_wheel.forward()
        Movement.right_wheel.forward()
        Movement.state = 'forward'
    
    @staticmethod
    def backward():
        if Movement.state == 'backward':
            return
        print('backward')
        Movement.left_wheel.backward()
        Movement.right_wheel.backward()
        Movement.state = 'backward'
    
    @staticmethod
    def right():
        if Movement.state == 'right':
            return
        print('right')
        Movement.left_wheel.forward()
        Movement.right_wheel.backward()
        Movement.state = 'right'
    
    @staticmethod
    def left():
        if Movement.state == 'left':
            return
        print('left')
        Movement.left_wheel.backward()
        Movement.right_wheel.forward()
        Movement.state = 'left'
    
    @staticmethod
    def stop():
        if Movement.state == 'stop':
            return
        print('stop')
        Movement.left_wheel.stop()
        Movement.right_wheel.stop()
        Movement.state = 'stop'
    
    @staticmethod
    def execute(direction, soft=False):
        print("movement:", direction)
        if direction == 'forward':
            Movement.forward()

        if direction == 'backward':
            Movement.backward()

        if direction == 'right':
            Movement.right()

        # if direction == 'right':  #麥輪
        #     # wheel process...
        #     Movement.right_ahead_wheel.backward()
        #     Movement.right_rear_wheel.forward()
        #     Movement.left_ahead_wheel.forward()
        #     Movement.left_rear_wheel.backward()
        #     pass

        if direction == 'left':
            Movement.left()

        # if direction == 'left':   #麥輪
        #     # wheel process...
        #     Movement.right_ahead_wheel.forward()
        #     Movement.right_rear_wheel.backward()
        #     Movement.left_ahead_wheel.backward()
        #     Movement.left_rear_wheel.forward()
        #     pass

        # if direction == 'clockwise':
        #     Movement.right_wheel.backward()
        #     Movement.left_wheel.forward()
        #     pass
            
        # if direction == 'counterclockwise':
        #     Movement.right_wheel.forward()
        #     Movement.left_wheel.backward()
        #     pass

        if direction == 'stop':
            Movement.stop()
        
        # if soft and direction != 'stop':
        #     for speed in range(100, 256):
        #         Movement.right_wheel.setSpeed(speed)
        #         Movement.left_wheel.setSpeed(speed)
        #         sleep(0.005)
        # elif soft:
        #     for speed in range(0, 101)[::-1]:
        #         Movement.right_wheel.setSpeed(speed)
        #         Movement.left_wheel.setSpeed(speed)
        #         sleep(0.005)
        #     Movement.right_wheel.stop()
        #     Movement.left_wheel.stop()
                