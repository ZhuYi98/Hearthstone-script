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
from common import *

class sceneSelectTreasury(myScene):
    def __init__(self,name):
        myScene.__init__(self,'SelectTreasury')

    def proc(self,background):
        funcList={}
        for func in self.funcPng:
            bFind,x,y,w,h=bFindInBackground(background,func.png)
            if bFind:funcList[func.name]=(x,y,w,h)
        if 'funcDis' in funcList and 'funcTreasury' in funcList:
            pos=funcList['funcTreasury']
            pos1=[150,360,570]
            moveAndClick(pos[0]+pos[2]/2+pos1[random.randint(0,2)],pos[1]+pos[3]/2)
            return
        else:
            if 'funcSelOk' in funcList:
                if 'funcGet' in funcList:
                    pos=funcList['funcGet']
                    moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
                    myScene.gTreasury=myScene.gTreasury+1
                elif 'funcReplace' in funcList:
                    pos=funcList['funcReplace']
                    moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
                    myScene.gTreasury=myScene.gTreasury+1
                elif 'funcHold' in funcList:
                    pos=funcList['funcHold']
                    moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
                    myScene.gTreasury=myScene.gTreasury+1
            elif 'funcTreasury' in funcList:
                pos=funcList['funcTreasury']
                pos1=[150,360,570]
                moveAndClick(pos[0]+pos[2]/2+pos1[random.randint(0,2)],pos[1]+pos[3]/2)
