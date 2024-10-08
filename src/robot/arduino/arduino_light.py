from time import sleep

from .arduino import Arduino

class ArduinoLight:
    light_color_list = [
        [
            [0, 0, 0] for _ in range(15)
        ],
        [
            [255, 255, 0] for _ in range(15)
        ],
        [
            [0, 0, 0] for _ in range(15)
        ],
        [
            [0, 0, 0] for _ in range(15)
        ]
    ]
    
    tick = 100
    
    @staticmethod
    def refresh():
        while True:
            for lightNumber in range(4):
                for lightIndex in range(15):
                    if ArduinoLight.tick:
                        Arduino.setColor(lightNumber, lightIndex, *ArduinoLight.light_color_list[lightNumber][lightIndex], True)
                        ArduinoLight.tick -= 1
                    sleep(0.01)