from thuban_hid import Thuban_hid

thd = Thuban_hid('HID\VID_275D&PID_0BA6&REV_0100', 'HID\VID_046D&PID_C31C&REV_6401&MI_00')

import keyboard

def wefwef(event):

    if event.event_type == 'up':
        if event.name == 'f2':
            thd.send_str('abcdefghijklmnopqrstuvwxyz')

keyboard.hook(wefwef)