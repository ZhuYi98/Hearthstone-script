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

class sceneFightChoose(myScene):
    def __init__(self,name):
        myScene.__init__(self,'FightChoose')

    def proc(self,background):
        funcList={}
        for func in self.funcPng:
            bFind,x,y,w,h=bFindInBackground(background,func.png)
            if bFind:funcList[func.name]=(x,y,w,h)
        if myScene.gTreasury>=200:
            if 'funcTeamView' in funcList:
                pos=funcList['funcTeamView']
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
                return
        if 'funcStartInter' in funcList:
            pos=funcList['funcStartInter']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcStartGoto' in funcList:
            pos=funcList['funcStartGoto']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcStartShow' in funcList:
            pos=funcList['funcStartShow']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcStartGet' in funcList:
            pos=funcList['funcStartGet']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcStartSkip' in funcList:
            pos=funcList['funcStartSkip']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        else:
            if 'funcSurprise' in funcList:
                pos=funcList['funcSurprise']
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
            elif 'funcHeroRed' in funcList:
                pos=funcList['funcHeroRed']
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2+50)
            elif 'funcHeroGreen' in funcList:
                pos=funcList['funcHeroGreen']
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2+50)
            elif 'funcHeroBlue' in funcList:
                pos=funcList['funcHeroBlue']
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2+50)
            elif 'funcSkip1' in funcList:
                pos=funcList['funcSkip1']
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
            elif 'funcSkip2' in funcList:
                pos=funcList['funcSkip2']
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
            elif 'funcSkip3' in funcList:
                pos=funcList['funcSkip3']
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
            elif 'funcSkip4' in funcList:
                pos=funcList['funcSkip4']
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
