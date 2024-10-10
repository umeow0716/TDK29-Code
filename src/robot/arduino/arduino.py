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
        # mmpppppp 0000000v
        # v: 0 or 1 -> LOW or HIGH
        if val not in [0, 1]:
            raise ValueError("digitalWrite: val only can be 0 or 1 -> LOW or HIGH")
        
        buffer = (0x00 << 14)
        buffer = buffer | (pin << 8)

        buffer = buffer | (1 if val else 0)
        
        packet = buffer.to_bytes(2)
        Arduino.ser.write(packet)
    
    @staticmethod
    def analogWrite(pin: int, val: int): # mode: 1
        # packet - m: mode p: pin v: val 0: useless
        # mmpppppp vvvvvvvv
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
    def setColor(light_number: int, light_index: int, red=0, green=0, blue=0): # mode: 2
        return
        # print(red, green, blue)
        # packet - m: mode n: lightNumber i:lightIndex r: Red g: Green b: Blue u: Need Update 
        # mmnniiii rrrrrrrr gggggggg bbbbbbbb
        buffer = (0x02 << 30)
        
        buffer = buffer | (light_number << 28)
        
        buffer = buffer | (light_index << 24)
        
        buffer = buffer | (red << 16)
        buffer = buffer | (green << 8)
        buffer = buffer | blue
        
        packet = buffer.to_bytes(4)
        Arduino.ser.write(packet)
        
    @staticmethod
    def show():
        # mm000000 00000000 00000000 00000000
        buffer = (0x03 << 30)
        packet = buffer.to_bytes(4)
        Arduino.ser.write(packet)

    @staticmethod
    def listening():
        while True:
            try:
                while Arduino.ser.in_waiting:
                    response = Arduino.ser.read_all()
                    print(response.decode())
            except:
                pass
