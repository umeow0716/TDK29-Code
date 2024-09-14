import json

from time import sleep
from threading import Thread

from ..joystick.joystick import Joystick

from .movement import Movement
from .front_board import FrontBoard
from .back_board import BackBoard
from .platform import Platform
from .ball_door import BallDoor
from .catch_ball import CatchBall
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
        previous_menu = False
        while True:
            if not Joystick.jstest_exist:
                sleep(2)
                continue
            
            hat_x = Joystick.hat[0]
            hat_y = Joystick.hat[1]
            
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
            
            
            if Joystick.RB:
                FrontBoard.up()
            elif Joystick.state['RT'] > 0.8:
                FrontBoard.down()
            else:
                FrontBoard.stop()
            
            if Joystick.LB:
                BackBoard.up()
            elif Joystick.LT > 0.8:
                BackBoard.down()
            else:
                BackBoard.stop()
                
            if Joystick.button_x:
                Platform.up()
            elif Joystick.button_a:
                Platform.down()
            else:
                Platform.stop()

            if Joystick.button_y:
                CatchBall.up()
            elif Joystick.button_b:
                CatchBall.down()
            else:
                CatchBall.stop()
                
            if Joystick.button_menu and Joystick.button_menu != previous_menu:
                BallDoor.next_step()
            previous_menu = Joystick.button_menu
                
            sleep(0.05)