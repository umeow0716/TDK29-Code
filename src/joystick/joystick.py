import subprocess

from time import sleep
from os.path import exists
from threading import Thread
from xbox360controller import Xbox360Controller
from ..robot.joystick_command_parser import JoystickCommandParser

class Joystick:
    exist = False
    proc = None
    # controller = Xbox360Controller(0, axis_threshold=0)
    
    # @staticmethod
    # def get_state():
    #     if not Joystick.exist or Joystick.controller is None:
    #         return None
        
    #     return {
    #         'button_a': Joystick.controller.button_a.is_pressed,
    #         'button_b': Joystick.controller.button_b.is_pressed,
    #         'button_x': Joystick.controller.button_x.is_pressed,
    #         'button_y': Joystick.controller.button_y.is_pressed,
    #         'button_trigger_l': Joystick.controller.button_trigger_l.is_pressed,
    #         'button_trigger_r': Joystick.controller.button_trigger_r.is_pressed,
    #         'button_thumb_l': Joystick.controller.button_thumb_l.is_pressed,
    #         'button_thumb_r': Joystick.controller.button_thumb_r.is_pressed,
    #         'button_start': Joystick.controller.button_start.is_pressed,
    #         'button_select': Joystick.controller.button_select.is_pressed,
    #         'button_mode': Joystick.controller.button_mode.is_pressed,
    #         'axe_trigger_l': Joystick.controller.trigger_l.value,
    #         'axe_trigger_r': Joystick.controller.trigger_r.value,
    #         'axis_l': (round(Joystick.controller.axis_l.x, 2), -round(Joystick.controller.axis_l.y, 2)),
    #         'axis_r': (round(Joystick.controller.axis_r.x, 2), -round(Joystick.controller.axis_r.y, 2)),
    #         'hat': (Joystick.controller.hat._value_x, Joystick.controller.hat._value_y)
    #     }
        
    @staticmethod
    def start_thread():
        thread = Thread(target=Joystick._thread_job)
        thread.setDaemon(True)
        thread.start()
        
        proc_thread = Thread(target=Joystick._process_readline)
        proc_thread.setDaemon(True)
        proc_thread.start()
        
    @staticmethod
    def _thread_job():
        while True:
            exist_previous = Joystick.exist
            Joystick.exist = exists('/dev/input/js0')
            
            is_changed = exist_previous != Joystick.exist
        
            if Joystick.exist and is_changed:
                Joystick.proc = subprocess.Popen('jstest /dev/input/js0', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
                print(Joystick.proc.stdout.read(241).encode())
                # Joystick.controller = Xbox360Controller(0, axis_threshold=0)
                # JoystickCommandParser.setting_controller(Joystick.controller)
            elif is_changed:
                Joystick.proc.kill()
                Joystick.proc = None
                # Joystick.controller = None
            
            sleep(0.2)
    
    @staticmethod
    def _process_readline():
        while True:
            try:
                if Joystick.proc is None:
                    continue
                
                line = Joystick.proc.stdout.read(173).encode()
                print(line)
                # arr = [s for s in line.split(' ') if s]
                # print(line)
                # axis_l = (arr[2], -arr[4], arr[-3].split(':')[1])
                # axis_r = (arr[8], -arr[10], arr[-2].split(':')[1])
            except:
                pass
            
        
        