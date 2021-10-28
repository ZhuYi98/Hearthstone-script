# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
from common import *

class scInterZone(myScene):
    def __init__(self):
        self.name='PvpSelectCard'
        self.path='resource/mercenary/pvp/scPvpSelectCard'
        self.tagPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('tag')]
        self.funcPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('func')]

    def proc(self,background):
        funcList={}
        for func in self.funcPng:
            bFind,x,y,w,h=bFindInBackground(background,func.png)
            if bFind:funcList[func.name]=(x,y,w,h)
        if 'funcStart' in funcList:
            pos=funcList['funcStart']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
