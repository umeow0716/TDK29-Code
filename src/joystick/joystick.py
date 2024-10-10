from evdev import InputDevice, ff, ecodes

from time import sleep
from os.path import exists
from threading import Thread

def safety_func_wrapper(func):
    def executor(*args, **kwargs):
        try:
            Thread(target=func, args=args, kwargs=kwargs, daemon=True).start()
        except Exception as err:
            print(err)
    return executor

class Joystick:
    exist = False
    dev = None
    
    button_a_change_func_list = []
    button_b_change_func_list = []
    button_x_change_func_list = []
    button_y_change_func_list = []
    button_select_change_func_list = []
    button_mode_change_func_list = []
    button_start_change_func_list = []
    
    button_a_previous_press_timestamp = None
    button_b_previous_press_timestamp = None
    button_x_previous_press_timestamp = None
    button_y_previous_press_timestamp = None
    
    lb_change_func_list = []
    lt_change_func_list = []
    
    rb_change_func_list = []
    rt_change_func_list = []
    
    axis_left_change_func_list = []
    axis_left_x = 0
    axis_left_y = 0
    axis_left_btn = False
    
    axis_right_change_func_list = []
    axis_right_x = 0
    axis_right_y = 0
    axis_right_btn = False
    
    axis_hat_change_func_list = []
    axis_hat_x = 0
    axis_hat_y = 0
    
    @staticmethod
    def when_button_a_change_wrapper(func):
        safety_func = safety_func_wrapper(func)
        Joystick.button_a_change_func_list.append(safety_func)
        
    @staticmethod
    def when_button_b_change_wrapper(func):
        safety_func = safety_func_wrapper(func)
        Joystick.button_b_change_func_list.append(safety_func)
        
    @staticmethod
    def when_button_x_change_wrapper(func):
        safety_func = safety_func_wrapper(func)
        Joystick.button_x_change_func_list.append(safety_func)
        
    @staticmethod
    def when_button_y_change_wrapper(func):
        safety_func = safety_func_wrapper(func)
        Joystick.button_y_change_func_list.append(safety_func)
        
    @staticmethod
    def when_button_select_change_wrapper(func):
        safety_func = safety_func_wrapper(func)
        Joystick.button_select_change_func_list.append(safety_func)
        
    @staticmethod
    def when_button_mode_change_wrapper(func):
        safety_func = safety_func_wrapper(func)
        Joystick.button_mode_change_func_list.append(safety_func)
        
    @staticmethod
    def when_button_start_change_wrapper(func):
        safety_func = safety_func_wrapper(func)
        Joystick.button_start_change_func_list.append(safety_func)
        
    @staticmethod
    def when_rb_change_wrapper(func):
        safety_func = safety_func_wrapper(func)
        Joystick.rb_change_func_list.append(safety_func)
        
    @staticmethod
    def when_lb_change_wrapper(func):
        safety_func = safety_func_wrapper(func)
        Joystick.lb_change_func_list.append(safety_func)
    
    @staticmethod
    def when_lt_change_wrapper(func):
        safety_func = safety_func_wrapper(func)
        Joystick.lt_change_func_list.append(safety_func)
    
    @staticmethod
    def when_rt_change_wrapper(func):
        safety_func = safety_func_wrapper(func)
        Joystick.rt_change_func_list.append(safety_func)
        
    @staticmethod
    def when_axis_left_change_wrapper(func):
        safety_func = safety_func_wrapper(func)
        Joystick.axis_left_change_func_list.append(safety_func)
    
    @staticmethod
    def when_axis_right_change_wrapper(func):
        safety_func = safety_func_wrapper(func)
        Joystick.axis_right_change_func_list.append(safety_func)
    
    @staticmethod
    def when_axis_hat_change_wrapper(func):
        safety_func = safety_func_wrapper(func)
        Joystick.axis_hat_change_func_list.append(safety_func)
    
    @staticmethod
    def start_thread():
        thread = Thread(target=Joystick._thread_job, daemon=True)
        thread.start()
        
        proc = Thread(target=Joystick._process_job, daemon=True)
        proc.start()
        
    @staticmethod
    def vibration():
        try:
            Joystick.dev.write(ecodes.EV_FF, 0, 1)
        except:
            pass
    
    @staticmethod
    def _thread_job():
        while True:
            evtest_exist_previous = Joystick.exist
            Joystick.exist = exists('/dev/input/by-id/usb-ASUSTeK_ROG_RAIKIRI_PRO_0123456789AB-event-joystick')
            
            is_changed = evtest_exist_previous != Joystick.exist
            
            if Joystick.exist and is_changed:
                Joystick.dev = InputDevice('/dev/input/by-id/usb-ASUSTeK_ROG_RAIKIRI_PRO_0123456789AB-event-joystick')
                rumble = ff.Rumble(strong_magnitude=0xffff, weak_magnitude=0x0000)
                effect_type = ff.EffectType(ff_rumble_effect=rumble)
                duration_ms = 3000

                effect = ff.Effect(
                    ecodes.FF_RUMBLE, -1, 0,
                    ff.Trigger(0, 0),
                    ff.Replay(duration_ms, 0),
                    effect_type
                )
                Joystick.dev.upload_effect(effect)
            elif is_changed:
                Joystick.dev = None
            sleep(5)
    
    @staticmethod
    def _process_job():
        try:
            while True:
                if Joystick.dev is None:
                    sleep(1)
                    continue
            
                for event in Joystick.dev.read_loop():
                    # print(event)
                    if event.type == 0:
                        pass
                    
                    elif event.code == 304:
                        for func in Joystick.button_a_change_func_list:
                            func(event.value, timestamp=event.timestamp(), previous_press_timestamp=Joystick.button_a_previous_press_timestamp)
                        if event.value:
                            Joystick.button_a_previous_press_timestamp = event.timestamp()
                    
                    elif event.code == 305:
                        for func in Joystick.button_b_change_func_list:
                            func(event.value, timestamp=event.timestamp(), previous_press_timestamp=Joystick.button_b_previous_press_timestamp)
                        if event.value:
                            Joystick.button_b_previous_press_timestamp = event.timestamp()
                    
                    elif event.code == 307:
                        for func in Joystick.button_x_change_func_list:
                            func(event.value, timestamp=event.timestamp(), previous_press_timestamp=Joystick.button_x_previous_press_timestamp)
                        if event.value:
                            Joystick.button_x_previous_press_timestamp = event.timestamp()
                    
                    elif event.code == 308:
                        for func in Joystick.button_y_change_func_list:
                            func(event.value, timestamp=event.timestamp(), previous_press_timestamp=Joystick.button_y_previous_press_timestamp)
                        if event.value:
                            Joystick.button_y_previous_press_timestamp = event.timestamp()
                    
                    elif event.code == 314:
                        for func in Joystick.button_select_change_func_list:
                            func(event.value)
                    
                    elif event.code == 315:
                        for func in Joystick.button_start_change_func_list:
                            func(event.value)
                    
                    elif event.code == 316:
                        for func in Joystick.button_mode_change_func_list:
                            func(event.value)
                            
                    elif event.code == 310:
                        for func in Joystick.lb_change_func_list:
                            func(event.value)
                    
                    elif event.code == 2:
                        for func in Joystick.lt_change_func_list:
                            func(event.value)
                    
                    elif event.code == 311:
                        for func in Joystick.rb_change_func_list:
                            func(event.value)
                    
                    elif event.code == 5:
                        for func in Joystick.rt_change_func_list:
                            func(event.value)
                            
                    elif event.code == 0:
                        Joystick.axis_left_x = event.value
                        for func in Joystick.axis_left_change_func_list:
                            func((Joystick.axis_left_x, Joystick.axis_left_y, Joystick.axis_left_btn))
                    
                    elif event.code == 1:
                        Joystick.axis_left_y = (-event.value) - 1
                        for func in Joystick.axis_left_change_func_list:
                            func((Joystick.axis_left_x, Joystick.axis_left_y, Joystick.axis_left_btn))
                    
                    elif event.code == 317:
                        Joystick.axis_left_btn = event.value
                        for func in Joystick.axis_left_change_func_list:
                            func((Joystick.axis_left_x, Joystick.axis_left_y, Joystick.axis_left_btn))
                            
                    elif event.code == 3:
                        Joystick.axis_right_x = event.value
                        for func in Joystick.axis_right_change_func_list:
                            func((Joystick.axis_right_x, Joystick.axis_right_y, Joystick.axis_right_btn))
                    
                    elif event.code == 4:
                        Joystick.axis_right_y = (-event.value) -1
                        for func in Joystick.axis_right_change_func_list:
                            func((Joystick.axis_right_x, Joystick.axis_right_y, Joystick.axis_right_btn))
                    
                    elif event.code == 318:
                        Joystick.axis_right_btn = event.value
                        for func in Joystick.axis_right_change_func_list:
                            func((Joystick.axis_right_x, Joystick.axis_right_y, Joystick.axis_right_btn))
                    
                    elif event.code == 16:
                        Joystick.axis_hat_x = event.value
                        for func in Joystick.axis_hat_change_func_list:
                            func((Joystick.axis_hat_x, Joystick.axis_hat_y))
                            
                    elif event.code == 17:
                        Joystick.axis_hat_y = -event.value
                        for func in Joystick.axis_hat_change_func_list:
                            func((Joystick.axis_hat_x, Joystick.axis_hat_y))
        except Exception as err:
            print(err)
            pass
        
        