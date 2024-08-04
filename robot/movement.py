from .arduino.arduino_motor import ArduinoMotor
from .raspberry.motor import Motor

class Movement:
    right_wheel = ArduinoMotor(22, 23, 2)
    left_wheel = ArduinoMotor(24, 25, 3)
    
    right_wheel.stop()
    left_wheel.stop()
    
    @staticmethod
    def execute(direction):
        print("movement:", direction)
        if direction == 'forward':
            # wheel process...
            Movement.right_wheel.forward()
            Movement.left_wheel.forward()
            pass

        if direction == 'backward':
            # wheel process...
            Movement.right_wheel.backward()
            Movement.left_wheel.backward()
            pass

        if direction == 'right':
            # wheel process...
            Movement.left_wheel.forward()
            pass

        # if direction == 'right':  #麥輪
        #     # wheel process...
        #     Movement.right_ahead_wheel.backward()
        #     Movement.right_rear_wheel.forward()
        #     Movement.left_ahead_wheel.forward()
        #     Movement.left_rear_wheel.backward()
        #     pass

        if direction == 'left':
            # wheel process...
            Movement.right_wheel.forward()
            pass

        # if direction == 'left':   #麥輪
        #     # wheel process...
        #     Movement.right_ahead_wheel.forward()
        #     Movement.right_rear_wheel.backward()
        #     Movement.left_ahead_wheel.backward()
        #     Movement.left_rear_wheel.forward()
        #     pass

        if direction == 'clockwise':
            Movement.right_wheel.backward()
            Movement.left_wheel.forward()
            pass
            
        if direction == 'counterclockwise':
            Movement.right_wheel.forward()
            Movement.left_wheel.backward()
            pass

        if direction == 'stop':
            # wheel process...
            Movement.right_wheel.stop()
            Movement.left_wheel.stop()
            pass