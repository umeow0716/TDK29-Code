
import RPi.GPIO as GPIO

import src.joystick.joystick_event
from src.joystick.joystick import Joystick
from src.websocket.websocket_server import WebSocketServer

def keep_alive():
    pass

if __name__ == '__main__':
    Joystick.start_thread()
    WebSocketServer.start_thread()
    
    while True:
        keep_alive()