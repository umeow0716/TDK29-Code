from time import sleep
from .arduino.arduino_motor import ArduinoMotor

class Movement:
    left_wheel = ArduinoMotor(22, 23, 2)
    right_wheel = ArduinoMotor(24, 25, 3)
    
    @staticmethod
    def execute(direction, soft=True):
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
            Movement.right_wheel.backward()
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
            Movement.left_wheel.backward()
            Movement.right_wheel.forward()
            pass

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

        if not soft and direction == 'stop':
            # wheel process...
            Movement.right_wheel.stop()
            Movement.left_wheel.stop()
            pass
        
        if soft and direction != 'stop':
            for speed in range(100, 256):
                Movement.right_wheel.setSpeed(speed)
                Movement.left_wheel.setSpeed(speed)
                sleep(0.005)
        elif soft:
            for speed in range(0, 101)[::-1]:
                Movement.right_wheel.setSpeed(speed)
                Movement.left_wheel.setSpeed(speed)
                sleep(0.005)
            Movement.right_wheel.stop()
            Movement.left_wheel.stop()
                