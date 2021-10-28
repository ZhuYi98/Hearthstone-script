# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
from common import *

class scPointChoose(myScene):
    def __init__(self):
        self.bValid=False
        self.name='PointChoose'
        self.path='resource/mercenary/base/scPointChoose'
        self.tagPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('tag')]
        self.funcPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('func')]

    def proc(self,background):
        funcList={}
        for func in self.funcPng:
            bFind,x,y,w,h=bFindInBackground(background,func.png)
            if bFind:funcList[func.name]=(x,y,w,h)
        if 'funcPve' in funcList:
            pos=funcList['funcPve']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,2)
        elif 'funcPvp' in funcList:
            pos=funcList['funcPvp']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,2)
