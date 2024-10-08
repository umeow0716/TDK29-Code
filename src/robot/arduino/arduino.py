import os
import serial

def getTTYName():
    filelist = os.listdir('/dev')
    for filename in filelist:
        if filename.startswith('ttyUSB'):
            return f'/dev/{filename}'
        if filename.startswith('ttyACM'):
            return f'/dev/{filename}'

class Arduino:
    ser = serial.Serial(getTTYName(),
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE)
    
    @staticmethod
    def digitalWrite(pin: int, val: int): # mode: 0
        # packet - m: mode p: pin v: val 0: useless
        # mmpppppp0000000v
        # v: 0 or 1 -> LOW or HIGH
        if val not in [0, 1]:
            raise ValueError("digitalWrite: val only can be 0 or 1 -> LOW or HIGH")
        
        buffer = (0x00 << 14)
        buffer = buffer | (pin << 8)

        buffer = buffer | val
        
        packet = buffer.to_bytes(2)
        Arduino.ser.write(packet)
    
    @staticmethod
    def analogWrite(pin: int, val: int): # mode: 1
        # packet - m: mode p: pin v: val 0: useless
        # mmppppppvvvvvvvv
        if val < 0:
            raise ValueError("analogWrite: val can't less than 0")
        if val > 255:
            raise ValueError("analogWrite: val can't bigger than 255")
        
        buffer = (0x01 << 14)
        
        buffer = buffer | (pin << 8)
        
        buffer = buffer | val
        
        packet = buffer.to_bytes(2)
        Arduino.ser.write(packet)

    @staticmethod
    def setColor(light_number: int, light_index: int, red=0, green=0, blue=0, need_update=False): # mode: 2
        # packet - m: mode n: lightNumber i:lightIndex r: Red g: Green b: Blue u: Need Update 
        # mmnniiii rrrrrrrr gggggggg bbbbbbbb 000000u
        buffer = (0x02 << 38)
        
        buffer = buffer | (light_number << 36)
        
        buffer = buffer | (light_index << 32)
        
        buffer = buffer | (red << 24)
        buffer = buffer | (green << 16)
        buffer = buffer | (blue << 8)
        buffer = buffer | (1 if need_update else 0)
        
        packet = buffer.to_bytes(5)
        Arduino.ser.write(packet)

    @staticmethod
    def listening():
        while True:
            try:
                while Arduino.ser.in_waiting:
                    response = int.from_bytes(Arduino.ser.read(2))
                    mode = response & 0x03
                    pin = (response & 0xfc) >> 2
                    val = (response & 0xff00) >> 8
                
                    print(mode, pin, val)
            except:
                pass
