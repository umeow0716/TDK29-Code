from evdev import ecodes
from src.joystick.joystick import Joystick

@Joystick.when_axis_hat_change_wrapper
def f(value, *args, **kwargs):
    print('axis_hat:', value)

@Joystick.when_axis_left_change_wrapper
def f(value, *args, **kwargs):
    print('axis_left:', value)
    
@Joystick.when_axis_right_change_wrapper
def f(value, *args, **kwargs):
    print('axis_right:', value)

@Joystick.when_button_a_change_wrapper
def f(value, *args, **kwargs):
    if value and kwargs['previous_press_timestamp'] is not None:
        d_time = kwargs['timestamp'] - kwargs['previous_press_timestamp']
        if d_time < 0.15:
            Joystick.dev.write(ecodes.EV_FF, 0, 1)
    print('button_a:', value)

@Joystick.when_button_b_change_wrapper
def f(value, *args, **kwargs):
    print('button_b:', value)

@Joystick.when_button_x_change_wrapper
def f(value, *args, **kwargs):
    print('button_x:', value)

@Joystick.when_button_y_change_wrapper
def f(value, *args, **kwargs):
    print('button_y:', value)

@Joystick.when_button_select_change_wrapper
def f(value, *args, **kwargs):
    print('button_select:', value)

@Joystick.when_button_start_change_wrapper
def f(value, *args, **kwargs):
    print('button_start:', value)

@Joystick.when_button_mode_change_wrapper
def f(value, *args, **kwargs):
    print('button_mode:', value)

@Joystick.when_lb_change_wrapper
def f(value, *args, **kwargs):
    print('lb:', value)

@Joystick.when_lt_change_wrapper
def f(value, *args, **kwargs):
    print('lt:', value)

@Joystick.when_rb_change_wrapper
def f(value, *args, **kwargs):
    print('rb:', value)

@Joystick.when_rt_change_wrapper
def f(value, *args, **kwargs):
    print('rt:', value)

def keep_alive():
    pass

if __name__ == '__main__':
    Joystick.start_thread()
    
    while True:
        keep_alive()