from gpiozero import Motor, LED

try:
    right_ahead_wheel = Motor(24, 23)
    right_rear_wheel = Motor(26, 19)

    left_ahead_wheel = Motor(27, 17)
    left_rear_wheel = Motor(5, 6)

    pwm0 = LED(21)
    pwm1 = LED(20)
    pwm2 = LED(12)
    pwm3 = LED(13)
    pwm0.on()
    pwm1.on()
    pwm2.on()
    pwm3.on()

except:
    pass

class Movement:
    @staticmethod
    def execute(direction):
        print("movement:", direction)
        if direction == 'forward':
            # wheel process...
            right_ahead_wheel.forward()
            right_rear_wheel.forward()
            left_ahead_wheel.forward()
            left_rear_wheel.forward()
            pass

        if direction == 'backward':
            # wheel process...
            right_ahead_wheel.backward()
            right_rear_wheel.backward()
            left_ahead_wheel.backward()
            left_rear_wheel.backward()
            pass

        # if direction == 'right':
        #     # wheel process...
        #     right_ahead_wheel.backward()
        #     right_rear_wheel.backward()
        #     left_ahead_wheel.forward()
        #     left_rear_wheel.forward()
        #     pass

        if direction == 'right':  #麥輪
            # wheel process...
            right_ahead_wheel.backward()
            right_rear_wheel.forward()
            left_ahead_wheel.forward()
            left_rear_wheel.backward()
            pass

        # if direction == 'left':
        #     # wheel process...
        #     right_ahead_wheel.forward()
        #     right_rear_wheel.forward()
        #     left_ahead_wheel.backward()
        #     left_rear_wheel.backward()
        #     pass

        if direction == 'left':   #麥輪
            # wheel process...
            right_ahead_wheel.forward()
            right_rear_wheel.backward()
            left_ahead_wheel.backward()
            left_rear_wheel.forward()
            pass

        if direction == 'stop':
            # wheel process...
            right_ahead_wheel.stop()
            right_rear_wheel.stop()
            left_ahead_wheel.stop()
            left_rear_wheel.stop()
            pass