import os
import serial

def getTTYName():
    filelist = os.listdir('/dev')
    for filename in filelist:
        if filename.startswith('ttyACM'):
            return f'/dev/{filename}'

class Arduino:
    ser = serial.Serial(getTTYName(),
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE)
    
    @staticmethod
    def analogWrite(pin: int, val: int): # mode: 1
        # packet - m: mode p: pin v: val 0: useless
        # vvvvvvvvppppppmm
        if val < 0:
            raise ValueError("analogWrite: val can't less than 0")
        if val > 255:
            raise ValueError("analogWrite: val can't bigger than 255")
        
        buffer = pin << 2
        
        buffer = buffer | (val << 8)
        
        buffer = buffer | 0x01
        
        packet = buffer.to_bytes(2)
        Arduino.ser.write(packet)

    @staticmethod
    def digitalRead(pin: int): # mode: 2
        # packet - m: mode p: pin 0: useless
        # 00000000ppppppmm
        
        # response - m: mode p: pin v: value 0: useless
        # 0000000vppppppmm
        # v: 0 or 1 -> LOW or HIGH
        buffer = pin << 2
        
        buffer = buffer | 0x02
        
        packet = buffer.to_bytes(2)
        Arduino.ser.write(packet)

    @staticmethod
    def analogRead(pin: int): # mode: 3
        # packet - m: mode p: pin 0: useless
        # 00000000ppppppmm
        # response - m: mode p: pin v: value 0: useless
        # vvvvvvvvppppppmm
        buffer = pin << 2
        
        buffer = buffer | 0x03
        
        packet = buffer.to_bytes(2)
        Arduino.ser.write(packet)
    
    @staticmethod
    def digitalWrite(pin: int, val: int): # mode: 0
        # packet - m: mode p: pin v: val 0: useless
        # 0000000vppppppmm
        # v: 0 or 1 -> LOW or HIGH
        if val not in [0, 1]:
            raise ValueError("digitalWrite: val only can be 0 or 1 -> LOW or HIGH")
        
        buffer = pin << 2
        buffer = buffer | (val << 8)

        buffer = buffer | 0x00
        
        packet = buffer.to_bytes(2)
        Arduino.ser.write(packet)

    @staticmethod
    def listening():
        while True:
            while Arduino.ser.in_waiting:
                response = int.from_bytes(Arduino.ser.read(2))
                mode = response & 0x03
                pin = (response & 0xfc) >> 2
                val = (response & 0xff00) >> 8
                
                print(mode, pin, val)
