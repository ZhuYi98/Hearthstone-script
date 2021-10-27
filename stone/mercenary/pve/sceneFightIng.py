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

class sceneFightIng(myScene):
    def __init__(self,name):
        myScene.__init__(self,'FightIng')

    def proc(self,background):
        funcList={}
        for func in self.funcPng:
            bFind,x,y,w,h=bFindInBackground(background,func.png)
            if bFind:funcList[func.name]=(x,y,w,h)
        if 'funcHeroNone' in funcList:
            pos=funcList['funcHeroNone']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcSkill1' in funcList:
            pos=funcList['funcSkill1']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcSkill2' in funcList:
            pos=funcList['funcSkill2']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcSkill3' in funcList:
            pos=funcList['funcSkill3']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcSkill4' in funcList:
            pos=funcList['funcSkill4']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcSkill5' in funcList:
            pos=funcList['funcSkill5']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcSkill6' in funcList:
            pos=funcList['funcSkill6']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcSkillOk' in funcList:
            pos=funcList['funcSkillOk']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcSkillError' in funcList:
            pos=funcList['funcSkillError']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
