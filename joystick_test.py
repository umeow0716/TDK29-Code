from time import sleep
import json
from joystick.joystick import Joystick

Joystick.start_thread()

while True:
    sleep(3)
    d = Joystick.get_state()
    for key in d.keys():
        if type(d[key]) == bool:
            d[key] = { 'when_pressed': None, 'when_released': None }
        else:
            d[key] = { 'when_moved': None }
    
    f = open('joystick-setting.json', 'w', encoding='utf-8')
    f.write(json.dumps(d, indent=4))
    sleep(1)