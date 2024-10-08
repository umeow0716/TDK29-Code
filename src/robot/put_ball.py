from time import sleep
from ..joystick.joystick import Joystick
from .raspberry.servo import Servo

class PutBall():
    first = True
    last_button_state = 0
    
    servos = {
        3: Servo(3, mode=360),
        4: Servo(4, mode=360),
        17: Servo(17, mode=360),
    }
    
    state = {
        3: 0,
        4: 0,
        17: 0,
    }
    
    button_0_last_state = 0
    button_1_last_state = 0
    
    @Joystick.when_axis_right_change_wrapper
    def reset(value, *args, **kwargs):
        if value[2] and PutBall.last_button_state != value[2]:
            PutBall.first = True
        PutBall.last_button_state = value[2]
    
    def change_servo_state(pin, value):
        if value == 0 and PutBall.state[pin] != 1:
            PutBall.stop(pin)
        
        if value == 0:
            return
        
        if PutBall.state[pin] == 0:
            PutBall.state[pin] += 1
            PutBall.ccw(pin)
        elif PutBall.state[pin] == 1:
            PutBall.state[pin] = 0
            PutBall.cw(pin)
    
    def cw(pin):
        print(f'put_ball{pin}: cw')
        PutBall.servos[pin].write(3)
    
    def ccw(pin):
        print(f'put_ball{pin}: ccw')
        PutBall.servos[pin].write(12)
    
    def stop(pin):
        print(f'put_ball{pin}: stop')
        PutBall.servos[pin].write(7.5)
        sleep(0.5)
        PutBall.servos[pin].write(0)
    
    @Joystick.when_axis_hat_change_wrapper
    def joystick_update(value, *args, **kwargs):
        if (value[0] == -1 or PutBall.servos[3].angle != 0) and value[0] != PutBall.button_0_last_state:
            PutBall.change_servo_state(3, value[0])

        elif (value[1] == 1 or PutBall.servos[4].angle != 0) and value[1] != PutBall.button_1_last_state:
            PutBall.change_servo_state(4, value[1])
        
        elif (value[0] == 1 or PutBall.servos[17].angle != 0) and value[0] != PutBall.button_0_last_state:
            PutBall.change_servo_state(17, value[0])

        PutBall.button_0_last_state = value[0]
        PutBall.button_1_last_state = value[1]

        
    
    @staticmethod
    def execute(data):
        pass