# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import cv2
import pyautogui
import win32gui,win32con
import time
import os
import numpy as np
import random

class runStatus(object):

    _bRunning=True
    _bRunOk=True
    _runTime=int(time.time())

    def __init__(self):
        pass

    def bRunning(self):
        return self._bRunning

    def setRunning(self,result):
        self._bRunning=result

    def bRunOk(self):
        return self._bRunOk

    def setRunning(self,result):
        self._bRunOk=result

    def getRunTime(self):
        return runStatus._runTime

    def setRunTime(self):
        runStatus._runTime=int(time.time())

def bFindInBackground(background,png):
    result=cv2.matchTemplate(background,png,cv2.TM_CCOEFF_NORMED)
    minVal,maxVal,minLoc,maxLoc=cv2.minMaxLoc(result)
    if maxVal>0.8:
        x=maxLoc[0]
        y=maxLoc[1]
        w,h=png.shape[::-1]
        if 0:
            left_top=maxLoc
            right_bottom=(left_top[0]+w,left_top[1]+h)
            img=cv2.imread("png/big.png",1)
            cv2.rectangle(img,left_top,right_bottom,(0,0,255),2)
            img=cv2.resize(img,(0,0),fx=0.5,fy=0.5,interpolation=cv2.INTER_NEAREST)
            print('maxVal='),
            print(maxVal)
            cv2.imshow("processed",img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        return True,x,y,w,h
    else:
        return False,0,0,0,0

def moveAndClick(x,y):
    if x>10 and x<=1910 and y>10 and y<=1070:
        pyautogui.moveTo(x,y)
        pyautogui.click(clicks=1)
        pyautogui.moveTo(5,5)
        pyautogui.click(clicks=1)
    else:
        pyautogui.moveTo(5,5)
        pyautogui.click(clicks=1)

class myPng(object):
    def __init__(self,path,name):
        self.name=name.split('.')[0]
        p=path+'/'+str(name)
        p.replace("'","\"")
        self.png=cv2.imread(p,cv2.IMREAD_GRAYSCALE)

class myScene(object):

    gFightTotal=0
    gTreasury=0
    gCurrScene=None

    def __init__(self,name):
        self.name=str(name)
        self.path='png/'+'sc'+str(name)
        self.tagPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('tag')]
        self.funcPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('func')]

    def isOwn(self,background):
        for tga in self.tagPng:
            bFind,x,y,w,h=bFindInBackground(background,tga.png)
            if not bFind:
                myScene.gCurrScene=None
                return False
        myScene.gCurrScene=self.name
        return True

    def proc(self,background):None