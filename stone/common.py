# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import pyautogui
import time
import random
import numpy as np
from myGui import *
from openCv import *

def moveAndClick(x,y):
    if x>=10 and x<=1910 and y>=10 and y<=1070:
        pyautogui.moveTo(x,y)
        pyautogui.click(clicks=2)
        pyautogui.moveTo(10,10)
        pyautogui.click(clicks=1)

def drag(x0,y0,x1,y1):
    if x0>=10 and x0<=1910 and y0>=10 and y0<=1070 and \
       x1>=10 and x1<=1910 and y1>=10 and y1<=1070:
        pyautogui.mouseDown(x0,y0)
        pyautogui.moveTo(x1,y1)
        time.sleep(0.2)
        pyautogui.mouseUp(x1,y1)
        pyautogui.moveTo(10,10,)
        pyautogui.click(clicks=1)

class myPng(object):
    def __init__(self,path,name):
        self.path=path+'/'+str(name)
        self.name=name.split('.')[0]
        self.data=None
        if path!='' and name!='':
            self.data=cv2.imread(self.path.\
            replace("'","\""),cv2.IMREAD_GRAYSCALE)

class myScene(object):
    def __init__(self):
        self.bValid=False
        self.name=''
        self.path=''
        self.tagPng=[myPng('','')]
        self.funcPng=[myPng('','')]
    
    def enable(self):
        self.bValid=True

    def dis(self):
        self.bValid=False

    def isOwn(self,background):
        if self.bValid:
            for tag in self.tagPng:
                bFind,x,y,w,h=bFindInBackground(background,tag)
                if not bFind:return False
            return True
        else:
            return False

    def proc(self,background):None
