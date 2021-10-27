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

class sceneFightEnd(myScene):
    def __init__(self,name):
        myScene.__init__(self,'FightEnd')

    def proc(self,background):
        funcList={}
        for func in self.funcPng:
            bFind,x,y,w,h=bFindInBackground(background,func.png)
            if bFind:funcList[func.name]=(x,y,w,h)
        if 'funcVictory' in funcList:
            pos=funcList['funcVictory']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcDefeat' in funcList:
            pos=funcList['funcDefeat']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcContinue1' in funcList:
            pos=funcList['funcContinue1']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcContinue2' in funcList:
            pos=funcList['funcContinue2']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcContinue3' in funcList:
            pos=funcList['funcContinue3']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcContinue4' in funcList:
            pos=funcList['funcContinue4']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)

