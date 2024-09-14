import subprocess

from time import sleep
from os.path import exists
from threading import Thread

class Joystick:
    jstest_exist = False
    jstest_proc = None
    evtest_exist = False
    evtest_proc = None
    
    axis_r = (0, 0, False)
    axis_l = (0, 0, False)
    hat = (0, 0)
    button_a = False
    button_b = False
    button_x = False
    button_y = False
    LB = False
    RB = False
    button_select = False
    button_menu = False
    button_start = False
    LT = 0
    RT = 0
    
    button_a_press_func_list = []
    button_b_press_func_list = []
    button_x_press_func_list = []
    button_y_press_func_list = []
    
    button_a_release_func_list = []
    button_b_release_func_list = []
    button_x_release_func_list = []
    button_y_release_func_list = []
    
    @staticmethod
    def when_button_a_press_wrapper(func):
        Joystick.button_a_press_func_list.append(func)
        
    @staticmethod
    def start_thread():
        jstest_thread = Thread(target=Joystick._jstest_thread_job)
        jstest_thread.setDaemon(True)
        jstest_thread.start()
        
        jstest_proc = Thread(target=Joystick._process_jstest_readline)
        jstest_proc.setDaemon(True)
        jstest_proc.start()
        
        evtest_thread = Thread(target=Joystick._evtest_thread_job)
        evtest_thread.setDaemon(True)
        evtest_thread.start()
        
        evtest_proc = Thread(target=Joystick._process_evtest_readline)
        evtest_proc.setDaemon(True)
        evtest_proc.start()
        
    @staticmethod
    def _jstest_thread_job():
        while True:
            jstest_exist_previous = Joystick.jstest_exist
            Joystick.jstest_exist = exists('/dev/input/js0')
            
            is_changed = jstest_exist_previous != Joystick.jstest_exist
        
            if Joystick.jstest_exist and is_changed:
                Joystick.jstest_proc = subprocess.Popen('jstest /dev/input/js0', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
                Joystick.jstest_proc.stdout.read(241)
            elif is_changed:
                Joystick.jstest_proc.kill()
                Joystick.jstest_exist = None
            sleep(5)
    
    @staticmethod
    def _process_jstest_readline():
        while True:
            packet = None
            try:
                if Joystick.jstest_proc is None:
                    sleep(2)
                    continue
                
                char = Joystick.jstest_proc.stdout.read(1)
                if char == '\n':
                    header = Joystick.jstest_proc.stdout.read(4)
                    if header != 'Axes':
                        continue
                    data = Joystick.jstest_proc.stdout.read(168)
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
                
                button_select = 'on' == arr[31]
                button_menu = 'on' == arr[33]
                button_start = 'on' == arr[35]
                
                LT = (int(arr[6]) + 32768) / 65535
                RT = (int(arr[12]) + 32768) / 65535
                
                Joystick.axis_l = (axis_l_x, axis_l_y, axis_l_button)
                Joystick.axis_r = (axis_r_x, axis_r_y, axis_r_button)
                Joystick.hat = (hat_x, hat_y)
                Joystick.button_a = button_a
                Joystick.button_b = button_b
                Joystick.button_x = button_x
                Joystick.button_y = button_y
                Joystick.LB = LB
                Joystick.RB = RB
                Joystick.button_select = button_select
                Joystick.button_menu = button_menu
                Joystick.button_start = button_start
                Joystick.LT = LT
                Joystick.RT = RT
            except Exception as err:
                print(err)
                pass
    
    @staticmethod
    def _evtest_thread_job():
        while True:
            evtest_exist_previous = Joystick.evtest_exist
            Joystick.evtest_exist = exists('/dev/input/by-id/usb-ASUSTeK_ROG_RAIKIRI_PRO_0123456789AB-event-joystick')
            
            is_changed = evtest_exist_previous != Joystick.evtest_exist
            
            if Joystick.evtest_exist and is_changed:
                Joystick.evtest_proc = subprocess.Popen('evtest /dev/input/by-id/usb-ASUSTeK_ROG_RAIKIRI_PRO_0123456789AB-event-joystick', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            elif is_changed:
                Joystick.evtest_proc.kill()
                Joystick.evtest_proc = None
            sleep(5)
    
    @staticmethod
    def _process_evtest_readline():
        while True:
            try:
                if Joystick.evtest_proc is None:
                    sleep(5)
                    continue
                
                line = Joystick.evtest_proc.stdout.readline().decode('utf-8')
                
                if not line.startswith('Event:'):
                    continue
                
                arr = line.split(',')

                if not arr[2].startswith(' code'):
                    continue
                    
                code_num = int(arr[2].split(' ')[2])
                
                value_num = None
                
                if arr[3].startswith(' value'):
                    value_num = int(arr[3].split(' ')[2])
                
                print(code_num)
                print(value_num)
                
                if code_num == 304 and value_num == 1:
                    for func in Joystick.button_a_press_func_list:
                        func()
            except:
                pass
        
        