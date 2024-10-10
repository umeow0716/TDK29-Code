from random import randrange
from threading import Thread
from time import sleep

from src.joystick.joystick import Joystick
from src.websocket.websocket_server import WebSocketServer

from src.robot.command_parser import CommandParser
from src.robot.arduino.arduino import Arduino
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
    
def random_color():
    return (randrange(256), randrange(256), randrange(256))

def brightness_circle(lightNumber):
    length = len(ArduinoLight.light_color_list[lightNumber])
    while True:
        for brightness in range(0, 100, 5):
            for i in range(length):
                ArduinoLight.setLightBrightness(lightNumber, i, brightness * 0.01)
            sleep(0.5)
        for brightness in range(0, 100, 5)[::-1]:
            for i in range(length):
                ArduinoLight.setLightBrightness(lightNumber, i, brightness * 0.01)
            sleep(0.5)
    
def star_light(lightNumber):
    length = len(ArduinoLight.light_color_list[lightNumber])
    while True:
        for i in range(2, length+3):
            ArduinoLight.setLightColor(lightNumber, i-3, 0, 0, 0)
            
            if ArduinoLight.isBlack(lightNumber, i-2):
                ArduinoLight.setLightColor(lightNumber, i-2, *random_color())
            
            if ArduinoLight.isBlack(lightNumber, i-1):
                ArduinoLight.setLightColor(lightNumber, i-1, *random_color())
            
            ArduinoLight.setLightColor(lightNumber, i, *random_color())
            sleep(0.15)

def star_light_reverse(lightNumber):
    length = len(ArduinoLight.light_color_list[lightNumber])
    while True:
        for i in range(-3, length)[::-1]:
            ArduinoLight.setLightColor(lightNumber, i+3, 0, 0, 0)
            
            if ArduinoLight.isBlack(lightNumber, i+2):
                ArduinoLight.setLightColor(lightNumber, i+2, *random_color())
            
            if ArduinoLight.isBlack(lightNumber, i+1):
                ArduinoLight.setLightColor(lightNumber, i+1, *random_color())
            
            ArduinoLight.setLightColor(lightNumber, i, *random_color())
            sleep(0.15)

def refresh_light():
    while True:
        ArduinoLight.show()
        sleep(0.2)
    

if __name__ == '__main__':
    Joystick.start_thread()
    
    WebSocketServer.start_thread()
    
    Thread(target=Arduino.listening, daemon=True).start()
    
    sleep(0.8)
    
    # ArduinoLight.fill(0, 0, 255, 0)
    # ArduinoLight.fill(1, 255, 0, 0)
    
    # Thread(target=refresh_light, daemon=True).start()
    # Thread(target=ArduinoLight.refresh, daemon=True).start()
    
    # Thread(target=brightness_circle, args=(0,), daemon=True).start()
    # Thread(target=brightness_circle, args=(1,), daemon=True).start()
    # Thread(target=star_light_reverse, args=(2,), daemon=True).start()
    # sleep(1)
    # Thread(target=star_light_reverse, args=(3,), daemon=True).start()
    
    
    while True:
        keep_alive()