from rpi_ws281x import *

# avaiable_pin = []

# for n in range(1, 26):
#     try:
#         Adafruit_NeoPixel(14, n).begin()
#         avaiable_pin.append(f"{n} 0")
#         continue
#     except:
#         pass
#     try:
#         Adafruit_NeoPixel(14, n, channel=1).begin()
#         avaiable_pin.append(f"{n} 1")
#         continue
#     except:
#         pass

# print(avaiable_pin)

# # strip = Adafruit_NeoPixel(14, 26)
# # strip.begin()

# # try:
# #     strip.setPixelColorRGB(0, 255, 0, 0)
# #     strip.show()
# # except Exception as err:
# #     print(err)
# #     pass

class Light:
    _light_color_list = [
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
    
    _light_brightness = [
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

    _light_list: list[Adafruit_NeoPixel] = [
        Adafruit_NeoPixel(14, 21, channel=0),
        Adafruit_NeoPixel(14, 19, channel=1),
        Adafruit_NeoPixel(14, 13, channel=1),
        Adafruit_NeoPixel(15, 12, channel=0)
    ]
    
    def getPixelColorRGB(light_number, light_index):
        if not Light.available_pos(light_number, light_index):
            return None
        
        return (
            int(Light._light_color_list[light_number][light_index][0] * Light._light_brightness[light_number][light_index]),
            int(Light._light_color_list[light_number][light_index][1] * Light._light_brightness[light_number][light_index]),
            int(Light._light_color_list[light_number][light_index][2] * Light._light_brightness[light_number][light_index]),
        )
    
    @staticmethod
    def begin():
        for i, light in enumerate(Light._light_list):
            light.begin()
            
            for j in range(Light.get_light_length(i)):
                light.setPixelColorRGB(i, *Light.getPixelColorRGB(i, j))
    
    @staticmethod
    def get_light_length(light_number):
        if not Light.available_pos(light_number):
            return None
        if light_number != 3:
            return 14
        else:
            return 15
    
    @staticmethod
    def availble_RGB(value):
        try:
            if 0 <= value < 256:
                return True
        except:
            pass
        
        return False
    
    @staticmethod
    def fill(light_number, r=None, g=None, b=None, need_update=True):
        if not Light.available_pos(light_number):
            return
                    
        for i in range(Light.get_light_length(light_number)):
            if Light.availble_RGB(r):
                Light._light_color_list[light_number][i][0] = r
            if Light.availble_RGB(g):
                Light._light_color_list[light_number][i][1] = g
            if Light.availble_RGB(b):
                Light._light_color_list[light_number][i][2] = b
            
            Light._light_list[light_number].setPixelColorRGB(i, *Light.getPixelColorRGB(light_number, i))
        
        if need_update:
            Light._light_list[light_number].show()
    
    @staticmethod
    def available_pos(light_number=None, light_index=None):
        if light_number is None and light_index is None:
            return False
        
        try:
            if light_number < 0 or light_number > 3:
                return False
            if light_index is None:
                return True
            if light_index < 0 or light_index >= Light.get_light_length(light_number):
                return False
            return True
        except:
            return False

    @staticmethod
    def is_black(light_number, light_index):
        if not Light.available_pos(light_number, light_index):
            return None
        
        try:
            return sum(Light._light_color_list[light_index][light_number]) == 0
        except:
            return True
    
    @staticmethod
    def set_light_color(light_number, light_index, r=None, g=None, b=None, need_update=True):
        if not Light.available_pos(light_number, light_index):
            return None
        
        if Light.availble_RGB(r):
            Light._light_color_list[light_number][light_index][0] = r
        if Light.availble_RGB(g):
            Light._light_color_list[light_number][light_index][1] = g
        if Light.availble_RGB(b):
            Light._light_color_list[light_number][light_index][2] = b
        
        Light._light_list[light_number].setPixelColorRGB(light_index, *Light.getPixelColorRGB(light_number, light_index))
        
        if need_update:
            Light._light_list[light_number].show()
    
    @staticmethod
    def set_light_brightness(light_number, light_index, val, need_update=True):
        if not Light.available_pos(light_number, light_index):
            return None
        
        try:
            if val < 0 or val > 1:
                return None
        except:
            return None
        
        Light._light_brightness[light_number][light_index] = val
        Light._light_list[light_number].setPixelColorRGB(light_index, *Light.getPixelColorRGB(light_number, light_index))
        
        if need_update:
            Light._light_list[light_number].show()
        