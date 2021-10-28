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

class sceneFightShow(myScene):
    def __init__(self,name):
        myScene.__init__(self,'FightShow')

    def proc(self,background):
        funcList={}
        for func in self.funcPng:
            bFind,x,y,w,h=bFindInBackground(background,func.png)
            if bFind:funcList[func.name]=(x,y,w,h)
        if 'funcShow' in funcList:
            pos=funcList['funcShow']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)