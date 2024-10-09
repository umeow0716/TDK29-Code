from time import sleep
from threading import Thread

from .arduino import Arduino

class ArduinoLight:
    light_color_list = [
        [
            [0, 0, 0] for _ in range(15)
        ],
        [
            [0, 0, 0] for _ in range(15)
        ],
        [
            [0, 0, 0] for _ in range(15)
        ],
        [
            [0, 0, 0] for _ in range(15)
        ]
    ]
    
    @staticmethod
    def setLightColor(lightNumber, lightIndex, r=None, g=None, b=None):
        if r is not None:
            ArduinoLight.light_color_list[lightNumber][lightIndex][0] = r
        
        if g is not None: 
            ArduinoLight.light_color_list[lightNumber][lightIndex][1] = g
        
        if b is not None:
            ArduinoLight.light_color_list[lightNumber][lightIndex][2] = b
    
    @staticmethod
    def show():
        Thread(target=ArduinoLight._refresh_thread, daemon=True).start()
    
    @staticmethod
    def _refresh_thread(tick=120):
        while True:
            for lightNumber in range(4):
                for lightIndex in range(15):
                    Arduino.setColor(lightNumber, lightIndex, *ArduinoLight.light_color_list[lightNumber][lightIndex], True)
                    tick -= 1
                    
                    if not tick:
                        return
                    
                    sleep(0.005)