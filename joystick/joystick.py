from time import sleep
from os.path import exists
from threading import Thread
from xbox360controller import Xbox360Controller
from robot.joystick_command_parser import JoystickCommandParser

class Joystick:
    exist = False
    controller = Xbox360Controller(0, axis_threshold=0.2)
    
    @staticmethod
    def get_state():
        if not Joystick.exist or Joystick.controller is None:
            return None
        
        return {
            'button_a': Joystick.controller.button_a.is_pressed,
            'button_b': Joystick.controller.button_b.is_pressed,
            'button_x': Joystick.controller.button_x.is_pressed,
            'button_y': Joystick.controller.button_y.is_pressed,
            'button_trigger_l': Joystick.controller.button_trigger_l.is_pressed,
            'button_trigger_r': Joystick.controller.button_trigger_r.is_pressed,
            'button_thumb_l': Joystick.controller.button_thumb_l.is_pressed,
            'button_thumb_r': Joystick.controller.button_thumb_r.is_pressed,
            'button_start': Joystick.controller.button_start.is_pressed,
            'button_select': Joystick.controller.button_select.is_pressed,
            'button_mode': Joystick.controller.button_mode.is_pressed,
            'axe_trigger_l': Joystick.controller.trigger_l.value,
            'axe_trigger_r': Joystick.controller.trigger_r.value,
            'axis_l': (round(Joystick.controller.axis_l.x, 2), -round(Joystick.controller.axis_l.y, 2)),
            'axis_r': (round(Joystick.controller.axis_r.x, 2), -round(Joystick.controller.axis_r.y, 2)),
            'hat': (Joystick.controller.hat._value_x, Joystick.controller.hat._value_y)
        }
        
    @staticmethod
    def start_thread():
        thread = Thread(target=Joystick._thread_job)
        thread.setDaemon(True)
        thread.start()
        
    @staticmethod
    def _thread_job():
        while True:
            exist_previous = Joystick.exist
            Joystick.exist = exists('/dev/input/js0')
            
            is_changed = exist_previous != Joystick.exist
        
            if Joystick.exist and is_changed:
                Joystick.controller = Xbox360Controller(0, axis_threshold=0.2)
                JoystickCommandParser.setting_controller(Joystick.controller)
            elif is_changed:
                Joystick.controller = None
            
            sleep(0.2)
            
        
        