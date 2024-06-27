import json
from robot.movement import Movement

class CommandParser():
    @staticmethod
    def parse(command_str):
        command = json.loads(command_str)
        if command['type'] == 'movement':
            Movement.execute(command['data'])