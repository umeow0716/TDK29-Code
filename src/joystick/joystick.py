import subprocess

from time import sleep
from os.path import exists
from threading import Thread

class Joystick:
    exist = False
    proc = None
    state = {
        'axis_r': (0, 0, False),
        'axis_l': (0, 0, False),
        'hat': (0, 0),
        'button_a': False,
        'button_b': False,
        'button_x': False,
        'button_y': False,
        'LB': False,
        'RB': False,
        'button_share': False,
        'button_menu': False,
        'button_start': False,
        'LT': 0,
        'RT': 0,
    }
        
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
                Joystick.proc.stdout.read(241)
            elif is_changed:
                Joystick.proc.kill()
                Joystick.proc = None
            sleep(2)
    
    @staticmethod
    def _process_readline():
        while True:
            packet = None
            try:
                if Joystick.proc is None:
                    continue
                
                char = Joystick.proc.stdout.read(1)
                if char == '\n':
                    header = Joystick.proc.stdout.read(4)
                    if header != 'Axes':
                        continue
                    data = Joystick.proc.stdout.read(168)
                    packet = char + header + data
                
                if packet is None:
                    continue
                    
                delimiters = [':']
 
                for delimiter in delimiters:
                    packet = ' '.join(packet.split(delimiter))
 
                arr = packet.split()
                
                axis_l_x = int(arr[2])
                axis_l_y = -int(arr[4])
                axis_l_button = 'on' == arr[-3]
                
                axis_r_x = int(arr[8])
                axis_r_y = -int(arr[10])
                axis_r_button = 'on' == arr[-1]
                
                hat_x = int(arr[14]) // 32767
                hat_y = -int(arr[16]) // 32767
                
                button_a = 'on' == arr[19]
                button_b = 'on' == arr[21]
                button_x = 'on' == arr[23]
                button_y = 'on' == arr[25]
                
                LB = 'on' == arr[27]
                RB = 'on' == arr[29]
                
                button_share = 'on' == arr[31]
                button_menu = 'on' == arr[33]
                button_start = 'on' == arr[35]
                
                LT = (int(arr[6]) + 32768) / 65535
                RT = (int(arr[12]) + 32768) / 65535
                
                Joystick.state['axis_l'] = (axis_l_x, axis_l_y, axis_l_button)
                Joystick.state['axis_r'] = (axis_r_x, axis_r_y, axis_r_button)
                Joystick.state['hat'] = (hat_x, hat_y)
                Joystick.state['button_a'] = button_a
                Joystick.state['button_b'] = button_b
                Joystick.state['button_x'] = button_x
                Joystick.state['button_y'] = button_y
                Joystick.state['LB'] = LB
                Joystick.state['RB'] = RB
                Joystick.state['button_share'] = button_share
                Joystick.state['button_menu'] = button_menu
                Joystick.state['button_start'] = button_start
                Joystick.state['LT'] = LT
                Joystick.state['RT'] = RT
            except Exception as err:
                print(err)
                pass
            
        
        