import clr
from tkinter import *

clr.AddReference("System")
clr.AddReference("AutoHotInterception")

import AutoHotInterception
import System

import pyautogui
import time

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
        's':31,'t':20,'u':22,'v':47,'w':17,'x':45,'y':21,'z':44,
         '`':41,'1':2,'2':3,'3':4,'5':6,'7':8,'8':9,'9':10,'0':11,'-':12,'=':13,'backspace':14,'enter':284,
         'tab':15,'capslock':58,'rshift':42,'lctrl':29,'lwin':347,'lalt':56,'space':57,'한영':114,
        'esc':1,'f1':59,'f2':60,'f3':61,'f4':62,'f5':63,'f6':64,'f7':65,'f8':66,'f9':67,'f10':68,'f11':87,'f12':88,
        'printscreen':311}

        
    def click_mouse(self, state='left'):

        if state == 'left':
            self.instance.SendMouseButtonEvent(self.mouse_handle, 0, 1)
            self.instance.SendMouseButtonEvent(self.mouse_handle, 0, 0)
        elif state == 'right':
            self.instance.SendMouseButtonEvent(self.mouse_handle, 1, 1)
            self.instance.SendMouseButtonEvent(self.mouse_handle, 1, 0)
        else:
            pass
        
        time.sleep(0.1)

        
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
        
        time.sleep(0.1)
        
        
    def send_key(self, key):
        code = self.GetKeySC[key.lower()]
        self.instance.SendKeyEvent(self.keyboard_handle, code, 1)
        self.instance.SendKeyEvent(self.keyboard_handle, code, 0)
        
        
    def send_str(self, str_list):
        for char in str_list:
            self.send_key(char)
            
            
    def push_key(self, key):
        code = self.GetKeySC[key.lower()]
        self.instance.SendKeyEvent(self.keyboard_handle, code, 1)
        
        
    def up_key(self, key):
        code = self.GetKeySC[key.lower()]
        self.instance.SendKeyEvent(self.keyboard_handle, code, 0)
        

    def search_image(self, img_path, confidence):
        p_list = pyautogui.locateAllOnScreen(img_path, confidence=confidence)
        p_list = list(p_list)
        if len(p_list) > 0:
            return p_list
        else:
            None