import json
from robot.movement import Movement
from robot.arduino import Arduino

class CommandParser():
    @staticmethod
    def parse(command_str):
        command = json.loads(command_str)
        
        print(command['type'])
        if command['type'] == 'movement':
            Movement.execute(command['data'])
            
        if command['type'] == 'arduino':
            Arduino.execute(command['data'])
            pass