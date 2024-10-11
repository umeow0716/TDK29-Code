from random import randrange
from threading import Thread
from time import sleep

from src.joystick.joystick import Joystick
from src.websocket.websocket_server import WebSocketServer

from src.robot.command_parser import CommandParser
from src.robot.arduino.arduino import Arduino
from src.robot.raspberry.light import Light

# @Joystick.when_button_a_change_wrapper
# def f(value, *args, **kwargs):
#     if value and kwargs['previous_press_timestamp'] is not None:
#         d_time = kwargs['timestamp'] - kwargs['previous_press_timestamp']
#         print(d_time)
#         if d_time < 0.15:
#             Joystick.vibration()

def keep_alive():
    sleep(1000000)
    
def random_color():
    return (randrange(256), randrange(256), randrange(256))

def brightness_circle(light_number):
    length = Light.get_light_length(light_number)
    while True:
        for brightness in range(0, 100, 5):
            for i in range(length):
                Light.set_light_brightness(light_number, i, brightness * 0.01)
            sleep(0.5)
        for brightness in range(0, 100, 5)[::-1]:
            for i in range(length):
                Light.set_light_brightness(light_number, i, brightness * 0.01)
            sleep(0.5)
    
def star_light(light_number):
    length = Light.get_light_length(light_number)
    while True:
        for i in range(2, length+3):
            Light.set_light_color(light_number, i-3, 0, 0, 0)
            
            if Light.is_black(light_number, i-2):
                Light.set_light_color(light_number, i-2, *random_color())
            
            if Light.is_black(light_number, i-1):
                Light.set_light_color(light_number, i-1, *random_color())
            
            Light.set_light_color(light_number, i, *random_color())
            sleep(0.15)

def star_light_reverse(light_number):
    length = Light.get_light_length(light_number)
    while True:
        for i in range(-3, length)[::-1]:
            Light.set_light_color(light_number, i+3, 0, 0, 0)
            
            if Light.is_black(light_number, i+2):
                Light.set_light_color(light_number, i+2, *random_color())
            
            if Light.is_black(light_number, i+1):
                Light.set_light_color(light_number, i+1, *random_color())
            
            Light.set_light_color(light_number, i, *random_color())
            sleep(0.15)

if __name__ == '__main__':
    Joystick.start_thread()
    
    WebSocketServer.start_thread()
    
    Thread(target=Arduino.listening, daemon=True).start()
    
    sleep(0.8)
    
    Light.fill(0, 0, 255, 0)
    Light.fill(1, 255, 0, 0)
    
    Thread(target=brightness_circle, args=(0,), daemon=True).start()
    Thread(target=brightness_circle, args=(1,), daemon=True).start()
    Thread(target=star_light_reverse, args=(2,), daemon=True).start()
    sleep(1)
    Thread(target=star_light_reverse, args=(3,), daemon=True).start()
    
    
    while True:
        keep_alive()