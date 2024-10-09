from threading import Thread
from time import sleep

from src.joystick.joystick import Joystick
from src.websocket.websocket_server import WebSocketServer

from src.robot.command_parser import CommandParser
from src.robot.arduino.arduino_light import ArduinoLight

# @Joystick.when_button_a_change_wrapper
# def f(value, *args, **kwargs):
#     if value and kwargs['previous_press_timestamp'] is not None:
#         d_time = kwargs['timestamp'] - kwargs['previous_press_timestamp']
#         print(d_time)
#         if d_time < 0.15:
#             Joystick.vibration()

def keep_alive():
    sleep(1000000)

if __name__ == '__main__':
    Joystick.start_thread()
    
    WebSocketServer.start_thread()
    
    while True:
        keep_alive()