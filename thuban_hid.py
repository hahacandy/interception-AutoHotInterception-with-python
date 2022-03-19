import clr
from tkinter import *

clr.AddReference("System")
clr.AddReference("AutoHotInterception")

import AutoHotInterception
import System

class Thuban_hid():
    
    def __init__(self, mouse_handle_name, keyboard_handle_name):
        
        self.instance = AutoHotInterception.Manager()
        
        # 使用者のhid装置のhandle
        self.mouse_handle = self.instance.GetDeviceIdFromHandle(True, mouse_handle_name, 1)
        self.keyboard_handle = self.instance.GetDeviceIdFromHandle(False, keyboard_handle_name, 1)
        

        #モニターの解像度がどれぐらいなのか
        root = Tk()
        self.monitor_width = root.winfo_screenwidth()
        self.monitor_height = root.winfo_screenheight()
        
        self.GetKeySC = \
        {'a':30,'b':48,'c':46,'d':32,'e':18,'f':33,'g':34,'h':35,'i':23,'j':36,'k':37,'l':38,'m':50,'n':49,'o':24,'p':25,'q':16,'r':19,
       's':31,'t':20,'u':22,'v':47,'w':17,'x':45,'y':21,'z':44, 'lwin':347}

        
    def click_mouse(self, state='left'):

        if state == 'left':
            self.instance.SendMouseButtonEvent(self.mouse_handle, 0, 1)
            self.instance.SendMouseButtonEvent(self.mouse_handle, 0, 0)
        elif state == 'right':
            self.instance.SendMouseButtonEvent(self.mouse_handle, 1, 1)
            self.instance.SendMouseButtonEvent(self.mouse_handle, 1, 0)
        else:
            pass

        
    def push_mouse(self, state='left'):

        if state == 'left':
            self.instance.SendMouseButtonEvent(self.mouse_handle, 0, 1)
        elif state == 'right':
            self.instance.SendMouseButtonEvent(self.mouse_handle, 1, 1)
        else:
            pass

        
    def up_mouse(self, state='left'):

        if state == 'left':
            self.instance.SendMouseButtonEvent(self.mouse_handle, 0, 0)
        elif state == 'right':
            self.instance.SendMouseButtonEvent(self.mouse_handle, 1, 0)
        else:
            pass

        
    def move_mouse(self, x, y):

        Send_X = 65535 / self.monitor_width * x 
        Send_Y = 65535 / self.monitor_height * y  
        self.instance.SendMouseMoveAbsolute(self.mouse_handle, Send_X, Send_Y)
        
    def send_key(self, key):
        code = self.GetKeySC[key.lower()]
        self.instance.SendKeyEvent(self.keyboard_handle, code, 1)
        self.instance.SendKeyEvent(self.keyboard_handle, code, 0)
        
    def send_str(self, str_list):
        
        for char in str_list:
            self.send_key(char)