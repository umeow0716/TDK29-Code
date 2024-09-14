
from src.joystick.joystick import Joystick

def keep_alive():
    pass

if __name__ == '__main__':
    Joystick.start_thread()
    
    while True:
        keep_alive()