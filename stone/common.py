# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

#import cv2
import pyautogui
import time
import random
from myGui import *

def moveAndClick(x,y):
    if x>10 and x<=1910 and y>10 and y<=1070:
        pyautogui.moveTo(x+random.randint(-5, 5),y+random.randint(-5, 5))
        pyautogui.click(clicks=1)
        pyautogui.moveTo(650,20)
        pyautogui.click(clicks=1)
    else:
        pyautogui.moveTo(650,20)
        pyautogui.click(clicks=1)

def drag(x0,y0,x1,y1):
    if x0>10 and x0<=1910 and y0>10 and y0<=1070 and x1>10 and x1<=1910 and y1>10 and y1<=1070:
        pyautogui.mouseDown(x0+random.randint(-5,5),y0+random.randint(-5,5))
        pyautogui.moveTo(x1+random.randint(-5,5),y1+random.randint(-5,5))
        time.sleep(0.5)
        pyautogui.mouseUp(x1+random.randint(-5,5),y1+random.randint(-5,5))
        pyautogui.moveTo(650,20)
        pyautogui.click(clicks=1)
    else:
        pyautogui.moveTo(650,20)
        pyautogui.click(clicks=1)

def bFindInBackground(background,png):
    if 0:
        result=cv2.matchTemplate(background,png,cv2.TM_CCOEFF_NORMED)
        minVal,maxVal,minLoc,maxLoc=cv2.minMaxLoc(result)
        if maxVal>0.8:
            x=maxLoc[0]
            y=maxLoc[1]
            w,h=png.shape[::-1]
            if MyGui.gDebug:
                left_top=maxLoc
                right_bottom=(left_top[0]+w,left_top[1]+h)
                img=cv2.imread("resource/background.png",1)
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
    return False,0,0,0,0

class myPng(object):
    def __init__(self,path,name):
        self.name=name.split('.')[0]
        self.png=None
        if path!='' and name!='':
            p=path+'/'+str(name)
            p.replace("'","\"")
            #self.png=cv2.imread(p,cv2.IMREAD_GRAYSCALE)
            self.png=None

class myScene(object):

    gFightTotal=0
    gTreasury=0
    gCurrScene=None

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
        if not self.bValid:return False
        for tag in self.tagPng:
            bFind,x,y,w,h=bFindInBackground(background,tag.png)
            if not bFind:
                myScene.gCurrScene=None
                return False
        myScene.gCurrScene=self.name
        return True

    def proc(self,background):None
