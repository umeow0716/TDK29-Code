from ..robot.joystick_command_parser import JoystickCommandParser

@JoystickCommandParser.func_register_wrapper('when_axis_l_change')
def when_axis_l_change(axis):
    x, y = (round(axis.x, 2), round(axis.y, 2))
    print(x, y)

@JoystickCommandParser.func_register_wrapper('when_axis_r_change')
def when_axis_r_change(axis):
    print('func: when_axis_r_change')
