# from rpi_ws281x import *

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

# strip = Adafruit_NeoPixel(14, 26)
# strip.begin()

# try:
#     strip.setPixelColorRGB(0, 255, 0, 0)
#     strip.show()
# except Exception as err:
#     print(err)
#     pass

import board
import neopixel

from adafruit_blinka.microcontroller.bcm283x.pin import Pin

light1 = neopixel.NeoPixel(Pin(21), 14, brightness=1, auto_write=False, pixel_order=neopixel.RGB)
light2 = neopixel.NeoPixel(Pin(18), 14, brightness=1, auto_write=False, pixel_order=neopixel.RGB)
light3 = neopixel.NeoPixel(Pin(12), 14, brightness=1, auto_write=False, pixel_order=neopixel.RGB)
# light4 = neopixel.NeoPixel(Pin(18), 14, brightness=1, auto_write=False, pixel_order=neopixel.RGB)

light1.fill((255, 0, 0))
light1.show()

light2.fill((0, 255, 0))
light2.show()

light3.fill((0, 0, 255))
light3.show()

# light4.fill((255, 255, 0))
# light4.show()