from threading import Thread
from time import sleep

from src.robot.arduino.arduino import Arduino

def listening():
    while True:
        while Arduino.ser.in_waiting:
            response = Arduino.ser.read_all().decode()
            
            print(response)

try:
    Thread(target=listening, daemon=True).start()
    sleep(2)
    while True:
        for i in range(0, 256):
            Arduino.setColor(0, 0, i, 0, 0)
            sleep(0.01)
        for i in range(0, 256)[::-1]:
            Arduino.setColor(0, 0, i, 0, 0)
            sleep(0.01)
        for j in range(0, 256):
            Arduino.setColor(0, 0, 0, j, 0)
            sleep(0.01)
        for j in range(0, 256)[::-1]:
            Arduino.setColor(0, 0, 0, j, 0)
            sleep(0.01)
        for k in range(0, 256):
            Arduino.setColor(0, 0, 0, 0, k)
            sleep(0.01)
        for k in range(0, 256)[::-1]:
            Arduino.setColor(0, 0, 0, 0, k)
            sleep(0.01)
except KeyboardInterrupt:
    pass