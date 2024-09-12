import json

from ..joystick.joystick import Joystick

from .movement import Movement
from .front_board import FrontBoard
from .platform import Platform
from .ball_door import BallDoor
# from .top_machine import TopMachine
# from robot.arduino import Arduino

class CommandParser():
    @staticmethod
    def parse(command_str):
        if Joystick.exist:
            return 'using joystick!'
        
        command = json.loads(command_str)
        
        print(command['type'])
        
        if command['type'] == 'movement':
            Movement.execute(command['data'])
        elif command['type'] == 'front_board':
            FrontBoard.execute(command['data'])
        elif command['type'] == 'platform':
            Platform.execute(command['data'])
        elif command['type'] == 'ball_door':
            BallDoor.execute(command['data'])
            
        return 'done!'
    
        # if command['type'] == 'arduino':
        #     Arduino.execute(command['data'])
        #     pass