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

class sceneFightBox(myScene):
    def __init__(self,name):
        myScene.__init__(self,'FightBox')

    def proc(self,background):
        funcList={}
        for func in self.funcPng:
            bFind,x,y,w,h=bFindInBackground(background,func.png)
            if bFind:funcList[func.name]=(x,y,w,h)
        if 'funcPass' in funcList:
            pos=funcList['funcPass']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
            myScene.gFightTotal+=1
        elif 'funcBox1' in funcList:
            pos=funcList['funcBox1']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcBox2' in funcList:
            pos=funcList['funcBox2']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcBox3' in funcList:
            pos=funcList['funcBox3']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcBox4' in funcList:
            pos=funcList['funcBox4']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcBox5' in funcList:
            pos=funcList['funcBox5']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
