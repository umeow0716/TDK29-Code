from gpiozero import Motor

try:
    right_ahead_wheel = Motor(5, 6)
    right_rear_wheel = Motor(7, 8)

    left_ahead_wheel = Motor(9, 10)
    left_rear_wheel = Motor(11, 12)
except:
    pass

class Movement:
    @staticmethod
    def execute(direction):
        print(direction)
        if direction == 'forward':
            # wheel process...
            pass
        if direction == 'backward':
            # wheel process...
            pass
        if direction == 'right':
            # wheel process...
            pass
        if direction == 'left':
            # wheel process...
            pass
        if direction == 'stop':
            # wheel process...
            pass