# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
from common import *

class scPvpSurrender(myScene):
    def __init__(self):
        self.name='PvpSelectCard'
        self.path='resource/mercenary/pvp/scPvpSurrender'
        self.tagPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('tag')]
        self.funcPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('func')]

    def proc(self,background):
        self.myRunStatus.setRunTime()
        funcList={}
        for func in self.funcPng:
            bFind,x,y,w,h=bFindInBackground(background,func.png)
            if bFind:funcList[func.name]=(x,y,w,h)
        if 'funcSurrender' in funcList:
            pos=funcList['funcSurrender']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcSet' in funcList and 'funcDis' not in funcList:
            pos=funcList['funcSet']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2) 
