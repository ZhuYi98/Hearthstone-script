# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import cv2
import sys
import pyautogui
import time
import random
import numpy as np
from myGui import *

w,h=pyautogui.size()
def moveAndClick(x,y,t=1.5):
    if x>=10 and x<=(w-10) and y>=10 and y<=(h-10):
        MyGui.gWait=t+0.5
        pyautogui.moveTo(x,y)
        time.sleep(0.1)
        pyautogui.mouseDown(x,y)
        time.sleep(0.1)
        pyautogui.mouseUp(x,y)
        time.sleep(0.3)
        pyautogui.moveTo(10,10)
        time.sleep(t)

def Click(x,y,t=0):
    if x>=10 and x<=(w-10) and y>=10 and y<=(h-10):
        pyautogui.moveTo(x,y)
        pyautogui.mouseDown(x,y)
        pyautogui.mouseUp(x,y)
        time.sleep(t)

def Drag(x0,y0,x1,y1,t=1.5):
    if x0>=10 and x0<=(w-10) and y0>=10 and y0<=(h-10) and \
       x1>=10 and x1<=(w-10) and y1>=10 and y1<=(h-10):
        pyautogui.moveTo(x0,y0)
        pyautogui.mouseDown(x0,y0)
        time.sleep(0.1)
        pyautogui.moveTo(x1,y1)
        time.sleep(0.2)
        pyautogui.mouseUp(x1,y1)
        pyautogui.moveTo(10,10,)
        time.sleep(t)

def SaveScreen():
    pyautogui.screenshot("resource/background.png")
    return cv2.imread("resource/background.png",cv2.IMREAD_GRAYSCALE)

def SaveAwardPng():
    pyautogui.screenshot(str(time.strftime(
        'config/box/%Y-%m-%d_%H-%M-%S.png',time.localtime(time.time()))))

def SaveErrorPng():
    pyautogui.screenshot(str(time.strftime(
        'config/error/%Y-%m-%d_%H-%M-%S.png',time.localtime(time.time()))))

class MyLog(object):
    def __init__(self):
        self.orgstdout=sys.stdout
        self.log=open("log/log.txt","a")

    def write(self,msg):
        self.orgstdout.write(msg)
        self.log.write(msg)

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

    def isOwn(self,background):None

    def proc(self,background):None
