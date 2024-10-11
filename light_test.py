from random import randrange
from threading import Thread
from time import sleep
from src.robot.raspberry.light import Light

def keep_alive():
    sleep(1000000)
    
def random_color():
    return (randrange(256), randrange(256), randrange(256))

def brightness_circle(light_number):
    length = Light.get_light_length(light_number)
    while True:
        for brightness in range(0, 100, 1):
            for i in range(length):
                Light.set_light_brightness(light_number, i, brightness * 0.01)
            sleep(0.01)
        for brightness in range(0, 100, 1)[::-1]:
            for i in range(length):
                Light.set_light_brightness(light_number, i, brightness * 0.01)
            sleep(0.01)
    
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
    Light.begin()  
    # Light.fill(0, 255, 255, 255)
    # Light.fill(1, 255, 0, 0)
    
    # Thread(target=brightness_circle, args=(0,), daemon=True).start()
    # Thread(target=brightness_circle, args=(1,), daemon=True).start()
    Thread(target=star_light_reverse, args=(0,), daemon=True).start()
    # Thread(target=star_light_reverse, args=(3,), daemon=True).start()
    
    
    while True:
        keep_alive()