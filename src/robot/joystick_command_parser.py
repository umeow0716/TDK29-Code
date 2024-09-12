import json

class JoystickCommandParser():
    commands = {}
    
    @staticmethod
    def func_register_wrapper(name):
        def wrapper(func):
            JoystickCommandParser.commands[name] = func
            return func
        return wrapper
    
    @staticmethod
    def get_func_by_name(name):
        if name not in JoystickCommandParser.commands:
            return None
        return JoystickCommandParser.commands[name]
    
    @staticmethod
    def setting_controller(controller):
        file = open('joystick-setting.json', 'r', encoding='utf-8')
        setting_str = file.read()
        setting = json.loads(setting_str)
        
        for key in setting.keys():
            try:
                button = controller.__getattribute__(key)
            except:
                print(f'lost button: {key}')
                continue

            if 'when_pressed' in setting[key] and setting[key]['when_pressed'] is not None:
                button.when_pressed = JoystickCommandParser.get_func_by_name(setting[key]['when_pressed'])
            
            if 'when_released' in setting[key] and setting[key]['when_released'] is not None:
                button.when_released = JoystickCommandParser.get_func_by_name(setting[key]['when_released'])
            
            if 'when_moved' in setting[key] and setting[key]['when_moved'] is not None:
                button.when_moved = JoystickCommandParser.get_func_by_name(setting[key]['when_moved'])