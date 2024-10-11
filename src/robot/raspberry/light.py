from colorsys import hls_to_rgb
from random import randrange
from threading import Thread
from time import sleep
from rpi_ws281x import *
from math import inf

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
            [0, 0, 0] for _ in range(15)
        ]
    ]
    
    _light_brightness = [
        [
            1 for _ in range(14)
        ],
        [
            1 for _ in range(15)
        ],
    ]

    _light_list: list[Adafruit_NeoPixel] = [
        Adafruit_NeoPixel(14, 21, channel=0),
        Adafruit_NeoPixel(15, 19, channel=1),
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
                light.setPixelColorRGB(j, 0, 0, 0)
                
            light.show()
    
    @staticmethod
    def get_light_length(light_number):
        if not Light.available_pos(light_number):
            return None
        if light_number != 1:
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
            if light_number < 0 or light_number > 1:
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
            return None
    
    @staticmethod
    def set_light_color(light_number, light_index, r=None, g=None, b=None, need_update=True):
        if not Light.available_pos(light_number, light_index):
            if need_update:
                Light._light_list[light_number].show()
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
    
    @staticmethod
    def random_color():
        r = randrange(256)
        g = randrange(256)
        b = randrange(256)
        
        if r - g - b > 180:
            return Light.random_color()
        
        if g - r - b > 180:
            return Light.random_color()
        
        if b - r - g > 180:
            return Light.random_color()
        
        return (r, g, b)
    
    @staticmethod       
    def double_star_light(light_number, brightness=1.0):
        length = Light.get_light_length(light_number)
        
        for i in range(length):
            Light.set_light_brightness(light_number, i, brightness, False)
        
        while True:
            print(Light.afk_tick)
            Light.afk_tick += 1
            
            if Light.afk_tick > 30:
                Light.is_afk = True
                
            up_index = length-1
            down_index = 0
            while up_index >= down_index:
                if Light.up_tick or Light.down_tick or Light.is_afk:
                    return
                Light.set_light_color(light_number, up_index, *Light.random_color(), need_update=False)
                Light.set_light_color(light_number, down_index, *Light.random_color(), need_update=False)
                
                Light.set_light_color(light_number, up_index+3, 0, 0, 0, need_update=False)
                Light.set_light_color(light_number, down_index-3, 0, 0, 0)
                up_index -= 1
                down_index += 1
                sleep(0.15)
                
            up_index += 1
            down_index -= 1
                
            end_up = up_index
            end_down = down_index
            
            for d in range(1, 4)[::-1]:
                if Light.up_tick or Light.down_tick or Light.is_afk:
                    return
                Light.set_light_color(light_number, up_index+d, 0, 0, 0, need_update=False)
                Light.set_light_color(light_number, down_index-d, 0, 0, 0)
                sleep(0.15)
            
            while down_index > 0 or up_index < length:
                if Light.up_tick or Light.down_tick or Light.is_afk:
                    return
                Light.set_light_color(light_number, up_index, *Light.random_color(), need_update=False)
                Light.set_light_color(light_number, down_index, *Light.random_color())
                
                if up_index-3 >= end_up:
                    Light.set_light_color(light_number, up_index-3, 0, 0, 0, need_update=False)
                
                if down_index-3 <= end_down:
                    Light.set_light_color(light_number, down_index+3, 0, 0, 0)
                    
                up_index += 1
                down_index -= 1
                sleep(0.15)
            
            for d in range(1, 4)[::-1]:
                if Light.up_tick or Light.down_tick or Light.is_afk:
                    return
                Light.set_light_color(light_number, up_index-d, 0, 0, 0, need_update=False)
                Light.set_light_color(light_number, down_index+d, 0, 0, 0)
                sleep(0.15)
    
    @staticmethod
    def star_light(light_number, brightness=1):
        length = Light.get_light_length(light_number)
        
        for i in range(length):
            Light.set_light_brightness(light_number, i, brightness, False)
            
        while True:
            for i in range(2, length+3):
                if not Light.up_tick:
                    return
                
                Light.set_light_color(light_number, i-3, 0, 0, 0, need_update=False)
                
                if Light.is_black(light_number, i-2):
                    Light.set_light_color(light_number, i-2, *Light.random_color(), need_update=False)
                
                if Light.is_black(light_number, i-1):
                    Light.set_light_color(light_number, i-1, *Light.random_color(), need_update=False)
                
                Light.set_light_color(light_number, i, *Light.random_color())
                sleep(0.15)
                
    @staticmethod
    def star_light_reverse(light_number, brightness=1):
        length = Light.get_light_length(light_number)
        
        for i in range(length):
            Light.set_light_brightness(light_number, i, brightness, False)
            
        while True:
            for i in range(-3, length)[::-1]:
                if not Light.down_tick:
                    return
                
                Light.set_light_color(light_number, i+3, 0, 0, 0, need_update=True)
                
                if Light.is_black(light_number, i+2):
                    Light.set_light_color(light_number, i+2, *Light.random_color(), need_update=False)
                
                if Light.is_black(light_number, i+1):
                    Light.set_light_color(light_number, i+1, *Light.random_color(), need_update=False)
                
                Light.set_light_color(light_number, i, *Light.random_color())
                sleep(0.15)
                
    @staticmethod
    def rainbow(light_number, brightness=1.0):
        length = Light.get_light_length(light_number)
        h = 0
        
        for i in range(length):
            Light.set_light_brightness(light_number, i, brightness, False)
            
        while True:
            if h >= 1:
                h -= 1
            for i in range(length):
                if not Light.is_afk:
                    return
                target_h = h + (i * 0.01)
                if target_h >= 1:
                    target_h -= 1
                
                r, g, b = hls_to_rgb(target_h, 0.5, 1)
                r *= 255
                g *= 255
                b *= 255
                Light.set_light_color(light_number, i, r, g, b, i==length-1)
            h += 0.02
            sleep(0.05)
    
    up_tick = 0
    down_tick = 0
    
    @staticmethod
    def robot_up():
        Light.up_tick = inf
        Light.down_tick = 0
        Light.fill(0, 0, 0, 0)
        Light.fill(1, 0, 0, 0)

    @staticmethod
    def robot_down():
        Light.up_tick = 0
        Light.down_tick = inf
        Light.fill(0, 0, 0, 0)
        Light.fill(1, 0, 0, 0)
    
    @staticmethod
    def robot_stop():
        if Light.up_tick:
            Light.up_tick = 10
            Light.down_tick = 0
            Light.is_afk = False
        elif Light.down_tick:
            Light.up_tick = 0
            Light.down_tick = 10
            Light.is_afk = False
        else:
            Light.up_tick = 0
            Light.down_tick = 0
            Light.is_afk = False
    
    @staticmethod
    def robot_noafk():
        Light.is_afk = False
        Light.afk_tick = 0
    
    is_afk = False
    afk_tick = 0
    afk_light1 = None
    afk_light2 = None
    
    idle_light1 = None
    idle_light2 = None
    
    up_light1 = None
    up_light2 = None
    
    down_light1 = None
    down_light2 = None
    
    @staticmethod
    def afk_thread_state():
        return (
            Light.afk_light1 is not None and Light.afk_light1.is_alive(),
            Light.afk_light2 is not None and Light.afk_light2.is_alive(),
        )
    
    @staticmethod
    def idle_thread_state():
        return (
            Light.idle_light1 is not None and Light.idle_light1.is_alive(),
            Light.idle_light2 is not None and Light.idle_light2.is_alive(),
        )

    @staticmethod
    def up_thread_state():
        return (
            Light.up_light1 is not None and Light.up_light1.is_alive(),
            Light.up_light2 is not None and Light.up_light2.is_alive(),
        )
    
    @staticmethod
    def down_thread_state():
        return (
            Light.down_light1 is not None and Light.down_light1.is_alive(),
            Light.down_light2 is not None and Light.down_light2.is_alive(),
        )
            
    
    @staticmethod
    def robot():
        while True:
            if Light.up_tick > 0:
                Light.up_tick -= 1
            elif Light.up_tick <= 0:
                Light.up_tick = 0
                
            if Light.down_tick > 0:
                Light.down_tick -= 1
            elif Light.down_tick <= 0:
                Light.down_tick = 0
                
            # print(Light.up_tick, Light.down_tick)
            
            if Light.up_tick:
                state = Light.up_thread_state()
                
                if not state[0]:
                    Light.fill(0, 0, 0, 0)
                    Light.up_light1 = Thread(target=Light.star_light, args=(0,), daemon=True)
                    Light.up_light1.start()
                
                if not state[1]:
                    Light.fill(1, 0, 0, 0)
                    Light.up_light2 = Thread(target=Light.star_light, args=(1,), daemon=True)
                    Light.up_light2.start()
            elif Light.down_tick:
                state = Light.down_thread_state()
                
                if not state[0]:
                    Light.fill(0, 0, 0, 0)
                    Light.down_light1 = Thread(target=Light.star_light_reverse, args=(0,), daemon=True)
                    Light.down_light1.start()
                
                if not state[1]:
                    Light.fill(1, 0, 0, 0)
                    Light.down_light2 = Thread(target=Light.star_light_reverse, args=(1,), daemon=True)
                    Light.down_light2.start()
            elif not Light.is_afk:
                state = Light.idle_thread_state()
                if not state[0]:
                    Light.afk_tick = 0
                    Light.fill(0, 0, 0, 0)
                    Light.idle_light1 = Thread(target=Light.double_star_light, args=(0, ), daemon=True)
                    Light.idle_light1.start()
                
                if not state[1]:
                    Light.afk_tick = 0
                    Light.fill(1, 0, 0, 0)
                    Light.idle_light2 = Thread(target=Light.double_star_light, args=(1, ), daemon=True)
                    Light.idle_light2.start()
            else:
                state = Light.afk_thread_state()
                if not state[0]:
                    Light.afk_tick = 0
                    Light.fill(0, 0, 0, 0)
                    Light.afk_light1 = Thread(target=Light.rainbow, args=(0, ), daemon=True)
                    Light.afk_light1.start()
                
                if not state[1]:
                    Light.afk_tick = 0
                    Light.fill(1, 0, 0, 0)
                    Light.afk_light2 = Thread(target=Light.rainbow, args=(1, ), daemon=True)
                    Light.afk_light2.start()
            
            sleep(0.1)
            
        
        
        
        