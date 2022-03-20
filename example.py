from thuban_hid import Thuban_hid
import keyboard



thd = Thuban_hid('HID\VID_275D&PID_0BA6&REV_0100', 'HID\VID_046D&PID_C31C&REV_6401&MI_00')


def call_hook_event(event):

    if event.event_type == 'up':
        if event.name == 'f6':
            thd.send_str('abcdefghijklmnopqrstuvwxyz')
        elif event.name == 'f7':
            thd.send_key('한영')

keyboard.hook(call_hook_event)