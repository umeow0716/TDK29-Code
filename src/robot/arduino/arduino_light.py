from time import sleep
from threading import Thread

from .arduino import Arduino

class ArduinoLight:
    tick = 120
    _thread = None
    
    light_color_list = [
        [
            [0, 0, 0] for _ in range(14)
        ],
        [
            [0, 0, 0] for _ in range(14)
        ],
        [
            [0, 0, 0] for _ in range(14)
        ],
        [
            [0, 0, 0] for _ in range(15)
        ]
    ]
    
    light_brightness = [
        [
            1 for _ in range(14)
        ],
        [
            1 for _ in range(14)
        ],
        [
            1 for _ in range(14)
        ],
        [
            1 for _ in range(15)
        ]
    ]
    
    @staticmethod
    def fill(lightNumber, r=None, g=None, b=None):
        for i in range(14):
            if r is not None:
                ArduinoLight.light_color_list[lightNumber][i][0] = r
            if g is not None:
                ArduinoLight.light_color_list[lightNumber][i][1] = g
            if b is not None:
                ArduinoLight.light_color_list[lightNumber][i][2] = b
        
            ArduinoLight.setLightColor(lightNumber, i, *ArduinoLight.light_color_list[lightNumber][i])
    
    @staticmethod
    def isBlack(lightNumber, lightIndex):
        try:
            return sum(ArduinoLight.light_color_list[lightNumber][lightIndex]) == 0
        except:
            return True
    
    @staticmethod
    def setLightBrightness(lightNumber, lightIndex, val):
        if lightNumber < 0 or lightNumber > 3:
            return
        if lightIndex < 0 or lightIndex > 14:
            return
        
        if lightNumber < 3 and lightIndex > 13:
            return
        if lightNumber == 3 and lightIndex > 14:
            return
        
        if val < 0 or val > 1:
            return
        
        ArduinoLight.light_brightness[lightNumber][lightIndex] = val
        
        output_r = ArduinoLight.light_color_list[lightNumber][lightIndex][0] * val
        output_g = ArduinoLight.light_color_list[lightNumber][lightIndex][1] * val
        output_b = ArduinoLight.light_color_list[lightNumber][lightIndex][2] * val
        
        Arduino.setColor(lightNumber, lightIndex, int(output_r), int(output_g), int(output_b))
    
    
    @staticmethod
    def setLightColor(lightNumber, lightIndex, r=None, g=None, b=None):
        if lightNumber < 0 or lightNumber > 3:
            return
        if lightIndex < 0 or lightIndex > 14:
            return
        
        if lightNumber < 3 and lightIndex > 13:
            return
        if lightNumber == 3 and lightIndex > 14:
            return
        
        if r is not None:
            ArduinoLight.light_color_list[lightNumber][lightIndex][0] = r
        
        if g is not None: 
            ArduinoLight.light_color_list[lightNumber][lightIndex][1] = g
        
        if b is not None:
            ArduinoLight.light_color_list[lightNumber][lightIndex][2] = b
        
        output_r = ArduinoLight.light_color_list[lightNumber][lightIndex][0] * ArduinoLight.light_brightness[lightNumber][lightIndex]
        output_g = ArduinoLight.light_color_list[lightNumber][lightIndex][1] * ArduinoLight.light_brightness[lightNumber][lightIndex]
        output_b = ArduinoLight.light_color_list[lightNumber][lightIndex][2] * ArduinoLight.light_brightness[lightNumber][lightIndex]
        
        Arduino.setColor(lightNumber, lightIndex, int(output_r), int(output_g), int(output_b))
    
    @staticmethod
    def show():
        Arduino.show()
        
    @staticmethod
    def refresh():
        while True:
            for lightNumber in range(4):
                for lightIndex, _ in enumerate(ArduinoLight.light_color_list[lightNumber]):
                    r, g, b = ArduinoLight.light_color_list[lightNumber][lightIndex]
                    r *= ArduinoLight.light_brightness[lightNumber][lightIndex]
                    g *= ArduinoLight.light_brightness[lightNumber][lightIndex]
                    b *= ArduinoLight.light_brightness[lightNumber][lightIndex]
                    Arduino.setColor(lightNumber, lightIndex, int(r), int(g), int(b))
            sleep(2)
            