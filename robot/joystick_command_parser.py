import json

class JoystickCommandParser():
    @staticmethod
    def get_func_by_name(name):
        return None
    
    @staticmethod
    def setting_controller(controller):
        file = open('joystick-setting.json', 'r', encoding='utf-8')
        setting_str = file.read()
        setting = json.loads(setting_str)
        
        for key in setting.keys():
            print(key)