from time import sleep
import json
from src.joystick.joystick import Joystick
import src.joystick.joystick_event

Joystick.start_thread()

while True:
    sleep(1)