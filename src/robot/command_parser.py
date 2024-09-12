import json

from time import sleep
from threading import Thread

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
        
    @staticmethod
    def start_joystick_thread():
        thread = Thread(target=CommandParser._joystickParser_thread, daemon=True)
        thread.start()
        
    @staticmethod
    def _joystickParser_thread():
        while True:
            if not Joystick.exist:
                continue
            
            hat_x = Joystick.state['hat'][0]
            hat_y = Joystick.state['hat'][1]
            
            if hat_x == 0 and hat_y == 0:
                Movement.stop()
            elif hat_x == 0 and hat_y == 1:
                Movement.forward()
            elif hat_x == 0 and hat_y == -1:
                Movement.backward()
            elif hat_x == 1 and hat_y == 0:
                Movement.right()
            elif hat_x == -1 and hat_y == 0:
                Movement.left()
            elif hat_x == 1 and hat_y == 1:
                Movement.forward()
                Movement.right_wheel.setSpeed(128)
                Movement.left_wheel.setSpeed(255)
            elif hat_x == -1 and hat_y == 1:
                Movement.forward()
                Movement.right_wheel.setSpeed(255)
                Movement.left_wheel.setSpeed(128)
            elif hat_x == 1 and hat_y == -1:
                Movement.backward()
                Movement.right_wheel.setSpeed(128)
                Movement.left_wheel.setSpeed(255)
            elif hat_x == -1 and hat_y == -1:
                Movement.backward()
                Movement.right_wheel.setSpeed(255)
                Movement.left_wheel.setSpeed(128)
            
            sleep(0.1)